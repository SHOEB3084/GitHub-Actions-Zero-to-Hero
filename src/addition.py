# This file is created to test the functionality of the github Actions.
# app.py 
# This is a test commit
# Addition function 
def add(a, b):
    return a + b
# Test addition function 
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
