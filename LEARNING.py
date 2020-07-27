#### Party 1, Party 2, Party3....####

## Party 1 and Party 2 
#  50000        25000
#  if party 1 has more votes than party 2 obviously party 1 wins!!
#  Else  Party 2 wins...

## Party 1 , Party 2, Party 3
#  50000,      25000,   75000
# if party 1 has more votes than party 2 and Party 3 obviously party 1 wins!!
# else if party 2 has more votes than party 1 and party 3 obviously party 2 wins!!
# else party 3 wins....


Party_1 = int(input("Enter the total number of votes for party 1: "))
Party_2 = int(input("Enter the total number of votes for party 2: "))
Party_3 = int(input("Enter the total number of votes for party 3: "))

if Party_1 > Party_2 and Party_1 > Party_3:
    print("Party 1 wins with " ,Party_1, "votes!!")

elif Party_2 > Party_1 and Party_2 > Party_3:
    print("Party 2 wins with " ,Party_2, "votes!!")

else:
    print("Party 3 wins with " ,Party_3, "votes!!")
