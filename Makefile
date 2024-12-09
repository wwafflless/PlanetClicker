##
# PlanetClicker
#
# @file
# @version 0.1

main:
	python -m planetclicker

test:
	pytest

fmt:
	black .
	isort planetclicker/**/*.py


# end
