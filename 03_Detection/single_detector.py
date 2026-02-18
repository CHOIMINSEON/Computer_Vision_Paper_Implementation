#이미 학습되어있는 coco dataset으로 폴더에 있는 사진들에서 객채를 검출하고 
#한 폴더에 저장하며 저장한 객체와 정확도를 csv파일로 저장하는 코드.

import torch
from PIL import Image
import os
import pandas as pd
import numpy as np

# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt')

# COCO 클래스 이름 불러오기
classes = model.module.names if hasattr(model, 'module') else model.names

# 이미지 폴더 경로 설정
image_folder = 'C:/object/OlympicPark'

# 결과 저장 폴더 경로 설정
output_folder = 'C:/object/runs/detect'

# 결과 CSV 파일 경로 설정
output_csv_file = 'C:/object/runs/result.csv'

# 이미지 파일 목록 가져오기
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('.jpg', '.jpeg', '.png'))]

# 객체 정보를 저장할 리스트 생성
object_list = []

# 결과 폴더가 존재하지 않으면 생성
os.makedirs(output_folder, exist_ok=True)

# 이미지들을 순회하며 객체 검출 수행
for image_file in image_files:
    # 이미지 불러오기
    image = Image.open(image_file)

    # 이미지를 YOLOv5 모델에 적용하여 객체 검출 수행
    results = model(image)

    # 검출된 객체 정보를 리스트로 가져오기
    objects = results.pandas().xyxy[0]

    # 객체 정보를 리스트에 추가
    for _, obj in objects.iterrows():
        label = classes[int(obj[5])]
        confidence = obj[4]
        object_info = {'Image': os.path.basename(image_file), 'Label': label, 'Confidence': confidence}
        object_list.append(object_info)

    # 객체 검출된 이미지에 바운딩 박스 그리기
    image_results = results.render()

    # 이미지들을 저장
    image_name = os.path.splitext(os.path.basename(image_file))[0]
    for i, img_result in enumerate(image_results):
        output_image_file = os.path.join(output_folder, f'{image_name}_{i}.jpg')
        Image.fromarray(img_result).save(output_image_file)

# 객체 정보를 CSV 파일로 저장
df = pd.DataFrame(object_list)
df.to_csv(output_csv_file, index=False)

# 객체 정보 출력
print(df)
