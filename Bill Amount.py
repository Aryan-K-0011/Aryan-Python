def calculate_bill_amount(item_price, discount_rate=0, tax_rate=0):
  # Apply discount if provided
  if discount_rate > 0:
    discounted_price = item_price * (1 - discount_rate)
  else:
    discounted_price = item_price

  # Calculate tax amount
  tax_amount = discounted_price * tax_rate

  # Calculate final bill amount
  bill_amount = discounted_price + tax_amount

  return bill_amount

# Example usage with discount and tax
item_price = 100.00
discount_rate = 0.10  # 10% discount
tax_rate = 0.08  # 8% tax

bill_amount = calculate_bill_amount(item_price, discount_rate, tax_rate)

print(f"The bill amount for the item is: ${bill_amount:.2f}")

# Example usage without discount or tax
item_price = 50.00

bill_amount = calculate_bill_amount(item_price)

print(f"The bill amount for the item is: ${bill_amount:.2f}")
