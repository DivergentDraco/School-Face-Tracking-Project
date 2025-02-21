# Face Tracking Manual 

## 2302307 Interactive Science and Social Project (ISSP) AY 2024

[Read about **eye** tracking here](https://github.com/DivergentDraco/School-Eye-Gaze-Project)

[อ่านฉบับภาษาไทยได้ที่นี่ | Click here for Thai version](MANUAL_TH.md)

---

# Introduction

Face tracking is an alternative way to compensate for eye-tracking weaknesses; it was implemented by using camera to detect the components of the face. This project came to the light, after we initiated a detailed analysis through observation, interview questions, and surveys throughout the school.

This repository was made specifically for the  **Interactive Science and Social Project 
 (ISSP)**, in collaboration with Worcester Polytechnic Institute, USA. The students studying in Bachelor of Science in Applied Chemistry, Chemistry Department, Faculty of Science, Chulalongkorn University has to accomplish. In this project, Sri Sangwan School is our sponsor. We are interested in the open-source, face-tracking software to utilize it for the gaze bubble to follow with the mouse, along with face movement.

---

## Members
 * Sean Arackal, *Worcester Polytechnic Institute*
 * Mohamed Adem Djadid, *Worcester Polytechnic Institute*
 * Pawin Harijanwong, *Chulalongkorn University* ([@DivergentDraco](https://github.com/DivergentDraco))
 * Siraphop Homhual, *Chulalongkorn University*
 * Madalyn Nguyen, *Worcester Polytechnic Institute*
 * Marissa Rukachantarakul, *Chulalongkorn University*
 * Bhurinat Sumetchotimaytha, *Chulalongkorn University*
 * Mahit Verma, *Worcester Polytechnic Institute* ([@MaVeryo](https://github.com/MaVeryo))

---

# Project Overview

**Sri Sangwan School** is an institution that provides inclusive education for children with disabilities. Our project mission is to assist them by making insightful research recommendations that will make digital education more accessible. Read more about Sri Sangwan School ([>>here<<](http://www.swn.ac.th/mainpage))

This project focuses on improving the well-being of Sri Sangwan School by providing research recommendations through surveys, interviews, classroom observations. However, after the students had experimented using eye-tracking software, it came to the conclusion that face-tracking software is a more stable alternative software. There is no eye fatigue and more precision. The first difference between these 2 programs is that for eye-tracking software, the camera tracks the eyes only, meaning if the detection of the eyes is not decent, new calibration of the software is required. While the face-tracking software enable the camera to follow the eyes where they go. In other words, face-tracking software allows precision by letting mouse cursor follow wherever the eyes are moving to.

![School Banner](https://github.com/user-attachments/assets/9b123cf6-f919-4abe-b54b-365a5b79b447)

## Our Goal
The goal of this project is to try and see methods that can be used within Sri Sangwan School's computer science lab, which houses students that has loss of limb, uncontrollable muscle, or Cerebral Palsy, etc.

### Coding language used
#### To install the program, you will need the programs and files as stated:
##### Required Programs and Files
 - Python **3.9.13** ([Website](https://www.python.org/downloads/release/python-3913/))
 - Provided file in the repository

##### Required Equipments
 - **Webcam** is an important equipment for tracking the face. Low quality webcam is encouraged with 30 fps laptop webcam is enough.
   Recommendation is Logitech C270 HD which costs around 590 baht.

# Demo Video
[Find it here]()

---

# Installation

## Installation Video
[Find it here]() 

## Installation steps
1. Install the following program\
 1.1 Python 3.9.13\
 1.2 Code editor (ex. Visual Studio Code)\
 1.3 Webcam
3. Install the provided file\
 2.1 Open the file folder, go to the *API* folder, and go to the *Python* folder.\
 2.2 Open **tracker_sample.py**

You should be able to run the code, and it will turn the webcam on. This should be the following result.
![image](https://github.com/user-attachments/assets/36076fa7-91a7-4614-afd1-66ebf377c9c8)


> [!WARNING]
> Unlike the eye-tracking repository, this face tracking doesn't consume budget on programs.

> [!WARNING]
> > This face-tracking project is in development progress, which does not intend to be implemented due to many factors, such as calibration and sensitivity problems. This project was made to help with recommendations to the school and give other future teams to help with decision-making.

In conclusion, the face-tracking software has a better precision than eye-tracking software increasing the potential for the real applicaiton.

# Encountered Issues
- Face and neck movement\
  Some students at the school may suffer from abnormal neck muscle movement. Further study and troubleshooting needs to be conducted.

Should you encounter any problems, please feel free to contact us via Srisangwanissp@gmail.com
