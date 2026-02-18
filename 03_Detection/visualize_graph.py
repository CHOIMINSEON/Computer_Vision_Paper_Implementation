#누적 막대그래프 성공
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 파일 경로와 열 이름 설정
file_paths = ['C:/object/chat/runs/통계2/모든_객체의_비율.csv', 'C:/object/chat/runs/통계2/모든_객체의_비율2.csv']
column_names = ['File', 'Label', 'count']

# 데이터프레임 생성 및 파일 이름 열 추가
combined_df = pd.DataFrame()
for file_path in file_paths:
    df = pd.read_csv(file_path)
    file_name = file_path.split('/')[-1]
    df['File'] = file_name
    combined_df = pd.concat([combined_df, df])

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 누적 막대그래프 그리기
sns.barplot(x='File', y='count', hue='Label', data=combined_df, palette='Set3', ci=None, estimator=sum, dodge=False)

plt.title('Object Count by File', fontsize=14)
plt.xlabel('File', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Label', loc='upper right')

plt.show()

