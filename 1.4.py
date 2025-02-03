import math

class Point:
    def __init__(self, x, y):
        """Initialize the point with x and y coordinates."""
        self.x = x
        self.y = y

    def show(self):
        """Display the coordinates of the point."""
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        """Move the point by dx and dy."""
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        """Compute the distance between the current point and another point."""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
p1 = Point(2, 3)
p2 = Point(5, 7)

p1.show()  # Output: Point coordinates: (2, 3)
p1.move(3, -1)  # Move p1 by (3, -1)
p1.show()  # Output: Point coordinates: (5, 2)

distance = p1.dist(p2)
print(f"Distance between p1 and p2: {distance}")  # Output: Distance between p1 and p2: 5.0
