from datetime import datetime
from data import vegtables
from data import price

total_price = 0
purchased_items = []
now = datetime.now()

# ✅ Merge function: only used at the end
def get_merged_items():
    merged = {}
    for item in purchased_items:
        name = item["name"]
        if name in merged:
            merged[name]["amount"] += item["amount"]
            merged[name]["cost"] += item["cost"]
        else:
            merged[name] = {
                "name": name,
                "amount": item["amount"],
                "cost": item["cost"]
            }
    return list(merged.values())

if __name__ == "__main__":
    recipient_name = input(f"\n👤 Enter recipient's name: ").strip()

    while True:
        try:
            item_key = input(f"\nEnter vegtable key {len(purchased_items) + 1} ('q' to quit, 'r' to remove last entry, or number to remove specific): ").strip().lower()

            if item_key == "q":
                break

            if item_key == "n":
                recipient_name = input(f"\n👤 Enter recipient's name: ").strip()

            if item_key == "r":
                if not purchased_items:
                    print("⚠️ Billing has not started yet.")
                else:
                    removed_item = purchased_items.pop()
                    total_price -= removed_item["cost"]
                    print(f"❌ Removed last entry: {removed_item['name']} ({removed_item['amount']}g, ₹{removed_item['cost']:.2f})")
                    print(f"💰 Updated Total: ₹{total_price:.2f}")
                continue

            if item_key.isdigit():
                position = int(item_key)
                if 1 <= position <= len(purchased_items):
                    removed_item = purchased_items.pop(position - 1)
                    total_price -= removed_item["cost"]
                    print(f"❌ Removed entry {position}: {removed_item['name']} ({removed_item['amount']}g, ₹{removed_item['cost']:.2f})")
                    print(f"💰 Updated Total: ₹{total_price:.2f}")
                else:
                    print(f"⚠️ Invalid number. Enter a number between 1 and {len(purchased_items)}.")
                continue

            if item_key not in vegtables:
                print("❌ Invalid vegtable key! Available keys:", ", ".join(vegtables.keys()))
                continue

            vegtables_name = vegtables[item_key]
            item_price_per_gram = price[vegtables_name]

            amount = float(input(f"Enter amount of {vegtables_name} in grams: "))
            amount = round(amount, 2)
            cost = round(amount * item_price_per_gram, 2)
            total_price += cost

            purchased_items.append({
                "name": vegtables_name,
                "amount": amount,
                "cost": cost
            })

            print(f"\n✅ {amount}g of {vegtables_name} costs ₹{cost:.2f}")
            print(f"💰 Total so far: ₹{total_price:.2f}\n")

        except Exception as e:
            print("⚠️ Error:", e)

    # 🧾 Final merged summary
    merged_items = get_merged_items()
    summary = []
    print("====================================================================================")
    summary.append(f"\n🧾 Purchase Summary -\n")
    summary.append(f"👤 Recipient Name: {recipient_name:<30} Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    summary.append("------------------------------------------------------------------------------------")
    summary.append(f"\n{'No.':<5}{'vegtables':<15}{'Amount(g)':<12}{'Price(₹)':<10}")
    summary.append("------------------------------------------------------------------------------------")

    for i, item in enumerate(merged_items, 1):
        summary.append(f"{i:<5}{item['name']:<15}{item['amount']:<12.2f}{item['cost']:<10.2f}")

    summary.append("------------------------------------------------------------------------------------")
    summary.append(f"📦 Total Items: {len(merged_items)}")
    summary.append(f"💸 Gross Total: ₹{total_price:.2f}")
    summary.append(f"====================================================================================\n")

    print("\n".join(summary))

    with open("recipient_data.txt", "a", encoding="utf-8") as file:
        file.write("\n".join(summary) + "\n")
