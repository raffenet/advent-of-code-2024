import re

sample = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
input = open("day3/input.txt", 'r')
muls = re.findall(r'mul\([1-9]\d{0,2},[1-9]\d{0,2}\)', input.read(), flags=re.M)
pairs = map(lambda x: x.lstrip('mul(').rstrip(')').split(','), muls)
print("part 1:", sum(map(lambda x: int(x[0]) * int(x[1]), pairs)))

sample = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
input.seek(0)
prods = []
for do in re.split(r'do\(\)', input.read(), flags=re.M):
    enabled = re.split(r'don\'t\(\)', do)[0]
    muls = re.findall(r'mul\([1-9]\d{0,2},[1-9]\d{0,2}\)', enabled)
    pairs = map(lambda x: x.lstrip('mul(').rstrip(')').split(','), muls)
    prods.append(sum(map(lambda x: int(x[0]) * int(x[1]), pairs)))
print("part 2:", sum(prods))
