hash = {
    "H": False, "2B": False, "3B": False, "HR": False
}
for i in range(4):
  hash[input()] = True

if False in list(hash.values()):
  print("No")
else:
  print("Yes")

