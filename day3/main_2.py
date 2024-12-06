import re


def match_expression(file: str) -> list:
    res = 0
    enabled = True
    with open(file, mode="r") as data:
        content = data.read()
        for a, b, do, dont in re.findall(
            r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", content
        ):
            if dont:
                enabled = False
            elif do:
                enabled = True
            else:
                res += enabled * int(a) * int(b)
    return res


if __name__ == "__main__":
    res = match_expression("./input.txt")
    print(res)
