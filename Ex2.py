print("Insert string: ")
S = input()
le = len(S)
print(le)
if le < 4:
    Out = ""
else:
    Out = S[0] + S[1] + S[le-2] + S[le-1]

print(Out)