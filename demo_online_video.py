import glob
import os
import pandas as pd
import argparse
import numpy as np
import cv2
import time
import sys

sys.path.append(os.getcwd())
from tqdm import tqdm
from siamfc import SiamFCTracker

# 一些参数的外部定义
rect = [0, 0, 0, 0]
leftButtonDown = False
leftButtonUp = True


def main(video_dir, gpu_id, model_path):
    # load videos
    # python bin/demo_siamfc.py --model_path models/siamfc_pretrained.pth --gpu-id 0 --video-dir e:/save_data/5.mp4
    filenames = sorted([os.path.join(video_dir, file_name) for file_name in os.listdir(video_dir)],
                       key=lambda x: int(os.path.basename(x).split('.')[0]))
    frames = [
        cv2.resize(cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB),
                   (900, 600)) for filename in filenames
    ]

    title = video_dir.split('/')[-1]
    # starting tracking
    tracker = SiamFCTracker(model_path, gpu_id)
    for idx, frame in enumerate(frames):
        print(idx)
        if idx == 0:
            # 回调函数，鼠标的取点行为
            def draw_bbox(event, x, y, flags, param):
                global rect
                global leftButtonDown
                global leftButtonUp
                # 当按下左键是返回起始位置坐标,cv2.EVENT_LBUTTONDOWN是鼠标左键按下的信号
                if event == cv2.EVENT_LBUTTONDOWN:
                    rect[0] = x
                    rect[2] = x
                    rect[1] = y
                    rect[3] = y
                    leftButtonUp = False
                    leftButtonDown = True

                # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
                elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
                    if leftButtonDown and not leftButtonUp:
                        rect[2] = x
                        rect[3] = y

                elif event == cv2.EVENT_LBUTTONUP:
                    if leftButtonDown and not leftButtonUp:
                        x_min = min(rect[0], rect[2])
                        y_min = min(rect[1], rect[3])

                        x_max = max(rect[0], rect[2])
                        y_max = max(rect[1], rect[3])

                        rect[0] = x_min
                        rect[1] = y_min
                        rect[2] = x_max
                        rect[3] = y_max

                        leftButtonUp = True
                        leftButtonDown = False

            cv2.namedWindow('frame')
            cv2.imshow('frame', frame)
            cv2.setMouseCallback('frame', draw_bbox)
            while cv2.waitKey(1) == -1:
                if not leftButtonUp and leftButtonDown:
                    frame_ = frame.copy()
                    cv2.rectangle(frame_, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
                    cv2.imshow('frame', frame_)
            cv2.destroyAllWindows()

            bbox_xy = rect  # 左上+右下坐标格式
            bbox_wh = (rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])  # 左上，宽高

            # 将第一帧，以及第一帧的bbox作为输入
            tracker.init(frame, bbox_wh)

        else:
            # 除了第一帧外的其他帧，找到该帧上兴趣区域的位置
            bbox_xy = tracker.update(frame)

        # bbox xmin ymin xmax ymax
        frame = cv2.rectangle(
            frame,
            (int(bbox_xy[0]), int(bbox_xy[1])),
            (int(bbox_xy[2]), int(bbox_xy[3])),
            (0, 255, 0),  # green
            2)

        if len(frame.shape) == 3:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.putText(frame, str(idx), (5, 20),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
        cv2.imshow(title, frame)
        cv2.waitKey(30)


if __name__ == "__main__":
    # Fire(main)
    # the abs-path of the generated frame of your video
    video_dir = './frame'
    gpu_id = 0
    model_path = r'models\siamfc_pretrained.pth'
    main(video_dir, gpu_id, model_path)
