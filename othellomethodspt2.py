
def maxValue(depth, player): # Return the MAXIMUM value of the boards created by appending black moves.
#---Initialize and check assertions.
    global M
    assert player  == HUMAN
    setOfMoveValuesAndMoves = []
    depth = depth-1
    global M
    setOfMoveValuesAndMoves = []
    for r in range(8):
        for c in range(8):
            if M[r][c]!=0:
                continue
            if not LocateTurnedPieces(r,c,player):
                continue
            makeTheMoveAndTurnOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
            setOfMoveValuesAndMoves().append(baseCaseForEvenPlyDepth(depth+1, player),r,c)
            takeBackTheMoveAndTurnBackOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
    if set==[]:
        value=0
    maxthing=setOfMoveValuesAndMoves
    return max(maxthing),r,c
            # 2. WRITE THIS FUNCTION

#----------------------------------------------------------------------------------------------------Othello--
# Return the MINIMUM value of the boards created by appending white moves. Remember, the higher the value,
# the better for black.
def minValue(depth, player):
#---Initialize and check assertions.
    global M
    assert player == COMPUTER # = white
    setOfMoveValuesAndMoves = []        # 3. WRITE THIS FUNCTION
    #EDIT AFTER COMMENT
    depth = depth-1
    global M
    setOfMoveValuesAndMoves = []
    for r in range(8):
        for c in range(8):
            if M[r][c]!=0:
                continue
            if not LocateTurnedPieces(r,c,player):
                continue
            makeTheMoveAndTurnOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
            setOfMoveValuesAndMoves().append(baseCaseForOddPlyDepth(depth+1, player))
            takeBackTheMoveAndTurnBackOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
    if set==[]:
        value=0
    minthing=setOfMoveValuesAndMoves[0]
    for n in range(len(setOfMoveValuesAndMoves)):
        if setOfMoveValuesAndMoves[n][0]<minthing[0]: minthing=setOfMoveValuesAndMoves[n]
    return minthing,r,c
#----------------------------------------------------------------------------------------------------Othello--



# Note that this function is identical to the maxValue function (and is called from the maxValue function),
# except that it does not get its points from its children. Instead, it uses an evaluation function. Why
# return the maximum? The higher the score the better for black.
def baseCaseForEvenPlyDepth(depth, player):
#---Initialize and check assertions.
    global M
    assert player  == HUMAN
    setOfMoveValuesAndMoves = []
    depth = depth-1
    global M
    setOfMoveValuesAndMoves = []
    for r in range(8):
        for c in range(8):
            if M[r][c]!=0:
                continue
            if not LocateTurnedPieces(r,c,player):
                continue
            makeTheMoveAndTurnOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
            setOfMoveValuesAndMoves().append(boardscore(player),r,c) #return the max
            takeBackTheMoveAndTurnBackOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
    if set==[]:
        value=0
    return max(setOfMoveValuesAndMoves),r,c
#----------------------------------------------------------------------------------------------------Othello--

#  This function is identical to the minValue function (and is called from the minValue function), except that
#  it does not get its points from its children. Instead, it uses an evaluation function.
def baseCaseForOddPlyDepth(depth, player):
    global M
    assert depth == 0, [depth]
    updateThePointMatrices()
    minPlayerValue = float('inf')       # 5. WRITE THIS FUNCTION
    setOfMoveValuesAndMoves = []
    for r in range(8):
        for c in range(8):
            if M[r][c]!=0:
                continue
            if not LocateTurnedPieces(r,c,player):
                continue
            makeTheMoveAndTurnOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
            setOfMoveValuesAndMoves().append(boardscore(player),r,c) #return the max
            takeBackTheMoveAndTurnBackOverThePieces(r,c,LocateTurnedPieces(r,c,player),player)
    if set==[]:
        value=0
    return min(setOfMoveValuesAndMoves),r,c