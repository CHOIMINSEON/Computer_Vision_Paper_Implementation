#결과csv 파일을 여러 결과로 저장 
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('C:/object/runs/결과2.csv')

# 객체별 이미지 포함 비율 계산
image_count = len(df['Image'].unique())
object_counts = df['Label'].value_counts()
object_ratios = object_counts / image_count * 100

# 객체별 이미지 포함 비율 출력
print("각 객체가 포함된 이미지 비율:")
print(object_ratios)

# 객체별 이미지 포함 비율 그래프 생성 및 저장
plt.figure(figsize=(10, 6))
object_ratios.plot(kind='bar')
plt.xlabel('객체')
plt.ylabel('이미지 포함 비율 (%)')
plt.title('객체별 이미지 포함 비율')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/object/runs/객체별_이미지_포함_비율.png')

# 1번 결과를 CSV 파일로 저장
object_ratios.to_csv('C:/object/runs/객체별_이미지_포함_비율.csv')

# 모든 객체의 비율 계산
total_count = len(df)
total_object_ratios = object_counts / total_count * 100

# 모든 객체의 비율 출력
print("모든 객체의 비율:")
print(total_object_ratios)

# 모든 객체의 비율 그래프 생성 및 저장
plt.figure(figsize=(10, 6))
total_object_ratios.plot(kind='bar')
plt.xlabel('객체')
plt.ylabel('객체 비율 (%)')
plt.title('모든 객체의 비율')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/object/runs/모든_객체의_비율.png')

# 2번 결과를 CSV 파일로 저장
total_object_ratios.to_csv('C:/object/runs/모든_객체의_비율.csv')

# 객체별 정확도 통계 계산
accuracy_stats = df.groupby('Label')['Confidence'].mean()

# 객체별 정확도 통계 출력
print("객체별 정확도 통계:")
print(accuracy_stats)

# 3번 결과를 CSV 파일로 저장
accuracy_stats.to_csv('C:/object/runs/객체별_정확도_통계.csv')
