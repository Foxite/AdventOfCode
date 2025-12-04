# Generate prime factors for the amount of digits in an ID, then checks if the ID is equal to a substring of that length concatenated by itself.
# This works for the example input, but not for the real input.
# Takes about 1.15 seconds.

import time

idRanges = []

with open("day2.txt") as file:
    text = file.read()
    fileRanges = text.split(",")
    for fileRange in fileRanges:
        sections = fileRange.split("-")
        idRanges.append({
            "start": int(sections[0]),
            "end":   int(sections[1]),
        })

def prime_factors(num):
    if num == 1:
        return [1]

    ret = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            ret.append(i)
    return ret

def is_invalid_id(idStr):
    for factor in prime_factors(len(idStr)):
        mult = int(len(idStr) / factor)
        if idStr == (idStr[:factor] * mult):
            #print(f"{idStr[:factor]} {idStr}")
            return True
    return False

# test prime factor function
primeFactorCases = {
    1:  [1],
    2:  [1],
    3:  [1],
    4:  [1, 2],
    5:  [1],
    6:  [1, 2, 3],
    7:  [1],
    8:  [1, 2, 4],
    9:  [1, 3],
    10: [1, 2, 5],
}

for num in primeFactorCases.keys():
    if prime_factors(num) != primeFactorCases[num]:
        raise Exception(f"incorrect result for {num}: got {prime_factors(num)}, expected {primeFactorCases[num]}")

# compute puzzle answer
start = time.time()
answer = 0
for idRange in idRanges:
    for checkId in range(idRange["start"], idRange["end"] + 1):
        if is_invalid_id(str(checkId)):
            #print(checkId)
            answer += checkId

end = time.time()

print()
print(answer)
print(f"Time taken: {end-start} seconds")
