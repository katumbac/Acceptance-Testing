from behave import given, when, then
from todo_list import ToDoList, Task

@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{description}" with priority "{priority}"')
def step_when_add_task(context, description, priority):
    context.todo_list.add_task(description, priority)

@when('the user lists all tasks')
def step_when_list_all_tasks(context):
    context.result = context.todo_list.list_tasks()

@when('the user marks task "{description}" as completed')
def step_when_mark_task_completed(context, description):
    context.todo_list.mark_task_completed(description)

@when('the user marks task "{description}" as pendiente')
def step_when_mark_task_pendiente(context, description):
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
def step_when_update_task_priority(context, description, new_priority):
    context.todo_list.update_task_priority(description, new_priority)

@then('the to-do list should contain "{description}" with priority "{priority}"')
def step_then_check_task_priority(context, description, priority):
    tasks = context.todo_list.list_tasks()
    task = next((t for t in tasks if t.description == description), None)
    assert task is not None, f"Task with description '{description}' not found"
    assert task.priority == priority, f"Expected priority '{priority}', but got '{task.priority}'"

@then('the tasks should be:')
def step_then_check_tasks(context):
    tasks = context.result
    expected_tasks = [tuple(row.values()) for row in context.table]
    actual_tasks = [(task.description, task.priority) for task in tasks]
    assert expected_tasks == actual_tasks, f"Expected tasks {expected_tasks}, but got {actual_tasks}"

@then('the to-do list should show task "{description}" as completed')
def step_then_check_task_status_completed(context, description):
    tasks = context.todo_list.list_tasks()
    task = next((t for t in tasks if t.description == description), None)
    assert task is not None, f"Task with description '{description}' not found"
    assert task.status == "Completed", f"Expected status 'Completed', but got '{task.status}'"

@then('the to-do list should show task "{description}" as pendiente')
def step_then_check_task_status_pendiente(context, description):
    tasks = context.todo_list.list_tasks()
    task = next((t for t in tasks if t.description == description), None)
    assert task is not None, f"Task with description '{description}' not found"
    assert task.status == "Pending", f"Expected status 'Pending', but got '{task.status}'"

@then('the to-do list should be empty')
def step_then_check_list_empty(context):
    tasks = context.todo_list.list_tasks()
    assert len(tasks) == 0, "Expected the to-do list to be empty, but it is not"

