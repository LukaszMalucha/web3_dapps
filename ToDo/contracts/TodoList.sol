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

    constructor() public {
        createTask("Check out encyclopedia");
    }

    function createTask(string memory _content) public {
        taskCount ++;
        tasks[taskCount] = Task(taskCount, _content, false);
    }

}



