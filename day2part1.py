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

def is_invalid_id(idStr):
    if len(idStr) % 2 == 1:
        return False

    halfLength = int(len(idStr) / 2)
    if idStr[:halfLength] == idStr[halfLength:]:
        return True
    else:
        return False

answer = 0
for idRange in idRanges:
    for checkId in range(idRange["start"], idRange["end"] + 1):
        if is_invalid_id(str(checkId)):
            #print(checkId)
            answer += checkId

print(answer)
