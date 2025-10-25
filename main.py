import itertools
import concurrent.futures
import os

def generate_and_save_dot_combinations(base_name: str, max_dots=5, file_name_prefix="emails_part", max_lines_per_file=100000):
    """
    Tạo tất cả các biến thể của tên người dùng với dấu chấm (dot) và lưu ngay vào các file.
    """
    positions = range(1, len(base_name))  # Các vị trí có thể chèn dấu chấm vào (không phải đầu và cuối)
    
    part_number = 1
    lines_written = 0

    # Mở file để ghi
    with open(f"{file_name_prefix}_{part_number}.txt", "w", encoding="utf-8") as file:
        # Tạo các tổ hợp dấu chấm cho từ 1 đến max_dots
        for num_dots in range(1, max_dots + 1):
            for dot_positions in itertools.combinations(positions, num_dots):
                # Tạo biến thể tên người dùng với dấu chấm tại các vị trí trong dot_positions
                variation = ''.join([base_name[i] + '.' if i in dot_positions else base_name[i] for i in range(len(base_name))])
                
                # Ghi vào file ngay lập tức
                file.write(f"{variation}@gmail.com\n")
                lines_written += 1

                # Nếu số dòng đã đủ, chuyển sang file tiếp theo
                if lines_written >= max_lines_per_file:
                    part_number += 1
                    lines_written = 0
                    file.close()  # Đóng file hiện tại
                    file = open(f"{file_name_prefix}_{part_number}.txt", "w", encoding="utf-8")  # Mở file mới

    print(f"✅ Đã lưu tất cả dữ liệu vào các file {part_number} phần.")

def process_and_save(base_name, max_dots=5):
    """
    Xử lý và lưu các biến thể email vào các file .txt chia theo phần.
    """
    generate_and_save_dot_combinations(base_name, max_dots)
    print(f"✅ Đã lưu tất cả dữ liệu vào các file txt chia theo phần!")

def main():
    base_name = "meghanbethnewmankierstincarlei"  # Tên dài ví dụ
    max_dots = 35  # Giới hạn tối đa 35 dấu chấm
    
    # Sử dụng ProcessPoolExecutor để tối ưu việc xử lý song song
    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.submit(process_and_save, base_name, max_dots)

if __name__ == "__main__":
    main()

