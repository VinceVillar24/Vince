def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    count=0
    temp=''
    for _ in secretWord:
        if (_ in lettersGuessed):
           count+=1 
           temp= temp + _
        else:
            temp=temp + '_' + ' '
    return temp


