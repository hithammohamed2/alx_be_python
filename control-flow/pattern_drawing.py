num_pattern = int(input("Enter the size of the pattern: "))

row = 0
while row < num_pattern:      # ← لازم while هنا
    for col in range(num_pattern):
        print("*", end="")
    print()
    row += 1