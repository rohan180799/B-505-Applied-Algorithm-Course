e = [0, 3, 2, 0, 1, 6, 0, 4, 5, 1, 4]
count = []
sorted_arr = [0 for i in range(len(e))]

for i in range(0, max(e) + 1):
    count.append(0)
print (count)
for i in range(0, len(e)):
    count[e[i]] = count[e[i]] + 1
print (count)
for i in range(1, len(count)):
    count[i] = count[i] + count[i-1]
print (count)
for i in range(len(e)):
    sorted_arr[count[e[i]] - 1] = e[i]
    count[e[i]] -= 1
print (sorted_arr)

for i in range(0, len(sorted_arr)):
    e[i] = sorted_arr[i]
# print (sorted_arr)
print (e)