cdef class Point:
    cdef double x
    cdef double y

    def __init__(self, double x, double y):
        self.x = x
        self.y = y

    cpdef double distance_to(self, Point other):
        cdef double dx = self.x - other.x
        cdef double dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5