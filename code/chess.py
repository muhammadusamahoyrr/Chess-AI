import sys
import math

# Unicode pieces for better visualization
WHITE_PIECES = {'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙'}
BLACK_PIECES = {'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'}
EMPTY = '.'

# Color constants
WHITE = "white"
BLACK = "black"

# Initialize the board
def initialize_board():
    return [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # Black pieces (lowercase)
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # White pieces (uppercase)
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

# Print the board with Unicode pieces and coordinates
def print_board(board):
    # Print column labels
    print("\n  a   b   c   d   e   f   g   h")
    
    # Print top border
    print("  " + "-" * 33)
    
    # Print each row with pieces
    for i, row in enumerate(board):
        print(f"{8-i}|", end=" ")
        for piece in row:
            if piece == '.':
                print(" ", end=" | ")
            elif piece.isupper():  # White pieces
                print(WHITE_PIECES.get(piece, piece), end=" | ")
            else:  # Black pieces
                print(BLACK_PIECES.get(piece, piece), end=" | ")
        print(f" {8-i}")
        
        # Print row separator
        print("  " + "-" * 33)
    
    # Print column labels again
    print("  a   b   c   d   e   f   g   h\n") 
    
# Convert algebraic notation to board coordinates
def algebraic_to_coordinates(move):
    col = ord(move[0]) - ord('a')
    row = 8 - int(move[1])
    return row, col

# Convert board coordinates to algebraic notation
def coordinates_to_algebraic(coords):
    row, col = coords
    return f"{chr(col + ord('a'))}{8 - row}"

# Check if a move is valid
def is_valid_move(board, start, end, player):
    x1, y1 = start
    x2, y2 = end
    piece = board[x1][y1]
    target = board[x2][y2]

    dx = x2 - x1
    dy = y2 - y1
    abs_dx = abs(dx)
    abs_dy = abs(dy)

    # Check if the piece belongs to the player
    if piece == '.' or (player == WHITE and not piece.isupper()) or (player == BLACK and piece.isupper()):
        return False

    # Check if the target square is occupied by the player's own piece
    if target != '.' and ((player == WHITE and target.isupper()) or (player == BLACK and not target.isupper())):
        return False

    # Pawn movement
    if piece.lower() == 'p':
        if player == WHITE:  # White pawns move upward (decreasing row)
            # Move one square forward
            if x2 == x1 - 1 and y2 == y1 and target == '.':     
                return True
            # Capture diagonally
            if x2 == x1 - 1 and abs(y2 - y1) == 1 and target != '.' and not target.isupper():  
                return True
            # Move two squares forward on the first move
            if x1 == 6 and x2 == 4 and y2 == y1 and board[5][y1] == '.' and target == '.':
                return True
        else:  # Black pawns move downward (increasing row)
            # Move one square forward
            if x2 == x1 + 1 and y2 == y1 and target == '.':
                return True
            # Capture diagonally
            if x2 == x1 + 1 and abs(y2 - y1) == 1 and target != '.' and target.isupper():
                return True
            # Move two squares forward on the first move
            if x1 == 1 and x2 == 3 and y2 == y1 and board[2][y1] == '.' and target == '.':
                return True
        return False

    # Bishop movement
    elif piece.lower() == 'b':
        if abs_dx != abs_dy:
            return False
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        x, y = x1 + step_x, y1 + step_y
        while x != x2 or y != y2:  # Fixed: Changed 'and' to 'or'
            if board[x][y] != '.':
                return False
            x += step_x
            y += step_y
        return True
    
    # Knight movement
    elif piece.lower() == 'n':
        return (abs_dx == 2 and abs_dy == 1) or (abs_dx == 1 and abs_dy == 2)

    # Rook movement
    elif piece.lower() == 'r':
        if x1 != x2 and y1 != y2:
            return False
        if x1 == x2:  # Horizontal move
            start_y, end_y = min(y1, y2), max(y1, y2)
            for y in range(start_y + 1, end_y):
                if board[x1][y] != '.':
                    return False
        else:  # Vertical move
            start_x, end_x = min(x1, x2), max(x1, x2)
            for x in range(start_x + 1, end_x):
                if board[x][y1] != '.':
                    return False
        return True
        
    # Queen movement
    elif piece.lower() == 'q':
        # Diagonal like bishop
        if abs_dx == abs_dy:
            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1
            x, y = x1 + step_x, y1 + step_y
            while x != x2 or y != y2:  # Fixed: Changed 'and' to 'or'
                if board[x][y] != '.':
                    return False
                x += step_x
                y += step_y
            return True
        # Straight line like rook
        elif x1 == x2 or y1 == y2:
            if x1 == x2:  # Horizontal move
                start_y, end_y = min(y1, y2), max(y1, y2)
                for y in range(start_y + 1, end_y):
                    if board[x1][y] != '.':
                        return False
            else:  # Vertical move
                start_x, end_x = min(x1, x2), max(x1, x2)
                for x in range(start_x + 1, end_x):
                    if board[x][y1] != '.':
                        return False
            return True
        return False
    
    # King movement
    elif piece.lower() == 'k':
        return abs_dx <= 1 and abs_dy <= 1

    return False

# Make a move
def make_move(board, start, end):
    x1, y1 = start
    x2, y2 = end
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = '.'

# Check if king is in check
def is_in_check(board, player):
    # Find the king
    king_piece = 'K' if player == WHITE else 'k'
    king_pos = None
    for i in range(8):
        for j in range(8):
            if board[i][j] == king_piece:
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        return False  # No king found (shouldn't happen in a valid game)
    
    # Check if any opponent piece can capture the king
    opponent = BLACK if player == WHITE else WHITE
    opponent_moves = get_all_moves(board, opponent)
    for move in opponent_moves:
        if move[1] == king_pos:
            return True
    
    return False

# Evaluate the board
def evaluate_board(board):
    piece_values = {
        'P': 100, 'p': -100,    # Pawns
        'N': 320, 'n': -320,    # Knights
        'B': 330, 'b': -330,    # Bishops
        'R': 500, 'r': -500,    # Rooks
        'Q': 900, 'q': -900,    # Queens
        'K': 20000, 'k': -20000  # Kings (high value to prioritize king safety)
    }
    
    score = 0
    
    # Material evaluation
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece in piece_values:
                score += piece_values[piece]
    
    # Position evaluation - center control bonus
    position_values = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [5, -5, -10, 0, 0, -10, -5, 5],
        [0, 0, 0, 20, 20, 0, 0, 0],
        [5, 5, 10, 25, 25, 10, 5, 5],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece == 'P':  # White pawn
                score += position_values[i][j]
            elif piece == 'p':  # Black pawn
                score -= position_values[7-i][j]  # Mirror for black
            
            # Knights and bishops benefit from central positions
            if piece == 'N' or piece == 'B':
                score += position_values[i][j] * 0.5
            elif piece == 'n' or piece == 'b':
                score -= position_values[7-i][j] * 0.5
    
    # Check for check (bonus for putting opponent in check)
    if is_in_check(board, BLACK):  # Black is in check
        score += 50
    if is_in_check(board, WHITE):  # White is in check
        score -= 50
    
    return score

# Alpha-beta pruning with iterative deepening
def alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate_board(board)
    
    player = WHITE if maximizing_player else BLACK
    moves = get_all_moves(board, player)
    
    if maximizing_player:
        best_value = -math.inf
        for move in moves:
            # Make a deep copy of the board
            new_board = [row[:] for row in board]
            make_move(new_board, move[0], move[1])
            
            # Recursive evaluation
            value = alpha_beta(new_board, depth - 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            
            if beta <= alpha:
                break  # Beta cutoff
        return best_value
    else:
        best_value = math.inf
        for move in moves:
            # Make a deep copy of the board
            new_board = [row[:] for row in board]
            make_move(new_board, move[0], move[1])
            
            # Recursive evaluation
            value = alpha_beta(new_board, depth - 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            
            if beta <= alpha:
                break  # Alpha cutoff
        return best_value

# Get best move using alpha-beta search
def get_best_move(board, player, depth):
    best_move = None
    if player == WHITE:
        best_value = -math.inf
        maximizing = True
    else:
        best_value = math.inf
        maximizing = False
    
    moves = get_all_moves(board, player)
    
    # Shuffle moves to add variety
    import random
    random.shuffle(moves)
    
    for move in moves:
        # Make a deep copy of the board
        new_board = [row[:] for row in board]
        make_move(new_board, move[0], move[1])
        
        # Evaluate position after move
        value = alpha_beta(new_board, depth - 1, -math.inf, math.inf, not maximizing)
        
        if player == WHITE and value > best_value:
            best_value = value
            best_move = move
        elif player == BLACK and value < best_value:
            best_value = value
            best_move = move
    
    return best_move, best_value

# Get all possible moves for a player
def get_all_moves(board, player):
    moves = []
    for i in range(8):
        for j in range(8):
            # Check if piece belongs to the player
            piece = board[i][j]
            if piece != '.' and ((player == WHITE and piece.isupper()) or (player == BLACK and not piece.isupper())):
                for x in range(8):
                    for y in range(8):
                        if is_valid_move(board, (i, j), (x, y), player):
                            moves.append(((i, j), (x, y)))
    return moves

# Main game loop
def main():
    try:
        # Configure stdout for UTF-8 encoding if available
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        # For Python versions that don't support reconfigure
        pass

    board = initialize_board()
    print("Welcome to Chess Engine!")
    print("Enter moves in algebraic notation (e.g., 'e2 e4')")
    print("Type 'quit' to exit the game.")
    print_board(board)
    
    # Game settings
    human_player = WHITE  # Human plays white (uppercase pieces)
    computer_player = BLACK  # Computer plays black (lowercase pieces)
    ai_depth = 3  # Default search depth (adjust based on performance)
    current_player = WHITE  # White moves first

    while True:
        if current_player == human_player:
            # Human's turn
            try:
                move_input = input("Your move (e.g., 'e2 e4'): ").strip().lower()
                if move_input in ['quit', 'exit']:
                    print("Thanks for playing!")
                    break
                
                # Parse the move
                move_parts = move_input.split()
                if len(move_parts) != 2:
                    print("Invalid input format. Use notation like 'e2 e4'.")
                    continue
                
                from_algebraic, to_algebraic = move_parts
                start = algebraic_to_coordinates(from_algebraic)
                end = algebraic_to_coordinates(to_algebraic)
                
                # Check if the move is valid
                if not is_valid_move(board, start, end, human_player):
                    print("Invalid move. Try again.")
                    continue
                
                # Make the move
                make_move(board, start, end)
                print(f"You moved from {from_algebraic} to {to_algebraic}")
                print_board(board)
                
                # Check for win conditions
                if not any('k' in ''.join(row) for row in board):  # Check for black king (lowercase k)
                    print("You win! The computer's king has been captured.")
                    break
                
                # Switch player
                current_player = computer_player
                
            except Exception as e:
                print(f"Error: {e}")
                print("Please use algebraic notation like 'e2 e4'")
        
        else:
            # Computer's turn
            print("Computer is thinking...")
            
            # Use iterative deepening
            best_move = None  # Initialize best_move
            move_value = 0    # Initialize move_value
            for current_depth in range(1, ai_depth + 1):
                best_move, move_value = get_best_move(board, computer_player, current_depth)
                
                # Print the evaluation for the current depth
                if current_depth == ai_depth:
                    evaluation = "favorable for computer" if move_value < 0 else "favorable for you"
                    if abs(move_value) < 100:
                        evaluation = "roughly equal"
                    print(f"Computer evaluation: {evaluation}")
            
            if best_move:
                from_pos, to_pos = best_move
                from_algebraic = coordinates_to_algebraic(from_pos)
                to_algebraic = coordinates_to_algebraic(to_pos)
                
                # Make the move
                make_move(board, from_pos, to_pos)
                print(f"Computer moves from {from_algebraic} to {to_algebraic}")
                print_board(board)
                
                # Check for win conditions
                if not any('K' in ''.join(row) for row in board):  # Check for white king (uppercase K)
                    print("Computer wins! Your king has been captured.")
                    break
                
                # Check if human is in check
                if is_in_check(board, human_player):
                    print("You are in check!")
                
                # Switch player
                current_player = human_player
            else:
                print("Computer has no valid moves. It's a stalemate!")
                break

if __name__ == "__main__":
    main()