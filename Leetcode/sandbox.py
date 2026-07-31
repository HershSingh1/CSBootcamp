strs = ["act", "pots", "tops", "cat", "stop", "hat"]
answer = {}
for str in strs:
    count = [0] * 26
    for letter in str:
        count[ord(letter) - ord("a")] += 1
    if tuple(count) in answer:
        answer[tuple(count)].append(str)
    else:
        answer[tuple(count)] = [str]
print(list(answer.values()))
