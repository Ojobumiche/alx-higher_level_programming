#!/usr/bin/python3
"""Defines a locked class."""
#101-loked_class.py

class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ =["first_name]
