import os, shutil

class update_files:
    def __init__(self, update_temp_DIR):
        self.BASE_PATH = f".\\{update_temp_DIR}"

        self.fileUpdate(self.BASE_PATH)

        # 끝난뒤 업데이트 파일 삭제
        shutil.rmtree(f".\\{update_temp_DIR}")

    def fileUpdate(self, now_checkPath):

        itemList = os.listdir(now_checkPath)

        for item in itemList:
            # 현재 item 의 경로
            nowItem_path = os.path.join(now_checkPath, item)

            originFile_path = ".\\" + os.path.relpath(nowItem_path, self.BASE_PATH)

            if os.path.isfile(nowItem_path):
                # nowItem_path 를 복사하여 originFile_path 로 붙여넣기
                shutil.copy2(nowItem_path, originFile_path)
            
            elif os.path.isdir(nowItem_path):
                # 존재하는 디렉토리 시
                if os.path.exists(originFile_path):
                    # 함수 재호출
                    self.fileUpdate(nowItem_path)
                
                # 존재하지 않는 디렉토리 시
                else:
                    create_path = ".\\" + os.path.relpath(now_checkPath, self.BASE_PATH)
                    shutil.move(nowItem_path, create_path)
