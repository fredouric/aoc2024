def compute_safe(file: str) -> int:
    safe = 0
    with open(file, mode="r") as data:
        for line in data:
            level = list(map(int, line.split()))
            print(level)
            if check_safety(level):
                safe += 1
    return safe


def check_safety(level: list) -> bool:
    if is_safe(level):
        return True

    for i in range(len(level)):
        modified_level = level[:i] + level[i + 1 :]
        if is_safe(modified_level):
            return True

    return False


def is_safe(level: list) -> bool:
    if not (level == sorted(level) or level == sorted(level, reverse=True)):
        return False

    for i in range(len(level) - 1):
        diff = abs(level[i + 1] - level[i])
        if diff < 1 or diff > 3:
            return False

    return True


if __name__ == "__main__":
    safe = compute_safe("./input.txt")
    print(safe)
