from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table.rows:
        context.todo_list.add_task(row['Task'], row['Priority'])

@when('the user updates the priority of "{description}" to "{new_priority}"')
def step_when_update_task_priority(context, description, new_priority):
    context.result = context.todo_list.update_task_priority(description, new_priority)

@then('the priority of "{description}" should be "{expected_priority}"')
def step_then_priority_updated(context, description, expected_priority):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.priority == expected_priority
    assert context.result is True

@then('the priority of "{description}" should not be updated')
def step_then_priority_not_updated(context, description):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.priority != 'High'
    assert context.result is False
