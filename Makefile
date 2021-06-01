unit-test:
	pytest flask_api/tests/unit

unit-test-coverage:
	coverage run -m	pytest flask_api/tests/unit
	coverage report

integration-test:
	pytest flask_api/tests/integration

integration-test-coverage:
	coverage run -m	pytest flask_api/tests/integration
	coverage report

run:
	FLASK_APP=flask_api/app.py flask run
