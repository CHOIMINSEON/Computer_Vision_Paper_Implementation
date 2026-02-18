# 컴퓨터 비전(computer vision) 논문 답습(2024)
* 객체 검출(Object_Detection) 모델을 활용해 서울시 녹지 공간을 분석.
* 답습 논문 : Song, Y., Ning, H., Ye, X., Chandana, D., & Wang, S. (2022). Analyze the usage of urban greenways through social media images and computer vision. Environment and Planning B: Urban Analytics and City Science, 49(6), 1682-1696.

### 프로젝트 개요

본 프로젝트는 특정 장소의 시간별/월별 이미지를 수집하고, COCO 데이터셋으로 학습된 YOLOv5 모델을 활용하여 객체를 검출한 뒤, 검출 결과를 다양한 통계 지표로 분석하고 시각화합니다.

### 주요 기능
- **자동 데이터 수집**: 네이버 이미지 검색 크롤링 (일별/월별)
- **데이터셋 변환**: COCO → YOLO 형식 자동 변환
- **객체 검출**: YOLOv5 기반 80개 클래스 검출
- **통계 분석**: 다각도 데이터 분석 및 집계
- **시각화**: 그래프 및 차트 자동 생성

---

**📁 Directory Structure**
```text
Computer_Vision_Paper_Implementation/
├── 01_Crawling/ # 이미지 데이터 수집
│ ├── monthly_crawler.py # 월별 이미지 크롤링
│ └── daily_crawler.py # 일별 이미지 크롤링
│
├── 02_Training/ # 데이터셋 준비 및 변환
│ ├── instances_train2017.json # COCO 데이터셋 (80개 클래스)
│ ├── cocotoyolo.jar # COCO→YOLO 변환 도구
│ └── convert_command.txt # 변환 실행 명령어
│
├── 03_Detection/ # YOLO 객체 검출 및 시각화
│ ├── batch_detector.py # 배치 검출 (폴더 일괄 처리)
│ ├── single_detector.py # 단일 검출 (즉시 CSV 생성)
│ ├── label_to_csv.py # 라벨 파일 → CSV 변환
│ ├── detection_statistics.py # 검출 결과 통계 분석
│ └── visualize_graph.py # 누적 막대그래프 생성
│
└── 04_Analysis/ # 통계 분석 및 집계
  ├── group_by_object.py # 객체별 그룹화 및 통계
  ├── filter_objects.py # 특정 객체 필터링 (5개)
  ├── count_persons.py # 사람 수 집계
  ├── image_counter.py # 월별 이미지 수 집계
  ├── yearly_statistics.py # 연도별 통합 통계
  └── monthly_statistics.py # 월별 객체 비율
```

---

**Flowchart**
```text
[검색어 입력]
       │
       ▼
1. 01_Crawling ─────────────────────────────────┐
       │ monthly_crawler.py                     │ 네이버 이미지 검색
       │ daily_crawler.py                       │ 월별/일별 크롤링
       │ (Output: 이미지 파일들)                 │
       ▼                                        │
2. 02_Training ─────────────────────────────────┤
       │ cocotoyolo.jar                         │ COCO → YOLO 변환
       │ (Input: instances_train2017.json)      │ 80개 클래스 매핑
       │ (Output: 라벨 .txt)                    │
       ▼                                        │
3. 03_Detection ────────────────────────────────┤
       │ batch_detector.py or single_detector.py│ YOLO 객체 검출 or 라벨 → CSV 변환
       │ (Output: original/*.csv)               │
       ├── detection_statistics.py              │ 검출 결과 통계
       ├── visualize_graph.py                   │ 그래프 생성
       ▼                                        │
4. 04_Analysis ─────────────────────────────────┘
       ├── group_by_object.py (original → sum) 객체별 그룹화 및 통계
       ├── filter_objects.py (sum → sum_object) 5개 객체 필터링
       ├── 개별 통계
       │   ├─ count_persons.py (사람 수 집계)
       │   └─ image_counter.py (이미지 수 집계)
       └── 통합 통계
           ├─ yearly_statistics.py (연도별 통합)
           └─ monthly_statistics.py (월별 비율)
```
---
### [모델 학습 결과]
<img width="764" height="109" alt="image" src="https://github.com/user-attachments/assets/6c3317fa-ec7d-4985-b64d-2ddda80e4db3" />


### [객체 검출 결과]
<img width="1000" height="600" alt="overall_object_ratios1" src="https://github.com/user-attachments/assets/46578f9e-8d81-4539-8bc6-85383bab5ac6" />
<img width="945" height="351" alt="image" src="https://github.com/user-attachments/assets/8bb26459-5165-413e-a81c-1e1f93bf9653" />
<img width="730" height="315" alt="image" src="https://github.com/user-attachments/assets/3d090786-7517-4935-a415-0725b615d9bd" />
<img width="1171" height="397" alt="image" src="https://github.com/user-attachments/assets/4a038ba7-80da-461f-823b-9031bee80852" />





