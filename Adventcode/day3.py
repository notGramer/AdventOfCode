import re


# Open the file and read the data
with open('input-day3.txt', 'r') as file:
    data = file.readlines()

title_search = re.search('<title>(.*)</title>', txt, re.IGNORECASE)

if title_search:
    title = title_search.group(1)
# search_group() gibt dir das nth element von der regex

result = 0
mules = []


# Process each line
for line in data:
    # Find all instances of 'mul(X,Y)' in the line
    matches = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
    mules.append(matches)


print(result)
print(mules)