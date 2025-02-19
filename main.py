from itertools import combinations_with_replacement

def can_make_total(total, num_coins, coin_values):
    """
    Determines if it is possible to make the given total using the specified number of coins.

    :param total: Target total in cents (e.g., $1.00 → 100 cents)
    :param num_coins: Number of coins to use
    :param coin_values: List of available coin values in cents
    :return: True if possible, False otherwise
    """
    for combo in combinations_with_replacement(coin_values, num_coins):
        if sum(combo) == total:
            return True
    return False

# Coin values in cents (U.S. currency)
coin_values = [1, 5, 10, 25, 50]  # Penny, Nickel, Dime, Quarter, Half Dollar

# Example usage
target_total = int(input("Enter Amount: "))
num_coins = int(input("Enter Count: "))

if can_make_total(target_total, num_coins, coin_values):
    print(f"Yes, it is possible to make ${target_total / 100:.2f} using {num_coins} coins.")
else:
    print(f"No, it is not possible to make ${target_total / 100:.2f} using {num_coins} coins.")