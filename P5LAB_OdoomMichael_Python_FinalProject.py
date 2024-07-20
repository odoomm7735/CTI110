# Michael Odoom
# July 20, 2024
# P5LAB Assignment (Python Final Project just for fun)
# A program to simulate a grocery self-checkout system using loops, functions, and module imports.

def disperse_change(amount):
    denominations = [50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    change = {}
    for denom in denominations:
        count, amount = divmod(amount, denom)
        change[denom] = int(count)
    print("Change to be returned:")
    for denom in denominations:
        if denom >= 1:
            print(f"${denom:.0f}: {change[denom]}")
        else:
            print(f"{int(denom * 100)}¢: {change[denom]}")

def show_avail_items(grocery_dict):
    print("Available grocery items:")
    for item, price in grocery_dict.items():
        print(f"{item}: ${price:.2f}")

def show_cart(cart_list):
    print("Items in your cart:")
    for item in cart_list:
        print(f"- {item}")

def calc_total(cart_list, grocery_dict):
    subtotal = sum(grocery_dict[item] for item in cart_list)
    tax = subtotal * 0.02
    total = subtotal + tax
    print("Itemized Receipt:")
    for item in cart_list:
        print(f"{item}: ${grocery_dict[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (2%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    return total

def normalize_item(item):
    # Convert to lower case and remove trailing 's' if present
    item = item.lower().rstrip('s')
    return item

def main():
    grocery_dict = {
        "Apples": 1.00,
        "Bread": 2.50,
        "Milk": 3.00,
        "Cheese": 4.50,
        "Carrots": 0.75,
        "Ice cream": 2.10,
        "Chips": 2.00,
        "Tomatoes": 3.15
    }

    # Convert dictionary keys to lowercase and normalized for case insensitive and plural/singular comparison
    grocery_dict_lower = {normalize_item(item): price for item, price in grocery_dict.items()}

    show_avail_items(grocery_dict)

    cart_list = []
    while True:
        item = input("Add an item to your cart (type 'end' to finish): ")
        normalized_item = normalize_item(item)
        if normalized_item == 'end':
            break
        elif normalized_item in grocery_dict_lower:
            # Append the original case item name for display purposes
            cart_list.append(next(key for key in grocery_dict if normalize_item(key) == normalized_item))
        else:
            print("Item not found. Please choose from the available items.")

    show_cart(cart_list)
    total = calc_total(cart_list, grocery_dict)

    amount_paid = float(input(f"Your total is ${total:.2f}. Enter the amount paid: $"))
    if amount_paid < total:
        print("Insufficient payment. Please pay the full amount.")
    else:
        change_to_return = amount_paid - total
        disperse_change(change_to_return)

if __name__ == "__main__":
    main()
