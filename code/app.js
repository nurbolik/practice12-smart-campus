import { checkAvailability, BOOKINGS, CURRENT_TIME } from './rule.js';

const form = document.querySelector('#form');
const startInput = document.querySelector('#start');
const durationInput = document.querySelector('#duration');
const blockedInput = document.querySelector('#blocked');
const resultBox = document.querySelector('#result');

function render(result) {
  resultBox.className = result.available ? 'available' : 'unavailable';
  const title = result.available ? 'Available' : 'Unavailable';
  resultBox.innerHTML = `<strong>${title}</strong>${result.message}`;
}

function check() {
  const start = Number(startInput.value);
  const duration = Number(durationInput.value);
  render(checkAvailability({
    start,
    duration,
    blocked: blockedInput.checked,
    bookings: BOOKINGS,
    currentTime: CURRENT_TIME,
  }));
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  check();
});

const params = new URLSearchParams(location.search);
if (params.get('auto') === '1') {
  startInput.value = params.get('start') ?? '660';
  durationInput.value = params.get('duration') ?? '60';
  blockedInput.checked = params.get('blocked') === '1';
  check();
}
