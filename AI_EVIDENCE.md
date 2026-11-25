# AI Evidence - Practice 12

Tool: DeepSeek Harness coding agent
Model: DeepSeek-V4.1-Flash
Date: 25 November 2026

## Prompt summary

"Implement the same Smart Campus availability contract twice: (1) a code-based HTML/JS page
with a pure rule module and eight Node tests; (2) a low-code track. Use fixed bookings
600-660 and 720-780, current time 540, start+duration+blocked inputs, and the six acceptance
criteria. Separate validation, rule and UI. Label any low-code limitation honestly."

## Output used

- `code/rule.js`, `code/app.js`, `code/index.html`, `code/tests/rule.test.mjs`.
- `lowcode/config.json`, `lowcode/engine.js`, `lowcode/renderer.js`, `lowcode/tests/engine.test.mjs`.
- `SHARED_REQUIREMENTS.md`, `TEST_TABLE.md`, `COMPARISON_MATRIX.md`, `SECURITY_CHECKLIST.md`.

## Problems found and changes

- Appsmith/Google sign-in required a password that was unavailable; the editor could not be
  used safely. I rejected pretending a published Appsmith app existed, built a clearly
  labelled config-driven simulation and recorded the limitation.
- The first UI idea interpolated user text into `innerHTML`; I kept output messages fixed and
  did not inject input, reducing XSS risk.
- The low-code and code-based rules are intentionally separate files; a shared engine would
  hide the duplication that a real platform would also introduce.

## Human verification

- Ran both Node suites: 8/8 each.
- Opened both pages with `?auto=1` and checked Available and overlap states.
- Reviewed the directories for secrets/personal data: none.
- Not run: real Appsmith/Budibase app, automated SAST/DAST, GitHub Pages after deployment.
