import json
from pathlib import Path

sales_path = Path(__file__).resolve().parent.parent / "data" / "sales.json" 

with sales_path.open("r", encoding="utf-8-sig") as file:
    sales = json.load(file)

print("資料的 Python 型別：", type(sales))
print("銷售紀錄總筆數：", len(sales))

for sale in sales:
    print(f"order_id：{sale['order_id']}，product：{sale['product']}")
