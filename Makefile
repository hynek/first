test:
	python -m doctest first.py
	python -m doctest README.rst
	python test_first.py

cov:
	py.test --cov first --cov-report=term-missing .

pep8:
	py.test --pep8 .

.PHONY: test cov
