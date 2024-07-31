from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table.rows:
        context.todo_list.add_task(row['Task'])
        if row.get('Status') == 'Completed':
            task = next((task for task in context.todo_list.list_tasks() if task.description == row['Task']), None)
            if task:
                task.mark_completed()

@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = ToDoList()

@when('the user clears the to-do list')
def step_when_clear_list(context):
    context.todo_list.clear_list()

@then('the to-do list should be empty')
def step_then_list_is_empty(context):
    tasks = context.todo_list.list_tasks()
    assert len(tasks) == 0
