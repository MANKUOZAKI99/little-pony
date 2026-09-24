"""pages/page3.py — หน้ารายละเอียดสิ่งของ
ผู้รับผิดชอบ: นาย ปราโมทย์ โครตหัน
แบบจาก catalog: detail
"""
import models
import storage

TITLE = "รายละเอียดสิ่งของ"


def build(query):
    items = storage.load()
    if len(items) == 0:
        return {"item": None, "item_obj": None, "count": 0}

    # รับค่า ID จาก URL เช่น ?id=101 หรือ ?i=0
    target_id_str = query.get("id", "").strip()
    selected_row = None
    selected_index = 0

    if target_id_str.isdigit():
        target_id = int(target_id_str)
        # วนลูปค้นหาข้อมูลใน data.json ตาม ID
        for idx in range(len(items)):
            if items[idx].get("id") == target_id:
                selected_row = items[idx]
                selected_index = idx
                break

    # ถ้าไม่พบตาม ID หรือไม่ได้ระบุ ให้ลองดู index หรือใช้รายการแรก
    if selected_row is None:
        idx_param = query.get("i", "0").strip()
        if idx_param.isdigit():
            idx_val = int(idx_param)
            if 0 <= idx_val < len(items):
                selected_index = idx_val
        selected_row = items[selected_index]

    # สร้าง Object จาก Class ใน models.py
    item_obj = models.Item(
        id=selected_row.get("id", 0),
        type=selected_row.get("type", "lost"),
        title=selected_row.get("title", ""),
        location=selected_row.get("location", ""),
        reward=selected_row.get("reward", 0),
        status=selected_row.get("status", 1),
        phone=selected_row.get("phone", ""),
    )

    prev_item = items[selected_index - 1] if selected_index > 0 else None
    next_item = items[selected_index + 1] if selected_index < len(items) - 1 else None

    is_returned = item_obj.is_returned()

    return {
        "item": selected_row,
        "item_obj": item_obj,
        "is_returned": is_returned,
        "status_label": item_obj.status_label(),
        "type_label": item_obj.type_label(),
        "prev_item": prev_item,
        "next_item": next_item,
        "count": len(items),
    }
