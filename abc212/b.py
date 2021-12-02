X = input()
X = list(map(int,list(X)))


# check all digits are same or not
digit_dict = {}
for digit in X:
    digit_dict[digit] = True

if len(digit_dict) == 1:
    print("Weak")
    exit(0)

for i in range(1,4):
    if X[i] - X[i-1] != 1 and X[i] - X[i-1] != -9:
        print("Strong")
        exit(0)


print("Weak")