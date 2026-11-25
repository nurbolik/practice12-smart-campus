# Practice 12 - Code-based vs Low-code

Student: Abu Nurbol (24B031597)
Date: 25 November 2026
AI assistant: DeepSeek Harness coding agent (DeepSeek-V4.1-Flash)

## What is here

| Folder | Track | Status |
|---|---|---|
| `code/` | Code-based HTML + JavaScript | Working; 8/8 tests |
| `lowcode/` | Low-code **simulation** (config-driven) | Working; 8/8 tests; explicitly labelled simulated |
| `report/` | Comparison report PDF | - |

The low-code track is **not** a published Appsmith/Budibase app. Appsmith/Google sign-in
was unavailable in this environment, so I built a config-driven simulation of the same
workflow and labelled it as such, as the practice allows for incomplete/simulated behavior.

## Shared contract

- Start time is minutes from midnight; it must be after 540 (09:00).
- Duration must be greater than 0 and at most 120 minutes.
- Bookings are read-only: B001 600-660 and B002 720-780.
- Blocked room is unavailable.
- Output: `available` boolean, `reasonCode`, and a visible message.
- Checks never mutate the booking data.

## Run locally

```bash
# code-based
cd code
python -m http.server 5180
# open http://127.0.0.1:5180/code/

# low-code simulation
python -m http.server 5180
# open http://127.0.0.1:5180/lowcode/
```

## Tests

```bash
cd code && node --test --test-reporter=spec tests/rule.test.mjs
cd lowcode && node --test --test-reporter=spec tests/engine.test.mjs
```

Both tracks: 8 tests, 8 passed, 0 failed.

## Public links

- Repository: https://github.com/nurbolik/practice12-smart-campus
- Code-based demo: https://nurbolik.github.io/practice12-smart-campus/code/
- Low-code simulation: https://nurbolik.github.io/practice12-smart-campus/lowcode/

## Known limitations

- Low-code is simulated, not a real platform export; no Appsmith/Budibase account was available.
- No real authentication, database or personal data.
- UI is a single page; no framework.
- GitHub Pages serves static files; no server-side code.
