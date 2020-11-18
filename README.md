# Introduction
 This is a simple GUI for YOLO darknet detection.

## Requirements
   - **PyQt5**
   - **YOLO darknet installed**

## How To Use

#### Step 0: Compile YOLO darknet 

Follow AlexeyAB's instruction of [How to compile YOLO darknet on Linux or Windows](https://github.com/AlexeyAB/darknet#how-to-compile-on-linuxmacos-using-cmake)

#### Step 1: Install PyQt5 

Simple installation from PyPI
```bash
pip install PyQt5
```
From Conda
```bash
conda install -c anaconda pyqt
```

#### Step 2: Setup Folder

- Move `main.py`,`main_window.py`, and `splashscreen.py` to your darknet folder. 
- Edit `main_window.py` on line 190 to your darknet data folder directory path.
- If your OS is Windows or you have different name for your own cfg or weights files then edit `main_window.py` on line 200 to `darknet.exe detector test cfg/[your configuration].data cfg/[your configuration].cfg [your weights].weights data/data.jpg -dont_show`

#### Step 3: Run Program
Run `main.py` 

