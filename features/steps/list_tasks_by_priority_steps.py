from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table.rows:
        context.todo_list.add_task(row['Task'], row['Priority'])

@when('the user lists tasks with priority "{priority}"')
def step_when_list_tasks_by_priority(context, priority):
    tasks = context.todo_list.list_tasks_by_priority(priority)
    context.output = "\n".join([f"{task.description} ({task.priority})" for task in tasks])

@then('the output should be:')
def step_then_output(context):
    expected_output = "\n".join([f"{row['Task']} ({row['Priority']})" for row in context.table.rows])
    assert context.output == expected_output
