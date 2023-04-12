#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeomery




bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
