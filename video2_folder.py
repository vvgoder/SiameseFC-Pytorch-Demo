import cv2
import os


if __name__ == '__main__':
    video_path = r'demo.avi'
    frame_path = r'frame'
    current_path = os.getcwd()

    if not os.path.exists(frame_path):
        os.mkdir(frame_path)

    cap = cv2.VideoCapture(video_path)  # 读取地址的mp4文件
    fps = cap.get(5)  # 读取帧率
    print('fps is', fps)  # 帧率
    count = 0

    custom_intervel_and_startend = False
    start_time = 0  # 单位为s
    end_time = 10000

    save_frequency = 1
    while cap.isOpened():
        frame_id = cap.get(1)  # 读取当前帧的次序
        ret, frame = cap.read()  # 读取当前的桢
        if ret is not True:
            break
        if custom_intervel_and_startend:
            if (frame_id >= start_time * fps) & (frame_id <= end_time * fps):  # 以下操作取每秒的桢，并把它存为图片
                filename = '{}.jpg'.format(count)
                count = count + 1
                # print(count)
                if count % save_frequency == 0:
                    save_path = os.path.join(current_path, frame_path)
                    os.chdir(save_path)
                    cv2.imwrite(filename, frame)  # 取出文件名filename的，将其frame存在当前操作目录
        else:
            filename = '{}.jpg'.format(count)
            count = count + 1
            # print(count)
            if count % save_frequency == 0:
                save_path = os.path.join(current_path, frame_path)
                os.chdir(save_path)
                cv2.imwrite(filename, frame)  # 取出文件名filename的，将其frame存在当前操作目录

    cap.release()  # 释放cap
    print('done')
