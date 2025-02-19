"""
Python 3 Object-Oriented Programming 4th ed.

Chapter 2, Objects in Python.
"""


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

p1=Point(5,10)
p2=Point()
print(p1.x)
p1.reset()
print(p1.x)
