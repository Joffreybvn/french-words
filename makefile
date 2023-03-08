
test:
	pytest tests

qa:
	black .
	pyre
	ruff check french_words/

build-linux:
	sh ./build_linux.sh
