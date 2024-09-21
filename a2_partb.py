# Main Author: Maharshi Patel
# Main Reviewer: Jeel Patel , Shailendra Zala

# Define a function to copy the game board.
def copy_board(board):
    current_board = []   # Initialize an empty list to store the copied board.
    height = len(board)  # Get the number of rows in the board.
    # Iterate through each row of the board.
    for i in range(height):
        # Append a copy of the row to the current_board list.
        current_board.append(board[i].copy())
    return current_board  # Return the copied board.

# Define a function to evaluate the game board.
def evaluate_board(board, player):
    score = 0  # Initialize the score to 0.
    # Iterate through each cell in the board.
    for row in board:
        for cell in row:
            # If the cell contains 4 consecutive pieces of the current player, add a high score to the player.
            if cell == 4 * player:
                score += 100 * player  
            # If the cell contains a piece of the current player, add 1 to the score.
            elif cell == player:
                score += 1
            # If the cell contains a piece of the opponent player, subtract 1 from the score.
            elif cell == -player:
                score -= 1
    return score  # Return the score.

# Define a class for the game tree.
class GameTree:
    # Define a nested class for the tree nodes.
    class Node:
        # Constructor to initialize a node with the given board, depth, player, and tree height.
        def __init__(self, board, depth, player, tree_height=4):
            # Copy the board to the node.
            self.board = copy_board(board)
            self.depth = depth  # Set the depth of the node.
            self.player = player  # Set the player of the node.
            self.children = []  # Initialize an empty list to store the children nodes.
            # Generate children nodes if the depth is less than the tree height.
            if depth < tree_height:
                self.generate_children(tree_height)

        # Method to generate children nodes for the current node.
        def generate_children(self, tree_height):
            height = len(self.board)  # Get the number of rows in the board.
            width = len(self.board[0])  # Get the number of columns in the board.
            # Iterate through each cell in the board.
            for row in range(height):
                for col in range(width):
                    # If the cell is empty, create a new board with the current player's piece in that cell.
                    if self.board[row][col] == 0:
                        new_board = copy_board(self.board)  # Copy the current board.
                        new_board[row][col] = self.player  # Place the current player's piece in the cell.
                        # Create a new child node with the updated board, depth, player, and tree height.
                        self.children.append(GameTree.Node(new_board, self.depth + 1, -self.player, tree_height))

    # Constructor to initialize the game tree with the given board, player, and tree height.
    def __init__(self, board, player, tree_height=4):
        self.player = player  # Set the player of the game tree.
        # Create the root node of the game tree with the given board, depth 0, player, and tree height.
        self.root = self.Node(board, 0, player, tree_height)

    # Method to perform minimax algorithm on the game tree.
    def minimax(self, node, maximizing_player):
        # If the node has no children or the depth is equal to the tree height, return the evaluation of the node's board.
        if len(node.children) == 0 or node.depth == 3:
            return evaluate_board(node.board, self.player)

        # If the maximizing player is True, perform max evaluation.
        if maximizing_player:
            max_eval = float('-inf')  # Initialize the maximum evaluation to negative infinity.
            # Iterate through each child node of the current node.
            for child in node.children:
                # Perform minimax algorithm recursively on the child node with maximizing_player set to False.
                eval = self.minimax(child, False)
                max_eval = max(max_eval, eval)  # Update the maximum evaluation.
            return max_eval  # Return the maximum evaluation.

        # If the maximizing player is False, perform min evaluation.
        else:
            min_eval = float('inf')  # Initialize the minimum evaluation to positive infinity.
            # Iterate through each child node of the current node.
            for child in node.children:
                # Perform minimax algorithm recursively on the child node with maximizing_player set to True.
                eval = self.minimax(child, True)
                min_eval = min(min_eval, eval)  # Update the minimum evaluation.
            return min_eval  # Return the minimum evaluation.

    # Method to get the best move for the current player.
    def get_move(self):
        best_move = None  # Initialize the best move to None.
        best_score = float('-inf')  # Initialize the best score to negative infinity.
        # Iterate through each child node of the root node.
        for child in self.root.children:
            score = self.minimax(child, False)  # Perform minimax algorithm on the child node.
            # If the score is greater than the best score, update the best score and best move.
            if score > best_score:
                best_score = score  # Update the best score.
                max_row_index = 0  # Initialize the row index of the best move to 0.
                max_col_index = 0  # Initialize the column index of the best move to 0.
                max_val = float('-inf')  # Initialize the maximum value to negative infinity.
                # Iterate through each cell in the child node's board.
                for i in range(len(child.board)):
                    for j in range(len(child.board[0])):
                        # If the value of the cell multiplied by the player's piece is greater than the maximum value.
                        if child.board[i][j] * self.player > max_val:
                            max_val = child.board[i][j] * self.player  # Update the maximum value.
                            max_row_index = i  # Update the row index of the best move.
                            max_col_index = j  # Update the column index of the best move.
                best_move = (max_row_index, max_col_index)  # Update the best move.
        return best_move  # Return the best move.

    # Method to clear the game tree.
    def clear_tree(self):
        self.root = None  # Set the root node to None.

