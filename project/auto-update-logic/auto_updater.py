import requests, os, sys, zipfile, shutil

# GITHUB_REPO : "gitHub 아이디/Repository-NAME"
GITHUB_REPO = "JiHongKim98/auto-update-logic"
# private 용 API token 키
GITHUB_API_TOKEN = "api-token key 번호"
API_SERVER_URL = f"https://api.github.com/repos/{GITHUB_REPO}"

# public REPO
response = requests.get(f"{API_SERVER_URL}/releases/latest")

# private REPO
# response = requests.get(f"{API_SERVER_URL}/releases/latest", auth=("gitHub 아이디", GITHUB_API_TOKEN))

if response.status_code != 200:
    print("릴리스 체크 실패")
    
receive = response.json()

# 현재 버전 정보 읽기!
with open("version.txt", "r") as f:
    now_current = f.read()
    print(f"현재 버전 ==> {now_current}")

if receive["tag_name"] != now_current :
    # assets 다운 REST API 요청 url
    download_url = receive["assets"][0]["url"]
    
    # public REPO
    response = requests.get(download_url, headers={'Accept': 'application/octet-stream'}, stream=True)
    
    # private REPO : auth 정보 필요!
    #response = requests.get(download_url, auth=("gitHub 아이디", GITHUB_API_TOKEN), headers={'Accept': 'application/octet-stream'}, stream=True)
    
    if response.status_code == 200:
	    # 다운로드 받은 zip 파일명 설정하기!
        update_newFile = "newAssets.zip" 

        with open(update_newFile, "wb") as update_file:
            for chunk in response.iter_content(chunk_size=8192*1024): #8MB 씩 Stream
                update_file.write(chunk)
    else:
        print("다운로드 요청 실패")
    

    # 압축 해제 로직
    update_temp_DIR = "update_temp_DIR" # 새로운 디렉토리를 만들어 저장
    with zipfile.ZipFile(update_newFile, 'r') as zip_ref:
        zip_ref.extractall(update_temp_DIR)

    # 파일 덮어씌우기 로직 시작
    # 현재 디렉토리 경로
    current_directory = os.path.dirname(os.path.realpath(__file__))
    
    # "전체" 실행 파일을 받아서 원본파일 위로 덮어쓰기
    shutil.copytree(os.path.join(current_directory, f"{update_temp_DIR}"), current_directory, dirs_exist_ok=True)

    # "수정된 된" 부분의 파일만 받아서 원본파일 위로 덮어쓰기
    #import update_new_assets # 내가 작성한 로직인 "update_new_assets.py" 호출
    #update_new_assets.update_files(update_temp_DIR= update_temp_DIR)

    # 업데이트 zip 파일과 해당 파일을 압축 해제한 디렉토리 삭제
    os.remove(update_newFile)
    shutil.rmtree(os.path.join(current_directory, f"{update_temp_DIR}"))

    # 버전 변경(최신화)
    with open("version.txt", "w") as f:
        f.write(f"{receive['tag_name']}")
        print(f"{receive['tag_name']} 버전으로 업데이트 완료")

    # 현재 실행중인 파일인 "auto_update.py" 를 재실행 하여
    # 최신 버전의 "auto_update.py" 로 실행
    update_script = os.path.join("auto_updater.py")
    os.system(f"python {update_script}")
    sys.exit(0)

else:
    print("이미 최신 버전")