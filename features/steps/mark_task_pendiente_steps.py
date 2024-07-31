from behave import given, when, then
from todo_list import ToDoList, Task

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table.rows:
        task = context.todo_list.add_task(row['Task'])
        if row.get('Status') == 'Completed':
            task.mark_completed()

@when('the user marks the task "{description}" as pending')
def step_when_mark_task_pendiente(context, description):
    context.result = context.todo_list.mark_task_pendiente(description)

@then('the task "{description}" should be pending')
def step_then_task_pendiente(context, description):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.status == "Pending"
    assert context.result is True

@then('the task "{description}" should not be marked as pending')
def step_then_task_not_pendiente(context, description):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.status != "Pending"
    assert context.result is False
