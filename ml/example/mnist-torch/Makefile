PYTHON = 3.9
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=conda-forge defaults pytorch

env:
	conda create -n $(BASENAME)  python=$(PYTHON)

setup:
	conda install --file requirements.txt $(addprefix -c ,$(CONDA_CH))

format:
	black src .
	isort src .

helloworld:
	uvicorn src.server:app --reload
	