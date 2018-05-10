import doctest

class Square(object):
    """A square object"""

    def __init__(self, value): #requires value upon initialization
        self.up = None # default
        self.down = None # default
        self.left = None # default
        self.right = None # default
        self.value = value # taken in above
        self.coordinates = None


def carrot_missile(matrix):
    """Takes in matrix, holds other functions
    """

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
    print object_matrix
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
        if (object_matrix[indices[0]][indices[1]]).value > max_value:

            max_value = (object_matrix[indices[0]][indices[1]]).value
            print "Max Value:", max_value
            coordinates = (indices[0],indices[1])
            square = object_matrix[indices[0]][indices[1]]
    carrot_count = square.value
    square.value = 0
    return (coordinates, carrot_count)


def carrot_seeking(coordinates, carrot_count, object_matrix):
    """Look at 4 surrounding squares for highest carrot amount
       Stop when zero carrots are to be found """

    current_square = object_matrix[coordinates[0]][coordinates[1]]
    surrounding_squares = [current_square.up, current_square.down, current_square.right, current_square.left]

    new_squares = []
    for square in surrounding_squares:
        if square != None:
            new_squares.append(square)

    square_check = 0
    if new_squares != []:
        for square in new_squares:
            square_check += square.value
        print "Square Check", square_check


    if square_check == 0:
        return carrot_count
    else:
        highest_value = 0
        for square in new_squares:
            if square.value > highest_value:
                highest_value = square.value
                print "HV", highest_value

        for square in new_squares:
            if square.value == highest_value:
                carrot_count += square.value
                current_square = square
                square.value = 0
                coordinates = current_square.coordinates
                print "Current Square Value:", current_square.value
                print "Carrot Count:", carrot_count

                carrot_seeking(coordinates, carrot_count, object_matrix)
