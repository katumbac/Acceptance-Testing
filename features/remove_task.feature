Feature: Remove Task from To-Do List

  Scenario: Remove an existing task
    Given the to-do list contains tasks:
      | Task             |
      | Buy groceries    |
      | Pay bills        |
    When the user removes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"

  Scenario: Attempt to remove a non-existing task
    Given the to-do list contains tasks:
      | Task             |
      | Buy groceries    |
    When the user removes the task "Pay bills"
    Then the to-do list should still contain "Buy groceries"
