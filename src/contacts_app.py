import json
import os

CONTACTS_FILE = "data/contacts.json"


def load_contacts():
    """Tải danh bạ từ file JSON, nếu không có file thì trả về danh sách rỗng."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_contacts(contacts):
    """Lưu danh sách danh bạ vào file JSON."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)


def add_contact(contacts):
    """Thêm một liên hệ mới vào danh sách."""
    name = input("Nhập tên: ").strip()
    phone = input("Nhập số điện thoại: ").strip()
    email = input("Nhập email (nếu có): ").strip()
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Đã thêm liên hệ thành công.")


def list_contacts(contacts):
    """Hiển thị danh sách các liên hệ."""
    if not contacts:
        print("Danh bạ trống!")
        return
    print("\n--- Danh Bạ ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact.get('email', '')}")
    print("----------------\n")


def search_contact(contacts):
    """Tìm kiếm liên hệ theo tên."""
    keyword = input("Nhập tên cần tìm: ").strip().lower()
    results = [c for c in contacts if keyword in c["name"].lower()]
    if results:
        print("\n--- Kết Quả Tìm Kiếm ---")
        for contact in results:
            print(f"{contact['name']} - {contact['phone']} - {contact.get('email', '')}")
        print("------------------------\n")
    else:
        print("Không tìm thấy liên hệ nào.")


def delete_contact(contacts):
    """Xóa liên hệ theo số thứ tự."""
    list_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("Nhập số thứ tự liên hệ cần xóa: "))
        if 1 <= idx <= len(contacts):
            removed = contacts.pop(idx - 1)
            save_contacts(contacts)
            print(f"Đã xóa liên hệ: {removed['name']}")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")


def main():
    contacts = load_contacts()
    menu = """
Chọn một tùy chọn:
1. Thêm liên hệ
2. Hiển thị danh bạ
3. Tìm kiếm liên hệ
4. Xóa liên hệ
5. Thoát
Lựa chọn của bạn: """

    while True:
        choice = input(menu).strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


if __name__ == "__main__":
    main()
