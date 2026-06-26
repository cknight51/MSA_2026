''' Create a variable for the amount due and set it to 50
Use a while loop that prompts the user to input a coin until amount_due is less than or equal to 0
Use a list to validate that the coin is valid (1, 5, 10, 25)
Decrease amount_due by the value of the coin
When amount_due is less than 1, output the amount owed to the user'''

def main():
    amount_due = 50
    print("\nVending Machine\n----------------")
    
    while amount_due > 0:
            print(f"Amount Due: {amount_due}")
            coin = input("Insert Coin: ")
            if coin in {"1", "5", "10","25"}:
                amount_due -= int(coin)

    change_owed = 0 - amount_due
    print(f"Change Owed: {change_owed}")

main()
