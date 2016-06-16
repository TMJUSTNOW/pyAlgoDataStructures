"""
    https://community.topcoder.com/stat?c=problem_statement&pm=2235&rd=5070
    https://www.topcoder.com/community/data-science/data-science-tutorials/greedy-is-good/
"""


def GoldMine(mines, miners):
    # sanitize input
    t = []
    for mine in mines:
        t.append([int(i) / 100 for i in mine.split(', ')])
    mines = t
    # Construct value table
    mines_value = []
    for mine in mines:
        miners_calc = 0
        mine_value = []
        miners_used = 0
        while miners_used <= miners:
            total = 0
            for ore, prob in enumerate(mine):
                if miners_used < ore:
                    total += 60 * miners_used * prob
                elif miners_used == ore:
                    total += 50 * miners_used * prob
                else:
                    total += (50 * ore - 20 * (miners_used - ore)) * prob
            mine_value.append(total)
            miners_used += 1
        mines_value.append(mine_value)

    miner = 1
    miner_distribution = [0] * len(mines)
    while miner <= miners:
        best_value = float('-inf')
        to_update = None
        for i, mine_value in enumerate(mines_value):
            increase_in_value = mine_value[miner_distribution[i] + 1] - mine_value[miner_distribution[i]]
            if increase_in_value > best_value:
                best_value = increase_in_value
                to_update = i
        miner_distribution[to_update] += 1
        miner += 1
    return miner_distribution


test_mines = ["000, 030, 030, 040, 000, 000, 000",
              "020, 020, 020, 010, 010, 010, 010"]
test_miners = 4
result = GoldMine(test_mines, test_miners)
solution = [2, 2]
print('Test case result: ', result == solution)
test_mines = ["026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004",
              "026, 012, 005, 013, 038, 002, 004"]
test_miners = 56
result = GoldMine(test_mines, test_miners)
solution = [2,  2,  2,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
print('Test case result: ', result == solution)
test_mines = ["100, 000, 000, 000, 000, 000, 000",
              "090, 010, 000, 000, 000, 000, 000",
              "080, 020, 000, 000, 000, 000, 000",
              "075, 025, 000, 000, 000, 000, 000",
              "050, 050, 000, 000, 000, 000, 000",
              "025, 075, 000, 000, 000, 000, 000",
              "020, 080, 000, 000, 000, 000, 000",
              "010, 090, 000, 000, 000, 000, 000",
              "000, 100, 000, 000, 000, 000, 000",
              "000, 090, 010, 000, 000, 000, 000",
              "000, 080, 020, 000, 000, 000, 000",
              "000, 075, 025, 000, 000, 000, 000",
              "000, 050, 050, 000, 000, 000, 000",
              "000, 025, 075, 000, 000, 000, 000",
              "000, 020, 080, 000, 000, 000, 000",
              "000, 010, 090, 000, 000, 000, 000",
              "000, 000, 100, 000, 000, 000, 000",
              "000, 000, 090, 010, 000, 000, 000",
              "000, 000, 080, 020, 000, 000, 000",
              "000, 000, 075, 025, 000, 000, 000",
              "000, 000, 050, 050, 000, 000, 000",
              "000, 000, 025, 075, 000, 000, 000",
              "000, 000, 020, 080, 000, 000, 000",
              "000, 000, 010, 090, 000, 000, 000",
              "000, 000, 000, 100, 000, 000, 000",
              "000, 000, 000, 100, 000, 000, 000",
              "000, 000, 000, 090, 010, 000, 000",
              "000, 000, 000, 080, 020, 000, 000",
              "000, 000, 000, 075, 025, 000, 000",
              "000, 000, 000, 050, 050, 000, 000",
              "000, 000, 000, 025, 075, 000, 000",
              "000, 000, 000, 020, 080, 000, 000",
              "000, 000, 000, 010, 090, 000, 000",
              "000, 000, 000, 000, 100, 000, 000",
              "000, 000, 000, 000, 090, 010, 000",
              "000, 000, 000, 000, 080, 020, 000",
              "000, 000, 000, 000, 075, 025, 000",
              "000, 000, 000, 000, 050, 050, 000",
              "000, 000, 000, 000, 025, 075, 000",
              "000, 000, 000, 000, 020, 080, 000",
              "000, 000, 000, 000, 010, 090, 000",
              "000, 000, 000, 000, 000, 100, 000",
              "000, 000, 000, 000, 000, 090, 010",
              "000, 000, 000, 000, 000, 080, 020",
              "000, 000, 000, 000, 000, 075, 025",
              "000, 000, 000, 000, 000, 050, 050",
              "000, 000, 000, 000, 000, 025, 075",
              "000, 000, 000, 000, 000, 020, 080",
              "000, 000, 000, 000, 000, 010, 090",
              "000, 000, 000, 000, 000, 000, 100"]
test_miners = 150
result = GoldMine(test_mines, test_miners)
solution = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6]
print('Test case result: ', result == solution)
