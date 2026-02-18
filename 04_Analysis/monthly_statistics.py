#객체를 하나의 파일에 모아 월별로 각 객체의 비율을 csv로 저장하는 코드
import os
import pandas as pd
import datetime

# 입력 및 출력 경로 설정
input_directory = 'C:/object/yolov5x/YeouidoHangangPark/sum_object'
output_directory = 'C:/object/yolov5x/YeouidoHangangPark'
output_filename = 'object_count_month.csv'

# 클래스 이름 지정
class_names = ['bench', 'bicycle', 'car', 'cell phone', 'handbag']

# 결과 DataFrame 생성
result_df = pd.DataFrame(columns=['File_Name'] + class_names)

# 입력 디렉토리 내의 파일들 순회
for i, filename in enumerate(os.listdir(input_directory)):
    if filename.endswith('.csv'):  # 확장자가 .csv인 파일만 처리
        file_path = os.path.join(input_directory, filename)
        
        # CSV 파일 읽기
        df = pd.read_csv(file_path)
        
        # 파일 이름 추출
        month = filename.split('.')[0]
        
        # 파일 이름에 포함된 날짜 문자열을 날짜 형식으로 변환
        date_obj = datetime.datetime.strptime(month, '%Y-%m')
        
        # 월만 영어로 표시
        month_str = date_obj.strftime('%B')
        
        # 클래스별 비율 계산
        total_count = df['count'].sum()
        row_data = [month_str]
        for class_name in class_names:
            class_count = df.loc[df['class_name'] == class_name, 'count'].sum()
            percentage = (class_count / total_count) * 100
            row_data.append(percentage)
        
        # 결과 DataFrame에 현재 파일의 데이터 추가
        result_df.loc[i] = row_data

# 결과 파일 경로 생성
output_path = os.path.join(output_directory, output_filename)

# 결과 DataFrame을 CSV 파일로 저장
result_df.to_csv(output_path, index=False)

print('병합 및 변환이 완료되었습니다.')
