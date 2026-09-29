"""
NEUROVA Platform - RAG Engine
Offline retrieval over rag_chunks.json and master_compilation.md.
Preserves [SOURCE] vs [DERIVED] chunk metadata and returns domain context for grounding local LLM generation.
"""

import json
import os
import re
from typing import List, Dict, Any

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAG_CHUNKS_PATH = os.path.join(PROJECT_DIR, "rag_chunks.json")
MASTER_COMPILATION_PATH = os.path.join(PROJECT_DIR, "master_compilation.md")


class RAGEngine:
    def __init__(self):
        self.chunks: List[Dict[str, Any]] = []
        self._load_chunks()

    def _load_chunks(self):
        if os.path.exists(RAG_CHUNKS_PATH):
            with open(RAG_CHUNKS_PATH, "r", encoding="utf-8") as f:
                self.chunks = json.load(f)
        else:
            self.chunks = []

    def search(self, stage: str = "all", query: str = "", top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Offline keyword + stage matching retrieval.
        Filters chunks matching patient stage (or 'all') and calculates relevance score based on search terms.
        """
        stage_clean = (stage or "all").lower()
        keywords = set(re.findall(r'\w+', query.lower())) if query else set()

        scored_chunks = []
        for chunk in self.chunks:
            chunk_stage = str(chunk.get("stage", "all")).lower()
            
            # Stage match check
            if chunk_stage != "all" and stage_clean != "all" and chunk_stage != stage_clean:
                stage_score = 0.5  # Partial match
            else:
                stage_score = 1.5  # Direct match

            # Text match check
            text = chunk.get("text", "").lower()
            topic = chunk.get("topic", "").lower()
            
            keyword_score = 0
            if keywords:
                for kw in keywords:
                    if kw in text or kw in topic:
                        keyword_score += 1.0

            total_score = stage_score + keyword_score
            scored_chunks.append((total_score, chunk))

        # Sort by total score descending
        scored_chunks.sort(key=lambda x: x[0], reverse=True)
        return [chunk for _, chunk in scored_chunks[:top_k]]

    def get_grounding_context(self, patient_intake: Dict[str, Any]) -> str:
        """
        Builds a concise ground-truth context block from retrieved RAG chunks to insert into the system prompt.
        """
        stage = patient_intake.get("basic_info", {}).get("current_stage", "middle")
        strengths = patient_intake.get("cognitive_baseline", {}).get("domain_strengths", {})
        triggers = patient_intake.get("behavioral_safety", {}).get("known_triggers", [])

        query_str = f"stage {stage} strengths {' '.join(strengths.values() if isinstance(strengths, dict) else [])} triggers {' '.join(triggers)}"
        retrieved_chunks = self.search(stage=stage, query=query_str, top_k=6)

        context_lines = ["=== RETRIEVED DOMAIN KNOWLEDGE (RAG CHUNKS) ==="]
        for c in retrieved_chunks:
            source_tag = f"[{c.get('type', 'derived').upper()}]"
            context_lines.append(f"{source_tag} Topic: {c.get('topic')} | Stage: {c.get('stage')}")
            context_lines.append(f"Content: {c.get('text')}\n")

        return "\n".join(context_lines)


# Global instance
rag_engine = RAGEngine()
