s = input()
result = ""
for c in s:
    if c == " ":
        if len(result) == 0 or len(result) > 0 and result[-1] != " ":
            result += c
    else:
        result += c
print(result)