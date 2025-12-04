# Use a regex to check if the ID is a repeat of its own start.
# Takes about 0.65 seconds, surprisingly twice as fast as the first attempt.

import re
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

# Note: a highly-upvoted SO answer says Python automatically compiles and caches your regexes
# when you use re.match, which would mean that there is no performance benefit from doing this
# yourself - but manually compiling this regex cuts the program runtime in HALF.
# https://stackoverflow.com/a/452143
compiledRegex = re.compile("^(\\d+)\\1+$")
def is_invalid_id(idStr):
    return compiledRegex.match(idStr)

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
