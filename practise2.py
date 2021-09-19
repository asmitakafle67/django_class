import random

# for i in range(3):
#     print(random.randint(10,20))
# members = ['john', 'Mary','harry','mosh','zayn']

# leader = random.choice(members)
# print(leader)

class Dice:
     def roll(self):
         first = random.randint(1,6)
         seconmd = random.randint(1,6)

         return (first, seconmd)

dice = Dice()
print(dice.roll())