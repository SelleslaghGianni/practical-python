# bounce.py
#
# Exercise 1.5
Bounce = 100
for i in range(10):
    Bounce = (Bounce / 100)*60
    print(round(Bounce, 4))