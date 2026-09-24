"""pages/page2.py — ฟอร์มแจ้งของหายและแจ้งเก็บของได้
ผู้รับผิดชอบ: นางสาว ปวรรัตน์ คำจันทร์ลา
แบบจาก catalog: form
"""
import storage

TITLE = "แจ้งของหาย / พบของ"


def build():
    items = storage.load()
    return {"items": items, "count": len(items)}


def read_number(text, default=0):
    """แปลงข้อความเป็นตัวเลขจำนวนเต็ม หากผิดพลาดให้คืนค่า default"""
    if not text:
        return default
    try:
        val = int(float(text))
        return val if val >= 0 else default
    except (ValueError, TypeError):
        return default


def check(form):
    """ตรวจสอบความถูกต้องของฟอร์ม คืนข้อความแจ้งเตือนเมื่อไม่ถูกต้อง"""
    title = form.get("title", "").strip()
    location = form.get("location", "").strip()
    phone = form.get("phone", "").strip()

    if title == "":
        return "กรุณากรอกชื่อสิ่งของ"
    if location == "":
        return "กรุณาระบุสถานที่ที่ทำหายหรือสถานที่พบ"
    if phone == "":
        return "กรุณากรอกเบอร์โทรศัพท์สำหรับติดต่อ"
    return ""


def handle(form):
    items = storage.load()

    # จัดการกรณีลบรายการ
    if "delete" in form:
        target_id_str = form.get("delete", "")
        if target_id_str.isdigit():
            target_id = int(target_id_str)
            filtered = []
            found = False
            for it in items:
                if it.get("id") == target_id:
                    found = True
                else:
                    filtered.append(it)
            if found:
                storage.save(filtered)
                return "🗑 ลบรายการเรียบร้อยแล้ว"
        return "✗ ไม่พบรายการที่จะลบ"

    # จัดการเปลี่ยนสถานะเป็นคืนสำเร็จแล้ว
    if "mark_returned" in form:
        target_id_str = form.get("mark_returned", "")
        if target_id_str.isdigit():
            target_id = int(target_id_str)
            for it in items:
                if it.get("id") == target_id:
                    it["status"] = 2
                    storage.save(items)
                    return "✓ อัปเดตสถานะเป็นคืนสำเร็จแล้ว"
        return "✗ ไม่สามารถอัปเดตสถานะได้"

    # ตรวจสอบฟอร์มเพิ่มข้อมูลใหม่
    error = check(form)
    if error != "":
        return "✗ " + error

    # สร้าง ID ใหม่
    max_id = 100
    for it in items:
        if it.get("id", 0) > max_id:
            max_id = it.get("id", 0)
    new_id = max_id + 1

    item_type = form.get("type", "lost")
    if item_type not in ("lost", "found"):
        item_type = "lost"

    category = form.get("category", "ของใช้ส่วนตัว").strip()
    if category == "":
        category = "ของใช้ส่วนตัว"

    reward_val = read_number(form.get("reward", "0"), default=0)

    new_item = {
        "id": new_id,
        "type": item_type,
        "title": form.get("title", "").strip(),
        "category": category,
        "location": form.get("location", "").strip(),
        "reward": reward_val,
        "phone": form.get("phone", "").strip(),
        "status": 1,
    }

    items.append(new_item)
    storage.save(items)
    return "✓ เพิ่มรายการ " + new_item["title"] + " เรียบร้อยแล้ว"
