from collections import deque
from enum import Enum

class Suit(Enum): # Do I really need to explain this?
    HEARTS = 1
    SPADES = 2
    DIAMONDS = 3
    CLUBS = 4
    
class Rank(Enum): # Well duh?
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    
class Card:
    # Each card is made of a Suit and a Rank
    def __init__(self, Suit, Rank):
        self.Suit = Suit
        self.Rank = Rank

    # Overloading the equality operator such that Cards can be compared
    def __eq__(self, other): 
        if(self.Suit == other.Suit): # Check Suits are equal first
            if(self.Rank == other.Rank): # Then check the Rank of the card
                return True
            else:
                return False
        else: 
            return False
        
    def __repr__(self): # String representation of the Card done here instead of creating seperate repr in Rank and Suit because I'm dumb :p
        if self.Suit == Suit.HEARTS:
            if self.Rank == Rank.ACE:
                return(u"\U0001F0B1")
            elif self.Rank == Rank.TWO:
                return(u"\U0001F0B2")
            elif self.Rank == Rank.THREE:
                return(u"\U0001F0B3")
            elif self.Rank == Rank.FOUR:
                return(u"\U0001F0B4")
            elif self.Rank == Rank.FIVE:
                return(u"\U0001F0B5")
            elif self.Rank == Rank.SIX:
                return(u"\U0001F0B6")
            elif self.Rank == Rank.SEVEN:
                return(u"\U0001F0B7")
            elif self.Rank == Rank.EIGHT:
                return(u"\U0001F0B8")
            elif self.Rank == Rank.NINE:
                return(u"\U0001F0B9")
            elif self.Rank == Rank.TEN:
                return(u"\U0001F0BA")
            elif self.Rank == Rank.JACK:
                return(u"\U0001F0BB")
            elif self.Rank == Rank.QUEEN:
                return(u"\U0001F0BC")
            elif self.Rank == Rank.KING:
                return(u"\U0001F0BD")
        elif self.Suit == Suit.SPADES:
            if self.Rank == Rank.ACE:
                return(u"\U0001F0A1")
            elif self.Rank == Rank.TWO:
                return(u"\U0001F0A2")
            elif self.Rank == Rank.THREE:
                return(u"\U0001F0A3")
            elif self.Rank == Rank.FOUR:
                return(u"\U0001F0A4")
            elif self.Rank == Rank.FIVE:
                return(u"\U0001F0A5")
            elif self.Rank == Rank.SIX:
                return(u"\U0001F0A6")
            elif self.Rank == Rank.SEVEN:
                return(u"\U0001F0A7")
            elif self.Rank == Rank.EIGHT:
                return(u"\U0001F0A8")
            elif self.Rank == Rank.NINE:
                return(u"\U0001F0A9")
            elif self.Rank == Rank.TEN:
                return(u"\U0001F0AA")
            elif self.Rank == Rank.JACK:
                return(u"\U0001F0AB")
            elif self.Rank == Rank.QUEEN:
                return(u"\U0001F0AC")
            elif self.Rank == Rank.KING:
                return(u"\U0001F0AD")
        elif self.Suit == Suit.DIAMONDS:
            if self.Rank == Rank.ACE:
                return(u"\U0001F0C1")
            elif self.Rank == Rank.TWO:
                return(u"\U0001F0C2")
            elif self.Rank == Rank.THREE:
                return(u"\U0001F0C3")
            elif self.Rank == Rank.FOUR:
                return(u"\U0001F0C4")
            elif self.Rank == Rank.FIVE:
                return(u"\U0001F0C5")
            elif self.Rank == Rank.SIX:
                return(u"\U0001F0C6")
            elif self.Rank == Rank.SEVEN:
                return(u"\U0001F0C7")
            elif self.Rank == Rank.EIGHT:
                return(u"\U0001F0C8")
            elif self.Rank == Rank.NINE:
                return(u"\U0001F0C9")
            elif self.Rank == Rank.TEN:
                return(u"\U0001F0CA")
            elif self.Rank == Rank.JACK:
                return(u"\U0001F0CB")
            elif self.Rank == Rank.QUEEN:
                return(u"\U0001F0CC")
            elif self.Rank == Rank.KING:
                return(u"\U0001F0CD")
        elif self.Suit == Suit.CLUBS:
            if self.Rank == Rank.ACE:
                return(u"\U0001F0D1")
            elif self.Rank == Rank.TWO:
                return(u"\U0001F0D2")
            elif self.Rank == Rank.THREE:
                return(u"\U0001F0D3")
            elif self.Rank == Rank.FOUR:
                return(u"\U0001F0D4")
            elif self.Rank == Rank.FIVE:
                return(u"\U0001F0D5")
            elif self.Rank == Rank.SIX:
                return(u"\U0001F0D6")
            elif self.Rank == Rank.SEVEN:
                return(u"\U0001F0D7")
            elif self.Rank == Rank.EIGHT:
                return(u"\U0001F0D8")
            elif self.Rank == Rank.NINE:
                return(u"\U0001F0D9")
            elif self.Rank == Rank.TEN:
                return(u"\U0001F0DA")
            elif self.Rank == Rank.JACK:
                return(u"\U0001F0DB")
            elif self.Rank == Rank.QUEEN:
                return(u"\U0001F0DC")
            elif self.Rank == Rank.KING:
                return(u"\U0001F0DD")
        else:
            return("Ill-formed Card")
        
class Deck:
    # A simple object that provides deck-like functionality
    def __init__(self, maxLength = 52):
        self.deck = deque(maxlen=maxLength)
        
    def populateWithFrenchPlayingDeck(self):
        for a in Suit:
            for b in Rank:
                self.deck.append(Card(a,b))
        
        
    # Returns the current size of the Deck
    def getSizeOfDeck(self):
        return len(self.deck)
    
    def __repr__(self):
        outputstring = ""
        for card in self.deck:
            outputstring += repr(card)
        return outputstring
    
    
    # Takes a list variable, cards, and iteratively adds them to the end of the deck
    def addCardsToDeck(self, cards):
        for card in cards:
            self.d.append(card)
        return