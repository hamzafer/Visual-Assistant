# Visual-Assistant

Visual Assistant is an interface which will give the scene understanding to its users by using machine learning and image processing algorithms on live video. One of our users is visually impaired people, which can now see. They can now also get the understanding of their surroundings without actually seeing it and without the aid of any another person. This interface will be used in a mobile application to efficiently generate speech in real time scenario. Through this the blind persons can be able to understand their environment by getting the speech from real time video. The application will generate speech on the basis of objects detected, the distance of objects from the person and nearby objects and will learn the environment by combining the knowledge of all objects in the environment. The application will not only make them imagine their surroundings but also suggest them the possible actions, a person can normally take in a specific environment.
Moreover, our interface can be used by other systems to get the knowledge of the environment in an efficient way.

# Architecture

<img width="686" alt="image" src="https://user-images.githubusercontent.com/45764331/195984684-febdc5ed-df5f-4f8f-96d4-4f76cd69ce6a.png">

# Technial Details

Visual Assistant is an android application for visually impaired people that will identify objects and their positions with respect to camera in real time. It will inform user about the objects in his environment and their locations in the form of speech. Let’s suppose, there is a cup and chair 3ft and 5.5ft away from the user respectively. The application will inform user that “There’s cup 3ft away from you and chair 5.5ft away from you”. Moreover, on the basis of this information it will also inform the user about the environment he is currently present in. Let’s suppose a user is sitting in a classroom environment. The system will recognize the environment and will inform him that he’s sitting in a classroom environment. Apart from that, Visual Assistant will also act as an interface which can be used by other systems which requires real time object identification and localization. For example, it can also be used in auto-driving automobiles for environment detection, robots, and major systems like Facebook, Instagram etc. The system will detect object, find its relative distance, recognize it, and then convert this information into voice or text according to user’s requirement.

# Concept

<img width="714" alt="image" src="https://user-images.githubusercontent.com/45764331/195984182-d9c0bfc8-9b20-450e-b671-5f8209a98960.png">

# Motivation

Through this project, we want to contribute to the society by helping the society’s special people who are unable to truly visualize their surroundings. This will cause a reduction in number of incidents directly or indirectly involving them. Moreover, we also want to contribute to the industry by providing an efficient environment recognizer which can be used in robotics and larger systems.

# Trained Models

### Path
backend/Classes/utills/model.11-0.6262.hdf5
backend/Classes/utills/yolov3.weights

### Files
https://drive.google.com/drive/folders/1AJePC6a89pxQfZOh5KPx2XH62YeReJF2?usp=sharing

# References

[1] Joseph Redmon, Ali Farhadi. YOLOv3: An Incremental Improvement. Visited: November 2019.
https://pjreddie.com/darknet/yolo/
[2] https://keras.io/api/applications/inceptionresnetv2/
[3] https://priuschat.com/attachments/analysis-of-blind-pedestrian-deaths-and-
injuries-from-motor-vehicle-crashes-revised-doc.10892/
[4] https://storage.googleapis.com/openimages/web/index.html
[5] Arun Ponnusamy. High level Computer Vision Library for Python. Visited: April 15, 2020.
https://github.com/arunponnusamy/cvlib
[6] http://web.mit.edu/torralba/www/indoor.html

![image](https://user-images.githubusercontent.com/45764331/195984722-ef6b755a-fde7-4ebf-bcbe-9905e751ba25.png)
![image](https://user-images.githubusercontent.com/45764331/195984729-e9e96afd-0f08-4990-bc50-d9fb7826b5f0.png)


