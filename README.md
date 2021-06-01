# flask-react-todo

To-do list application written with Python and Javascript using Client + API architechture

---

#### Technologies
- React 16.4.1
- Python 3.6.4
- Flask 1.0.2
- Flask-SQLAlchemy 2.3.2
- SQLite 3.7.17

#### How to run
1. Clone repository via SSH or HTTP and `cd` into it.
2. `FLASK_APP=flask_api/app.py flask run`
3. `npm run --prefix react_client start`
4. Access [http://127.0.0.1:3000](http://127.0.0.1:3000) (should open automatically).


#### Run Tests
1. Run unit tests
```bash
make unit-test
```

2. Run unit tests and check code coverage
```bash
make unit-test-coverage
```

3. Run integration tests
```bash
make integration-test
```

4. Run integration tests and check coverage
```bash
test-coverage
```