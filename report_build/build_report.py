# -*- coding: utf-8 -*-
import os, re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = r"C:\Users\abunu\Documents\Practice12_Abu_Nurbol"
SHOTS = os.path.join(ROOT, "screenshots")
OUT = os.path.join(ROOT, "report")
os.makedirs(OUT, exist_ok=True)
TEAL = RGBColor(0x0F, 0x76, 0x6E); DARK = RGBColor(0x11, 0x18, 0x27); GRAY = RGBColor(0x6B, 0x72, 0x80)
TEAL_HEX = "0F766E"; LIGHT_HEX = "F0FDFA"; CODE_HEX = "F3F4F6"; BORDER_HEX = "D1D5DB"

doc = Document(); sec = doc.sections[0]
sec.page_width = Cm(21.0); sec.page_height = Cm(29.7)
sec.top_margin = Cm(1.55); sec.bottom_margin = Cm(1.45); sec.left_margin = Cm(1.75); sec.right_margin = Cm(1.75)
sec.header_distance = Cm(0.7); sec.footer_distance = Cm(0.6); sec.different_first_page_header_footer = True
normal = doc.styles["Normal"]; normal.font.name = "Calibri"; normal.font.size = Pt(9.7); normal.font.color.rgb = DARK
normal.paragraph_format.space_after = Pt(3.4); normal.paragraph_format.line_spacing = 1.04
for name, size, color in [("Heading 1", 13.0, TEAL), ("Heading 2", 10.4, DARK)]:
    st = doc.styles[name]; st.font.name = "Calibri"; st.font.size = Pt(size); st.font.bold = True; st.font.color.rgb = color
    st.paragraph_format.space_before = Pt(8); st.paragraph_format.space_after = Pt(3); st.paragraph_format.keep_with_next = True

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:fill"), fill); tcPr.append(shd)
def rich(p, text, size=None):
    for part in re.split(r"(\*\*.+?\*\*|`.+?`)", text):
        if not part: continue
        if part.startswith("**") and part.endswith("**"): r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = p.add_run(part[1:-1]); r.font.name = "Liberation Mono"; r.font.size = Pt((size or 9.7)-0.8)
        else: r = p.add_run(part)
        if size: r.font.size = Pt(size)
def para(text, size=None, after=3.0):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after); rich(p, text, size); return p
def figure(filename, width, cap):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(1); p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(os.path.join(SHOTS, filename), width=Cm(width))
    c = doc.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER; c.paragraph_format.space_after = Pt(5)
    r = c.add_run(cap); r.italic = True; r.font.size = Pt(7.8); r.font.color.rgb = GRAY
def table(headers, rows, widths, fs=7.6):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.autofit = False
    for i,w in enumerate(widths): t.columns[i].width = Cm(w)
    for i,h in enumerate(headers):
        c=t.rows[0].cells[i]; c.width=Cm(widths[i]); c.text=""; p=c.paragraphs[0]; p.paragraph_format.space_after=Pt(0)
        r=p.add_run(h); r.bold=True; r.font.size=Pt(fs); r.font.color.rgb=RGBColor(255,255,255); shade(c,TEAL_HEX)
    trPr=t.rows[0]._tr.get_or_add_trPr(); hdr=OxmlElement("w:tblHeader"); hdr.set(qn("w:val"),"true"); trPr.append(hdr)
    for ri,row in enumerate(rows):
        cells=t.add_row().cells
        for i,val in enumerate(row):
            cells[i].width=Cm(widths[i]); cells[i].text=""; p=cells[i].paragraphs[0]; p.paragraph_format.space_after=Pt(0); p.paragraph_format.line_spacing=1.0
            rich(p,str(val),fs)
            if ri%2==1: shade(cells[i],"F9FAFB")
def h1(text):
    h=doc.add_heading(level=1); h.add_run(text)
def page_field(p):
    run=p.add_run(); f1=OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"),"begin"); it=OxmlElement("w:instrText"); it.set(qn("xml:space"),"preserve"); it.text=" PAGE "; f2=OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"),"end"); run._r.append(f1); run._r.append(it); run._r.append(f2)

hdr=sec.header.paragraphs[0]; hdr.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=hdr.add_run("Practice #12 | Code-based vs low-code | Abu Nurbol | 24B031597"); r.font.size=Pt(7.5); r.font.color.rgb=GRAY
ftr=sec.footer.paragraphs[0]; ftr.alignment=WD_ALIGN_PARAGRAPH.CENTER
r=ftr.add_run("Software Engineering - Practice #12 | 25 November 2026 | Page "); r.font.size=Pt(7.5); r.font.color.rgb=GRAY
page_field(ftr)
for r in ftr.runs: r.font.size=Pt(7.5); r.font.color.rgb=GRAY

p=doc.add_paragraph(); r=p.add_run("SOFTWARE ENGINEERING | PRACTICE WORK #12"); r.bold=True; r.font.size=Pt(9.2); r.font.color.rgb=TEAL; p.paragraph_format.space_after=Pt(2)
p=doc.add_paragraph(); r=p.add_run("Same Feature, Two Tracks: Code vs Low-code"); r.bold=True; r.font.size=Pt(22); r.font.color.rgb=DARK; p.paragraph_format.space_after=Pt(3)
p=doc.add_paragraph(); r=p.add_run("Shared contract, eight identical tests, comparison matrix and a documented simulation limit"); r.font.size=Pt(10); r.font.color.rgb=GRAY; p.paragraph_format.space_after=Pt(6)
table(["Student","ID","Subject","Date","Repository"], [["Abu Nurbol","24B031597","Software Engineering","25 November 2026","github.com/nurbolik/practice12-smart-campus"]], [3.2,2.2,4.0,3.4,4.5], 7.8)
doc.add_paragraph()

p=doc.add_paragraph(); pPr=p._p.get_or_add_pPr(); shd=OxmlElement("w:shd"); shd.set(qn("w:val"),"clear"); shd.set(qn("w:fill"),LIGHT_HEX); pPr.append(shd)
bdr=OxmlElement("w:pBdr"); left=OxmlElement("w:left"); left.set(qn("w:val"),"single"); left.set(qn("w:sz"),"18"); left.set(qn("w:space"),"8"); left.set(qn("w:color"),TEAL_HEX); bdr.append(left); pPr.append(bdr)
p.paragraph_format.left_indent=Cm(0.25); p.paragraph_format.right_indent=Cm(0.15); p.paragraph_format.space_after=Pt(6)
r=p.add_run("Summary. "); r.bold=True; r.font.size=Pt(9.7); r.font.color.rgb=TEAL
r=p.add_run("I built the same one-room availability checker twice: a code-based HTML/JavaScript page with a separate rule module, and a config-driven low-code simulation. Both pass all eight shared tests (8/8) and preserve the fictional bookings. The code-based track is more portable, easier to secure and versioned in Git; the low-code simulation is faster to assemble but is not a commercial platform. The report labels that limitation explicitly, compares effort, customization, security, portability and cost, and recommends the code-based track for this assignment.")
r.font.size=Pt(9.7)

h1("1. Shared requirement and acceptance criteria")
para("**User story:** as a student, I want to check one campus room for a future start time and duration, so that I can choose a valid slot without changing existing bookings. **Inputs:** start (minutes), duration, blocked flag, fixed bookings B001 600-660 and B002 720-780, current time 540. **Outputs:** available boolean, reason code and visible message.")
table(["ID","Criterion","Code evidence","Low-code evidence"], [
["AC1","Start must be in the future (>540)","rule.js PAST_START; T6","engine.js PAST_START; L6"],
["AC2","Duration >0 and <=120","rule.js INVALID_DURATION/TOO_LONG; T4/T5","engine.js same; L4/L5"],
["AC3","Overlap is unavailable","rule.js OVERLAP; T2","engine.js OVERLAP; L2"],
["AC4","Blocked room unavailable","rule.js BLOCKED; T3","engine.js BLOCKED; L3"],
["AC5","Clear decision, bookings unchanged","UI message; T8","config read-only; L8"],
["AC6","Invalid input feedback","message strings; T4-T6","message strings; L4-L6"]], [1.2,5.8,5.0,4.8], 7.4)
para("The full shared sheet is in `SHARED_REQUIREMENTS.md`; the test inputs were fixed before either implementation.")

h1("2. Code-based implementation")
para("`code/rule.js` is a pure function; `code/app.js` binds the form to it; `code/index.html` is the UI. Validation, availability calculation and display are separate. The UI uses a labelled result panel with `role=\"status\"` and `aria-live=\"polite\"`. The page is responsive at narrow width.")
figure("code-available.png", 13.5, "Figure 1. Code-based page: 660 + 60 min -> Available; B002 starts at 720, so touching is allowed.")
para("The rule rejects invalid duration, past start, duration over 120, blocked room and overlap, in that order. It reads a frozen `BOOKINGS` array and never writes to it. Eight tests run with `node --test`; the observed result is **8/8**.")

h1("3. Low-code track and its honest limit")
para("Appsmith was chosen as the low-code platform. The free cloud account opened, but the Google sign-in required a password that was not available in this environment; the editor could not be used reliably. Rather than fabricate a published Appsmith app, I built a **config-driven low-code simulation**: `lowcode/config.json` defines the fields, bookings and labels; `lowcode/renderer.js` builds the form from that config; `lowcode/engine.js` evaluates the same contract. The page is labelled **LOW-CODE (SIMULATED)** and explains the limit in the UI.")
figure("lowcode-available.png", 13.5, "Figure 2. Low-code simulation: same inputs, same Available result, explicit simulation label.")
para("This is **not** a commercial platform evaluation. It demonstrates the low-code workflow (configuration instead of hand-built UI) and the same eight behaviours, but it does not prove Appsmith permissions, connectors, export or hosting. The assignment allows clearly labelled simulated low-code behaviour; this limitation is stated here, in `README.md` and on the page.")

h1("4. Eight identical tests")
table(["ID","Input","Expected","Code","Low-code"], [
["T1","660 / 60 / no","Available","Pass","Pass"],
["T2","630 / 60 / no","OVERLAP","Pass","Pass"],
["T3","660 / 60 / yes","BLOCKED","Pass","Pass"],
["T4","660 / 0 / no","INVALID_DURATION","Pass","Pass"],
["T5","660 / 121 / no","TOO_LONG","Pass","Pass"],
["T6","500 / 60 / no","PAST_START","Pass","Pass"],
["T7","780 / 60 / no","Available (adjacent)","Pass","Pass"],
["T8","660 / 60 / no","Bookings unchanged","Pass","Pass"]], [1.2,5.0,5.2,2.6,2.8], 7.6)
para("Totals: **code 8/8, low-code 8/8**, no failed or skipped case. The raw test commands are `node --test --test-reporter=spec tests/rule.test.mjs` and `node --test --test-reporter=spec tests/engine.test.mjs`.")

h1("5. Comparison matrix and recommendation")
table(["Criterion","Code-based","Low-code (simulated)"], [
["Functional tests","8/8","8/8"],
["Build + repair time (approx.)","65 min","45 min"],
["Customization","Full control; separate rule/UI/tests","Fast config changes; new rules need the shared engine"],
["Security controls","Explicit validation, fixed messages, no secrets","Same simulation; real platform permissions not evaluated"],
["Versioning / portability","Git + static files; runs anywhere","Config + renderer; real platform export not tested"],
["Ongoing cost","0","0 in simulation; real free tiers vary"],
["Requirement coverage","All 6 AC","All 6 AC"],
["Unresolved defects","None in T1-T8","None in T1-T8"]], [4.4,5.8,5.8], 7.5)
para("**Recommendation:** use the code-based track for this assignment and for a real deployment. It has the clearest security boundary, full Git history, no platform lock-in and no account dependency. A low-code builder is reasonable for a quick internal prototype if the team accepts its permissions, export limits and per-seat pricing. The low-code result here is a simulation, not a platform recommendation.")
para("**Measured vs impression:** functional counts, reason codes and screenshots are measured; the 65/45-minute figures are approximate wall-clock observations, not a controlled stopwatch study.")

h1("6. Security review and AI reflection")
table(["Check","Code-based","Low-code simulation"], [
["Input validation","Integer/duration/start guards; T4-T6","Same engine; L4-L6"],
["Output handling","Fixed message strings; no user text in HTML","Same"],
["Secrets","None","None"],
["Dependencies","No third-party JS","No third-party JS"],
["Permissions / sharing","Static public page","Simulated static page; real platform not evaluated"],
["DAST","Manual form tests + automated rule tests","Same"]], [4.2,5.8,5.8], 7.5)
para("No SQL, server, login, personal data or secret is present. The low-code platform's real permissions/connectors were not reviewed because the account was not usable; this is the main unresolved security limitation.")
para("I used DeepSeek Harness (DeepSeek-V4.1-Flash). It received the shared requirement, fixed bookings, eight test inputs and acceptance criteria, and was asked for two small implementations. The useful suggestion was one shared contract and one test set for both tracks, which made the comparison factual. The weak suggestion was to present the config-driven page as a real Appsmith app; I rejected that and labelled it simulated. I personally ran both Node suites (8/8 each), checked the Available and overlap screenshots, and reviewed input/output handling. Tests changed my conclusion: functional equivalence is supported, but platform equivalence is not. Next I would retry Appsmith/Budibase with an authenticated account, publish a real app and compare its permissions and export options.")

h1("7. Submission")
para("**To:** b.azimkhanov@kbtu.kz (as written in the Practice #12 deck). **Subject:** `AI-Driven Software Engineering Practice #13, Abu Nurbol, 24B031597`. Include: this report, GitHub repository link, live demos, both screenshots, shared requirements, eight-case test table, comparison matrix, security checklist and AI reflection. No OneDrive, WinRAR or ZIP.")
para("**Links:** repository https://github.com/nurbolik/practice12-smart-campus; code demo https://nurbolik.github.io/practice12-smart-campus/code/; low-code simulation https://nurbolik.github.io/practice12-smart-campus/lowcode/.")
para("**AI-use record:** tool/model above; prompts and outputs are in `AI_EVIDENCE.md`; all test counts are from actual local runs; the low-code limitation is explicitly labelled.")

doc.core_properties.title = "Practice #12 - Code-based vs Low-code"
doc.core_properties.author = "Abu Nurbol"
out = os.path.join(OUT, "Practice12_Abu_Nurbol_Report.docx")
doc.save(out)
print("saved", out)
