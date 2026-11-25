# Shared Requirement and Acceptance Criteria

## User story

As a student, I want to check whether one campus room is free for a future start time and a
duration, so that I can choose a valid slot without changing existing bookings.

## Inputs

- `start` - minutes from midnight, integer, must be > 540.
- `duration` - minutes, integer, > 0 and <= 120.
- `blocked` - boolean; true means the room is blocked.
- Fictional bookings: B001 600-660, B002 720-780. Read-only.
- Current time: 540 (09:00).

## Outputs

- `available` - boolean.
- `reasonCode` - `AVAILABLE`, `OVERLAP`, `BLOCKED`, `PAST_START`, `INVALID_DURATION`, `TOO_LONG`.
- `message` - visible, understandable text.

## Acceptance criteria

- **AC1:** start time must be in the future (> 540).
- **AC2:** duration must be > 0 and <= 120 minutes.
- **AC3:** an interval overlapping a booking is unavailable.
- **AC4:** a blocked room is unavailable.
- **AC5:** display a clear decision and never change the booking data.
- **AC6:** invalid input receives understandable feedback.

## Test inputs (prepared before implementation)

| ID | Start | Duration | Blocked | Expected |
|---|---|---|---|---|
| T1 | 660 | 60 | no | Available |
| T2 | 630 | 60 | no | Unavailable - OVERLAP |
| T3 | 660 | 60 | yes | Unavailable - BLOCKED |
| T4 | 660 | 0 | no | Validation - INVALID_DURATION |
| T5 | 660 | 121 | no | Validation - TOO_LONG |
| T6 | 500 | 60 | no | Validation - PAST_START |
| T7 | 780 | 60 | no | Available (adjacent) |
| T8 | 660 | 60 | no | Booking array unchanged |
