import { evaluate, minutesToClock } from './engine.js';

const sample = document.querySelector('#sample');
const fields = document.querySelector('#fields');
const form = document.querySelector('#form');
const blocked = document.querySelector('#blocked');
const resultBox = document.querySelector('#result');
let config;

function renderSample() {
  const [first, second] = config.bookings;
  sample.innerHTML = `
    <div><span>Current time</span><b>${config.currentTime} (${minutesToClock(config.currentTime)})</b></div>
    <div><span>Booking 1</span><b>${first.start}-${first.end} (${minutesToClock(first.start)}-${minutesToClock(first.end)})</b></div>
    <div><span>Booking 2</span><b>${second.start}-${second.end} (${minutesToClock(second.start)}-${minutesToClock(second.end)})</b></div>`;
}

function renderFields() {
  fields.innerHTML = config.fields.map((field) => `
    <div>
      <label for="${field.id}">${field.label}</label>
      <input id="${field.id}" type="number" min="0" max="1440" value="${field.default}" />
    </div>`).join('');
}

function check() {
  const input = { start: document.querySelector('#start').value, duration: document.querySelector('#duration').value, blocked: blocked.checked };
  const out = evaluate(config, input);
  resultBox.className = out.available ? 'available' : 'unavailable';
  resultBox.innerHTML = `<strong>${out.available ? 'Available' : 'Unavailable'}</strong>${out.message}`;
}

async function boot() {
  config = await fetch('./config.json').then((response) => response.json());
  renderSample();
  renderFields();
  form.addEventListener('submit', (event) => { event.preventDefault(); check(); });
  const params = new URLSearchParams(location.search);
  if (params.get('auto') === '1') {
    document.querySelector('#start').value = params.get('start') ?? '660';
    document.querySelector('#duration').value = params.get('duration') ?? '60';
    blocked.checked = params.get('blocked') === '1';
    check();
  } else {
    resultBox.textContent = 'Enter a time and press Check availability.';
  }
}

boot();
