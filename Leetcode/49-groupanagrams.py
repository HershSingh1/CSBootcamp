answer = {}
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
for item in strs:
    count = [0] * 26
    for letter in item:
        count[ord(letter) - 97] += 1
    count = tuple(count)
    if count in answer:
        answer[count].append(item)
    else:
        answer[count] = [item]
print(answer.items())
