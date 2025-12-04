def sign(num):
    if num == 0:
        return 0
    if num > 0:
        return 1
    if num < 0:
        return -1

turns = []

with open("day1.txt") as file:
    for line in file:
        if not (line.startswith("R") or line.startswith("L")):
            raise f"Invalid line: {line}"

        direction = line.startswith("R")
        amount = int(line[1:])
        turns.append(amount * (1 if direction else -1))

number = 50
answer = 0
for turn in turns:
    # if it looks stupid but it works, it ain't stupid.
    for _ in range(abs(turn)):
        number += sign(turn)

        if number == 100:
            number -= 100
        if number == -1:
            number += 100
        if number == 0:
            answer += 1

print(answer)
