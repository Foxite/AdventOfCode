# Recursive function to brute-force every combination.
# Does not check one bank in less than a minute.
banks = []

with open("day3-test.txt") as file:
    bankLines = file.readlines()
    for bankLine in bankLines:
        bank = []
        for bankChar in bankLine:
            if bankChar == '\n': # silly but idc
                continue
            bank.append(bankChar)
        banks.append(bank)

def find_max_joltage(bank, offset=0):
    maxJoltage = 0
    for i in range(offset, len(bank)):
        if offset == 12:
            if int(bank[offset] + bank[i]) > maxJoltage:
                maxJoltage = int(bank[offset] + bank[i])
        else:
            newMax = find_max_joltage(bank, offset + 1)
            if newMax > maxJoltage:
                maxJoltage = newMax

    return maxJoltage

joltage = 0
for bank in banks:
    joltage += find_max_joltage(bank)

print(joltage)
