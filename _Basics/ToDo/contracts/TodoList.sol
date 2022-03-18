// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract TodoList {
    uint public taskCount = 0;

    struct Task {
        uint id;
        string content;
        bool completed;
    }
    //    Like Dictionary:
    mapping(uint => Task) public tasks;

    //    Constructor like __init__ - adds some starter tasks

    event TaskCreated(
        uint id,
        string content,
        bool completed
    );

    event TaskCompleted(
        uint id,
        bool completed
    );

    constructor() public {
        createTask("Check out encyclopedia");
    }

    function createTask(string memory _content) public {
        taskCount ++;
        tasks[taskCount] = Task(taskCount, _content, false);
        emit TaskCreated(taskCount, _content, false);
    }

    function toggleCompleted(uint _id) public {
//        Assign to variable of type 'Task'
        Task memory _task = tasks[_id];
//        Switch boolean
        _task.completed = !_task.completed;
//        Put value back to task
        tasks[_id] = _task;
//        Emit event
        emit TaskCompleted(_id, _task.completed);
    }

}



