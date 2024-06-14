from ultralytics import YOLO


import os

def move_class_to_beginning(label):
    class_dict = {
        "vehicle": 0,
        "plane": 1,
        "bridge": 2,
        "harbor": 3,
        "ship": 4
    }

    parts = label.split()
    class_label = parts[-1]
    class_index = class_dict[class_label]
    new_label = f"{class_index} {' '.join(parts[:-1])}"
    return new_label

def process_txt_files_in_directory(directory):
    for filename in os.listdir(directory):
        print(filename)
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
            with open(filepath, 'w') as file:
                for line in lines:
                    new_line = move_class_to_beginning(line.strip())
                    file.write(new_line + "\n")

# Kullanım
directory_path = "dataset/test/labels"
directory_path1 = "dataset/train/labels"
directory_path2 = "dataset/val/labels"

#process_txt_files_in_directory(directory_path)
#process_txt_files_in_directory(directory_path1)
#process_txt_files_in_directory(directory_path2)

def process_txt_files_in_directory(directory, image_width, image_height):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
            with open(filepath, 'w') as file:
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 9:  # Assuming each line has 9 values (class label and 8 coordinates)
                        class_label = parts[0]
                        normalized_coords = []
                        for i in range(1, len(parts)):
                            if i % 2 == 1:  # X coordinates
                                normalized_coords.append(float(parts[i]) / image_width)
                            else:  # Y coordinates
                                normalized_coords.append(float(parts[i]) / image_height)
                        new_line = " ".join([class_label] + [str(coord) for coord in normalized_coords])
                        file.write(new_line + "\n")
                    else:
                        file.write(line)

#process_txt_files_in_directory(directory_path,1024,1024)
#process_txt_files_in_directory(directory_path1,1024,1024)
#process_txt_files_in_directory(directory_path2,1024,1024)


#import splitfolders
#splitfolders.ratio("/content/part3",output="output", seed=42, ratio=(.8,.1,.1))

model = YOLO('best.pt')  # Assuming you have an 'obb' model config
#model.predict("C:/Users/ysfkm/Desktop/part3/dataset/val/images/P2747__1__0___1281.png", save=True, show_labels=False,show_conf=False)


test_directory = "dataset/test/images"

# Her bir resim dosyası için tahmin yap
for filename in os.listdir(test_directory):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        image_path = os.path.join(test_directory, filename)
        results = model.predict(image_path, conf=0.6,save_txt=True,save_conf=True)