from behave import given, when, then
from todo_list import ToDoList, Task

@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = ToDoList()

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table.rows:
        context.todo_list.add_task(row['Task'], row.get('Priority', 'Medium'))

@when('the user lists all tasks')
def step_when_list_tasks(context):
    tasks = context.todo_list.list_tasks()
    context.output = "\n".join([f"{task.description} ({task.priority})" for task in tasks])
    if not tasks:
        context.output = "The to-do list is empty."

@then('the output should be:')
def step_then_output(context):
    expected_output = "\n".join([f"{row['Task']} ({row.get('Priority', 'Medium')})" for row in context.table.rows])
    assert context.output == expected_output

@then('the output should be "The to-do list is empty."')
def step_then_empty_list_message(context):
    assert context.output == "The to-do list is empty."
