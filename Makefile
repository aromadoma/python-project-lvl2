install:
	poetry install

build:
	poetry build

run:
	poetry run gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip uninstall hexlet-code
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest gendiff/ tests

lint:
	poetry run flake8

check:
	lint test

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

