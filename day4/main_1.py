def parse_input(file: str) -> list:
    grid = []
    with open(file, "r") as data:
        for line in data:
            grid.append([i for i in line.strip()])
    return grid


def recursive_search(grid: list) -> list:
    occurences = []
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1, "right"),
        (1, 0, "down"),
        (1, 1, "diag_down_right"),
        (1, -1, "diag_down_left"),
        (0, -1, "left"),
        (-1, 0, "up"),
        (-1, -1, "diag_up_left"),
        (-1, 1, "diag_up_right"),
    ]

    def check_xmas(r, c, dr, dc):
        xmas = "XMAS"
        for i, letter in enumerate(xmas):
            nr, nc = r + i * dr, c + i * dc
            if not is_valid(nr, nc) or grid[nr][nc] != letter:
                return False
        return True

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc, direction in directions:
                if check_xmas(r, c, dr, dc):
                    occurences.append([r, c, direction])
    return occurences


if __name__ == "__main__":
    grid = parse_input("./input.txt")
    occurences = recursive_search(grid)
    print(len(occurences))
