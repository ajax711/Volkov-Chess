import chess
import chess.svg
import chess.polyglot
game = chess.Board('r1bqkb1r/pppp1ppp/2n2n2/4N3/4P3/2N5/PPPP1PPP/R1BQKB1R w KQkq - 0 1')

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

def whose_move():
    k=str(input("Whose move ('W'/'B')"))

    if k.lower()=='w':
        whitemove = True
    else:
        whitemove = False

def minimax(depth, alpha, beta, whitemove):
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
 
 
k=str(input("Whose move ('W'/'B')"))

if k.lower()=='w':
    whitemove = True
else:
    whitemove = False


def selectmove(depth):
    try:
        move = chess.polyglot.MemoryMappedReader("Performance.bin").weighted_choice(game).move()
        return move
    except:
        bestMove = chess.Move.null()
        maxValue = -123456
        alpha = -123456
        beta = 123456
        for move in game.legal_moves:
            game.push(move)
            boardValue = -minimax(depth-1, beta, alpha, whitemove)
            if boardValue > maxValue:
                maxValue = boardValue;
                bestMove = move
            if (boardValue > alpha):
                alpha = boardValue
            game.pop()
        return bestMove
print (selectmove(3))


