def parse_input(file: str) -> (list, list):
    left, right = [], []
    with open(file, mode="r") as data:
        for line in data:
            d = line.split()
            left.append(int(d[0]))
            right.append(int(d[1]))
    return sorted(left), sorted(right)


def compute_distances(left, right: list) -> list:
    return [abs(x - y) for x, y in zip(left, right)]


if __name__ == "__main__":
    left, right = parse_input("./input.txt")
    distances = compute_distances(left, right)
    print(sum(distances))
