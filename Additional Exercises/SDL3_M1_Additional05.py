# Additional 05

chemistry = int(input("Enter your chemistry mark here: "))
biology = int(input("Enter your biology mark here: "))
physics = int(input("Enter your physics mark here: "))

average = (chemistry + biology + physics) / 3

print()
if average > 84:
    print("Based on your average mark of", average, ", you've earned a distinction!")

if average > 64 and average < 85:
    print("Based on your average mark of", average, ", you've earned a pass!")

if average < 65:
    print("Based on your average mark of", average, ", you have unfortunately failed...")
