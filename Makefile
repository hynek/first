test:
	python -m pytest --doctest-glob='*.rst' --doctest-modules --ignore=setup.py

cov:
	python -m pytest --cov first --cov-report=term-missing .

.PHONY: test cov
