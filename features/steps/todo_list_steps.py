from behave import given, when, then
from todo_list import ToDoList, Task
from datetime import datetime

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task_description}" with priority "{priority}"')
def step_impl(context, task_description, priority):
    context.todo_list.add_task(task_description, priority)

@then('the to-do list should contain "{task_description}" with priority "{priority}"')
def step_impl(context, task_description, priority):
    tasks = context.todo_list.list_tasks()
    found = any(task.description == task_description and task.priority == priority for task in tasks)
    assert found, f'Task "{task_description}" with priority "{priority}" not found in the to-do list.'

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'], row['Priority'])
        # Optionally set the status and creation date if needed
        for task in context.todo_list.list_tasks():
            if task.description == row['Task']:
                task.status = row['Status']
                task.creation_date = datetime.strptime(row['Created on'], '%Y-%m-%d %H:%M:%S')

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = context.todo_list.list_tasks()

@then('the tasks should be')
def step_impl(context):
    expected_tasks = []
    for row in context.table:
        expected_tasks.append(Task(row['Task'], row['Priority'], row['Status']))
    
    listed_tasks = context.listed_tasks
    assert len(listed_tasks) == len(expected_tasks), f"Expected {len(expected_tasks)} tasks but found {len(listed_tasks)}."
    
    for i, task in enumerate(listed_tasks):
        assert task.description == expected_tasks[i].description
        assert task.priority == expected_tasks[i].priority
        assert task.status == expected_tasks[i].status
        assert task.creation_date.strftime('%Y-%m-%d %H:%M:%S') == context.table[i]['Created on']

@given('the to-do list contains a task "{task_description}" with status "{status}"')
def step_impl(context, task_description, status):
    context.todo_list = ToDoList()
    task = Task(task_description)
    task.status = status
    context.todo_list.tasks.append(task)

@when('the user marks task "{task_description}" as completed')
def step_impl(context, task_description):
    context.todo_list.mark_task_completed(task_description)

@then('the to-do list should show task "{task_description}" as completed')
def step_impl(context, task_description):
    tasks = context.todo_list.list_tasks()
    found = any(task.description == task_description and task.status == "Completed" for task in tasks)
    assert found, f'Task "{task_description}" is not marked as completed.'

@when('the user removes the task "{task_description}"')
def step_impl(context, task_description):
    context.todo_list.remove_task(task_description)

@then('the to-do list should contain only')
def step_impl(context):
    expected_tasks = [row['Task'] for row in context.table]
    remaining_tasks = [task.description for task in context.todo_list.list_tasks()]
    assert remaining_tasks == expected_tasks, f"Expected tasks {expected_tasks} but found {remaining_tasks}."

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_list()

@then('the to-do list should be empty')
def step_impl(context):
    tasks = context.todo_list.list_tasks()
    assert len(tasks) == 0, "The to-do list is not empty."

@when('the user lists tasks with priority "{priority}"')
def step_impl(context, priority):
    context.listed_tasks = context.todo_list.list_tasks_by_priority(priority)

@then('the tasks with priority "{priority}" should be')
def step_impl(context, priority):
    expected_tasks = [row['Task'] for row in context.table if row['Priority'] == priority]
    listed_tasks = [task.description for task in context.listed_tasks if task.priority == priority]
    assert listed_tasks == expected_tasks, f"Expected tasks {expected_tasks} but found {listed_tasks}."