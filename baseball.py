'''
Name: Jacob Courtney
Program: baseball.py
program description: The program will ask the user how many tickets they
would like to order and how much each will cost. Then the user will be
asked if they would like to purchase more tickets. 
After the program is concluded add up the total tickets purchased 
and the amount that will be spent on tickets
'''
#ask the user how many tickets will be purchased
tickets = int(input("How many tickets do you want?"))

#ask the user how much each ticket will cost
cost_each = float(input("How much does each cost?"))

#initialize the total amount of tickets
total_tickets = 0

#initialize the amount of money that has been collected in total
total_collected = 0

#set the amount of extras including food per ticket
EXTRAS = 50.00

#calculate the amount of tickets purchased
total_tickets = total_tickets + tickets

#calculate the amount spent on tickets  
cost_for_tickets = tickets * cost_each

#calculate the total amount for all of the extras    
total_extras = tickets * EXTRAS

#calculate the total cost with all of the tickets and the extras    
total_cost = cost_for_tickets + total_extras

#add up all of the totals collected (this will be a running total 
#for all purchases
total_collected = total_collected + total_cost

#output the amount of tickets and total spent for this purchase
print ("Number of tickets ", tickets)
print("Cost per ticket $", format(cost_each, ',.2f'))
print("Cost for the tickets $", format(cost_for_tickets, ',.2f'))
print("Cost of extras including food $", format(total_extras, ',.2f'))
print ("Total cost to go to the game is $",format(total_cost, ',.2f'))

#ask if the user would like to purchase more tickets
another = input("would you like to order more tickets? (y or yes):")

#create a loop that if the user enters y or yes will ask for more input
while another == 'y' or another == 'yes':
    
    #ask how many more tickets to be purchased
    tickets = int(input("How many tickets do you want?"))
    
    #ask how much each ticket costs this round
    cost_each = float(input("How much does each cost?"))
    
    #set total for extras on this purchase
    EXTRAS = 50.00
    
    #calculate the total of tickets purchase
    total_tickets = total_tickets + tickets
    
    #calculate the total for the tickets purchased
    cost_for_tickets = tickets * cost_each
    
    #calculate the amount of extras based on the amount of tickets
    total_extras = tickets * EXTRAS
    
    #calculate the total cost of both the tickets and the extras
    total_cost = cost_for_tickets + total_extras
    
    #add up all of the totals collected (this will be a running total 
    #for all purchases
    total_collected = total_collected + total_cost
    
    #output the amount of tickets and total spent for this purchase
    print ("Number of tickets ", tickets)
    print("Cost per ticket $", format(cost_each, ',.2f'))
    print("Cost for the tickets $", format(cost_for_tickets, ',.2f'))
    print("Cost of extras including food $", format(total_extras, ',.2f'))
    print ("Total cost to go to the game is $",format(total_cost, ',.2f'))
    
    #ask the user if they would like to make another ticket purchase
    another = input("would you like to order more tickets? (y or yes):")

#if the user is done inputting purchasing tickets, output the 
#total amount of tickets purchased and money collected for the game. 
print("The total amount of tickets ordered is: ", total_tickets)
print("your total to go the game is: ", format(total_collected, ',.2f'))
