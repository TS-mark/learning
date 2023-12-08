#!/bin/bash

# 解压压缩包
unzip $1

# 运行 autosave.py 将相同路径下的文件
python3 autosave.py --sourcepath 3 --savepath 4

# 运行 cropvideo.py
python3 cropvideo.py --video_path 4 --save_path 5


cd /home/markzhang/yolov5-7.0

# 运行 detect.py
# python3 detect.py --weights $6 --source 5 --device $8
/usr/bin/python3 /home/markzhang/yolov5-7.0/detect.py \
--source  5 \
--weights /home/markzhang/yolov5-7.0/runs/train/TLD_train65/weights/best.pt \
--device $3 --save-txt

cd /home/markzhang/autodetected

# 运行 coco2json.py
python coco2json.py --labelpath 9 --savepath 10

# 打包结果
zip -r result.zip 10
