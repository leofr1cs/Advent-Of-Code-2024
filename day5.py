from aocd import get_data

data = get_data(day=5, year=2024) 
# data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""


def part1(data):
    rules, pageRecords = [i.split("\n") for i in data.split("\n\n")]
    rules = [[int(v) for v in r.split("|")] for r in rules]
    pageRecords = [[int(v) for v in row.split(",")] for row in pageRecords]
    total = 0
    for rec in pageRecords:
        inRightOrder = True
        for rule in rules:
            bef = rule[0]
            aft = rule[1]
            if bef in rec and aft in rec:
                if rec.index(bef) > rec.index(aft):
                    inRightOrder = False
                
        if inRightOrder:
            mid = rec[len(rec)//2]
            total += mid
            
    return total



def part2(data):

    rules, pageRecords = [i.split("\n") for i in data.split("\n\n")]
    rules = [[int(v) for v in r.split("|")] for r in rules]
    pageRecords = [[int(v) for v in row.split(",")] for row in pageRecords]
    incorrectlyOrdered = []
    for rec in pageRecords:
        for r, rule in enumerate(rules):
            bef = rule[0]
            aft = rule[1]
            if bef in rec and aft in rec:
                if rec.index(bef) > rec.index(aft):
                    incorrectlyOrdered.append(rec[::])
                    break
                    
    total = 0
    for rec in incorrectlyOrdered:
        ordered = False
        while not ordered:
            ordered = True
            for rule in rules:
                bef = rule[0]
                aft = rule[1]
                if bef in rec and aft in rec:
                    while rec.index(bef) > rec.index(aft):
                        ordered = False
                        index = rec.index(bef)
                        rec.insert(index - 1, rec.pop(index))

        mid = rec[len(rec)//2]
        total += mid
    return total



print(part1(data))
print(part2(data))


print()