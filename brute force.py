import time

def draw(puzzle):
    for r in range(len(puzzle)):
        if r == 0 or r == 3 or r == 6:
            print("+-------+-------+-------+")
        for c in range(len(puzzle[r])):
            if c == 0 or c == 3 or c == 6:
                print("| ", end="")
            if puzzle[r][c] != 0:
                print(puzzle[r][c], end=" ")
            else:
                print(end="  ")
            if c == 8:
                print("|")
    print("+-------+-------+-------+")


def str_to_puzzle(s):
    puzzleSolution = []
    for i in range(len(s)):
        if i % 9 == 0:
            temp = []
            for j in s[i:i + 9]:
                temp.append(int(j))
            puzzleSolution.append(temp)
    return puzzleSolution


def same_row(i, j):
    if i // 9 == j // 9:
        return True
    return False


def same_col(i, j):
    if i % 9 == j % 9:
        return True
    return False


def same_block(i, j):
    if (i // 27 == j // 27) and (i % 9 // 3 == j % 9 // 3):
        return True
    return False


def sudoku_brute_force(s):
    if '0' not in s:  # Base case: If there are no empty cells, the puzzle is solved
        draw(str_to_puzzle(s))
        return

    # Find the index of the next empty cell
    i = s.find('0')

    # Determine the set of values that cannot be used for the current empty cell
    cannotuse = set()
    for j in range(len(s)):
        if same_row(i, j) or same_col(i, j) or same_block(i, j):
            cannotuse.add(s[j])

    # Try every possible value for the current empty cell
    for val in '123456789':
        if val not in cannotuse:
            # Assign the value to the empty cell
            updated_puzzle = s[:i] + val + s[i + 1:]
            sudoku_brute_force(updated_puzzle)


puzzleToSolve = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Convert the puzzle to a string representation
s = ''.join(map(str, [''.join(map(str, i)) for i in puzzleToSolve]))

print("Sudoku Problem")
draw(puzzleToSolve)
print("\nSudoku Solution")
start_time = time.process_time()
sudoku_brute_force(s)
print("Elapsed time:", time.process_time() - start_time, "seconds")
