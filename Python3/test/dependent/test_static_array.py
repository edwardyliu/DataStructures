# Configure Path 
import os
import sys
folder_uri = os.path.dirname(__file__)
sys.path.insert(1, os.path.join(folder_uri, "../../"))

from dependent.array.static_array import StaticArray

class Person:

    def __init__(self, name:str, age:int):
        self._name = name
        self._age = age
    
    def __str__(self):
        return "{0}|{1}".format(self._name, self._age)

    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def setName(self, name:str):
        self._name = name
    
    def setAge(self, age:int):
        self._age = age

def test_static_array():
    
    # String Test
    string_array = StaticArray("hello", "world", "nice", "to", "meet", "you!")
    print("String Array: {0}".format(string_array))
    print("[0]: {0}".format(string_array[0]))
    print("[5]: {0}".format(string_array[5]))
    print("get(2): {0}".format(string_array.get(2)))

    # Self-defined Class Test
    person_array = StaticArray(Person("Edward", 21), Person("Jingyu", 23), Person("Superman", 25))
    print("Person Array: {0}".format(person_array))
    print("[0]: {0}".format(person_array[0]))
    print("[2]: {0}".format(person_array[2]))
    print("[2]: {0}".format(person_array.get(2)))

if __name__ == "__main__":
    test_static_array()