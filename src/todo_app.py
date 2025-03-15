import json
import os

TASKS_FILE = "data/tasks.json"

def load_tasks():
    """Tải danh sách công việc từ file JSON, nếu không có file thì trả về danh sách rỗng."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """Lưu danh sách công việc vào file JSON."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task(tasks):
    """Thêm một công việc mới vào danh sách."""
    name = input("Nhập tên công việc: ").strip()
    description = input("Nhập mô tả công việc: ").strip()
    task = {"name": name, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Đã thêm công việc thành công.")

def list_tasks(tasks):
    """Hiển thị danh sách các công việc."""
    if not tasks:
        print("Danh sách công việc trống!")
        return
    print("\n--- Danh Sách Công Việc ---")
    for idx, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{idx}. {task['name']} - {task['description']} [{status}]")
    print("-----------------------------\n")

def mark_task_completed(tasks):
    """Đánh dấu một công việc là đã hoàn thành."""
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Nhập số thứ tự công việc cần đánh dấu hoàn thành: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["completed"] = True
            save_tasks(tasks)
            print("Đã cập nhật trạng thái công việc.")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def delete_task(tasks):
    """Xóa một công việc theo số thứ tự."""
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Nhập số thứ tự công việc cần xóa: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"Đã xóa công việc: {removed['name']}")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def main():
    tasks = load_tasks()
    menu = """
Chọn một tùy chọn:
1. Thêm công việc
2. Hiển thị danh sách công việc
3. Đánh dấu công việc hoàn thành
4. Xóa công việc
5. Thoát
Lựa chọn của bạn: """
    while True:
        choice = input(menu).strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()