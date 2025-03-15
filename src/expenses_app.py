import json
import os

EXPENSES_FILE = "data/expenses.json"

def load_expenses():
    """Tải danh sách chi tiêu từ file JSON, nếu không có file thì trả về danh sách rỗng."""
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_expenses(expenses):
    """Lưu danh sách chi tiêu vào file JSON."""
    with open(EXPENSES_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)

def add_expense(expenses):
    """Thêm một khoản chi tiêu mới vào danh sách."""
    name = input("Nhập tên khoản chi tiêu: ").strip()
    amount = input("Nhập số tiền: ").strip()
    category = input("Nhập danh mục (ăn uống, đi lại, giải trí, v.v.): ").strip()
    expense = {"name": name, "amount": amount, "category": category}
    expenses.append(expense)
    save_expenses(expenses)
    print("Đã thêm khoản chi tiêu thành công.")

