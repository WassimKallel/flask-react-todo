from flask_api.app import app
import pytest


@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_add_todo(test_client):
    # Given
    expected_status_code = 201
    expected_message = 'Task added.'
    expected_todo = {
        'done': False,
        'task': 'hello'
    }
    expected_todo_keys = ['done', 'task', 'id']

    # When
    response = test_client.post('/todos/', json={
        'task': 'hello'
    })

    # Then
    assert expected_status_code == response.status_code
    assert expected_status_code == response.json['code']
    assert expected_message == response.json['message']
    assert expected_todo.items() <= response.json['todo'].items()
    assert set(expected_todo_keys) == set(response.json['todo'].keys())


def test_list_todos(test_client):
    # Given
    expected_status_code = 200
    expected_response_type = list

    # When
    response = test_client.get('/todos/')

    # Then
    assert expected_status_code == response.status_code
    assert expected_response_type == type(response.json)
