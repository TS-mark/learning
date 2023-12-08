import os
import shutil
import argparse

def copy_mp4_files(source_folder, save_folder):
    # 创建目标文件夹（如果不存在）
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # 遍历源文件夹及其子文件夹
    for folder_path, subfolders, files in os.walk(source_folder):
        for file_name in files:
            if file_name.endswith('.mp4'):
                # 构建源文件的完整路径
                source_file_path = os.path.join(folder_path, file_name)

                # 构建目标文件的完整路径
                target_file_path = os.path.join(save_folder, file_name)

                # 复制源文件到目标文件夹
                shutil.move(source_file_path, target_file_path)
                print(f"Copied: {source_file_path} to {target_file_path}")

def main():
    parser = argparse.ArgumentParser(description='Copy .mp4 files from source folder to save folder')
    parser.add_argument('--sourcepath', required=True, help='Path to the source folder')
    parser.add_argument('--savepath', required=True, help='Path to the save folder')
    
    args = parser.parse_args()
    
    source_folder = args.sourcepath
    save_folder = args.savepath

    copy_mp4_files(source_folder, save_folder)

if __name__ == "__main__":
    main()
