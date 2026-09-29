/* NEUROVA Caregiver Dashboard Client Logic */

const API_BASE = "/api";

// Preset Synthetic Patients (matches backend dataset)
const SYNTHETIC_PRESETS = [
  {
    name: "Anand Sharma",
    subtitle: "Alzheimer's Disease • Preserves verbal recall & nostalgic music recall",
    age: 68,
    sex: "Male",
    dementia_type: "Alzheimer's",
    current_stage: "early",
    strength_memory: "strong",
    strength_recognition: "strong",
    strength_attention: "weak",
    strength_language: "strong",
    hearing_status: "normal",
    vision_status: "normal",
    caregiver_hours: 2.0,
    favorite_songs: "Borgeet melodies, Classic Oldies",
    known_triggers: "",
    disliked_activities: ""
  },
  {
    name: "Kamla Devi",
    subtitle: "Vascular Dementia • 15-minute caregiver time ceiling",
    age: 76,
    sex: "Female",
    dementia_type: "Vascular",
    current_stage: "middle",
    strength_memory: "weak",
    strength_recognition: "strong",
    strength_attention: "weak",
    strength_language: "moderate",
    hearing_status: "needs_loud_slow",
    vision_status: "needs_large_text",
    caregiver_hours: 0.25, // 15 mins!
    favorite_songs: "Folk songs",
    known_triggers: "Loud sudden sounds",
    disliked_activities: ""
  },
  {
    name: "Biren Roy",
    subtitle: "Mixed Dementia • Comfort, sensory & relational presence",
    age: 84,
    sex: "Male",
    dementia_type: "Mixed",
    current_stage: "late",
    strength_memory: "weak",
    strength_recognition: "weak",
    strength_attention: "weak",
    strength_language: "weak",
    hearing_status: "needs_loud_slow",
    vision_status: "normal",
    caregiver_hours: 1.0,
    favorite_songs: "Soft instrumental flute",
    known_triggers: "Crowded spaces",
    disliked_activities: ""
  },
  {
    name: "Unknown Intake Patient",
    subtitle: "Incomplete Profile • Middle-stage fallback active",
    age: 72,
    sex: "Male",
    dementia_type: "Unknown",
    current_stage: "", // MISSING
    strength_memory: "moderate",
    strength_recognition: "moderate",
    strength_attention: "moderate",
    strength_language: "moderate",
    hearing_status: "normal",
    vision_status: "normal",
    caregiver_hours: "", // MISSING
    favorite_songs: "",
    known_triggers: "",
    disliked_activities: ""
  },
  {
    name: "Pranab Das",
    subtitle: "Alzheimer's Disease • Dislikes music, prefers tactile sorting",
    age: 71,
    sex: "Male",
    dementia_type: "Alzheimer's",
    current_stage: "middle",
    strength_memory: "weak",
    strength_recognition: "strong",
    strength_attention: "weak",
    strength_language: "moderate",
    hearing_status: "normal",
    vision_status: "normal",
    caregiver_hours: 1.0,
    favorite_songs: "",
    known_triggers: "",
    disliked_activities: "music, singing, loud songs"
  },
  {
    name: "Maya Sen",
    subtitle: "Lewy Body Dementia • Music & group distress trigger substituted",
    age: 75,
    sex: "Female",
    dementia_type: "Lewy Body",
    current_stage: "middle",
    strength_memory: "weak",
    strength_recognition: "strong",
    strength_attention: "weak",
    strength_language: "moderate",
    hearing_status: "normal",
    vision_status: "normal",
    caregiver_hours: 1.0,
    favorite_songs: "",
    known_triggers: "music, group physical, loud radio",
    disliked_activities: ""
  },
  {
    name: "Dipankar Baruah",
    subtitle: "Vascular Dementia • High-contrast visual & large targets",
    age: 80,
    sex: "Male",
    dementia_type: "Vascular",
    current_stage: "middle",
    strength_memory: "weak",
    strength_recognition: "strong",
    strength_attention: "weak",
    strength_language: "moderate",
    hearing_status: "needs_loud_slow",
    vision_status: "needs_large_text",
    caregiver_hours: 0.75,
    favorite_songs: "",
    known_triggers: "",
    disliked_activities: ""
  }
];

let currentPatientIntake = null;
let currentActivePatientId = "syn_early_01";
let currentSubtitle = "Alzheimer's Disease • Preserves verbal recall & nostalgic music recall";

// Tab Switching
function switchTab(tabId) {
  document.querySelectorAll(".nav-tab").forEach(tab => tab.classList.remove("active"));
  document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

  const targetTab = document.getElementById(`tab-${tabId}`);
  if (targetTab) {
    targetTab.classList.add("active");
  }

  // Update button active state
  const tabs = document.querySelectorAll(".nav-tab");
  if (tabId === 'intake') tabs[0].classList.add("active");
  if (tabId === 'schedule') tabs[1].classList.add("active");
  if (tabId === 'games') tabs[2].classList.add("active");
  if (tabId === 'logs') tabs[3].classList.add("active");
}

function handlePresetSelectChange(e) {
  const index = parseInt(e.target.value);
  loadSyntheticPreset(index);
}

// Load Synthetic Preset into Form
function loadSyntheticPreset(index) {
  const p = SYNTHETIC_PRESETS[index];
  if (!p) return;

  currentSubtitle = p.subtitle;

  document.getElementById("patient-name").value = p.name;
  document.getElementById("patient-age").value = p.age;
  document.getElementById("patient-sex").value = p.sex;
  document.getElementById("dementia-type").value = p.dementia_type;
  document.getElementById("current-stage").value = p.current_stage;
  document.getElementById("strength-memory").value = p.strength_memory;
  document.getElementById("strength-recognition").value = p.strength_recognition;
  document.getElementById("strength-attention").value = p.strength_attention;
  document.getElementById("strength-language").value = p.strength_language;
  document.getElementById("hearing-status").value = p.hearing_status;
  document.getElementById("vision-status").value = p.vision_status;
  document.getElementById("caregiver-hours").value = p.caregiver_hours;
  document.getElementById("favorite-songs").value = p.favorite_songs;
  document.getElementById("known-triggers").value = p.known_triggers;
  document.getElementById("disliked-activities").value = p.disliked_activities;

  const selector = document.getElementById("patient-preset-selector");
  if (selector) selector.value = index;

  handleSaveIntake(new Event("submit"));
}

// Construct Patient Intake JSON Payload from Form
function buildIntakeFromForm() {
  const hoursVal = document.getElementById("caregiver-hours").value;
  const stageVal = document.getElementById("current-stage").value;

  const triggersVal = document.getElementById("known-triggers").value;
  const dislikesVal = document.getElementById("disliked-activities").value;

  return {
    patient_id: currentActivePatientId,
    name: document.getElementById("patient-name").value || "Patient",
    basic_info: {
      age: parseInt(document.getElementById("patient-age").value) || None,
      sex: document.getElementById("patient-sex").value,
      dementia_type: document.getElementById("dementia-type").value,
      current_stage: stageVal || None,
      comorbidities: []
    },
    cognitive_baseline: {
      domain_strengths: {
        memory: document.getElementById("strength-memory").value,
        recognition: document.getElementById("strength-recognition").value,
        attention: document.getElementById("strength-attention").value,
        language: document.getElementById("strength-language").value,
        problem_solving: "weak"
      },
      independence_level: "supervision_needed"
    },
    sensory_physical: {
      hearing_status: document.getElementById("hearing-status").value,
      vision_status: document.getElementById("vision-status").value,
      mobility_limitations: "none",
      literacy_level: "fluent"
    },
    daily_rhythm: {
      wake_time: "07:00",
      sleep_time: "21:30",
      sundowning_risk_window: "16:00-19:00"
    },
    personal_cultural: {
      favorite_songs: document.getElementById("favorite-songs").value.split(",").map(s => s.trim()).filter(Boolean),
      disliked_activities: dislikesVal.split(",").map(s => s.trim()).filter(Boolean)
    },
    behavioral_safety: {
      known_triggers: triggersVal.split(",").map(s => s.trim()).filter(Boolean)
    },
    caregiver_info: {
      primary_caregiver: "Family Caregiver",
      available_hours_per_day: hoursVal ? parseFloat(hoursVal) : None
    }
  };
}

// Save Intake Profile & Trigger Schedule Generation
async function handleSaveIntake(e) {
  if (e && e.preventDefault) e.preventDefault();

  currentPatientIntake = buildIntakeFromForm();

  try {
    const resp = await fetch(`${API_BASE}/schedule/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(currentPatientIntake)
    });

    if (!resp.ok) throw new Error("Schedule generation request failed");

    const scheduleData = await resp.json();
    renderSchedule(scheduleData);

    fetchNextGameTask();

    // Switch to Schedule tab
    switchTab('schedule');

  } catch (err) {
    console.error("Error saving intake & generating schedule:", err);
  }
}

function triggerGenerateSchedule() {
  handleSaveIntake(new Event("submit"));
}

// Render Daily Routine Schedule Timeline (Mockup Replica)
function renderSchedule(sched) {
  document.getElementById("sched-patient-title").innerText = `${sched.patient_name} — Daily Routine`;
  document.getElementById("sched-patient-subtitle").innerText = currentSubtitle;

  const totalMin = sched.total_duration_minutes || 40;
  const ceilingMin = sched.caregiver_time_ceiling_minutes || 120;
  const bufferMin = Math.max(0, ceilingMin - totalMin);
  const percent = Math.min(100, Math.round((totalMin / ceilingMin) * 100));

  document.getElementById("sched-time-label").innerText = `Scheduled Time   ${totalMin} / ${ceilingMin} min`;
  document.getElementById("sched-progress-fill").style.width = `${percent}%`;
  document.getElementById("sched-buffer-label").innerText = `${bufferMin} min buffer remaining today`;

  // Missing Fields Warning Banner
  const warningBanner = document.getElementById("missing-warning-banner");
  if (sched.missing_fields_warning && sched.missing_fields_warning.length > 0) {
    document.getElementById("missing-fields-list").innerText = sched.missing_fields_warning.join(", ");
    warningBanner.style.display = "block";
  } else {
    warningBanner.style.display = "none";
  }

  const timelineContainer = document.getElementById("schedule-timeline");
  timelineContainer.innerHTML = "";

  if (!sched.items || sched.items.length === 0) {
    timelineContainer.innerHTML = "<p style='color: #CBD5E1;'>No schedule items generated.</p>";
    return;
  }

  // Category Subtitles mapping for exact mockup look
  const catSubtitles = {
    memory: "Morning Warm-up • Preserves verbal & autobiographical recognition",
    language: "Acoustic & Verbal • Rhythmic recall and instrument recognition",
    orientation: "Physical & Spatiotemporal • Gentle motor and circadian reinforcement",
    recognition: "Visual Lead • Preserves family & face recognition",
    reminiscence: "Emotional Grounding • Music, texture and quiet presence",
    problem_solving: "Tactile Task • Category sorting & quiet routine",
    physical: "Gentle Motor • Seated rhythmic movement & stretching"
  };

  sched.items.forEach(item => {
    const itemEl = document.createElement("div");
    itemEl.className = "timeline-item";

    const catKey = (item.category || "memory").toLowerCase();
    const subDesc = catSubtitles[catKey] || "Targeted Cognitive Stimulation & Support";

    itemEl.innerHTML = `
      <div class="timeline-node"></div>
      <div class="timeline-header-row">
        <div class="time-cat-group">
          <span class="item-time">${item.time_or_slot}</span>
          <span class="item-cat-pill">${item.category}</span>
          <span class="item-activity-title">${item.activity}</span>
        </div>
        <div>
          <span class="item-duration-pill">${item.duration_minutes} min</span>
        </div>
      </div>
      <div class="item-sub-desc">${subDesc}</div>
      <div class="caregiver-guide-card">
        <span class="guide-icon">💡</span>
        <div><strong>Caregiver Guide:</strong> ${item.caregiver_note}</div>
      </div>
    `;
    timelineContainer.appendChild(itemEl);
  });
}

// Fetch Next CST Game Task
async function fetchNextGameTask() {
  if (!currentPatientIntake) {
    currentPatientIntake = buildIntakeFromForm();
  }

  try {
    const resp = await fetch(`${API_BASE}/game/next-task`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(currentPatientIntake)
    });

    if (!resp.ok) throw new Error("Game task request failed");

    const task = await resp.json();
    renderGameTask(task);

  } catch (err) {
    console.error("Error fetching game task:", err);
  }
}

// Render Game Task Screen
function renderGameTask(task) {
  document.getElementById("game-bridge-note").innerText = task.domain_bridge_note;
  document.getElementById("game-prompt").innerText = task.prompt_text;
  document.getElementById("game-guidance").innerHTML = `<span class="guide-icon">💡</span><div><strong>Caregiver Guidance:</strong> ${task.caregiver_guidance}</div>`;

  const optionsContainer = document.getElementById("game-options");
  optionsContainer.innerHTML = "";

  const options = task.options || ["Option A", "Option B", "Option C"];
  options.forEach(opt => {
    const btn = document.createElement("button");
    btn.className = "game-choice-btn";
    btn.innerText = opt;
    btn.onclick = () => handleGameChoice(task.task_id, task.category, opt);
    optionsContainer.appendChild(btn);
  });
}

// Handle Patient Choice in Game Task
async function handleGameChoice(taskId, category, selectedOption) {
  try {
    await fetch(`${API_BASE}/game/submit-result`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        patient_id: currentActivePatientId,
        task_id: taskId,
        category: category,
        user_response: selectedOption,
        outcome: "completed",
        timestamp: new Date().toISOString()
      })
    });
  } catch (err) {
    console.error("Error logging game session:", err);
  }

  alert(`👏 Warm effort! Recorded choice: "${selectedOption}". Remember, performance in a single session is not treated as a signal of cognitive decline (Part 2.5 Guardrail).`);

  fetchNextGameTask();
}

// Save Daily Outcome Log
async function handleSaveLog(e) {
  if (e && e.preventDefault) e.preventDefault();

  const logPayload = {
    patient_id: currentActivePatientId,
    activity_name: document.getElementById("log-activity-name").value,
    category: document.getElementById("log-category").value,
    outcome: document.getElementById("log-outcome").value,
    notes: document.getElementById("log-notes").value,
    timestamp: new Date().toISOString()
  };

  try {
    const resp = await fetch(`${API_BASE}/logs`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(logPayload)
    });

    if (resp.ok) {
      alert("Daily outcome log recorded!");
      fetchLogHistory();
    }
  } catch (err) {
    console.error("Error saving log:", err);
  }
}

// Fetch Activity Log History
async function fetchLogHistory() {
  try {
    const resp = await fetch(`${API_BASE}/logs/${currentActivePatientId}`);
    if (!resp.ok) return;

    const logs = await resp.json();
    const container = document.getElementById("log-history-list");
    container.innerHTML = "";

    if (!logs || logs.length === 0) {
      container.innerHTML = "<p style='color: #64748B;'>No activity logs submitted yet today.</p>";
      return;
    }

    logs.forEach(log => {
      const item = document.createElement("div");
      item.style.padding = "0.75rem 1rem";
      item.style.borderBottom = "1px solid #E2E8F0";
      item.innerHTML = `
        <strong>${log.activity_name}</strong> (${log.category}) — 
        <span style="color: var(--accent-emerald-dark); font-weight: 700;">${log.outcome.toUpperCase()}</span>
        <br><small style="color: #64748B;">${log.notes || 'No notes'} • ${new Date(log.timestamp).toLocaleTimeString()}</small>
      `;
      container.appendChild(item);
    });
  } catch (err) {
    console.error("Error loading logs:", err);
  }
}

// Initial Load
document.addEventListener("DOMContentLoaded", () => {
  loadSyntheticPreset(0);
});
