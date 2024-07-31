Feature: Update Task Priority

  Scenario: Update the priority of an existing task
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
    When the user updates the priority of "Buy groceries" to "High"
    Then the priority of "Buy groceries" should be "High"

  Scenario: Attempt to update the priority of a non-existing task
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
    When the user updates the priority of "Pay bills" to "High"
    Then the priority of "Pay bills" should not be updated
