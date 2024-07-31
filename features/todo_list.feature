Feature: To-Do List Management

  Scenario: Add a new task
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with priority "Medium"
    Then the to-do list should contain "Buy groceries" with priority "Medium"

  Scenario: List all tasks
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
    When the user lists all tasks
    Then the tasks should be:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |

  Scenario: Mark a task as completed
    Given the to-do list contains a task "Buy groceries" with status "Pending"
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Mark a task as pendiente
    Given the to-do list contains a task "Pay bills" with status "Completed"
    When the user marks task "Pay bills" as pendiente
    Then the to-do list should show task "Pay bills" as pendiente

  Scenario: Remove a task
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user removes the task "Buy groceries"
    Then the to-do list should contain only:
      | Task          |
      | Pay bills     |

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: List tasks by priority
    Given the to-do list contains tasks:
      | Task             | Priority |
      | Buy groceries    | Medium   |
      | Pay bills        | High     |
    When the user lists tasks with priority "High"
    Then the tasks should be:
      | Task     | Priority |
      | Pay bills | High     |

  Scenario: List tasks by status
    Given the to-do list contains tasks:
      | Task             | Status     |
      | Buy groceries    | Pending    |
      | Pay bills        | Completed  |
    When the user lists tasks with status "Pending"
    Then the tasks should be:
      | Task          | Status    |
      | Buy groceries | Pending   |

