#이미 학습된 pt파일로 크롤링한 이미지 돌리기.
#이미지 파일 속 하위 폴더 모두 돌리고 이미지 및 라벨 파일로 저장하는 코드.
import os
import glob

folder = "C:/object/crawling/2022_date/SeoulForest"

# 폴더 내 모든 하위 폴더를 가져옴
image_folders = glob.glob(os.path.join(folder, "*"))

for image_folder in image_folders:
    # 폴더 이름만 추출
    folder_name = os.path.basename(image_folder)
    
    # 결과 저장 폴더 경로 생성
    output_folder = os.path.join(folder, "output", folder_name, folder_name)
    
    # 결과 저장 폴더 생성 (이미 존재하는 경우 무시)
    os.makedirs(output_folder, exist_ok=True)
    
    # detect 명령어 실행
    command = f"python C:/object/yolov5-master/detect_.py --device cuda:0 --weight yolov5x.pt --source {image_folder} --project {output_folder} --name {folder_name} --save-txt --save-conf"

    os.system(command)

