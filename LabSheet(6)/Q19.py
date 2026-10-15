# 19. Write a program to create the power set of a given set.
s = {1, 2, 3}
power_set = [set()]

for element in s:
    power_set += [subset | {element} for subset in power_set]

print("Power set:", power_set)
