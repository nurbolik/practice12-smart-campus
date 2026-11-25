import test from 'node:test';
import assert from 'node:assert/strict';
import { checkAvailability, BOOKINGS } from '../rule.js';

test('T1 valid free interval -> Available', () => {
  const r = checkAvailability({ start: 660, duration: 60 });
  assert.equal(r.available, true);
  assert.equal(r.reasonCode, 'AVAILABLE');
});

test('T2 overlap with existing booking -> Unavailable', () => {
  const r = checkAvailability({ start: 630, duration: 60 });
  assert.equal(r.available, false);
  assert.equal(r.reasonCode, 'OVERLAP');
});

test('T3 blocked room -> Unavailable', () => {
  const r = checkAvailability({ start: 660, duration: 60, blocked: true });
  assert.equal(r.available, false);
  assert.equal(r.reasonCode, 'BLOCKED');
});

test('T4 duration = 0 -> validation error', () => {
  const r = checkAvailability({ start: 660, duration: 0 });
  assert.equal(r.available, false);
  assert.equal(r.reasonCode, 'INVALID_DURATION');
});

test('T5 duration = 121 -> validation error', () => {
  const r = checkAvailability({ start: 660, duration: 121 });
  assert.equal(r.available, false);
  assert.equal(r.reasonCode, 'TOO_LONG');
});

test('T6 past start time -> validation error', () => {
  const r = checkAvailability({ start: 500, duration: 60 });
  assert.equal(r.available, false);
  assert.equal(r.reasonCode, 'PAST_START');
});

test('T7 adjacent non-overlapping interval -> Available', () => {
  const r = checkAvailability({ start: 780, duration: 60 });
  assert.equal(r.available, true);
  assert.equal(r.reasonCode, 'AVAILABLE');
});

test('T8 booking data unchanged after checks', () => {
  const before = JSON.stringify(BOOKINGS);
  checkAvailability({ start: 660, duration: 60 });
  checkAvailability({ start: 630, duration: 60 });
  checkAvailability({ start: 780, duration: 60 });
  assert.equal(JSON.stringify(BOOKINGS), before);
  assert.equal(BOOKINGS.length, 2);
});
