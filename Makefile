.PHONY: install lint build package-install

install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check vd_games
