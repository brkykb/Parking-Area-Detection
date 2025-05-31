# 🚗 Parking Spot Detection System


A computer vision-based system for detecting **occupied and available parking spots** from a top-down camera view using image processing and deep learning.


## 🔍 About the Project


This project identifies the status of parking spots (occupied or empty) using video footage from a fixed, overhead camera. Users manually define parking spot regions in the first frame using a simple GUI tool. Once the areas are set, the model processes the remaining video to monitor parking availability in real time.


### 🧠 Key Features


- ✅ Parking spot detection via image processing
- 🎯 Manual region selection using a GUI (Coordinate Extractor)
- 🧰 Built with **OpenCV**, **Tkinter**, and a custom-trained model (with Pretrained Model MobileNetV2)
- 🏷️ Over **3000 images** manually labeled for training
- 🖥️ Simple and interactive desktop application
- 📦 Fully open-source and customizable

---


## 🚀 Getting Started


### 1. Clone the Repository

```bash
git clone https://github.com/brkykb/Parking-Area-Detection.git
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 📍 3. Coordinate Extraction


#### To define parking areas:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open the coordinate_extractor.py file.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set the path to your input video by modifying the video_source variable.


#### Run the script:
```bash
python coordinate_extractor.py
```
#### In the UI:


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Click to mark the corners of each parking space.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save your selections to a .txt file when done.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This coordinate file will be used in the main detection system.


### 🧪 4. Running the Detection System


#### Once you have both the video and the coordinates file:


#### Run the main application:
```bash
python main.py
```


#### In the GUI:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🗂️ Select your video file.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Load the coordinates file you previously saved.


#### The system will:


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Analyze each frame of the video.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Detect and highlight occupied and empty parking spots in real-time.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🚦 Easy-to-use, visual parking space monitoring made simple!


