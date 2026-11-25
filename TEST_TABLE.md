# Eight-Case Test Table

Both implementations were run with the same inputs. "Observed" is the actual result from the
test suite and the UI screenshots.

| ID | Input (start, duration, blocked) | Expected | Code-based observed | Low-code observed |
|---|---|---|---|---|
| T1 | 660, 60, no | Available | Pass - AVAILABLE | Pass - AVAILABLE |
| T2 | 630, 60, no | Unavailable - overlap | Pass - OVERLAP (B001) | Pass - OVERLAP (B001) |
| T3 | 660, 60, yes | Unavailable - blocked | Pass - BLOCKED | Pass - BLOCKED |
| T4 | 660, 0, no | Validation error | Pass - INVALID_DURATION | Pass - INVALID_DURATION |
| T5 | 660, 121, no | Validation error | Pass - TOO_LONG | Pass - TOO_LONG |
| T6 | 500, 60, no | Validation error | Pass - PAST_START | Pass - PAST_START |
| T7 | 780, 60, no | Available (adjacent) | Pass - AVAILABLE | Pass - AVAILABLE |
| T8 | 660, 60, no | Bookings unchanged | Pass - 2 bookings unchanged | Pass - config unchanged |

Totals: **code-based 8/8, low-code 8/8**. No failed case; no test was skipped.
The low-code UI is a config-driven simulation, so its "platform" result is not a commercial
builder claim.
