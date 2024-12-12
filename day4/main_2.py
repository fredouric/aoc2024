def parse_input(file: str) -> list:
    grid = []
    with open(file, "r") as data:
        for line in data:
            grid.append([i for i in line.strip()])
    return grid


def count_xmas_patterns(grid: list) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0
    pattern = ["SAM", "MAS"]

    for r in range(rows - 2):
        for c in range(cols - 2):
            diag_1 = "".join([grid[r][c], grid[r + 1][c + 1], grid[r + 2][c + 2]])
            diag_2 = "".join([grid[r + 2][c], grid[r + 1][c + 1], grid[r][c + 2]])
            count += diag_1 in pattern and diag_2 in pattern
    return count


if __name__ == "__main__":
    grid = parse_input("./input.txt")
    result = count_xmas_patterns(grid)
    print(result)
