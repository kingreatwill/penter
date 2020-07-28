# https://github.com/OlafenwaMoses/ImageAI

# 图像分类
def demo01():
    # https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Prediction/README.md
    from imageai.Prediction import ImagePrediction
    import os

    execution_path = os.getcwd()

    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    # https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_weights_tf_dim_ordering_tf_kernels.h5
    prediction.setModelPath(r"E:\bigdata\ai\imageai\resnet50_weights_tf_dim_ordering_tf_kernels.h5") #(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
    prediction.loadModel()

    predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "1.png"), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)

# 对象检测
def demo02():
    # https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/README.md
    from imageai.Detection import ObjectDetection
    import os

    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    # https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
    detector.setModelPath(r"E:\bigdata\ai\imageai\yolo.h5") # (os.path.join(execution_path, "yolo.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "1.png"),
                                                 output_image_path=os.path.join(execution_path, "image2new.jpg"),
                                                 minimum_percentage_probability=10)

    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
        print("--------------------------------")

# 视频目标检测、跟踪与分析
def demo03():
    # https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/VIDEO.md
    from imageai.Detection import VideoObjectDetection
    import os

    execution_path = os.getcwd()

    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()
    # https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5
    detector.setModelPath(r"E:\bigdata\ai\imageai\resnet50_coco_best_v2.0.1.h5") #(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "AInextcon.mp4"),
                                                 output_file_path=os.path.join(execution_path, "AInextcon_detected")
                                                 , frames_per_second=20, log_progress=True)
    print(video_path)

demo03()