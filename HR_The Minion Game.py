"""
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string .
For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
For better understanding, see the image below:
banana.png
Your task is to determine the winner of the game and their score.
Input Format
A single line of input containing the string .
Note: The string  will contain only uppercase letters: .
Constraints
Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
Sample Input
BANANA
Sample Output
Stuart 12
Note :
Vowels are only defined as . In this problem, Y is not considered a vowel.
"""
"""def minion_game(string):
    S = string.upper()
    vowels = ["A", "E", "I", "O", "U"]
    stuart = []
    kevin = []
    for i in range(len(S)):
        if S[i] in vowels:
            kevin.append(S[i])
            for a in range(i+1,len(S)):
                kevin.append(S[i:a+1])
        else:
            stuart.append(S[i])
            for a in range(i+1,len(S)):
                stuart.append(S[i:a+1])
    if len(list(stuart)) >len(list(kevin)):
        print(f"Stuart {len(list(stuart))}")
    elif len(list(stuart)) < len(list(kevin)):
        print(f"Kevin {len(list(kevin))}")
    else:
        print(f"Draw")

        # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)"""
"""def minion_game(string):
    S = string.upper()
    vowels = ["A", "E", "I", "O", "U"]
    Stuart = 0
    Kevin = 0
    for i in range(len(S)):
        if S[i] in vowels:
            Kevin += 1
            for a in range(i+1,len(S)):
                Kevin += 1
        else:
            Stuart += 1
            for a in range(i+1,len(S)):
                Stuart += 1
    if Stuart > Kevin:
        print(f"Stuart {Stuart}")
    elif Stuart < Kevin:
        print(f"Kevin {Kevin}")
    else:
        print(f"Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
"""
def minion_game(string):
    Kevin = 0
    Stuart = 0
    word = list(string.upper())
    x = len(word)
    vowels = ['A','E','I','O','U']
    #print(list(enumerate(word)))
    for inx, w in enumerate(word):
        print(inx,w)
        if w in vowels:
            Kevin = Kevin + x
        else:
            Stuart = Stuart + x
        x = x - 1
    if Stuart > Kevin:
        print ('Stuart', Stuart)
    elif Kevin > Stuart:
        print ('Kevin', Kevin)
    else:
        print ('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
