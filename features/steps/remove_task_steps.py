from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table.rows:
        context.todo_list.add_task(row['Task'])

@when('the user removes the task "{description}"')
def step_when_remove_task(context, description):
    context.todo_list.remove_task(description)

@then('the to-do list should not contain "{description}"')
def step_then_task_not_in_list(context, description):
    tasks = context.todo_list.list_tasks()
    assert all(task.description != description for task in tasks)

@then('the to-do list should still contain "{description}"')
def step_then_task_still_in_list(context, description):
    tasks = context.todo_list.list_tasks()
    assert any(task.description == description for task in tasks)
