import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { evaluate } from '../engine.js';

const config = JSON.parse(await readFile(new URL('../config.json', import.meta.url), 'utf8'));

test('L1 valid free interval -> Available', () => {
  const r = evaluate(config, { start: 660, duration: 60 });
  assert.equal(r.available, true);
  assert.equal(r.reasonCode, 'AVAILABLE');
});

test('L2 overlap -> Unavailable', () => {
  const r = evaluate(config, { start: 630, duration: 60 });
  assert.equal(r.available, false);
  assert.equal(r.reasonCode, 'OVERLAP');
});

test('L3 blocked -> Unavailable', () => {
  const r = evaluate(config, { start: 660, duration: 60, blocked: true });
  assert.equal(r.available, false);
  assert.equal(r.reasonCode, 'BLOCKED');
});

test('L4 duration 0 -> validation', () => {
  const r = evaluate(config, { start: 660, duration: 0 });
  assert.equal(r.reasonCode, 'INVALID_DURATION');
});

test('L5 duration 121 -> validation', () => {
  const r = evaluate(config, { start: 660, duration: 121 });
  assert.equal(r.reasonCode, 'TOO_LONG');
});

test('L6 past start -> validation', () => {
  const r = evaluate(config, { start: 500, duration: 60 });
  assert.equal(r.reasonCode, 'PAST_START');
});

test('L7 adjacent interval -> Available', () => {
  const r = evaluate(config, { start: 780, duration: 60 });
  assert.equal(r.available, true);
});

test('L8 config unchanged', () => {
  const before = JSON.stringify(config);
  evaluate(config, { start: 660, duration: 60 });
  evaluate(config, { start: 630, duration: 60 });
  assert.equal(JSON.stringify(config), before);
});
