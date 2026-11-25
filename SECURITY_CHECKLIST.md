# Security Checklist - Practice 12

| Check | Code-based | Low-code (simulated) |
|---|---|---|
| Input validation | `Number.isInteger`, duration > 0, start > 540, duration <= 120 | Same engine; config values validated at run time |
| Output handling | `innerHTML` only for fixed messages; user input is not interpolated | Same; no user text is inserted as HTML |
| Injection / XSS | No SQL, no server, no user HTML; static page | Same in the simulation; a real platform would need its own XSS/permission review |
| Secrets | None; no API key, token or `.env` | None |
| Permissions / sharing | Static public page, read-only | Simulated public page; a real Appsmith app would need public-app permissions review |
| Connectors | None | None |
| Dependency / SCA | No third-party JS libraries | No third-party JS libraries |
| Platform updates | Browser/OS + static host | Real platform would own updates; simulation is static |
| Safe DAST check | Manual form tests: valid, overlap, blocked, invalid, past, adjacent | Same |
| Logging | No personal data logged | Same |
| Third-party scanning | Not performed; no authorization to scan a third party | Not performed |

## Runtime checks performed

- T1/T2/T3/T4/T5/T6/T7/T8 through the automated suites.
- Manual UI check of the Available and Unavailable messages.
- No secrets, tokens or personal data in either folder.

## Not performed

- Automated SAST/DAST tools.
- Real Appsmith/Budibase permission and connector review (no account access).
- Penetration testing of GitHub Pages.
