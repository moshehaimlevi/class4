# start

x: int = int (input('enter a number of slices'))

friends: int = x // 4

slices: int = x % 4

if friends > 0:
    print (f"{friends} with slices and another {slices} are left")
else:
    print (f"{friends} left with the last slices")

# end