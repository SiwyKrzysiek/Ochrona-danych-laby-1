file = open('dystrybucja_liter.txt', 'r')
data = file.read()

lines = data.split('\n')
# print(lines)

frequences = {}
for i in range(0, len(lines), 2):
    c, n = lines[i], lines[i+1]
    frequences[c] = n

print(frequences)