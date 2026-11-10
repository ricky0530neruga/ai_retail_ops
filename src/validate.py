required_fields = [
    "order_id",
    "product",
    "quantity",
    "unit_price",
    "sale_date"
]

test_sales = [
    {
        "order_id": "ORD001",
        "product": "電視",
        "quantity": 2,
        "unit_price": 30000,
        "sale_date": "2026-11-10"
    },
    {
        "order_id": "ORD002",
        "product": "冰箱",
        "unit_price": 25000,
        "sale_date": "2026-11-10"
    },
    {
        "order_id": "ORD003",
        "quantity": 1,
        "unit_price": 800,
        "sale_date": "2026-11-10"
    },
    {
    "order_id": "ORD004",
    "product": "耳機",
    "quantity": "3",
    "unit_price": 1500,
    "sale_date": "2026-11-10"
},
{
    "order_id": "ORD005",
    "product": "鍵盤",
    "quantity": True,
    "unit_price": "2500",
    "sale_date": "2026-11-10"
}
]
expected_types = {
    "order_id": str,
    "product": str,
    "quantity": int,
    "unit_price": int,
    "sale_date": str,
}
for sale in test_sales:
    for field in required_fields:
        if field not in sale:
            order_id = sale.get("order_id", "未知訂單")
            print(f"錯誤：訂單 {order_id} 缺少必要欄位 {field}")
        else:
            expected_type = expected_types[field]
            actual_type = type(sale[field])
            if actual_type is not expected_type:
                order_id = sale.get("order_id", "未知訂單")
                print(
                    f"錯誤：訂單 {order_id}，欄位 {field}，"
                    f"預期型別 {expected_type.__name__}，"
                    f"實際型別 {actual_type.__name__}"
                )

