install:
	uv sync

games:
	uv run games

even:
	uv run even

calc:
	uv run calc

gcd:
	uv run gcd

progression:
	uv run progression

prime:
	uv run brain-prime

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games