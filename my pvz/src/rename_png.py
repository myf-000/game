import os
EXT = ".png"

def rename_files(folder_path, new_name):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    
    # 过滤出数字命名的文件（如 "1", "2", "10"）
    numbered_files = []
    for file in files:
        filename, ext = os.path.splitext(file)
        if filename.isdigit():  # 检查文件名是否只包含数字
            numbered_files.append(filename)
    
    # 按数字大小排序（避免 "10" 排在 "2" 前面）
    numbered_files.sort(key=lambda x: int(x))
    
    print(numbered_files)
    # 遍历并重命名文件
    for idx, old_name in enumerate(numbered_files):
        # 构建新文件名，如 "test_00", "test_01"
        new_filename = f"{new_name}_{idx:02d}" + EXT
        
        # 获取文件扩展名（如果有）
        old_path = os.path.join(folder_path, old_name + EXT)
        if os.path.isfile(old_path):
            _, ext = os.path.splitext(old_name)
            new_filename += ext  # 保留原扩展名
        
        # 重命名文件
        new_path = os.path.join(folder_path, new_filename)
        print(old_path)
        print(new_path)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} → {new_filename}")

if __name__ == "__main__":
    folder_path = input("请输入文件夹路径: ")
    new_name = input("请输入新文件名前缀（如 test）: ")
    
    rename_files(folder_path, new_name)
    print("重命名完成！")