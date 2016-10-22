# Colors 'R' (Fire), 'G' (Wood), 'B' (Water), 'L' (Light), 'D' (Dark), 'H' (Heal)
# Possibly 'J' (Jammer), 'P' (Poison)


"""
Constants/Defaults
"""
ROW = 6 # The length of a row
COL = 5 # The length of a column

class Orb:
    """
    Orb object that tracks color and properties.
    """
    def __init__(self, color, x, y, enhanced=False, locked=False):
        self.color = color
        self.enhanced = enhanced
        self.locked = locked

        # only need these for hashing purposes
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.color == other.color
        return False
    
class Combo:
    """
    Combo object that tracks the orbs and their locations.
    """
    def __init__(self, orb_set):
        self.orb_set = orb_set

    """
    Returns True if the combo is a row.
    """
    def is_row(self, r=ROW):
        pass

    """
    Returns True if the combo is a TPA.
    """
    def is_tpa(self):
        pass

    """
    Returns True if the combo is a cross.
    """
    def is_cross(self):
        pass
        
class BoardState:
    """
    Holds the state of a board at a given step.
    """
    def __init__(self, board, row=ROW, col=COL):
        # board[y][x]
        self.board = board
        #g_placeholder = [[Orb('G') for x in range(0, ROW)] for y in range(0, COL)] # all greens placeholder for now
        self.row = row
        self.col = col
        #self.combos = None


    """
    Returns orb at (x, y) on the board.
    """
    def get_orb(self, x, y):
        return self.board[y][x]


    """
    Returns a list of all of the orbs and their coordinates on the board in tuples: (orb, x, y)
    """
    def board_as_list(self):
        return [self.get_orb(x, y) for x in range(0, self.row) for y in range(0, self.col)]

    """
    Returns a list of all of the combos on the current board state.


    *** AS OF NOW, IT IS MISSING THE CASE OF STACKED COMBOS.
    """
    def get_combos(self):
        combos = []
        board_list = self.board_as_list()
        num_visited = 0
        max_visits = self.row * self.col # need to visit this many orbs

        while len(board_list) > 0:
            # remove orbs from the list when they are visited
            current_orb = board_list[0] # (Orb, x, y)
            board_list.remove(current_orb) # this will actually be done later

            # check for a horizontal combo
            combo_horizontal = set()
            combo_horizontal.add(current_orb[0])
            
            x = current_orb.x - 1
            y = current_orb.y
            
            while x >= 0:
                orb = self.get_orb(x, y)
                if orb != current_orb:
                    break
                combo_horizontal.add(orb)
                x -= 1
            x = current_orb[1] + 1
            while x < self.row:
                orb = self.get_orb(x, y)
                if orb != current_orb[0]:
                    break
                combo_horizontal.add(orb)
                x += 1

            if len(combo_horizontal) < 2:
                combo_horizontal.clear()

            # check for a vertical combo
            combo_vertical = set()
            combo_vertical.add(current_orb)

            x = current_orb.x
            y = current_orb.y - 1

            while y >= 0:
                orb = self.get_orb(x, y)
                if orb != current_orb:
                    break
                combo_vertical.add(orb)
                y -= 1
            y = current_orb[1] + 1
            while y < self.col:
                orb = self.get_orb(x, y)
                if orb != current_orb:
                    break
                combo_vertical.append(orb)
                y += 1

            if len(combo_vertical) < 2:
                combo_vertical.clear()

            # combine the horizontal and vertical sets
            full_combo = combo_horizontal | combo_vertical

            # only work with the combo if it is valid
            if len(full_combo) > 0:
                # remove the orbs in the combo from the list
                for orb in full_combo:
                    if orb != current_orb[0]:
                        board_list.remove(orb)

                combo = Combo(full_combo)
                combos.append(combo)

        return combos

