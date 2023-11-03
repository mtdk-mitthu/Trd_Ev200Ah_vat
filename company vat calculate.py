pcs = int(input("How many pcs:"))  # Convert user input to an integer

item_price = 4639.95  # Price per item
total_price = pcs * item_price
vat = total_price * 0.15  # 15% VAT rate
intotal = total_price + vat

print(f"Total price without VAT: ${total_price:.2f}")
print(f"VAT (15%): ${vat:.2f}")
print(f"Total price with VAT: ${intotal:.2f}")