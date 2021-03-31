# Just for now, we upgrade that after
coverage run -m unittest discover tests -p "test*.py"
coverage report
coverage html