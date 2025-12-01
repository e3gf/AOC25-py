lines = ""
with open("1.txt", "r") as f:
    lines = f.read().split('\n')

current, count1, count2 = 50, 0, 0
for line in lines:
    if line == "":
        continue
    dir = line[0]
    num = int(line[1:])
    
    # --- Part 2 --- (handles the overflow and underflow for part 1 too)
    if dir == "R":
        current += num
        count2 += current // 100
        current %= 100
    elif dir == "L":
        current -= num
        count2 += abs(((current + 99) if current + num == 0 else (current - 1)) // 100)
        current %= 100

    # --- Part 1 ---
    if current == 0:
        count1 += 1

print("Part 1:", count1)
print("Part 2:", count2)
