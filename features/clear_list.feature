Feature: Clear All Tasks from To-Do List

  Scenario: Clear the entire to-do list when it contains tasks
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Pending  |
      | Pay bills        | Completed|
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Clear the entire to-do list when it is already empty
    Given the to-do list is empty
    When the user clears the to-do list
    Then the to-do list should be empty
