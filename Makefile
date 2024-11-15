install:
	poetry install
project:
	poetry run project
build:
	poetry build
publish:
	publish --dry-run
package-install:
	pipx install dist/*.whl
lint:
	poetry run flake8 project