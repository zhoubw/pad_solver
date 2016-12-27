from numpy import array

class Board:
    # Initializes the board and list of moves.
    def __init__(self, row_len=6, col_len=5, max_moves=50):
        # Orbs are represented by numbers that match their color. Jammer may be a
        # placeholder for now.
        # An initial empty board will be a board full of jammers.
        self.colors = {"Jammer": 0, "Fire": 1, "Water": 2, "Wood": 3, "Light": 4, "Dark": 5, "Heal": 6}
        
        # Initializes the board as a 1d list, to be easily converted to a board
        # state for the neural net.
        self.row_len = row_len
        self.col_len = col_len
        # self.board and self.moves will be combined to create a board state for the neural net.
        self.board = [self.colors["Jammer"] for i in range(row_len * col_len)]
        self.moves = [0 for i in range(max_moves)]

        # Current position will be converted to some two digit number representing
        # column then row, 1-indexed to avoid 0's
        # (x, y), where max y is on the bottom of the board
        self.current_pos = (1, 1)

    # Populates the board with a full set of colors.
    # type(colors) = list of colors
    # Assumes all colors are valid and len(colors) is valid.
    def populate_board(self, colors):
        for i in range(len(colors)):
            self.board[i] = colors[i]
        
    # Checks if position is valid on the board.
    # type(pos) = tuple.
    # A valid x is between 1 and row_len, while a valid y is between 1 and col_len.
    # Returns True if position is valid, False otherwise.
    def valid_pos(self, pos):
        return pos[0] >= 1 and pos[0] <= self.row_len and pos[1] >= 1 and pos[1] <= self.col_len

    # Check if both swap positions are valid.
    # Returns True if both positions are valid, False otherwise.
    def valid_swap(self, pos1, pos2):
        return valid_pos(pos1) and valid_pos(pos2)
    
    # Converts a position into its proper index in the board list.
    # type(pos) = tuple
    # Assumes position is valid.
    # This function is only used when operating directly on the board list.
    # Returns position index, (x - 1) + ((y - 1) * row_len).
    def pos_to_index(self, pos):
        return (pos[0] - 1) + (pos[1] - 1) * self.row_len

    # Swaps two orbs by position.
    # type(pos1) = type(pos2) = tuple
    # Assumes swap is valid.
    def swap(self, pos1, pos2):
        pos1_index = self.pos_to_index(pos1)
        pos2_index = self.pos_to_index(pos2)
        self.board[pos1_index], self.board[pos2_index] = self.board[pos2_index], self.board[pos1_index]
    
    # Generates a board state by combining the board with the current move list.
    # Returns the board state as a numpy array.
    def generate_board_state(self):
        return array(self.board + self.moves)

    # type(pos) = tuple
    # Assumes pos and the adjacent pos are valid.
    # Returns the orb adjacent to pos in the given direction.
    def get_adj(self, pos, direction="None"):
        if direction == "N":
            return (pos[0], pos[1] - 1)
        elif direction == "E":
            return (pos[0] + 1, pos[1])
        elif direction == "S":
            return (pos[0], pos[1] + 1)
        elif direction == "W":
            return (pos[0] - 1, pos[1])
        # diagonals for moves only
        elif direction == "NE":
            return (pos[0] + 1, pos[1] - 1)
        elif direction == "NW":
            return (pos[0] - 1, pos[1] - 1)
        elif direction == "SE":
            return (pos[0] + 1, pos[1] + 1)
        elif direction == "SW":
            return (pos[0] - 1, pos[1] + 1)
        
    # Calculates the expected damage of this board given the team.
    # By default, the team is None, and the damage will return 0.
    # ***** This function will be fully implemented in the future.
    # Returns expected damage.
    def calculate_damage(self, team=None):
        return 0

    # Returns a set of all of the existing colors on the board.
    def get_existing_colors(self):
        colors = set()
        for i in range(len(self.board)):
            colors.add(self.board[i])
        return colors

    # Returns a list of combos for each color on the board.
    # Combos are represented by the orb positions they take up.
    def get_combos(self):
        combos = {}
        existing_colors = self.get_existing_colors()
        # init an empty list for each color
        for x in existing_colors:
            combos[x] = []

        visit_map = [False for i in range(self.row_len * self.col_len)]

        for y in range(self.col_len):
            for x in range(self.row_len):
                search_pos = (x, y)
                search_pos_index = pos_to_index(search_pos)
                current_color = self.board(search_pos_index)
        
# End of Board


test_board = Board()
test_colors = [1,2,3,4,5,6] * 5
test_board.populate_board(test_colors)
print test_board.get_existing_colors()
'''
state = test_board.generate_board_state()
print state
test_board.swap((1, 1), (2, 1))
state = test_board.generate_board_state()
print state
'''
