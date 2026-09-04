# rockCV - Professional Resume Builder

**rockCV** is a modern, locally hosted FastAPI web application that allows users to create elegant, professional, ATS-friendly resumes for any industry — from Accounting and Finance to IT and Healthcare.

The system runs completely locally without external CDNs, offering real-time side-by-side document previews, industry-tailored Jinja2 templates, optional LinkedIn and GitHub profile imports, JSON import/export, and single-click A4 PDF print capability.

---

## 🌟 Key Features

- 💼 **Industry-Specific Professional Templates**:
  - **IT & Tech (`modern_tech`)**: Clean, code-first layout for Software Engineers, Systems Architects, and Data Scientists.
  - **Accounting & Corporate (`accounting_corporate`)**: Formal, executive-aligned design tailored for CPAs, Financial Analysts, and Auditors.
  - **Executive & Operations (`executive_leadership`)**: Bold slate header structure for Directors, Managers, and Operations Leaders.
  - **Marketing & Creative (`creative_portfolio`)**: Accent grid sidebar design for Content Strategists, Growth Lead, and Designers.
  - **Healthcare & General (`classic_professional`)**: Timeless serif typography for Clinical Specialists, RNs, and General Professionals.
- ⚡ **Real-Time Live Document Preview**: Immediate split-screen iframe rendering as form fields are updated.
- 🔗 **Optional Profile Importer (LinkedIn & GitHub)**: Users can supply LinkedIn or GitHub links to automatically extract public projects and profile details into their CV.
- 📁 **JSON Import & Export**: Save and reload complete resume configurations locally at any time.
- 🖨️ **Print & PDF Generation**: Styled `@media print` rules for clean single/multi-page A4/Letter PDF generation.
- 🔒 **100% Offline Capable**: Bundled local Tailwind CSS stylesheet ensures full functionality without external network dependencies.

---

## 🏗️ Project Architecture & Directory Structure

```text
rockCV/
├── app/
│   ├── main.py                  # FastAPI application & API route handlers
│   ├── profile_importer.py      # Profile parsing logic (LinkedIn & GitHub API)
│   ├── models/
│   │   ├── resume.py            # Pydantic schemas for Resume data models
│   │   └── samples.py           # Pre-configured sample resume datasets
│   ├── static/
│   │   ├── css/
│   │   │   └── tailwind.min.css # Bundled Tailwind CSS asset
│   │   └── js/
│   │       └── app.js           # Client-side dynamic forms & preview sync
│   └── templates/
│       ├── builder.html         # Main web application user interface
│       └── resume_templates/    # Industry Jinja2 HTML templates
│           ├── accounting_corporate.html
│           ├── classic_professional.html
│           ├── creative_portfolio.html
│           ├── executive_leadership.html
│           └── modern_tech.html
├── tests/
│   └── test_main.py             # Pytest test suite
├── requirements.txt             # Python dependencies
└── README.md                    # System documentation
```

---

## 🚀 Installation & Getting Started

### Prerequisites
- Python 3.10+

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/user/rockCV.git
   cd rockCV
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the application server**:
   ```bash
   PYTHONPATH=. uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

4. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## 📡 API Reference

| Endpoint | Method | Description |
|---|---|---|
| `/` | `GET` | Renders the main rockCV Builder UI. |
| `/api/samples` | `GET` | Returns list of available sample industries and template mappings. |
| `/api/samples/{sample_id}` | `GET` | Fetches full sample resume data for a specific industry (e.g., `accounting`, `it`, `executive`, `marketing`, `healthcare`). |
| `/api/render` | `POST` | Renders and returns HTML for selected Jinja2 template given a `Resume` payload. |
| `/api/export` | `POST` | Validates and returns structured JSON for download/backup. |
| `/api/import-profile` | `POST` | Parses optional LinkedIn & GitHub profile links and returns populated Resume JSON. |

---

## 🧪 Automated Testing & Final Test Execution Snapshot

The system includes a comprehensive `pytest` test suite verifying web route rendering, sample loading, model schema validation, template rendering across all industries, JSON export, and profile import handling.

### Running Tests
```bash
PYTHONPATH=. pytest -v
```

### 📸 Test Output Snapshot

```text
============================= test session starts ==============================
platform linux -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /app
plugins: anyio-4.15.0
collected 11 items

tests/test_main.py::test_get_builder PASSED                              [  9%]
tests/test_main.py::test_list_samples PASSED                             [ 18%]
tests/test_main.py::test_get_sample_detail PASSED                        [ 27%]
tests/test_main.py::test_get_nonexistent_sample PASSED                   [ 36%]
tests/test_main.py::test_render_resume_all_templates[accounting] PASSED  [ 45%]
tests/test_main.py::test_render_resume_all_templates[it] PASSED          [ 54%]
tests/test_main.py::test_render_resume_all_templates[executive] PASSED   [ 63%]
tests/test_main.py::test_render_resume_all_templates[marketing] PASSED   [ 72%]
tests/test_main.py::test_render_resume_all_templates[healthcare] PASSED  [ 81%]
tests/test_main.py::test_export_resume_json PASSED                       [ 90%]
tests/test_main.py::test_import_profile_endpoint PASSED                  [100%]

======================== 11 passed, 2 warnings in 1.19s ========================
```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for details.
