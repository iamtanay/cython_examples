from point import Point

def main():
    p1 = Point(1.0, 2.0)
    p2 = Point(4.0, 6.0)
    
    distance = p1.distance_to(p2)
    print(f"Distance between points: {distance:.2f}")

if __name__ == "__main__":
    main()