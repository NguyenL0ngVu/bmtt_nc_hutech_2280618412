from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        max_id = 1
        if (self.soLuongSV() > 0):
            max_id = max([sv.id for sv in self.listSinhVien]) + 1
            for sv in self.listSinhVien:
                if (max_id < sv.id):
                    max_id = sv.id
            max_id += 1
        return max_id
    
    def soLuongSV(self):
        return len(self.listSinhVien)
    
    def themSinhVien(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        id = self.generateID()
        sv = SinhVien(id, ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        self.listSinhVien.append(sv)
        print("Thêm sinh viên thành công!")
        print("ID sinh viên:", id)
        print("Tên sinh viên:", ten)
        print("Giới tính sinh viên:", gioi_tinh)
        print("Chuyên ngành sinh viên:", chuyen_nganh)
        print("Điểm trung bình sinh viên:", diem_trung_binh)
        print("Học lực sinh viên:", sv.get_hoc_luc())
        print("====================================")
        print("Danh sách sinh viên hiện tại:")
        self.xuatDanhSachSinhVien()
        print("====================================")
    def capNhatSinhVien(self, id, ten=None, gioi_tinh=None, chuyen_nganh=None, diem_trung_binh=None):
        for sv in self.listSinhVien:
            if sv.id == id:
                if ten is not None:
                    sv.ten = ten
                if gioi_tinh is not None:
                    sv.gioi_tinh = gioi_tinh
                if chuyen_nganh is not None:
                    sv.chuyen_nganh = chuyen_nganh
                if diem_trung_binh is not None:
                    sv.diem_trung_binh = diem_trung_binh
                print("Cập nhật thông tin sinh viên thành công!")
                print("ID sinh viên:", sv.id)
                print("Tên sinh viên:", sv.ten)
                print("Giới tính sinh viên:", sv.gioi_tinh)
                print("Chuyên ngành sinh viên:", sv.chuyen_nganh)
                print("Điểm trung bình sinh viên:", sv.diem_trung_binh)
                print("Học lực sinh viên:", sv.get_hoc_luc())
                return
        print("Không tìm thấy sinh viên với ID:", id)
    def xoaSinhVien(self, id):
        for sv in self.listSinhVien:
            if sv.id == id:
                self.listSinhVien.remove(sv)
                print("Xóa sinh viên thành công!")
                return
        print("Không tìm thấy sinh viên với ID:", id)
    def timKiemSinhVien(self, ten):
        found = False
        for sv in self.listSinhVien:
            if sv.ten.lower() == ten.lower():
                print("ID sinh viên:", sv.id)
                print("Tên sinh viên:", sv.ten)
                print("Giới tính sinh viên:", sv.gioi_tinh)
                print("Chuyên ngành sinh viên:", sv.chuyen_nganh)
                print("Điểm trung bình sinh viên:", sv.diem_trung_binh)
                print("Học lực sinh viên:", sv.get_hoc_luc())
                found = True
        if not found:
            print("Không tìm thấy sinh viên với tên:", ten)
    def sapXepTheoDiem(self):
        self.listSinhVien.sort(key=lambda sv: sv.diem_trung_binh, reverse=True)
        print("Danh sách sinh viên đã được sắp xếp theo điểm trung bình:")
        self.xuatDanhSachSinhVien()
    def sapXepTheoChuyenNganh(self):
        self.listSinhVien.sort(key=lambda sv: sv.chuyen_nganh)
        print("Danh sách sinh viên đã được sắp xếp theo chuyên ngành:")
        self.xuatDanhSachSinhVien()
    def xuatDanhSachSinhVien(self):
        if len(self.listSinhVien) == 0:
            print("Danh sách sinh viên rỗng!")
            return
        print("Danh sách sinh viên:")
        for sv in self.listSinhVien:
            print("ID sinh viên:", sv.id)
            print("Tên sinh viên:", sv.ten)
            print("Giới tính sinh viên:", sv.gioi_tinh)
            print("Chuyên ngành sinh viên:", sv.chuyen_nganh)
            print("Điểm trung bình sinh viên:", sv.diem_trung_binh)
            print("Học lực sinh viên:", sv.get_hoc_luc())
            print("------------------------------------")
    def menu(self):
        while True:
            print("====================================")
            print("QUẢN LÝ SINH VIÊN")
            print("1. Thêm sinh viên")
            print("2. Cập nhật thông tin sinh viên theo ID")
            print("3. Xóa sinh viên theo ID")
            print("4. Tìm kiếm sinh viên theo tên")
            print("5. Sắp xếp danh sách sinh viên theo điểm trung bình")
            print("6. Sắp xếp danh sách sinh viên theo chuyên ngành")
            print("7. Xuất danh sách sinh viên")
            print("8. Thoát")
            choice = input("Nhập lựa chọn của bạn: ")
            if choice == '1':
                ten = input("Nhập tên sinh viên: ")
                gioi_tinh = input("Nhập giới tính sinh viên: ")
                chuyen_nganh = input("Nhập chuyên ngành sinh viên: ")
                diem_trung_binh = float(input("Nhập điểm trung bình sinh viên: "))
                self.themSinhVien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
            elif choice == '2':
                id = int(input("Nhập ID sinh viên cần cập nhật: "))
                ten = input("Nhập tên sinh viên mới (để trống nếu không thay đổi): ")
                gioi_tinh = input("Nhập giới tính sinh viên mới (để trống nếu không thay đổi): ")
                chuyen_nganh = input("Nhập chuyên ngành sinh viên mới (để trống nếu không thay đổi): ")
                diem_trung_binh = input("Nhập điểm trung bình sinh viên mới (để trống nếu không thay đổi): ")
                if diem_trung_binh != "":
                    diem_trung_binh = float(diem_trung_binh)
                else:
                    diem_trung_binh = None
                self.capNhatSinhVien(id, ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
            elif choice == '3':
                id = int(input("Nhập ID sinh viên cần xóa: "))
                self.xoaSinhVien(id)
            elif choice == '4':
                ten = input("Nhập tên sinh viên cần tìm kiếm: ")
                self.timKiemSinhVien(ten)
            elif choice == '5':
                self.sapXepTheoDiem()
            elif choice == '6':
                self.sapXepTheoChuyenNganh()
            elif choice == '7':
                self.xuatDanhSachSinhVien()
            elif choice == '8':
                print("Thoát chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng nhập lại.")
if __name__ == "__main__":
    qlsv = QuanLySinhVien()
    qlsv.menu()
    # qlsv.themSinhVien("Nguyen Van A", "Nam", "CNTT", 8.5)
    # qlsv.themSinhVien("Nguyen Van B", "Nu", "KTMT", 7.5)
    # qlsv.themSinhVien("Nguyen Van C", "Nam", "KTMT", 6.5)
    # qlsv.themSinhVien("Nguyen Van D", "Nu", "CNTT", 9.5)
    # qlsv.themSinhVien("Nguyen Van E", "Nam", "CNTT", 5.5)
    # qlsv.themSinhVien("Nguyen Van F", "Nu", "KTMT", 4.5)
    # qlsv.themSinhVien("Nguyen Van G", "Nam", "CNTT", 8.0)
    # qlsv.themSinhVien("Nguyen Van H", "Nu", "KTMT", 7.0)
    # qlsv.themSinhVien("Nguyen Van I", "Nam", "CNTT", 6.0)
    # qlsv.themSinhVien("Nguyen Van J", "Nu", "KTMT", 9.0)
    # qlsv.themSinhVien("Nguyen Van K", "Nam", "CNTT", 5.0)
    # qlsv.themSinhVien("Nguyen Van L", "Nu", "KTMT", 4.0)
    # qlsv.themSinhVien("Nguyen Van M", "Nam", "CNTT", 8.5)