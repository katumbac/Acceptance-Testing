from behave import given, when, then
from todo_list import ToDoList, Task

@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{description}"')
def step_when_add_task(context, description):
    context.todo_list.add_task(description)
    context.task_added = description

@when('the user adds a task "{description}" with priority "{priority}"')
def step_when_add_task_with_priority(context, description, priority):
    context.todo_list.add_task(description, priority)
    context.task_added = description
    context.priority_added = priority

@when('the user lists all tasks')
def step_when_list_all_tasks(context):
    context.listed_tasks = context.todo_list.list_tasks()

@when('the user marks the task "{description}" as completed')
def step_when_mark_task_completed(context, description):
    context.todo_list.mark_task_completed(description)

@when('the user marks the task "{description}" as pending')
def step_when_mark_task_pendiente(context, description):
    context.todo_list.mark_task_pendiente(description)

@when('the user clears the to-do list')
def step_when_clear_list(context):
    context.todo_list.clear_list()

@when('the user lists tasks with priority "{priority}"')
def step_when_list_tasks_by_priority(context, priority):
    context.listed_tasks = context.todo_list.list_tasks_by_priority(priority)

@when('the user removes the task "{description}"')
def step_when_remove_task(context, description):
    context.todo_list.remove_task(description)

@when('the user lists tasks with status "{status}"')
def step_when_list_tasks_by_status(context, status):
    context.listed_tasks = context.todo_list.list_tasks_by_status(status)

@when('the user updates the priority of "{description}" to "{new_priority}"')
def step_when_update_task_priority(context, description, new_priority):
    context.todo_list.update_task_priority(description, new_priority)

@then('the to-do list should contain:')
def step_then_list_contains_task(context):
    tasks = context.todo_list.list_tasks()
    task_descriptions = [task.description for task in tasks]
    for row in context.table.rows:
        description = row['Task']
        priority = row['Priority']
        assert description in task_descriptions
        task = next(task for task in tasks if task.description == description)
        assert task.priority == priority

@then('the output should be:')
def step_then_output_should_be(context):
    tasks = context.listed_tasks
    for row in context.table.rows:
        description = row['Task']
        priority = row['Priority']
        task = next(task for task in tasks if task.description == description)
        assert task.priority == priority

@then('the task "{description}" should be completed')
def step_then_task_should_be_completed(context, description):
    task = next(task for task in context.todo_list.list_tasks() if task.description == description)
    assert task.status == "Completed"

@then('the task "{description}" should be pending')
def step_then_task_should_be_pending(context, description):
    task = next(task for task in context.todo_list.list_tasks() if task.description == description)
    assert task.status == "Pending"

@then('the to-do list should be empty')
def step_then_list_should_be_empty(context):
    assert len(context.todo_list.list_tasks()) == 0

@then('the priority of "{description}" should be "{priority}"')
def step_then_priority_should_be(context, description, priority):
    task = next(task for task in context.todo_list.list_tasks() if task.description == description)
    assert task.priority == priority

@then('the priority of "{description}" should not be updated')
def step_then_priority_should_not_be_updated(context, description):
    task = next(task for task in context.todo_list.list_tasks() if task.description == description)
    assert task.priority != context.priority_added
