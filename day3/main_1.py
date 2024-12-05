import re


def match_expression(file: str) -> list:
    matches = []
    with open(file, mode="r") as data:
        for line in data:
            matches.extend(re.findall("mul\(\d{1,3},\d{1,3}\)", line))
    return matches


def parse_match(match: str) -> int:
    num = list(map(int, re.findall("\d{1,3}", match)))
    return num[0] * num[1]


def compute_result(matches: list) -> int:
    res = 0
    for match in matches:
        res += parse_match(match)
    return res


if __name__ == "__main__":
    matches = match_expression("./input.txt")
    res = compute_result(matches)
    print(res)
