from time import perf_counter
# action when left has 2 1's and right has even number of 1's which is greater than 2
def l2rlargerequal2even(board , firstzeroindex,start):
    board[start],board[start+2]=board[start+2],board[start]
    board[start+1]=0
    print(board)
    board[firstzeroindex+1],board[firstzeroindex+3]=board[firstzeroindex+3],board[firstzeroindex+1]
    board[firstzeroindex+2]=0
    print(board)

#action when left has no 1's and right has 2 1's
def l0r2(board , start , end):
    board[end],board[start+1]=board[start+1],board[end]
    board[start+2]=0
    print(board)

#action when right has no 1's and left has 2 1's
def r0l2(board , start ):
    board[start],board[start+2]=board[start+2],board[start]
    board[start+1]=0
    print(board)

# actions to do when empty cell position wont lead to a board with only one peg
def restofstates():
    print("The choice of empty cell doesn't allow board to be reduced to only 1 peg","\n", "For a board to be reduced choices of empty cell must be 2 , 5 , n-1 and n-4 only" )

# action to do when there is 2 1's on the right and left side of 2 zeros has even number of 1's and greater than 2
def r2llargerequal2even(board , firstzeroindex,end):
    board[end],board[end-2]=board[end-2],board[end]
    board[end-1]=0
    print(board)
    board[firstzeroindex],board[firstzeroindex-2]=board[firstzeroindex-2],board[firstzeroindex]
    board[firstzeroindex-1]=0
    print(board)


# dictionary that stores the states the peg board will be in and also stores
# the appropriate action for each state
# l = left , r = right , and number donates how many 1's
solDict={
    'l0r2': l0r2,
    'l2r>=2even':l2rlargerequal2even ,
    'r0l2': r0l2,
    'r2l>=2even': r2llargerequal2even,
    'rest':restofstates
    # 'l0r>2': ,
    # 'l1r>=1': ,
    # 'l>2r>=1': ,
    # 'r0l>2': ,
    # 'r1l>=1': ,
    # 'r>2l>=1':
}


# recursive function that solves according to the above constraints
def solve(board , start , end):
    left = 0
    right = 0
    index = start
    zeroindex = 0


    #stop when reached the end of the board
    if (start >= end ):
        return

    # count how many 1's on the left of the 2 zeros

    for i in range(start,end+1):
        if board[i] == 1:
            left = left + 1
        elif board[i] == 0:
            zeroindex = index
            break
        index = index + 1

    #  count how many 1's on the right of the 2 zeros

    for i in range(zeroindex, end+1):
        if board[i] == 1:
            right = right + 1


    # choose from Dictionary the appropriate action to make

    if(left==0 and right==2):
        findInDict = 'l0r2'
        solDict[findInDict](board,start,end)
    elif (left==2 and right >= 2 and right % 2 == 0):
        findInDict = 'l2r>=2even'
        solDict[findInDict](board,zeroindex,start)
        # recursive call to the solve function sending it a subproblem
        solve(board,start+2,end)
    elif (right == 0 and left == 2):
        findInDict = 'r0l2'
        solDict[findInDict](board, start)
    elif (right==2 and left >= 2 and left % 2 == 0):
        findInDict = 'r2l>=2even'
        solDict[findInDict](board, zeroindex, end)
        # recursive call to the solve function sending it a subproblem
        solve(board, start, end-2)
    else:
        findInDict = 'rest'
        solDict[findInDict]()


# intial move to place 2 zeros next to eachother to begin solution then call solve function
def initialmove(board , empty , n):

    if (empty == n-4):
        board[empty + 2], board[empty] = board[empty], board[empty + 2]
        board[empty + 1] = 0

    elif empty == 1 or empty == 0 :
        board[empty + 2], board[empty] = board[empty], board[empty + 2]
        board[empty + 1] = 0
    else:
        board[empty-2],board[empty]=board[empty],board[empty-2]
        board[empty-1]=0

    print(board)
    solve(board, 0, len(board) - 1)



# check if user entered odd number or 2 or 0
def checknumberofcells(n):
    if n % 2 != 0 or n == 0 or n == 2 :
        return True


def main():
    n = int(input("Enter Number Of Cells : "))
    if checknumberofcells(n):
        print("N should be Even and Greater than 2")
    else:
        # initialize board and put empty cell in its place
        board = [1]*n
        print(board)
        empty = int(input("Choose Position Of Empty Cell : "))
        board[empty-1]=0
        print(board)
        initialmove(board,empty-1 ,n-1)



main()

