from datetime import datetime

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
},
    {
        "order_id": "ORD006",
        "product": "滑鼠",
        "quantity": 0,
        "unit_price": 500,
        "sale_date": "2026-11-10"
    },
    {
        "order_id": "ORD007",
        "product": "滑鼠",
        "quantity": 1,
        "unit_price": -200,
        "sale_date": "2026-11-10"
    },
    {
        "order_id": "ORD008",
        "product": "滑鼠",
        "quantity": 1,
        "unit_price": 500,
        "sale_date": "2026-02-30"
    },
    {
        "order_id": "ORD009",
        "product": "滑鼠",
        "quantity": 1,
        "unit_price": 500,
        "sale_date": "2026-1-2"
    }

]
expected_types = {
    "order_id": str,
    "product": str,
    "quantity": int,
    "unit_price": int,
    "sale_date": str,
}
####### 檢查欄位是否存在
for sale in test_sales:
    for field in required_fields:
        if field not in sale:
            order_id = sale.get("order_id", "未知訂單")
            print(f"錯誤：訂單 {order_id} 缺少必要欄位 {field}")
        else:
            expected_type = expected_types[field]
            actual_type = type(sale[field])
            ####### 檢查資料型別是否正確 避免"200" * 3 = 200 200 200 這種錯誤  
            if actual_type is not expected_type:
                order_id = sale.get("order_id", "未知訂單")
                print(
                    f"錯誤：訂單 {order_id}，欄位 {field}，"
                    f"預期型別 {expected_type.__name__}，"
                    f"實際型別 {actual_type.__name__}"
                )
            else:
                order_id = sale.get("order_id", "未知訂單")
                value = sale[field]
            #######   新增條件檢查資料是否合法 quuntity 不能 =< 0 price <0 但能 =0 贈品 
                if field == "quantity" and value <= 0:
                    print(f"錯誤：訂單 {order_id}，欄位 {field}，必須大於 0")
                elif field == "unit_price" and value < 0:
                    print(f"錯誤：訂單 {order_id}，欄位 {field}，必須大於或等於 0")
                elif field == "sale_date":
                    # strptime 接受部分未補零日期，因此先檢查固定格式。
                    ###
                    """
                    len(value) != 10	日期長度必須是 10
                    value[4] != "-"	位置 4 必須是 -
                    value[7] != "-"	位置 7 必須是 -
                    any(...)	年、月、日的每個字元都必須是 ASCII 數字
                    """
                    if (
                        len(value) != 10
                        or value[4] != "-"
                        or value[7] != "-"
                        or any(char not in "0123456789" for char in value[:4] + value[5:7] + value[8:]) #any 檢查 沒有任何char不是 0~9
                    ):
                        print(f"錯誤：訂單 {order_id}，欄位 {field}，日期格式必須為 YYYY-MM-DD")
                    else: 
                        try: #嘗試可能會錯誤的程式碼 若錯誤 則except
                            datetime.strptime(value, "%Y-%m-%d") #上述檢查通過進入這裡  datetime.strptime() 會嘗試將文字解析成日期
                        except ValueError:
                            print(f"錯誤：訂單 {order_id}，欄位 {field}，無效的日曆日期：{value}")
                            ########
