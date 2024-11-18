def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount if it's 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.

    Returns:
        float: The final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 25:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price


# Prompt user for input
try:
    original_price = float(input("160000"))
    discount_percent = float(input("20%"))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Print the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for the price and discount percentage.")
