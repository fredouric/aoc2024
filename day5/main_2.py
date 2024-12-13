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


def get_wrong_update(ordering_rules: dict, updates: list) -> list:
    wrong_updates = [
        update for update in updates if not is_valid_update(ordering_rules, update)
    ]
    return wrong_updates


def reorder_update(ordering_rules: dict, update: list) -> list:
    while not (is_valid_update(ordering_rules, update)):
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[i] in ordering_rules[update[j]]:
                    update[j], update[i] = update[i], update[j]
    return update


def add_middle_element(updates: list) -> int:
    res = 0
    for update in updates:
        res += update[len(update) // 2]
    return res


if __name__ == "__main__":
    ordering_rules, updates = parse_input("./input.txt")
    wrong_updates = get_wrong_update(ordering_rules, updates)
    ordered_updates = []
    for update in wrong_updates:
        ordered_updates.append(reorder_update(ordering_rules, update))

    for update in ordered_updates:
        print(is_valid_update(ordering_rules, update))

    print(add_middle_element(ordered_updates))
