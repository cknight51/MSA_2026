
def boat(type, length, value, grid):
    while True:
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        home_tile = input(f"Where would you like to place your {type} (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
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
                if grid[row][boat_column] == 0:
                    grid[row][boat_column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_row, boat_row - tiles_placed, -1):
                        grid[undo][boat_column] = 0
                    break
            if tiles_placed == length:
                break
        elif direction == "down":
            for row in range(boat_row, boat_row + length):
                if grid[row][boat_column] == 0:
                    grid[row][boat_column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_row, boat_row + tiles_placed):
                        grid[undo][boat_column] = 0
                    break
            if tiles_placed == length:
                break
        elif direction == "left":
            for column in range(boat_column, boat_column - length, -1):
                if grid[boat_row][column] == 0:
                    grid[boat_row][column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_column, boat_column - tiles_placed, -1):
                        grid[boat_row][undo] = 0
                    break
            if tiles_placed == length:
                break
        else:
            for column in range(boat_column, boat_column + length):
                if grid[boat_row][column] == 0:
                    grid[boat_row][column] = value
                    tiles_placed += 1
                else:
                    print("ERROR: Another boat is in the way")
                    for undo in range(boat_column, boat_column + tiles_placed):
                        grid[boat_row][undo] = 0
                    break
            if tiles_placed == length:
                break

def main():
    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    player_grid = []
    
    for row in range(len(rows)):
        row = []
        for column in range(len(columns)):
            row.append(0)
        player_grid.append(row)
        #grid_2.append(row)

    boat("Aircraft Carrier", 5, 1, player_grid)
    boat("Destroyer", 4, 2, player_grid)
    boat("Submarine", 3, 3, player_grid)
    boat("Battleship", 3, 4, player_grid)
    boat("Patrol Boat", 2, 5, player_grid)

    for row in player_grid:
        print(row)

main()
