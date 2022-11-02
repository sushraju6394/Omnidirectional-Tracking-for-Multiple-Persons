[Tracking comparison.docx](https://github.com/sushraju6394/Omnidirectional-Tracking-for-Multiple-Persons/files/9896583/Tracking.update.docx)
# Omnidirectional-Tracking-for-Multiple-Persons
## Overview
Yolo object detection is used to detect humans in the video. Multiple trackers have been implemented on the video but only CSRT tracker performs the best for the TUC(Technische Universität Chemnitz) dataset.
A unique id has been maintained throughout the video for every person. The dataset cannot be made public as it has been recorded at Technische Universität Chemnitz.
Yolo object detection is inspired from [https://github.com/thtrieu/darkflow]. The weights were downloaded from the mentioned link. 
```
git clone https://github.com/thtrieu/darkflow
```
## Dependencies
Python3, tensorflow 1.0, numpy, opencv 3, [https://pjreddie.com/darknet/install/]
## Installation
```
$ pip3 install python3
$ pip3 install tensorflow
$ pip3 install keras 
$ sudo apt update
$ sudo apt install nvidia-cuda-toolkit
$ nvcc --version
```
## Citation
```
@inproceedings{lukezic2017discriminative,
  title={Discriminative correlation filter with channel and spatial reliability},
  author={Lukezic, Alan and Vojir, Tomas and ˇCehovin Zajc, Luka and Matas, Jiri and Kristan, Matej},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={6309--6318},
  year={2017}
}
```
