# Go through the numbers and enable all 9s, then all 8s, etc
# Does not produce correct answers.
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

def find_max_joltage(bank):
    def computeJoltage(setting):
        joltage = ""
        for j in range(len(setting)):
            if setting[j]:
                joltage += str(bank[j])
        return int(joltage) if len(joltage) > 0 else 0

    result = [False for _ in range(len(bank))]
    maxResult = result
    maxJoltage = 0
    for i in reversed(range(10)):
        for j in reversed(range(len(result))):
            if bank[j] == str(i):
                result[j] = True

            newJoltage = computeJoltage(result)
            if newJoltage > maxJoltage:
                maxJoltage = newJoltage
                maxResult = result

            if sum(1 for enabled in result if enabled) >= 12:
                break

        if sum(1 for enabled in result if enabled) >= 12:
            break

    print([f"{idx}: {bank[idx]} {result[idx]}" for idx, _ in enumerate(maxResult)])

    return computeJoltage(maxResult)


joltage = 0
for bank in banks:
    bankJoltage = find_max_joltage(bank)
    print(bankJoltage)
    joltage += bankJoltage

print(joltage)
