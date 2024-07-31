Feature: List Tasks by Priority

  Scenario: List tasks with a specific priority
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
      | Clean the house  | Medium   |
    When the user lists tasks with priority "Medium"
    Then the output should be:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Clean the house  | Medium   |
