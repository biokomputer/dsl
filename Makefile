# Makefile for BioComputing Simulations

.PHONY: install run clean

install:
    python -m venv env
    source env/bin/activate
    python pip install --upgrade pip
    @pip install -r requirements.txt

run:
    python biocomp.py $(file)

clean:
    find . -name '__pycache__' -exec rm -r {} +
    find . -name '*.pyc' -exec rm -r {} +
    rm -rf build dist *.egg-info