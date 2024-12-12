def parse_input(file: str) -> (dict(), list[int]):
    ordering_rules, updates = {}, []
    with open(file, "r") as data:
        for line in data:
            if line == "\n":
                break
            key, value = map(int, line.strip().split("|"))
            ordering_rules.setdefault(key, []).append(value)

        updates = [list(map(int, line.strip().split(","))) for line in data]
    return ordering_rules, updates


def is_valid_update(ordering_rules: dict, update: list[int]) -> bool:
    for page, must_come_after in ordering_rules.items():
        if page in update:
            page_index = update.index(page)

            for after_page in must_come_after:
                if after_page in update:
                    after_index = update.index(after_page)
                    if after_index < page_index:
                        return False

    return True


def check_every_update(ordering_rules: dict, updates: list) -> list:
    valid_updates = [
        update for update in updates if is_valid_update(ordering_rules, update)
    ]
    return valid_updates


def add_middle_element(valid_updates: list) -> int:
    res = 0
    for update in valid_updates:
        res += update[len(update) // 2]
    return res


if __name__ == "__main__":
    ordering_rules, updates = parse_input("./input.txt")
    valid_updates = check_every_update(ordering_rules, updates)
    print(valid_updates)
    print(add_middle_element(valid_updates))
