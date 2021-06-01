from flask_api.models import Todo
from flask_api.utils import todo_serializer

def test_todo_serializer():
    # given
    todo = Todo(
        id=123,
        task='demo',
        done=True
    )

    expected_output = {
        'id': 123,
        'task': 'demo',
        'done': True
    }

    # when
    output = todo_serializer(todo)

    # then
    assert expected_output == output
