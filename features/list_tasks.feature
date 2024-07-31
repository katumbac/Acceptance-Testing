Feature: List Tasks from To-Do List

  Scenario: List all tasks when the list is empty
    Given the to-do list is empty
    When the user lists all tasks
    Then the output should be "The to-do list is empty."

  Scenario: List all tasks when there are tasks in the list
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
    When the user lists all tasks
    Then the output should be:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
