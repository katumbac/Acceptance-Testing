Feature: To-Do List Management

  Scenario: Add a new task
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with priority "Medium"
    Then the to-do list should contain "Buy groceries" with priority "Medium"

  Scenario: List all tasks
    Given the to-do list contains tasks
      | Task          | Priority | Status  | Created on          |
      | Buy groceries | Medium   | Completed | 2024-07-31 21:03:08 |
      | Pay bills     | High     | Pending | 2024-07-31 21:03:08 |
      | Walk          | Medium   | Pending | 2024-07-31 21:03:08 |
      | Talk with friends | High | Pending | 2024-07-31 21:03:08 |
      | Study         | High     | Pending | 2024-07-31 21:03:08 |
    When the user lists all tasks
    Then the tasks should be
      | Task          | Priority | Status  | Created on          |
      | Buy groceries | Medium   | Completed | 2024-07-31 21:03:08 |
      | Pay bills     | High     | Pending | 2024-07-31 21:03:08 |
      | Walk          | Medium   | Pending | 2024-07-31 21:03:08 |
      | Talk with friends | High | Pending | 2024-07-31 21:03:08 |
      | Study         | High     | Pending | 2024-07-31 21:03:08 |

  Scenario: Mark a task as completed
    Given the to-do list contains a task "Buy groceries" with status "Pending"
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Remove a task
    Given the to-do list contains tasks
      | Task          | Priority | Status  | Created on          |
      | Buy groceries | Medium   | Completed | 2024-07-31 21:03:08 |
      | Pay bills     | High     | Pending | 2024-07-31 21:03:08 |
      | Walk          | Medium   | Pending | 2024-07-31 21:03:08 |
      | Talk with friends | High | Pending | 2024-07-31 21:03:08 |
      | Study         | High     | Pending | 2024-07-31 21:03:08 |
    When the user removes the task "Buy groceries"
    Then the to-do list should contain only
      | Task          | Priority | Status  | Created on          |
      | Pay bills     | High     | Pending | 2024-07-31 21:03:08 |
      | Walk          | Medium   | Pending | 2024-07-31 21:03:08 |
      | Talk with friends | High | Pending | 2024-07-31 21:03:08 |
      | Study         | High     | Pending | 2024-07-31 21:03:08 |

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks
      | Task          | Priority | Status  | Created on          |
      | Pay bills     | High     | Pending | 2024-07-31 21:03:08 |
      | Walk          | Medium   | Pending | 2024-07-31 21:03:08 |
      | Talk with friends | High | Pending | 2024-07-31 21:03:08 |
      | Study         | High     | Pending | 2024-07-31 21:03:08 |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: List tasks by priority
    Given the to-do list contains tasks
      | Task          | Priority | Status  | Created on          |
      | Buy groceries | Medium   | Completed | 2024-07-31 21:03:08 |
      | Pay bills     | High     | Pending | 2024-07-31 21:03:08 |
      | Walk          | Medium   | Pending | 2024-07-31 21:03:08 |
      | Talk with friends | High | Pending | 2024-07-31 21:03:08 |
      | Study         | High     | Pending | 2024-07-31 21:03:08 |
    When the user lists tasks with priority "High"
    Then the tasks with priority "High" should be
      | Task          | Priority | Status  | Created on          |
      | Pay bills     | High     | Pending | 2024-07-31 21:03:08 |
      | Talk with friends | High | Pending | 2024-07-31 21:03:08 |
      | Study         | High     | Pending | 2024-07-31 21:03:08 |
