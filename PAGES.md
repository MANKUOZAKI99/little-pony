# PAGES · แดชบอร์ดความคืบหน้า

กรอกสัปดาห์ที่ 1 แล้วอัปเดตทุกครั้งที่ commit — อาจารย์ดูไฟล์นี้ + `git log` แทนการถาม

**หัวข้อ:** เว็บแจ้งของหาย
**data.json เก็บอะไร (field):** id, type, title, category, location, reward, phone, status
**คัดลอก data.json → data.sample.json แล้ว:** [x]

## team — หน้าทีม (สัปดาห์ 0)
- [x] กรอก `team.json` ครบทุกคน (ชื่อ, รหัส, บทบาท, งานที่รับผิดชอบ)
- [x] เปิด /team เห็นชื่อทุกคน
- [x] commit `team: members filled` + push

## page1 — ผู้รับผิดชอบ: นางสาว สิรภัทร ทองน้อย · แบบจาก catalog: list + search
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page1 ได้ ไม่มี TODO
- [x] `check.bat` → /page1 ✓ ไม่มี warning
- [x] commit `page1: รายการของหายและการค้นหา`

## page2 — ผู้รับผิดชอบ: นางสาว ปวรรัตน์ คำจันทร์ลา · แบบจาก catalog: form
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page2 ได้ ไม่มี TODO
- [x] `check.bat` → /page2 ✓ ไม่มี warning
- [x] commit `page2: ฟอร์มแจ้งของหายและพบของ`

## page3 — ผู้รับผิดชอบ: นาย ปราโมทย์ โครตหัน · แบบจาก catalog: detail
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page3 ได้ ไม่มี TODO
- [x] `check.bat` → /page3 ✓ ไม่มี warning
- [x] commit `page3: รายละเอียดสิ่งของและข้อมูลติดต่อ`

## models.py — ผู้รับผิดชอบ: นาย ปราโมทย์ โครตหัน
- [x] เปลี่ยนชื่อ class ให้ตรงหัวข้อ, field ตรง data.json
- [x] method 1 ตัวที่มีประโยชน์ (ไม่เหลือ TODO)
- [x] มีหน้าใดหน้าหนึ่งใช้ class นี้ (เช่น แบบ detail)
- [x] `python check_project.py` → class ✓ 9/9
- [x] commit `models: Item class with is_returned method`

## ส่งงาน
- [x] `check.bat` → 60/60, pytest 4 passed, ไม่มี warning
- [ ] ทุกคนอยู่ใน `git log`
- [ ] นำเสนอ: ทุกคนอธิบายหน้าของตัวเอง 1 นาที
