from data import vegtables
from data import price

no_of_vegtables = 0
total_price = 0
purchased_items = []

if __name__ == "__main__":
    while True:
        try:
            item_key = input(f"\nEnter vegtable key {no_of_vegtables + 1} (or 'q' to quit): ").strip().lower()
            
            if item_key == "q":
                break
            
            if item_key not in vegtables:
                print("❌ Invalid vegtable key! Available keys:", ", ".join(vegtables.keys()))
                continue

            vegtables_name = vegtables[item_key]
            item_price_per_gram = price[vegtables_name]

            amount = float(input(f"Enter amount of {vegtables_name} in grams: "))
            amount = round(amount, 2)
            cost = amount * item_price_per_gram
            total_price += cost
            no_of_vegtables += 1

            # Save the item details
            purchased_items.append({
                "name": vegtables_name,
                "amount": amount,
                "cost": cost
            })

            print(f"✅ {amount}g of {vegtables_name} costs ₹{cost:.2f}")
            print(f"💰 Total so far: ₹{total_price:.2f}\n")

        except Exception as e:
            print("⚠️ Error:", e)

    # Show summary after quitting
    print("\n🧾 Purchase Summary:")
    print("-------------------------------------------------")
    print(f"{'No.':<5}{'vegtables':<10}{'Amount(g)':<12}{'Price(₹)':<10}")
    print("-------------------------------------------------")
    for i, item in enumerate(purchased_items, 1):
        print(f"{i:<5}{item['name']:<10}{item['amount']:<12.2f}{item['cost']:<10.2f}")
    print("-------------------------------------------------")
    print(f"🛒 Total Items: {no_of_vegtables}")
    print(f"💸 Final Total: ₹{total_price:.2f}")
