lines = ""
with open("1.txt", "r") as f:
    lines = f.read().splitlines()

current1, current2, count1, count2 = 50, 50, 0, 0
for line in lines:
    dir = line[0]
    num = int(line[1:])

    # --- Part 1 ---
    current1 = (current1 + num) % 100 if dir == "R" else (current1 - num) % 100
    if current1 == 0:
        count1 += 1

    # --- Part 2 ---
    if dir == "R":
        current2 += num
        count2 += current2 // 100
    else:
        current2 -= num
        count2 += abs((current2 + 99) // 100 if current2 + num == 0 else (current2 - 1) // 100)
    current2 %= 100

print("Part 1:", count1)
print("Part 2:", count2)
