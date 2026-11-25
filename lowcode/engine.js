export function minutesToClock(min) {
  const h = Math.floor(min / 60);
  const m = min % 60;
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`;
}

/**
 * Platform-style expression evaluation. It reads the booking list from the
 * configuration and returns a reason code plus a message; it never writes to
 * the configuration.
 */
export function evaluate(config, input) {
  const start = Number(input.start);
  const duration = Number(input.duration);
  const blocked = Boolean(input.blocked);

  if (!Number.isInteger(start) || !Number.isInteger(duration) || duration <= 0) {
    return { available: false, reasonCode: 'INVALID_DURATION', message: 'Duration must be a whole number greater than zero.' };
  }
  if (start <= config.currentTime) {
    return { available: false, reasonCode: 'PAST_START', message: `Start time must be after ${minutesToClock(config.currentTime)}.` };
  }
  if (duration > 120) {
    return { available: false, reasonCode: 'TOO_LONG', message: 'Duration must be at most 120 minutes.' };
  }
  if (blocked) {
    return { available: false, reasonCode: 'BLOCKED', message: 'The room is blocked for the requested time.' };
  }
  const end = start + duration;
  const conflict = config.bookings.find((booking) => start < booking.end && end > booking.start);
  if (conflict) {
    return {
      available: false,
      reasonCode: 'OVERLAP',
      message: `Overlap with existing booking ${conflict.id} (${minutesToClock(conflict.start)}-${minutesToClock(conflict.end)}).`,
    };
  }
  return { available: true, reasonCode: 'AVAILABLE', message: `Available from ${minutesToClock(start)} for ${duration} minutes.` };
}
