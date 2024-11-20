import os
import shutil

# 다운로드 폴더 경로
download_folder = r"C:\Users\student\Downloads"

# 이동할 폴더 및 파일 확장자 정의
folders = {
    "images": ["jpg", "jpeg"],
    "data": ["csv", "xlsx"],
    "docs": ["txt", "doc", "pdf"],
    "archive": ["zip"],
}

# 각 폴더 경로 생성
folder_paths = {key: os.path.join(download_folder, key) for key in folders.keys()}

# 필요한 폴더 생성
for folder_path in folder_paths.values():
    os.makedirs(folder_path, exist_ok=True)

# 파일 이동 함수
def move_files():
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        # 파일인지 확인
        if os.path.isfile(file_path):
            # 파일 확장자 확인
            extension = filename.split(".")[-1].lower()
            for folder, extensions in folders.items():
                if extension in extensions:
                    shutil.move(file_path, folder_paths[folder])
                    print(f"Moved: {filename} -> {folder_paths[folder]}")
                    break

# 파일 이동 실행
if __name__ == "__main__":
    move_files()
    print("File moving complete!")
