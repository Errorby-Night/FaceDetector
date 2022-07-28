# FaceDetector
A simple python file to detect face

## How To:
  1. Clone the repo
  
     `git clone https://github.com/Errorby-Night/FaceDetector`
  
  2. Install opencv
  
      `pip install opencv-python`
  
  3. Run the `facefromcam.py` file to run it live in a web cam
      
       `python3 facefromcam.py`
        
        
  <p align="center"> OR </p>
  
  Run the `imageface.py` file to detect face in a single file
  
       `python3 imageface.py`
 ## Examples: 
 
 | No. | Original | Result |
 |:---|:-------------|:--------------|
 | 1 | <img src="src/oval (134).jpg" width="200" height="300"> | <img src="Output/oval (134).jpg" width="200" height="300"> |
 | 2 | <img src="src/oval (95).jpg" width="200" height="300"> | <img src="Output/oval (95).jpg" width="200" height="300"> |
 | 3 | <img src="src/oval (126).jpg" width="200" height="300"> | <img src="Output/oval (126).jpg" width="200" height="300"> |
 
 
 ## FAQ:
 
 1. **How to iterate over a series of photos in a folder?**
 
  ~ Run this code in that case:
  
  ```python
  import os
from os import listdir
folder_dir = "D:/Program/Output/"
for images in os.listdir(folder_dir):
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
        filename = "D:/Program/Output/" + images
        imageface(filename)
```
