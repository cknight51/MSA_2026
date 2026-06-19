def boat(type: str, length: int, value: str, grid: list, player: str):
    while True:
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        home_tile = input(f"{player}, where would you like to place your {type} (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
        home_tile[0] = home_tile[0].upper()
        
        if home_tile[0] not in rows:
            print("ERROR: Row value must be a letter from 'A' to 'J'")
            continue
        if home_tile[1] not in columns:
            print("ERROR: Column value must be a number from 1 to 10")
            continue
        
        direction = input("What direction should it go (up, right, down, or left): ").strip().lower()
        if direction not in {"up", "down", "left", "right"}:
            print("ERROR: Please enter a valid direction")
            continue
        
        if direction == "up":
            for _ in range(int(11 - length)):
                rows.pop()
            if home_tile[0] in rows:
                print(f"ERROR: {type} does not fit")
                continue
        elif direction == "down": 
            for _ in range(int(11 - length)):
                rows.pop(0)
            if home_tile[0] in rows:
                print(f"ERROR: {type} does not fit")
                continue
        elif direction == "left":
            for _ in range(int(11 - length)):
                columns.pop()
            if home_tile[1] in columns:
                print(f"ERROR: {type} does not fit")
                continue
        else:
            for _ in range(int(11 - length)):
                columns.pop(0)
            if home_tile[1] in columns:
                print(f"ERROR: {type} does not fit")
                continue
        
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        boat_row = rows.index(home_tile[0])
        boat_column = columns.index(home_tile[1])
        tiles_placed = 0
        
        if direction == "up":
            for row in range(boat_row, boat_row - length, -1):
                if grid[row][boat_column] == ' ':
                    grid[row][boat_column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_row, boat_row - tiles_placed, -1):
                        grid[undo][boat_column] = ' '
                    break
            if tiles_placed == length:
                return grid
            
        elif direction == "down":
            for row in range(boat_row, boat_row + length):
                if grid[row][boat_column] == ' ':
                    grid[row][boat_column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_row, boat_row + tiles_placed):
                        grid[undo][boat_column] = ' '
                    break
            if tiles_placed == length:
                return grid
            
        elif direction == "left":
            for column in range(boat_column, boat_column - length, -1):
                if grid[boat_row][column] == ' ':
                    grid[boat_row][column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_column, boat_column - tiles_placed, -1):
                        grid[boat_row][undo] = ' '
                    break
            if tiles_placed == length:
                return grid
            
        else:
            for column in range(boat_column, boat_column + length):
                if grid[boat_row][column] == ' ':
                    grid[boat_row][column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_column, boat_column + tiles_placed):
                        grid[boat_row][undo] = ' '
                    break
            if tiles_placed == length:
                return grid

def scan():
    pass

def shoot(player, player_grid, opponent_grid, shot_grid):
    print("\n\nYOUR FLEET:")
    for row in player_grid:
        print(row)
    print("\nYOUR SHOTS:")
    for row in shot_grid:
        print(row)

    while True:
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        tile = input(f"\n{player}, where would you like to shoot (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
        tile[0] = tile[0].upper()

        if tile[0] not in rows:
            print("ERROR: Row value must be a letter from 'A' to 'J'")
            continue
        if tile[1] not in columns:
            print("ERROR: Column value must be a number from 1 to 10")
            continue

        row_index = rows.index(tile[0])
        column_index = columns.index(tile[1])

        if opponent_grid[row_index][column_index] != ' ':
            print("HIT")
            opponent_grid[row_index][column_index] = 'X'
            shot_grid[row_index][column_index] = 'X'
            #win = scan(opponent_grid)
            #return win
            break
        elif shot_grid[row_index][column_index] in {'X', 'O'}:
            print("You've already shot there. Try Again.")
            continue
        else:
            print("MISS")
            opponent_grid[row_index][column_index] = 'O'
            shot_grid[row_index][column_index] = 'O'
            break

def main():
    player1_grid = []
    player1_shot_grid = []
    for row in range(10):
        row = []
        for column in range(10):
            row.append(' ')
        player1_grid.append(row)
    for row in range(10):
        row = []
        for column in range(10):
            row.append(' ')
        player1_shot_grid.append(row)
        

    player1_grid = boat("Aircraft Carrier", 5, '1', player1_grid, "Player 1")
    player1_grid = boat("Destroyer", 4, '2', player1_grid, "Player 1")
    player1_grid = boat("Submarine", 3, '3', player1_grid, "Player 1")
    player1_grid = boat("Battleship", 3, '4', player1_grid, "Player 1")
    player1_grid = boat("Patrol Boat", 2, '5', player1_grid, "Player 1")

    player2_grid = []
    player2_shot_grid = []
    for row in range(10):
        row = []
        for column in range(10):
            row.append(' ')
        player2_grid.append(row)
    for row in range(10):
        row = []
        for column in range(10):
            row.append(' ')
        player2_shot_grid.append(row)
    print()

    player2_grid = boat("Aircraft Carrier", 5, '1', player2_grid, "Player 2")
    player2_grid = boat("Destroyer", 4, '2', player2_grid, "Player 2")
    player2_grid = boat("Submarine", 3, '3', player2_grid, "Player 2")
    player2_grid = boat("Battleship", 3, '4', player2_grid, "Player 2")
    player2_grid = boat("Patrol Boat", 2, '5', player2_grid, "Player 2")

    end = False

    while not end:
        end = shoot("Player 1", player1_grid, player2_grid, player1_shot_grid)
        end = shoot("Player 2", player2_grid, player1_grid, player2_shot_grid)

main()