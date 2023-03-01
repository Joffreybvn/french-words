test:
	pytest tests

qa:
	black .
	pyre
	ruff check french_words/