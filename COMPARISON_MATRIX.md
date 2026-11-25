# Comparison Matrix and Recommendation

| Criterion | Code-based | Low-code (simulated) |
|---|---|---|
| Functional tests | 8/8 | 8/8 |
| Build + repair time (observed, approximate) | 65 min | 45 min |
| Customization | Full control; rule, UI and tests are separate files | Config changes are quick; any new rule needs the generic engine |
| Security controls | Explicit validation, `textContent`-based output, no secrets; CSP can be added | Same JS engine in this simulation; a real platform would add its own permissions and connectors |
| Versioning / portability | Plain Git; static export; runs anywhere | JSON config + renderer; portable in this simulation, but a real platform export may be limited |
| Ongoing cost | 0 (static hosting) | 0 in this simulation; real platform free tiers vary |
| Maintainability | More files, explicit boundaries | Less UI code, but the engine is shared and the platform is not real |
| Requirement coverage | All 6 AC | All 6 AC |
| Unresolved defects | None found in the 8 cases | None found in the 8 cases |
| Evidence | `code/`, `tests/rule.test.mjs`, screenshots | `lowcode/`, `tests/engine.test.mjs`, screenshots |

## Recommendation

Use the **code-based** implementation for this assignment and for any real deployment: it has
the clearest security boundary, full version control, no platform lock-in and no dependency on
an account. A low-code builder is a reasonable choice for a quick internal prototype when the
team accepts the platform's permissions, export limits and per-seat cost.

The low-code result here is a **simulation** because Appsmith/Google sign-in was unavailable;
it should not be presented as a commercial platform evaluation.

## Measured vs impression

The times above are approximate wall-clock observations from this session, not a controlled
stopwatch study. Functional counts, reason codes and screenshots are measured artifacts.
