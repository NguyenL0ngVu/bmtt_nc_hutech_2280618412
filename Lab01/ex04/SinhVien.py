#OOP
#Xây dụng lớp SinhVien quản lý thông tin sinh viên như mã sinh viên (id), tên, giới tính, chuyên ngành, điển trung bình (hệ 10), mã sinh viên tự tăng cho mỗi sinh viên
#Học lực sinh viên được phân loại như sau:
# - Xuất sắc: Điểm trung bình >= 9.0
# - Giỏi: Điểm trung bình >= 8.0 và < 9.0
# - Khá: Điểm trung bình >= 7.0 và < 8.0
# - Trung bình: Điểm trung bình >= 5.0 và < 7.0
# - Yếu: Điểm trung bình < 5.0
#Tạo menu với các chức năng:
# - Thêm sinh viên
# - Cập nhật thông tin sinh viên theo ID
# - Xóa sinh viên theo ID
# - Tìm kiếm sinh viên theo tên
# - Sắp xếp danh sách sinh viên theo điểm trung bình
# - Sắp xếp sinh viên theo chuyên ngành
# - Xuất danh sách sinh viên

class SinhVien:
    def __init__(self, id, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        self.id = id
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_trung_binh = diem_trung_binh

    def get_hoc_luc(self):
        if self.diem_trung_binh >= 9.0:
            return "Xuất sắc"
        elif self.diem_trung_binh >= 8.0:
            return "Giỏi"
        elif self.diem_trung_binh >= 7.0:
            return "Khá"
        elif self.diem_trung_binh >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"
