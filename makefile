run:
	poetry run uvicorn --host 127.0.0.1 --port 8080 --reload --log-level debug --app-dir src main:app
