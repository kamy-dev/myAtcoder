s = [ int(i) for i in input()]
count = 0
for i in range(len(s)):
    if s[i] == 1:
        count += 1
print(count)