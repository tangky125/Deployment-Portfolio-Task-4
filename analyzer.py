import csv
from datetime import datetime

INPUT_FILE = "/data/sales.csv"
OUTPUT_FILE = "/data/report.txt"

def main():
    total_revenue = 0.0
    total_items = 0
    product_counts = {}

    with open(INPUT_FILE, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            qty = int(row['quantity'])
            price = float(row['price'])
            total_revenue += qty * price
            total_items += qty
            product_counts[row['product']] = product_counts.get(row['product'], 0) + qty

    report_lines = [
        f"Sales Report — Generated {datetime.now()}",
        f"Total items sold: {total_items}",
        f"Total revenue: ${total_revenue:.2f}",
        "Breakdown by product:",
    ]
    for product, qty in product_counts.items():
        report_lines.append(f"  {product}: {qty} units")

    report = "\n".join(report_lines)
    print(report)

    with open(OUTPUT_FILE, "w") as f:
        f.write(report)

if __name__ == "__main__":
    main()