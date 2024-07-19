# fruits = ["apples","oranges","bananas"]

# new_fruits = [fruit.swapcase() for fruit in fruits]

# print(fruits,new_fruits)

# bits=[True, False, True, True, True, False, True]

# new_bits = [1 if bit==True else 0 for bit in bits]

# print(new_bits)

astring = "ThisIsTom."

new_astring= "".join([s if s.islower() else " "+s for s in astring])[1:]

print(new_astring)