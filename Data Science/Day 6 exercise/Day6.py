import random

def is_good_turn(x, y):
    return x + y > 6


cheif_dice = random.randint(1, 6)
chefina_dice = random.randint(1, 6)

print(f"Cheif rolled: {cheif_dice}")
print(f"Chefina rolled: {chefina_dice}")

if is_good_turn(cheif_dice, chefina_dice):
    print("It's a good turn!")
else:
    print("It's not a good turn.")
