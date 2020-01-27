import sys


with open(sys.argv[1],"r") as fi:
    id = []
    index = 0
    index1 = 0
    for ln in fi:
        if ln.startswith("<status status") and index == 0:
            id.append(ln[1:])
            index = index + 1
        if ln.startswith("<kw name") and index1 == 0:
            id.append(ln[1:])
            index1 = index1 + 1


str = id[0].split('"')
str1 = id[1].split('"')

job = str[1]
status = str1[1]
timeparse = str1[3].split(" ")
date = timeparse[0]
time = timeparse[1].split(".")
time = time[0]

print(job)
print(status)
print(date)
print(time)
