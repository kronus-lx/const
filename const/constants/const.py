# Wrapper container for const variable similar to C-style const

# Initialisation is done through either assignment or through the constructor

# Instance can only contain only one attribute at one time otherwise it will though a runtime error


from typing import Any

class const:

    def __init__(self, name=None, value=None):
        
        if name is not None and value is not None:
            super().__setattr__(name, value)

    """
    Set a key value pair of name which is string and value of any type
    """
    def __setattr__(self, name: str, value: Any) -> None:
        
        if len(self.__dict__) > 0:
            raise RuntimeError("Instance cannot contain more than one attribute")

        if name in self.__setattr__:
            raise RuntimeError(f"Cannot reassign const attribute: {name}")

        else:
            super().__setattr__(name, value)

    """
    Return dictionary key value of name and assigned value
    """
    def release(self) -> dict:
        return self.__dict__

   
    def __del__(self) -> None:
        self.__dict__.clear()