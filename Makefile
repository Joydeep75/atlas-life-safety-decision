.PHONY: install playground run test clean

install:
	uv sync

playground:
	uv run adk web app --host 127.0.0.1 --port 18081 --reload_agents --allow_origins '*'

run:
	uv run uvicorn app.fast_api_app:app --host 0.0.0.0 --port 8000

test:
	uv run pytest tests/

ui:
	uv run streamlit run streamlit_app.py --server.port 8501 --server.address 127.0.0.1

