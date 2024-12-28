import sys


def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readline().strip().split()
        center_x = float(data[0])
        center_y = float(data[1])
        radius = float(data[2])
    return (center_x, center_y, radius)


def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points


def determine_position(circle, points):
    center_x, center_y, radius = circle
    results = []
    for point in points:
        x, y = point
        distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2
        radius_squared = radius ** 2

        if distance_squared < radius_squared:
            results.append(1)  # точка внутри
        elif distance_squared == radius_squared:
            results.append(0)  # точка на окружности
        else:
            results.append(2)  # точка снаружи
    return results


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle = read_circle_data(circle_file)
    points = read_points(points_file)
    results = determine_position(circle, points)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
