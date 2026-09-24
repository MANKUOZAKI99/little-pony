"""pages/page1.py — รายการของหายและการค้นหา
ผู้รับผิดชอบ: นางสาว สิรภัทร ทองน้อย
แบบจาก catalog: list + search
"""
import storage

TITLE = "รายการของหาย"


def build(query):
    keyword = query.get("q", "").strip().lower()
    item_type = query.get("type", "").strip()

    items = storage.load()
    results = []

    count_lost = 0
    count_found = 0
    count_returned = 0

    for item in items:
        # เก็บสถิติสรุปภาพรวม
        if item.get("type") == "lost":
            count_lost = count_lost + 1
        elif item.get("type") == "found":
            count_found = count_found + 1

        if item.get("status") == 2:
            count_returned = count_returned + 1

        # กรองข้อมูลตามคำค้นหาและประเภท
        title = item.get("title", "").lower()
        category = item.get("category", "").lower()
        location = item.get("location", "").lower()

        match_keyword = (
            keyword == ""
            or keyword in title
            or keyword in category
            or keyword in location
        )

        match_type = item_type == "" or item.get("type") == item_type

        if match_keyword and match_type:
            results.append(item)

    return {
        "keyword": keyword,
        "selected_type": item_type,
        "results": results,
        "total": len(items),
        "count_lost": count_lost,
        "count_found": count_found,
        "count_returned": count_returned,
    }
