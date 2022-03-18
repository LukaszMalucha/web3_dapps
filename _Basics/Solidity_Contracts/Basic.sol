// SPDX-License-Identifier: MIT
pragma solidity >=0.4.24 <0.9.0;

contract MyContract {
    string value;

    constructor() {
        value = "startValue";
    }

    // Set public value that anyone can read
    function get()  public view returns(string memory){
        return value;
    }

    // allow anyone to set the value
    function set(string memory _value) public {
        value = _value;
    }

}