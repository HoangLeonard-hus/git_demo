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

def list_expenses(expenses):
    """Hiển thị danh sách các khoản chi tiêu."""
    if not expenses:
        print("Danh sách chi tiêu trống!")
        return
    print("\n--- Danh Sách Chi Tiêu ---")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['name']} - {expense['amount']} VND - {expense['category']}")
    print("-----------------------------\n")

def delete_expense(expenses):
    """Xóa một khoản chi tiêu theo số thứ tự."""
    list_expenses(expenses)
    if not expenses:
        return
    try:
        idx = int(input("Nhập số thứ tự khoản chi tiêu cần xóa: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            save_expenses(expenses)
            print(f"Đã xóa khoản chi tiêu: {removed['name']}")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")


