from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{description}"')
def step_when_add_task_default_priority(context, description):
    context.todo_list.add_task(description)

@when('the user adds a task "{description}" with priority "{priority}"')
def step_when_add_task_with_priority(context, description, priority):
    context.todo_list.add_task(description, priority)

@then('the to-do list should contain "{description}" with priority "{priority}"')
def step_then_task_in_list(context, description, priority):
    tasks = context.todo_list.list_tasks()
    task = next((task for task in tasks if task.description == description), None)
    assert task is not None
    assert task.priority == priority
