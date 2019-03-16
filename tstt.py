def find_mismatch(s1, s2):
    if s1.lower() == s2.lower():
        return 0
    count = 0
    j = 0
    if len(s1) == len(s2):
        for _ in s1:
            if s1[j].lower() != s2[j].lower():
                count += 1
            j += 1

    if (len(s1) == len(s2)) and (count < 2):
        return 1

    if (len(s1) != len(s2)) or (count >= 2):
        return 2


s1 = input("")
s2 = input("")
res = find_mismatch(s1, s2)
print(res)
