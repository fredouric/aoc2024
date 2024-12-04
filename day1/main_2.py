def parse_input(file: str) -> (list, list):
    left, right = [], []
    with open(file, mode="r") as data:
        for line in data:
            d = line.split()
            left.append(int(d[0]))
            right.append(int(d[1]))
    return left, right


def compute_similarity(left, right: list) -> int:
    score = 0
    for i in left: 
        occurences = right.count(i)
        score += i*occurences
    return score


if __name__ == "__main__":
    left, right = parse_input("./input.txt")
    score = compute_similarity(left, right)
    print(score)
