test:
	py.test --doctest-glob='*.rst' --doctest-modules --ignore=setup.py

cov:
	py.test --cov first --cov-report=term-missing .

pep8:
	py.test --pep8 .

.PHONY: test cov pep8
