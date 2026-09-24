"""models.py — Item class for Lost & Found project."""


class Item:
    def __init__(self, id, type, title, location, reward, status, phone=""):
        self.id = id
        self.type = type
        self.title = title
        self.location = location
        self.reward = reward
        self.status = status
        self.phone = phone

    def is_returned(self):
        """Return True if this item has already been returned to its owner."""
        return self.status == 2

    def status_label(self):
        """Return human-readable status text in Thai."""
        if self.is_returned():
            return "คืนสำเร็จแล้ว"
        if self.type == "lost":
            return "กำลังตามหา"
        return "รอเจ้าของติดต่อรับ"

    def type_label(self):
        """Return type label in Thai."""
        if self.type == "lost":
            return "ของหาย"
        return "เก็บของได้"
