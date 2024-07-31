from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table.rows:
        context.todo_list.add_task(row['Task'])
        task = next((task for task in context.todo_list.list_tasks() if task.description == row['Task']), None)
        if task and row.get('Status') == 'Completed':
            task.mark_completed()

@when('the user lists tasks with status "{status}"')
def step_when_list_tasks_by_status(context, status):
    tasks = context.todo_list.list_tasks_by_status(status)
    context.output = "\n".join([f"{task.description} ({task.status})" for task in tasks])

@then('the output should be:')
def step_then_output(context):
    expected_output = "\n".join([f"{row['Task']} ({row['Status']})" for row in context.table.rows])
    assert context.output == expected_output
