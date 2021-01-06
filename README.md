# Introduction
 This is a simple GUI using PyQt for YOLO darknet mass detection NeuralSIGHT from final bachelor capstone project.
![results](GUI.png)
## Requirements
   - **PyQt5**
   - **YOLO darknet installed**
   - **OpenCV >= 4.4.0**

## How To Use

#### Step 0: Compile YOLO darknet 

Follow AlexeyAB's instruction of [How to compile YOLO darknet on Linux or Windows](https://github.com/AlexeyAB/darknet#how-to-compile-on-linuxmacos-using-cmake)

#### Step 1: Install PyQt5 and OpenCV

Simple installation from PyPI
```bash
pip install PyQt5
pip install opencv-python
```
From Conda
```bash
conda install -c anaconda pyqt
```

#### Step 2: Setup Folder

- Move `main.py`,`main_window.py`, and `splashscreen.py` to your darknet folder.
- Put your `your-weight.weights` to weights folder.

**if you're going to use GUI with OpenCV skip to Step 3, otherwise follow these instructions for YOLO version inference**
- Edit `main_window.py` on line 190 to your darknet data folder directory path.
- If your OS is Windows or you have different name for your own cfg or weights files then edit `main_window.py` on line 200 to `darknet.exe detector test cfg/[your configuration].data cfg/[your configuration].cfg weights/[your weights].weights data/data.jpg -dont_show`

#### Step 3: Run Program
Run `main.py` for YOLO version inference

Run `mainCV.py` for OpenCV version inference 

## NeuralSIGHT Team
* [fahriwps](https://github.com/fahriwps)
* [mariojy10](https://github.com/mariojy10)
