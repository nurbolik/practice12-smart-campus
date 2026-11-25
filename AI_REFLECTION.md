# AI-Use Reflection - Practice 12

I used the DeepSeek Harness coding agent (DeepSeek-V4.1-Flash). It received the shared
requirement, the eight test inputs, the fixed booking data and the acceptance criteria. I
asked it to produce two small implementations: a code-based HTML/JavaScript page and a
config-driven low-code simulation. I also asked it to keep the rule engine separate from the UI
and to make the low-code limitation explicit.

The useful suggestion was to use one shared contract and the same eight test inputs for both
tracks. That made the comparison factual: both implementations return the same reason codes
for T1-T8, and both preserve the booking list. The weak suggestion was to present the
config-driven page as if it were a real Appsmith app. I rejected that because Appsmith/Google
sign-in was unavailable; the page is labelled "LOW-CODE (SIMULATED)" and the report says so.
A second weak point was an early `innerHTML` result renderer; I kept the message construction
fixed and did not interpolate user text, reducing XSS risk.

I personally ran both Node test suites, checked 8/8 for each, opened both pages, compared the
Available and overlap screenshots, and reviewed the input and output paths. The tests changed
my decision about the low-code claim: I can defend functional equivalence, but I cannot claim
a platform evaluation. The code-based track is more portable and easier to secure; the
low-code simulation is faster to assemble but does not prove platform behaviour. Next I would
retry Appsmith/Budibase with an authenticated account, publish a real app, and compare its
permissions and export options rather than only the UI workflow.

Word count: 262.
