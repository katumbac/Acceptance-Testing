Feature: Add Task to To-Do List

  Scenario: Add a new task with default priority
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries" with priority "Medium"

  Scenario: Add a new task with specified priority
    Given the to-do list is empty
    When the user adds a task "Pay bills" with priority "High"
    Then the to-do list should contain "Pay bills" with priority "High"