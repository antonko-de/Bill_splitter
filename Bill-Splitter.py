import random

# Ask the user for input so you know in between how many people the bill will be split
friends_count = input("Enter the number of friends joining (including you):\n")

# init a list for later use
names_list = []


def get_lucky(lst):
    # if this function is called we use it to chose one name at random from a list of names
    # and afterwards print it out
    winner = random.choice(lst)
    return winner


def bill_split(lst, bill, winner):
    # it creates a dictionary with the bill of each person
    # init a list for later use
    friends_group = {}
    if winner:
        for j in lst:
            if j == winner:
                friends_group[j] = 0
            else:
                friends_group[j] = round(bill / (len(lst) - 1), 2)
    else:
        for k in lst:
            friends_group[k] = round(bill / len(lst), 2)
    return friends_group


try:
    # takes care of the case where there are 0 friends

    if int(friends_count) <= 0:
        print('No one is joining for the party')
        quit()
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        # a loop to get all the friends so we know how much is the tab of each one
        for i in range(0, int(friends_count)):
            name = input()
            names_list.append(name)
    # get the total bill of the party

    total_bill = int(input("Enter the total bill value:\n"))
    # a lop to split the bull evenly and round it as necessary

    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    # if statement if the party wants to play a game with a lucky one

    if answer == 'Yes':
        the_winner = get_lucky(names_list)
        print(f"{the_winner} is the lucky one!\n")

    else:
        the_winner = None
        print("No one is going to be lucky\n")

    if bill_split(names_list,total_bill, the_winner):
        print(bill_split(names_list,total_bill, the_winner))
except ValueError:
    # takes care of the exception where the input is string
    print('No one is joining for the party')

