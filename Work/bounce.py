# bounce.py
#
# Exercise 1.5

current_height = 100
num_bounces = 0

while num_bounces < 10:
    num_bounces += 1
    current_height = current_height * 0.6
    print(num_bounces, round(current_height, 4))
