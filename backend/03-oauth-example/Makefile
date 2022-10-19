PYTHON = 3.9
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=conda-forge defaults
SERVER_PORT=8765

env:
	conda create -n $(BASENAME)  python=$(PYTHON)

setup:
	conda install --file requirements.txt $(addprefix -c ,$(CONDA_CH))

format:
	black src .
	isort src .

run-server:
	uvicorn src.main:app --reload --port $(SERVER_PORT)
	