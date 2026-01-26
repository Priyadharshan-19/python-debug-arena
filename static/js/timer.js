// static/js/timer.js
let seconds = 0;
const timerDisplay = document.getElementById('timer-display');

setInterval(() => {
    seconds++;
    let mins = Math.floor(seconds / 60);
    let secs = seconds % 60;
    timerDisplay.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}, 1000);