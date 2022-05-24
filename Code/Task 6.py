import json


# tower3 solves normal towers of hanoi of 3 pegs
def towers3(ndisks ,start=1 ,target=3 ,peg_set=set([1 ,2 ,3])):
    if ndisks == 0 or start == target:  # if there are no disks, or no move to make
        return []  # no moves
    my_move = "move(%s,%s) " %(start ,target)
    if ndisks == 1:  # trivial case if there is only one disk, just move it
        return [my_move]
    helper_peg = peg_set.difference([start ,target]).pop()
    moves_to_my_move = towers3(ndisks -1 ,start ,helper_peg,peg_set)
    moves_after_my_move = towers3(ndisks -1 ,helper_peg ,target,peg_set)
    return moves_to_my_move + [my_move] + moves_after_my_move

# memoizer used to store solutions to be used later , this is the dynamic programming enhancement
# if you wish to see its importance comment out the memoizer function and the decorator then call the
# framestewartsolution with 16 disks ( it will take almost 60 seconds) but with memoizer almost instantly under 1 second
def fsMemoizer(f):  # just a junky quick memoizer
    cx = {}
    def f2(*args):
        try:
            key= json.dumps(args)
        except:
            key =json.dumps(args[:-1] + (sorted(list(args[-1])),))
        if key not in cx:
            cx[key] = f(*args)
        return cx.get(key)

    return f2


@fsMemoizer
def FrameStewartSolution(ndisks, start=1, end=4, pegs=set([1, 2, 3, 4])):
    if ndisks == 0 or start == end:  # zero disks require zero moves
        return []
    if ndisks == 1 and len(pegs) > 1:  # if there is only 1 disk it will only take one move
        return ["move(%s,%s)" % (start, end)]
    if len(pegs) == 3:  # 3 pegs is well defined optimal solution of 2^n-1
        return towers3(ndisks, start, end, pegs)
    if len(pegs) >= 3 and ndisks > 0:
        best_solution = float("inf")
        best_score = float("inf")
        for kdisks in range(1, ndisks):
            helper_pegs = list(pegs.difference([start, end]))
            LHSMoves = FrameStewartSolution(kdisks, start, helper_pegs[0], pegs)
            pegs_for_my_moves = pegs.difference([helper_pegs[0]])# cant use the peg our LHS stack is sitting on
            MyMoves = FrameStewartSolution(ndisks - kdisks, start, end, pegs_for_my_moves)  # misleading variable name but meh
            RHSMoves = FrameStewartSolution(kdisks, helper_pegs[0], end, pegs)  # move the intermediat stack to
            if any(move is None for move in [LHSMoves, MyMoves, RHSMoves]): continue  # bad path :(
            move_list = LHSMoves + MyMoves + RHSMoves
            if (len(move_list) < best_score):
                best_solution = move_list
                best_score = len(move_list)
        if best_score < float("inf"):
            return best_solution
    # all other cases where there is no solution (namely one peg, or 2 pegs and more than 1 disk)
    return None





if __name__ == '__main__':
	# this will show a list of 33 moves performed
        print(FrameStewartSolution(8))
