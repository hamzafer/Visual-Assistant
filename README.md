# Visual-Assistant 👁️

**Visual Assistant** is an advanced real-time interface that enables scene understanding using machine learning and image
processing algorithms applied to live video. This tool is primarily designed to assist visually impaired individuals by
providing auditory feedback about their environment. By analyzing the visual data in real-time, the application
generates descriptions of the surrounding environment, thus allowing users to gain situational awareness without direct
visual input or assistance from others.

The application is designed to run on mobile devices and delivers speech output that describes detected objects, their
relative positions, and distances from the user. Moreover, the system can infer environmental context and suggest
possible actions, making it a comprehensive tool for users to interact with and understand their surroundings. In
addition to aiding visually impaired individuals, this system can be integrated into various applications, including
robotics and autonomous vehicles, for efficient environmental perception and object localization.

---

## Concept

![System Overview](https://user-images.githubusercontent.com/45764331/195984182-d9c0bfc8-9b20-450e-b671-5f8209a98960.png)

---

## Motivation

This project aims to contribute positively to society by improving the daily lives of individuals who are visually
impaired. By providing a tool that enables these individuals to better understand their surroundings, we can potentially
reduce the risk of accidents and increase their autonomy.

Furthermore, this technology holds promise for broader applications in various industries, including robotics,
autonomous vehicles, and smart systems, where real-time environmental recognition and situational awareness are
critical.

---

## Technical Details

**Visual Assistant** is an Android-based application that uses computer vision techniques to identify objects in real
time and determine their relative positions to the user. By leveraging state-of-the-art deep learning models, the system
provides speech output that describes detected objects and their distances from the user.

For example, if a user is in a room with a cup 3 feet away and a chair 5.5 feet away, the system will notify them with
audio feedback: "There’s a cup 3 feet away from you, and a chair 5.5 feet away."

In addition to object localization, the system can also recognize and describe the broader environment. For example, if
the user is sitting in a classroom, the system will detect the context and inform the user, "You are in a classroom."

The system is also adaptable for integration into larger systems that require real-time object detection and
environmental awareness. Potential applications include autonomous vehicles, robotics, and social media platforms like
Facebook and Instagram, where environmental recognition and interaction are essential.

---

## Architecture

![System Architecture](https://user-images.githubusercontent.com/45764331/195984684-febdc5ed-df5f-4f8f-96d4-4f76cd69ce6a.png)

---

## Trained Models

### Model Files

- **Path**: `backend/Classes/utills/model.11-0.6262.hdf5`
- **YOLO Weights**: `backend/Classes/utills/yolov3.weights`

### Pre-trained Model Resources:

[Download Models](https://drive.google.com/drive/folders/1AJePC6a89pxQfZOh5KPx2XH62YeReJF2?usp=sharing)

---

## References

1. Joseph Redmon, Ali Farhadi. *YOLOv3: An Incremental Improvement* [Link](https://pjreddie.com/darknet/yolo/)
2. Keras Documentation: *InceptionResNetV2* [Link](https://keras.io/api/applications/inceptionresnetv2/)
3. Research Paper: *Analysis of Blind Pedestrian Deaths and Injuries from Motor Vehicle
   Crashes* [Link](https://priuschat.com/attachments/analysis-of-blind-pedestrian-deaths-and-injuries-from-motor-vehicle-crashes-revised-doc.10892/)
4. Open Images Dataset [Link](https://storage.googleapis.com/openimages/web/index.html)
5. Arun Ponnusamy. *High-Level Computer Vision Library for Python* [Link](https://github.com/arunponnusamy/cvlib)
6. MIT Indoor Dataset [Link](http://web.mit.edu/torralba/www/indoor.html)

---

## Technologies

<p align="middle">
  <img src="https://user-images.githubusercontent.com/45764331/195984722-ef6b755a-fde7-4ebf-bcbe-9905e751ba25.png" width="100" />
  <img src="https://user-images.githubusercontent.com/45764331/195984729-e9e96afd-0f08-4990-bc50-d9fb7826b5f0.png" width="100" /> 
  <img src="https://user-images.githubusercontent.com/45764331/195984953-e45c5254-b837-4732-8dcc-7ec96543529a.png" width="100" /> 
</p>
