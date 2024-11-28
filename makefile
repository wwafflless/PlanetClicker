cov:
	pytest --cov --capture=fd -o console_output_style=classic

ut:
	pytest --tb=short --capture=sys -o console_output_style=classic

fmt:
    # sed -i "s/\"/'/g" src/**/*.py
	black --skip-string-normalization --line-length 80 src/**/*.py
	isort src/**/*.py

clean:
	find . -type d -name __pycache__ -exec rm -r {} \;

type:
	pyright
