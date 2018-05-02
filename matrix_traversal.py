
class Square(object):
    """A square object"""

    def __init__(self, value): #requires value upon initialization
        self.up = 0 # default
        self.down = 0 # default
        self.left = 0 # default
        self.right = 0 # default
        self.value = value # taken in above
        self.coordinates = None


def carrot_missile(matrix):
    """Takes in matrix, holds other function"""

    object_matrix = iterate_through_matrix(matrix)
    center_indices = find_center(object_matrix)
    coordinates, carrot_count = find_max_carrots(center_indices, object_matrix)
    carrots = carrot_seeking(coordinates, carrot_count, object_matrix)

    return carrots


def iterate_through_matrix(matrix):
    """Traverse through matrix
       define where each square is in relation to others
    """
    object_matrix = [] #creating a matrix to store objects that are created

    height = len(matrix)
    # find the length of matrix[0] <- (height)
    width = len(matrix[0])
    # find width

    for row in matrix:
        row_list = []
        for cell in row:
            square = Square(cell)
            row_list.append(square)
        object_matrix.append(row_list) # for each row in matrix, create an empty list

    # assign attributes to objects in matrix
    row_counter = 0
    for row in object_matrix: # using obj_row instead of i
        cell_counter = 0
        for cell in row: # using cell instead of j
            cell.coordinates = (row_counter, cell_counter)
            if cell_counter != (width - 1): # setting right
                cell.right = object_matrix[0][cell_counter + 1]
            if cell_counter != 0: # setting left
                cell.left = object_matrix[row_counter][cell_counter - 1]
            if row_counter != 0: # settting up
                cell.up = object_matrix[row_counter - 1][cell_counter]
            if row_counter != (height - 1):
                cell.down = object_matrix[row_counter + 1][cell_counter]
            cell_counter += 1
        row_counter +=1

    return object_matrix


def find_center(object_matrix):
    """Find the middle grid"""

    height = len(object_matrix)
    # find the length of matrix[0] <- (height)
    width = len(object_matrix[0])
    # find width

    if height == 0:
        return []

    elif height % 2 == 0 and width % 2 == 0: # both even
        center_indices = ((((height/2)-1),((width/2)-1)),
                          ((height/2)-1,(width/2)),
                          ((height/2),((width/2)-1)),
                          ((height/2),(width/2)),)

    elif height % 2 == 0 and width % 2 != 0: # number of lists even, length of lists odd
        center_indices = (((height/2)-1,(width/2)),
                          ((height/2),(width/2),))

    elif height % 2 != 0 and width % 2 == 0: # number of lists odd, length of lists even
        center_indices = (((height - 1)/2, ((width - 1)/2)),
                          ((height - 1)/2, width/2),)

    else: # odd
        center_indices = (height/2, width/2,)

    return center_indices


def find_max_carrots(center_indices, object_matrix):
    """Take in indices, find max carrots"""

    max_value = 0
    for indices in center_indices:
        if object_matrix[indices[0]][indices[1]] > max_value:
            coordinates = (indices[0],indices[1])
            square = object_matrix[indices[0]][indices[1]]
            carrot_count = square.value
    return (coordinates, carrot_count)


def carrot_seeking(coordinates, carrot_count, object_matrix):
    """Look at 4 surrounding squares for highest carrot amount
       Stop when zero carrots are to be found """

    current_square = object_matrix[coordinates[0]][coordinates[1]]
    new_squares = [current_square.up, current_square.down, current_square.right, current_square.left]
    if (current_square.up.value + current_square.down.value + current_square.left.value + current_square.right.value) == 0: # fail fast, base case
        return carrot_count
    else:
        highest_value = max(current_square.up.value,
                            current_square.down.value,
                            current_square.left.value,
                            current_square.right.value)
    for square in new_squares:
        if square.value == highest_value:
            current_square = square
            print current_square
            print "Up", current_square.up
            print "Down", current_square.down
            print "Left", current_square.left
            print "Right", current_square.right
            print current_square.value
            print current_square.coordinates
            coordinates = current_square.coordinates
            carrot_count += current_square.value
            carrot_seeking(coordinates, carrot_count, object_matrix)
