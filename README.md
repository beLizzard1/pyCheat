# pyCheat


Cheat is a card-shedding type game in which players attempt to win by having no more cards to lay down.

Traditionally, the player clockwise to the dealer chooses the first cards to be placed down by specifying the Rank of the card they are placing down first. Our initial implementation then goes through the players cyclically asking them to add cards of the same or +/- 1 from the rank of the last claim made to the Pile. 

If another player feels like the claim being made is False, they can announce or declare that their opponent is cheating. If their opponent is cheating then the cheater must pick up the entire pile of cards. If they were not cheating then the accuser must pick up the cards. 

https://en.wikipedia.org/wiki/Cheat_(game)

Cheat was chosen because, once the fundamentally human capabilities to discern the truth from fiction are removed, the game becomes significantly more complex with players attempting to optimise the probability of their claims being correct using false claims (that hopefully aren't too false) and predicting/tracking the game state over many iterations.

## Project  Structure

There are two key elements to this:

1. gameHost
2. playerClient
    - Bot Client
    - GUI Client

In order to seperate out the various aspects of the project there are two seperate projects, the first gameHost provides the actual game play mechanisms, constructs server-side player entities blah blah blah and keeps a track of the game state. The playerClient connects to the gameHost and waits for the game to start... Every time a decision is required of the client it is informed of its current state and asked for its move (and server-side validation is performed to ensure that the actions are valid).

### Project Objectives

- Create a playable game of Cheat for human operators
- Introduce non-human operators
- Non-human operators initially utilising a variety of different simplistic play styles.
- Attempt to incorporate a variety of different Machine Learning techniques 
- Have various different operators compete against one another (Genetic?)