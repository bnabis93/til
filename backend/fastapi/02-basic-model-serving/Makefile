PYTHON = 3.9
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=defaults conda-forge pytorch


env:
	conda create -n $(BASENAME)  python=$(PYTHON)

setup:
	conda install --file requirements.txt $(addprefix -c ,$(CONDA_CH))

