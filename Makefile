install: export PIPENV_VENV_IN_PROJECT=1
install:
	pipenv --python=3.9 install

run:
	pipenv run python main.py

clean:
	pipenv --rm

