#!/usr/bin/python3
"""
inherriting from class int
"""


class MyInt(int):
    """
    inside the class
    """

    def __eq__(self, other):
        """
        inside the eq method
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        inside the ne method
        """
        return super().__eq__(other)
