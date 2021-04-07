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

lint:
	poetry run flake8
