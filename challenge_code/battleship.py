class place:
    def boat(type: str, length: int):
            while True:
                rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
                home_tile = input(f"Where would you like to place your {type} (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
                home_tile[0].upper()
                
                if home_tile[0] not in {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}:
                    print("ERROR: Row value must be a letter from 'A' to 'J'")
                    continue
                if home_tile[1] not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
                    print("ERROR: Column value must be a number from 1 to 10")
                    continue
                
                direction = input("What direction should it go (up, right, down, or left): ").strip().lower()
                if direction not in {"up", "down", "left", "right"}:
                    print("ERROR: Please enter a valid direction")
                    continue
                
                if direction == "up" and home_tile[0] in {"A", "B", "C", "D"}:
                    print(f"ERROR: {type} does not fit")
                    continue
                if direction == "down" and home_tile[0] in {"G", "H", "I", "J"}:
                    print(f"ERROR: {type} does not fit")
                    continue
                if direction == "left" and home_tile[1] in range(1, 7):
                    print(f"ERROR: {type} does not fit")
                    continue
                if direction == "right" and home_tile[1] in range(6, 11):
                    print(f"ERROR: {type} does not fit")
                    continue
                
                boat = [home_tile, direction]
                return boat
    def carrier():
        while True:
            home_tile = input("Where would you like to place your aircraft carrier (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
            home_tile[0].upper()
            
            if home_tile[0] not in {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}:
                print("ERROR: Row value must be a letter from 'A' to 'J'")
                continue
            if home_tile[1] not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
                print("ERROR: Column value must be a number from 1 to 10")
                continue
            
            direction = input("What direction should it go (up, right, down, or left): ").strip().lower()
            if direction not in {"up", "down", "left", "right"}:
                print("ERROR: Please enter a valid direction")
                continue
            
            if direction == "up" and home_tile[0] in {"A", "B", "C", "D"}:
                print("ERROR: Aircraft carrier does not fit")
                continue
            if direction == "down" and home_tile[0] in {"G", "H", "I", "J"}:
                print("ERROR: Aircraft carrier does not fit")
                continue
            if direction == "left" and home_tile[1] in range(1, 7):
                print("ERROR: Aircraft carrier does not fit")
                continue
            if direction == "right" and home_tile[1] in range(6, 11):
                print("ERROR: Aircraft carrier does not fit")
                continue
            
            carrier = [home_tile, direction]
            return carrier

    def battleship():
        while True:
            home_tile = input("Where would you like to place your battleship (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
            home_tile[0].upper()
            
            if home_tile[0] not in {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}:
                print("ERROR: Row value must be a letter from 'A' to 'J'")
                continue
            if home_tile[1] not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
                print("ERROR: Column value must be a number from 1 to 10")
                continue
            
            direction = input("What direction should it go (up, right, down, or left): ").strip().lower()
            if direction not in {"up", "down", "left", "right"}:
                print("ERROR: Please enter a valid direction")
                continue
            
            if direction == "up" and home_tile[0] in {"A", "B", "C", "D"}:
                print("ERROR: Battleship does not fit")
                continue
            if direction == "down" and home_tile[0] in {"G", "H", "I", "J"}:
                print("ERROR: Battleship does not fit")
                continue
            if direction == "left" and home_tile[1] in range(1, 7):
                print("ERROR: Battleship does not fit")
                continue
            if direction == "right" and home_tile[1] in range(6, 11):
                print("ERROR: Battleship does not fit")
                continue
            
            battleship = [home_tile, direction]
            return battleship

    def destroyer():
        while True:
            home_tile = input("Where would you like to place your destroyer (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
            home_tile[0].upper()
            
            if home_tile[0] not in {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}:
                print("ERROR: Row value must be a letter from 'A' to 'J'")
                continue
            if home_tile[1] not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
                print("ERROR: Column value must be a number from 1 to 10")
                continue
            
            direction = input("What direction should it go (up, right, down, or left): ").strip().lower()
            if direction not in {"up", "down", "left", "right"}:
                print("ERROR: Please enter a valid direction")
                continue
            
            if direction == "up" and home_tile[0] in {"A", "B", "C", "D"}:
                print("ERROR: Destroyer does not fit")
                continue
            if direction == "down" and home_tile[0] in {"G", "H", "I", "J"}:
                print("ERROR: Destroyer does not fit")
                continue
            if direction == "left" and home_tile[1] in range(1, 7):
                print("ERROR: Destroyer does not fit")
                continue
            if direction == "right" and home_tile[1] in range(6, 11):
                print("ERROR: Destroyer does not fit")
                continue
            
            destroyer = [home_tile, direction]
            return destroyer

    def submarine():
        while True:
            home_tile = input("Where would you like to place your submarine (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
            home_tile[0].upper()
            
            if home_tile[0] not in {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}:
                print("ERROR: Row value must be a letter from 'A' to 'J'")
                continue
            if home_tile[1] not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
                print("ERROR: Column value must be a number from 1 to 10")
                continue
            
            direction = input("What direction should it go (up, right, down, or left): ").strip().lower()
            if direction not in {"up", "down", "left", "right"}:
                print("ERROR: Please enter a valid direction")
                continue
            
            if direction == "up" and home_tile[0] in {"A", "B", "C", "D"}:
                print("ERROR: Submarine does not fit")
                continue
            if direction == "down" and home_tile[0] in {"G", "H", "I", "J"}:
                print("ERROR: Submarine does not fit")
                continue
            if direction == "left" and home_tile[1] in range(1, 7):
                print("ERROR: Submarine does not fit")
                continue
            if direction == "right" and home_tile[1] in range(6, 11):
                print("ERROR: Submarine does not fit")
                continue
            
            submarine = [home_tile, direction]
            return submarine

    def patrol_boat():
        while True:
            home_tile = input("Where would you like to place your patrol boat (Enter in format 'row: A to J'-'column: 1 to 10' ex. B-5): ").strip().split("-")
            home_tile[0].upper()
            if home_tile[0] not in {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}:
                print("ERROR: Row value must be a letter from 'A' to 'J'")
                continue
            if home_tile[1] not in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
                print("ERROR: Column value must be a number from 1 to 10")
                continue

            direction = input("What direction should it go (up, right, down, or left): ").strip().lower()
            if direction not in {"up", "down", "left", "right"}:
                print("ERROR: Please enter a valid direction")
                continue  

            if direction == "up" and home_tile[0] == "A":
                print("ERROR: Patrol boat does not fit")
                continue
            if direction == "down" and home_tile[0] == "J":
                print("ERROR: Patrol boat does not fit")
                continue
            if direction == "left" and home_tile[1] == "1":
                print("ERROR: Patrol boat does not fit")
                continue
            if direction == "right" and home_tile[1] == "10":
                print("ERROR: Patrol boat does not fit")
                continue
            
            patrol_boat = [home_tile, direction]
            return patrol_boat

def main():
    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    player_grid = []
    #grid_2 = []
    
    for row in range(len(rows)):
        row = []
        for column in range(len(columns)):
            row.append(0)
        player_grid.append(row)
        #grid_2.append(row)

    print(place.patrol_boat())


main()