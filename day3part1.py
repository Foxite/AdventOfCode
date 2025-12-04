banks = []

with open("day3.txt") as file:
    for bankLine in file:
        bank = []
        for bankChar in bankLine:
            bank.append(bankChar)
        banks.append(bank)

def find_max_joltage(bank):
    maxJoltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            if int(bank[i] + bank[j]) > maxJoltage:
                maxJoltage = int(bank[i] + bank[j])
    return maxJoltage

joltage = 0
for bank in banks:
    joltage += find_max_joltage(bank)

print(joltage)
