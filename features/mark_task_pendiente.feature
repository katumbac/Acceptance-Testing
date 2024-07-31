Feature: Mark Task as Pending

  Scenario: Mark an existing task as pending
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Completed|
      | Pay bills        | Completed|
    When the user marks the task "Buy groceries" as pending
    Then the task "Buy groceries" should be pending

  Scenario: Attempt to mark a non-existing task as pending
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Completed|
    When the user marks the task "Pay bills" as pending
    Then the task "Pay bills" should not be marked as pending