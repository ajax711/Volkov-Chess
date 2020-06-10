import chess
import chess.polyglot

try:
    fen=str(input("Enter FEN of the position :"))
    game = chess.Board(fen)

except:
        print ("INVALID FEN")
        quit()


def material(game):
    
    wp = len(game.pieces(chess.PAWN, chess.WHITE))
    bp = len(game.pieces(chess.PAWN, chess.BLACK))
    wn = len(game.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(game.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(game.pieces(chess.BISHOP, chess.WHITE))
    bb = len(game.pieces(chess.BISHOP, chess.BLACK))
    wr = len(game.pieces(chess.ROOK, chess.WHITE))
    br = len(game.pieces(chess.ROOK, chess.BLACK))
    wq = len(game.pieces(chess.QUEEN, chess.WHITE))
    bq = len(game.pieces(chess.QUEEN, chess.BLACK))

    material= 1*(wp-bp) + 3*(wn+wb-bn-bb) + 5*(wr-br) + 9*(wq-bq)
    return material

def brain():
    if game.is_checkmate():
        if game.turn==chess.WHITE:
            return -123456
        else:
            return 123456
    if game.is_stalemate():
        return 0
    else:
        return material(game)

def minimax(depth, alpha, beta, whitemove): #minmax with alpha-beta pruning
    if depth == 0 or game.is_checkmate() or game.is_stalemate():
        return brain()
 
    if whitemove:
        maxEval = -123456
        for i in game.legal_moves:
            game.push(i)
            eval = minimax(depth - 1, alpha, beta, False)
            game.pop()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
 
    else:
        minEval = +123456
        for i in game.legal_moves:
            game.push(i)
            eval = minimax(depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            game.pop()
            if beta <= alpha:
                break
        return minEval
 

def play(depth):

    if fen=='r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq - 4 4' and whitemove:
        return 'f3e5' #Halloween Gambit
    
    else:

        try:
            move = chess.polyglot.MemoryMappedReader("Performance.bin").weighted_choice(game).move()
            return move
        except:
            movevaldict={}
            bestMove = chess.Move.null()
            maxValue = -123456
#           print (game.legal_moves)
            for move in game.legal_moves:
                game.push(move)
                boardValue = minimax(depth-1, 123456 , -123456, whitemove)
                movevaldict.update( {boardValue:move} )
                game.pop()

            if whitemove:
                    final_move=movevaldict.get(sorted(movevaldict)[len(movevaldict)-1])
            else:
                    final_move=movevaldict.get(sorted(movevaldict)[0])

#           print (movevaldict)

            return (final_move)



k=str(input("Whose move ('W'/'B')"))

if k.lower()=='w':
    whitemove = True
else:
    whitemove = False

print (play(10))
