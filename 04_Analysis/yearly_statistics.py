#파일 객체 이름 기준으로 합치는 코드, 신뢰도는 12로 따로 나눠줘야함..

import os
import pandas as pd

# 입력 및 출력 경로 설정
input_directory = r"C:/object/yolov5x/YeouidoHangangPark/sum_object"
output_directory = r"C:/object/yolov5x/YeouidoHangangPark"
output_filename = "object_count_confidence.csv"

# 빈 데이터프레임 생성
combined_df = pd.DataFrame(columns=["class_name", "count", "mean confidence"])

# 입력 디렉토리의 모든 파일에 대해 반복
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)
        
        # 파일을 읽어 데이터프레임으로 변환
        df = pd.read_csv(file_path)
        
        # class_name을 기준으로 파일을 합치기
        combined_df = pd.concat([combined_df, df]).groupby("class_name").sum().reset_index()
        
# 결과를 CSV 파일로 저장
output_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_path, index=False)

print("파일이 성공적으로 합쳐졌습니다. 결과는", output_path, "에 저장되었습니다.")
