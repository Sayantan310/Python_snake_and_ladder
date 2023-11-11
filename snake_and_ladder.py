import random
count = sum = 0
snake_table = {
    17: 7,
    62: 19,
    64: 60,
    54: 34,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}
ladder_table = {
    4: 14,
    9: 31,
    20: 38,
    40: 59,
    28: 84,
    63: 81,
    71: 91
}
while sum!=100:
    print(f"your current position is {sum}")
    print(f"dice is rolling ---- turn - {count}")
    dice = random.randint(1,6)
    count+=1
    print(f"dice result - {dice}")
    sum+=dice
    if sum > 100:
        print("Opps try again.... you have to get exact 100 to win....")
        sum-=dice
    elif sum in snake_table:
        print("Sssshhhhh beware of the snakes")
        sum = snake_table[sum]
    elif sum in ladder_table:
        print("Yehhh you got a ladder in your fortune..... quickly climb up....")
        sum = ladder_table[sum]
    elif sum == 100:
        print(f"Yepieeee you finally won the game in {count} dice rolls.......")
        break
