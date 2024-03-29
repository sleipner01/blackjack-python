from random import randint

#Global variables
blackjackScore = 21
dealerThreshold = 17
cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
dealerHand = []
totalDealerHand = 0
playerHand = []
totalPlayerHand = 0
finishGame = 'N'


#Gamecontrol
def blackjack():
    print('---------------------')
    print("Welcome to Blackjack!")
    
    #Gives the dealer cards
    dealerHand()
    
    #Gives player cards
    playerHand()
    
    #Checks what cards the player has
    checkPlayerHand()
    #Checks if the first two cards give blackjack
    checkBlackjack('player')
    
    #Checks the dealers hand
    checkDealerHand()
    #Checks if the first two cards give blackjack
    checkBlackjack('dealer')
    
    #As long as noone have gotten blackjack
    #Checks if user wants draw a card
    if finish != 'Y': drawCard()

    #See who won
    finish()

    
def playerHand():
    global playerHand
    playerHand = [cards[randint(0,12)], cards[randint(0,12)]]

    
def dealerHand():
    global dealerHand
    dealerHand = [cards[randint(0,12)], cards[randint(0,12)]]

    
def checkPlayerHand():
    print("Here are your cards:", playerHand)

    total = handTotal('playerHand')
    
    global totalPlayerHand
    totalPlayerHand = total
    
    print('Your score is:', totalPlayerHand)

    
def checkDealerHand():
    print("The dealers cards: ", str(dealerHand[0]) + ", ?")

    total = handTotal('dealerHand')
    
    global totalDealerHand
    totalDealerHand = total
    
    
def handTotal(hand):
    total = 0
    for i in globals()[hand]:
        if str(i) == 'J' or str(i) == 'Q' or str(i) == 'K':
            total += 10
        elif str(i) == 'Ace':
            if(total <= 10):
                total += 11
            else:
                total += 1
        else:
            total += i
    
    return total
    
    
def drawCard():
    answer = 'Y'
    while totalPlayerHand < blackjackScore and answer == 'Y':
        # Player
        question = str(input('Do you want another card? (Y/N): ')).upper()
        if question == 'Y':
            playerHand.append(cards[randint(0,12)])
            checkPlayerHand()
            
            # Dealer
            if handTotal('dealerHand') <= dealerThreshold:
                dealerHand.append(cards[randint(0,12)])
                checkDealerHand()
            print(dealerHand)
        elif question == 'N':
            answer = 'N'
        else:
            print('You have to answer with "Y" og "N"')
        

    
def checkBlackjack(origin):
    #If the first two cards are blackjack
    global finishGame
    if origin == 'player':
        if handTotal('playerHand') == blackjackScore:
            print('You have blackjack!')
            finishGame = 'Y'
        else:
            return
    if origin == 'dealer':        
        if handTotal('dealerHand') == blackjackScore:
            print('The dealer has blackjack!')
            finishGame = 'Y'
        else:
            return


def finish():
    #If the player passes blackjackScore
    if totalPlayerHand > blackjackScore:
        print(f'You passed {blackjackScore}')
        print('Sorry, you lost')
        
    #If the dealer passes blackjackScore
    if totalDealerHand > blackjackScore:
        print(f'The dealer passed {blackjackScore}')
        print('You won!')
        
    #If the player is finished drawing cards
    if totalPlayerHand <= blackjackScore:
        if totalPlayerHand > totalDealerHand:
            print('You won!')
        elif totalPlayerHand == totalDealerHand:
            print("OMG it's a tie!")
        else:
            print('The dealer won...')
            
    print('You had:', totalPlayerHand)
    print('The dealer had:', totalDealerHand)

    
blackjack()