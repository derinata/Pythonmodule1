# Initialize an empty set
names = set()

while True:
    name = input("Enter a name (empty to stop): ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nNames entered:")
for n in names:
    print(n)
