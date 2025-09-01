# Document AI for AU Licences & Certificates

Production-style pipeline that extracts **structured fields** from Australian licences & HRW certificates using **Azure Document Intelligence** (+ layout heuristics).

## ✨ Features
- Prebuilt **Layout/Read** vs **Custom** model switch
- Heuristics: table/list detection & field fallbacks
- Simple plugin system for new document types
- Optional Azure Functions hook

## 🧰 Tech Stack
azure-ai-documentintelligence · Python · pydantic

## 🔑 Setup
Set env vars:
AZURE_DI_ENDPOINT=...
AZURE_DI_KEY=...
MODEL_ID_CUSTOM=your-custom-model-id


## 🚀 Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python run_pipeline.py --input samples/ --out out.json --use_custom false

📁 Repo Structure

run_pipeline.py — CLI orchestrator

azure_client.py — Azure DI wrapper

parsers/ — type-specific field mappers

schemas.py — pydantic outputs

samples/ — demo PDFs/images
