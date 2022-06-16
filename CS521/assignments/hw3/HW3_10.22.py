import random

# suits and cards defined to store values
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# function checks to see if suit is in deck
def hasSuit(cards, suit):
    for i in cards:
        if suit in i:
            return True
    return False

# function checks to see if deck has all 4 suits
def hasAllSuit(cards):
    for i in suits:
        if not hasSuit(cards, i):
            return False
    return True

# main function runs 
def main():
    deck = []
    myCards= []
    j = 0

    # for loop used to append one random card
    for i in range(52):
        deck.append(cards[int(i/4)] + " of " + suits[i%4])

    # while loop used to count how many time it takes to get one suit to be picked once
    while not hasAllSuit(myCards):
        randomNumber = random.randint(0, 51)
        card = deck[randomNumber]
        if not hasSuit(myCards, card[0]):
            myCards.append(card)
        j += 1
    
    # prints result
    for i in myCards:
        print(i)
    print('Number of picks:', j)

main()