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

@when('the user adds a task "{description}" with priority "{priority}"')
def step_when_add_task(context, description, priority):
    context.todo_list.add_task(description, priority)

@when('the user lists all tasks')
def step_when_list_tasks(context):
    context.result = context.todo_list.list_tasks()

@when('the user marks task "{description}" as completed')
def step_when_mark_completed(context, description):
    context.todo_list.mark_task_completed(description)

@when('the user marks task "{description}" as pendiente')
def step_when_mark_pendiente(context, description):
    context.todo_list.mark_task_pendiente(description)

@when('the user removes the task "{description}"')
def step_when_remove_task(context, description):
    context.todo_list.remove_task(description)

@when('the user clears the to-do list')
def step_when_clear_list(context):
    context.todo_list.clear_list()

@when('the user lists tasks with priority "{priority}"')
def step_when_list_tasks_by_priority(context, priority):
    context.result = context.todo_list.list_tasks_by_priority(priority)

@when('the user lists tasks with status "{status}"')
def step_when_list_tasks_by_status(context, status):
    context.result = context.todo_list.list_tasks_by_status(status)

@when('the user updates the priority of "{description}" to "{new_priority}"')
def step_when_update_priority(context, description, new_priority):
    context.todo_list.update_task_priority(description, new_priority)

@then('the to-do list should contain "{description}" with priority "{priority}"')
def step_then_task_in_list(context, description, priority):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.priority == priority

@then('the tasks should be:')
def step_then_tasks_listed(context):
    tasks = context.todo_list.list_tasks()
    for row in context.table.rows:
        task = next((task for task in tasks if task.description == row['Task']), None)
        assert task is not None
        assert task.priority == row.get('Priority', 'Medium')
        assert task.status == row.get('Status', 'Pending')

@then('the to-do list should show task "{description}" as completed')
def step_then_task_completed(context, description):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.status == "Completed"

@then('the to-do list should show task "{description}" as pendiente')
def step_then_task_pendiente(context, description):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.status == "Pending"

@then('the to-do list should contain only:')
def step_then_only_tasks(context):
    tasks = context.todo_list.list_tasks()
    for row in context.table.rows:
        task = next((task for task in tasks if task.description == row['Task']), None)
        assert task is not None
    assert len(tasks) == len(context.table.rows)

@then('the to-do list should be empty')
def step_then_empty_list(context):
    assert len(context.todo_list.list_tasks()) == 0

@then('the priority of "{description}" should be "{priority}"')
def step_then_priority_updated(context, description, priority):
    task = next((task for task in context.todo_list.list_tasks() if task.description == description), None)
    assert task is not None
    assert task.priority == priority
