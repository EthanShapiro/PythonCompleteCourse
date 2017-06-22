nl = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nl[::][0])

for i in range(len(nl)-1, 0-1, -1):
    nl[::][i]

print(nl[0][2])
print(nl[::])
print([sublist[i] for sublist in nl for i in range(len(nl)-1, 0-1, -1)])

n = [['x', 'x'], ['x', 'x']]

if n[::].count(' ') > 0:
    print("found space")

x = 0
y = 4
if x or y < 0 or x or y > 3:
    print('x or y is less than 0')
