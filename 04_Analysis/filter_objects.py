#선택한 5개의 객체만 남겨서 csv파일로 저장하기.
import os
import pandas as pd

# 입력 경로
input_path = r"C:/object/yolov5x/YeouidoHangangPark/sum"
# 출력 경로
output_path = r"C:/object/yolov5x/YeouidoHangangPark/sum_object"

# 입력 경로의 모든 파일에 대해 반복
for filename in os.listdir(input_path):
    if filename.endswith(".csv"):
        input_file = os.path.join(input_path, filename)
        output_file = os.path.join(output_path, filename)
        
        # CSV 파일을 읽어옴
        df = pd.read_csv(input_file)
        
        # class_name 열에서 원하는 항목만 필터링
        filtered_df = df[df['class_name'].isin(['bench', 'car', 'handbag', 'cell phone', 'bicycle'])]
        
        # 필터링된 데이터프레임을 새로운 CSV 파일로 저장
        filtered_df.to_csv(output_file, index=False)
