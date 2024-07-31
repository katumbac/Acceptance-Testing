Feature: Manage To-Do List

  Background: 
    Given the to-do list is empty

  Scenario: Add a new task with default priority
    When the user adds a task "Buy groceries"
    Then the to-do list should contain:
      | Task             | Priority |
      | Buy groceries    | Medium   |

  Scenario: Add a new task with specified priority
    When the user adds a task "Pay bills" with priority "High"
    Then the to-do list should contain:
      | Task      | Priority |
      | Pay bills | High     |

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
      | Exercise         | High     |
    When the user lists all tasks
    Then the output should be:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
      | Exercise         | High     |

  Scenario: Mark an existing task as completed
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Pending  |
    When the user marks the task "Buy groceries" as completed
    Then the task "Buy groceries" should be completed

  Scenario: Mark an existing task as pending
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Completed|
    When the user marks the task "Buy groceries" as pending
    Then the task "Buy groceries" should be pending

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task             |
      | Buy groceries    |
      | Pay bills        |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: List tasks by priority
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
      | Exercise         | High     |
    When the user lists tasks with priority "High"
    Then the output should be:
      | Task      | Priority |
      | Pay bills | High     |
      | Exercise  | High     |

  Scenario: Remove an existing task
    Given the to-do list contains tasks:
      | Task             |
      | Buy groceries    |
      | Pay bills        |
    When the user removes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"

  Scenario: List tasks by status
    Given the to-do list contains tasks:
      | Task             | Status   |
      | Buy groceries    | Pending  |
      | Pay bills        | Completed|
      | Exercise         | Pending  |
    When the user lists tasks with status "Pending"
    Then the output should be:
      | Task             | Status   |
      | Buy groceries    | Pending  |
      | Exercise         | Pending  |

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
