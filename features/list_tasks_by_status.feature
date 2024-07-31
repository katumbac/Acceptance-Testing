Feature: List Tasks by Status

  Scenario: List tasks with a specific status
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Pending  |
      | Pay bills        | Completed|
      | Clean the house  | Pending  |
    When the user lists tasks with status "Pending"
    Then the output should be:
      | Task             | Status   |
      | Buy groceries    | Pending  |
      | Clean the house  | Pending  |
