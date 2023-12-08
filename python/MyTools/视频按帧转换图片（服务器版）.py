# 这段代码使用场景：路采的视频需要按帧保存成视频以待标注，
# 设定视频文件，设定开始时间，设定结束时间，设定间隔多少秒后，可以运行截帧

# 导入所需要的库
import cv2
import numpy as np
import os
import argparse
 
# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, file_name):
        # print("save path", address)
        address = os.path.join(addr, file_name + '.jpg')
        print("save path", address)
        cv2.imwrite(address, image)
 
# 功能：将视频以秒为单位，start_time开始，end_time结束，gap为间隔秒数->可以为小数，抽取图像帧
# start_time,end_time允许为"5:30"这种形式
def videoCrop2image(video_path,save_path,start_time,end_time,gap):
    # 读取视频文件 视频文件路径
    videoCapture = cv2.VideoCapture(video_path)

    fps = videoCapture.get(cv2.CAP_PROP_FPS)  # 获得视频文件的帧率

    if isinstance(start_time,str):
        start_time = int(start_time.split(":")[0])*60 + int(start_time.split(":")[1])
    if isinstance(end_time,str):
        end_time = int(end_time.split(":")[0])*60 + int(end_time.split(":")[1])

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 读帧
    videoCapture.set(cv2.CAP_PROP_POS_FRAMES, start_time * fps)
    pos = videoCapture.get(cv2.CAP_PROP_POS_FRAMES)  # 获得帧位置
    success, frame = videoCapture.read()
    
    i = 0
    timeF = int(gap * fps) # 间隔多少帧保存
    j = 0
    total = 0
    while pos < end_time * fps:
        i = i + 1
        if (i % timeF == 0):
            j = j + 1
            save_image(frame, save_path, os.path.basename(video_path).replace(".mp4","_" + str(start_time)+"_"+str(j))) #视频截成图片存放的位置
            total += 1
        
        pos = videoCapture.get(cv2.CAP_PROP_POS_FRAMES)
        success, frame = videoCapture.read()

    print("saved", total)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='对视频按帧截取图片')
    parser.add_argument('-save_path', type=str, help='第一个参数的说明')
    parser.add_argument('-video_path', type=str, help='第二个参数需要加-param2')
    parser.add_argument('-start_time',type = str)
    parser.add_argument('-end_time', type = str)
    parser.add_argument('-gap', type = float, default = 0.4)    

    # 解析命令行参数
    args = parser.parse_args()

    # 访问解析后的参数值
    save_path = args.save_path
    video_path = args.video_path
    start_time = args.start_time
    end_time = args.end_time
    gap = args.gap

    videoCrop2image(video_path,save_path,start_time,end_time,gap)