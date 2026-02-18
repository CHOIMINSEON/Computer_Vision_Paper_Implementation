#csv파일을 만들어보자.
import os
import pandas as pd

for x in range(1,12):

    # 라벨 파일이 들어있는 폴더 경로 설정
    label_folder = rf"C:/object/crawling/2022_date/YeouidoHangangPark/output/2022-{x:02d}/labels"


    # 상위 폴더 이름 가져오기
    parent_folder = os.path.basename(os.path.dirname(label_folder))

    # CSV 파일 이름 설정
    csv_file = f"{parent_folder}.csv"

    # 클래스 ID에 해당하는 영어 이름 매칭
    class_names = {
        0: "person", 1: "bicycle", 2: "car", 3: "motorcycle", 4: "airplane",
        5: "bus", 6: "train", 7: "truck", 8: "boat", 9: "traffic light",
        10: "fire hydrant", 11: "stop sign", 12: "parking meter", 13: "bench",
        14: "bird", 15: "cat", 16: "dog", 17: "horse", 18: "sheep",
        19: "cow", 20: "elephant", 21: "bear", 22: "zebra", 23: "giraffe",
        24: "backpack", 25: "umbrella", 26: "handbag", 27: "tie", 28: "suitcase",
        29: "frisbee", 30: "skis", 31: "snowboard", 32: "sports ball", 33: "kite",
        34: "baseball bat", 35: "baseball glove", 36: "skateboard", 37: "surfboard",
        38: "tennis racket", 39: "bottle", 40: "wine glass", 41: "cup", 42: "fork",
        43: "knife", 44: "spoon", 45: "bowl", 46: "banana", 47: "apple",
        48: "sandwich", 49: "orange", 50: "broccoli", 51: "carrot", 52: "hot dog",
        53: "pizza", 54: "donut", 55: "cake", 56: "chair", 57: "couch",
        58: "potted plant", 59: "bed", 60: "dining table", 61: "toilet", 62: "tv",
        63: "laptop", 64: "mouse", 65: "remote", 66: "keyboard", 67: "cell phone",
        68: "microwave", 69: "oven", 70: "toaster", 71: "sink", 72: "refrigerator",
        73: "book", 74: "clock", 75: "vase", 76: "scissors", 77: "teddy bear",
        78: "hair drier", 79: "toothbrush"
    }

    # DataFrame을 저장할 리스트 생성
    data_list = []

    # 라벨 폴더 내의 파일들을 순회하며 처리
    for file_name in os.listdir(label_folder):
        if file_name.endswith(".txt"):
            # 라벨 파일 경로 설정
            label_file = os.path.join(label_folder, file_name)

            # 라벨 파일 읽기
            with open(label_file, "r") as f:
                lines = f.readlines()

            # 라벨 정보 추출
            for line in lines:
                class_id, confidence, x, y, w, h = line.strip().split()
                class_id = int(class_id)
                confidence = float(confidence)
                x, y, w, h = map(float, (x, y, w, h))

                # 클래스 ID에 해당하는 영어 이름 매칭
                class_name = class_names.get(class_id, "")

                # 데이터 리스트에 추가
                data_list.append([file_name, class_name, confidence, x, y, w, h])

    # DataFrame 생성
    columns = ["file_name", "class_name", "x", "y", "w", "h", "confidence"]
    df = pd.DataFrame(data_list, columns=columns)

    # CSV 파일 경로 설정
    csv_folder = r"C:/object/crawling/2022_date/YeouidoHangangPark/csv"
    csv_path = os.path.join(csv_folder, csv_file)

    # CSV 파일로 저장
    df.to_csv(csv_path, index=False)
