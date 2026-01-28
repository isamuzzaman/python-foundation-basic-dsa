# Unique Name Collector
names = set()

while True:
    name = input("Enter name (or exit): ")
    if name.lower() == "exit":
        break
    names.add(name)

print("Unique Names:")
for n in names:
    print(n)
