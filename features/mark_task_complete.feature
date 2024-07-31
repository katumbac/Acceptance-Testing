Feature: Mark Task as Completed

  Scenario: Mark an existing task as completed
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Pending  |
      | Pay bills        | Pending  |
    When the user marks the task "Buy groceries" as completed
    Then the task "Buy groceries" should be completed

  Scenario: Attempt to mark a non-existing task as completed
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Pending  |
    When the user marks the task "Pay bills" as completed
    Then the task "Pay bills" should not be marked as completed
