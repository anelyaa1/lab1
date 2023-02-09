def solve1(rabbits, chicken):
    rabbits = legs // 4
    chicken = heads - legs // 4
    print(str(rabbits) + ' ' + str(chicken))


heads = int(input())
legs = int(input())

solve1(heads, legs)