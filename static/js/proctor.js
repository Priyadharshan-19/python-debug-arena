// static/js/proctor.js

let violationCount = 0;
const MAX_VIOLATIONS = 3;
let isLogging = false; 

// 1. Detect when a user is legitimately moving between pages
window.addEventListener("beforeunload", () => {
    sessionStorage.setItem('is_navigating', 'true');
});

function enterFullscreen() {
    const elem = document.documentElement;
    if (!document.fullscreenElement && !document.webkitFullscreenElement) {
        elem.requestFullscreen().catch((err) => {
            console.log("Fullscreen requires a click to re-activate.");
        });
    }
}

async function logViolation(reason = "policy_violation") {
    // 🛑 STOP: If the page is currently unloading or loading, ignore the exit
    if (isLogging || sessionStorage.getItem('is_navigating') === 'true') return;
    
    isLogging = true;
    try {
        const response = await fetch('/log_violation', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ reason: reason })
        });

        const data = await response.json();
        violationCount = data.violations;

        if (data.disqualified || violationCount >= MAX_VIOLATIONS) {
            window.location.href = "/disqualified";
            return;
        }
        showSecurityWarning(violationCount);
    } catch (err) {
        console.error("Connection error during logging.");
    } finally {
        setTimeout(() => { isLogging = false; }, 2000);
    }
}

function showSecurityWarning(count) {
    if (document.getElementById('security-warning-overlay')) return;
    const overlay = document.createElement('div');
    overlay.id = 'security-warning-overlay';
    overlay.className = 'fixed inset-0 z-[9999] flex items-center justify-center bg-slate-950/90 backdrop-blur-md';
    overlay.innerHTML = `
        <div class="bg-slate-900 border border-red-500/50 p-10 rounded-3xl text-center shadow-2xl">
            <h2 class="text-2xl font-bold text-white mb-4 uppercase">PROTOCOL VIOLATION</h2>
            <p class="text-slate-400 mb-6">Warning ${count} of ${MAX_VIOLATIONS}. Return to Fullscreen immediately.</p>
            <button onclick="resumeArena()" class="px-8 py-3 bg-red-600 text-white font-bold rounded-lg transition-all">RE-ENTER ARENA</button>
        </div>
    `;
    document.body.appendChild(overlay);
}

window.resumeArena = function() {
    document.getElementById('security-warning-overlay').remove();
    enterFullscreen();
};

/* --- Listeners --- */

document.addEventListener("fullscreenchange", () => {
    if (!document.fullscreenElement && sessionStorage.getItem('is_navigating') !== 'true') {
        logViolation("exit_fullscreen");
    }
});

document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "hidden" && sessionStorage.getItem('is_navigating') !== 'true') {
        logViolation("tab_switch");
    }
});

// Re-activate fullscreen on the first click in the new level
document.addEventListener('click', () => {
    sessionStorage.removeItem('is_navigating'); // Clear the navigation flag
    enterFullscreen();
});