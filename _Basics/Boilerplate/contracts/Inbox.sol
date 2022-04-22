// SPDX-License-Identifier: GPL-3.0

pragma solidity^0.4.17;

contract Inbox {
    string public message;


    function Inbox(string memory InitialMessage) public{
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

