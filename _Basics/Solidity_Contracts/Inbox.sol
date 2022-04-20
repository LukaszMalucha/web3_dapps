// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;


contract Inbox {
    string public message;

    // Function no longer can have the same name as contract - use 'constructor' keyword instead
    constructor(string memory InitialMessage) {
        message = InitialMessage;
    }

    function setMessage(string memory newMessage) public {
        message = newMessage;
    }
    // 'view' - we are not attempting to modify any data with that function
    // 'returns' - only with view or constant
    //  Duplicate of automatically created 'message' function
    // function getMessage() public view returns (string memory) {
    //     return message;
    // }

}

