export const CURRENT_TIME = 540;
export const BOOKINGS = Object.freeze([
  Object.freeze({ id: 'B001', start: 600, end: 660 }),
  Object.freeze({ id: 'B002', start: 720, end: 780 }),
]);

export function minutesToClock(min) {
  const h = Math.floor(min / 60);
  const m = min % 60;
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`;
}

/**
 * Deterministic availability rule shared by the code-based and the simulated
 * low-code page. The booking array is read-only and never mutated.
 */
export function checkAvailability({ start, duration, blocked = false, bookings = BOOKINGS, currentTime = CURRENT_TIME }) {
  if (!Number.isInteger(start) || !Number.isInteger(duration) || duration <= 0) {
    return { available: false, reasonCode: 'INVALID_DURATION', message: 'Duration must be a whole number greater than zero.' };
  }
  if (start <= currentTime) {
    return { available: false, reasonCode: 'PAST_START', message: `Start time must be after ${minutesToClock(currentTime)} (${currentTime}).` };
  }
  if (duration > 120) {
    return { available: false, reasonCode: 'TOO_LONG', message: 'Duration must be at most 120 minutes.' };
  }
  if (blocked) {
    return { available: false, reasonCode: 'BLOCKED', message: 'The room is blocked for the requested time.' };
  }
  const end = start + duration;
  const conflict = bookings.find((booking) => start < booking.end && end > booking.start);
  if (conflict) {
    return {
      available: false,
      reasonCode: 'OVERLAP',
      message: `Overlap with existing booking ${conflict.id} (${minutesToClock(conflict.start)}-${minutesToClock(conflict.end)}).`,
    };
  }
  return {
    available: true,
    reasonCode: 'AVAILABLE',
    message: `Available from ${minutesToClock(start)} for ${duration} minutes.`,
  };
}
