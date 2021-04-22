# Pytorch implementation of SiamFC 

## Declaration
I can't find the original version of this code(maybe the author had deleted it or i am blind).

If anyone find the original version,please give me the link in Issues, thank you!

I have added some code about DEMO ON YOUR OWN VIDEO, see in demo_online_video.py

## How to run SiamseFC on your own video

I have put the weight-file in folder "models", as you can see in  ***'models\siamfc_pretrained.pth'***

If you want to  run SiamseFC on your own video

- First, use **video2folder.py** script to convert your video to the folder with all frames

- Then,  modify the below code in **demo_online_video.py**

- **Put your frame path in video_dir variable**

```
if __name__ == "__main__":
    # Fire(main)
    video_dir = ''
    gpu_id = 0
    model_path = 'models\siamfc_pretrained.pth'
    main(video_dir, gpu_id, model_path)

```


## Reference
[1] Bertinetto, Luca and Valmadre, Jack and Henriques, Joo F and Vedaldi, Andrea and Torr, Philip H S
		Fully-Convolutional Siamese Networks for Object Tracking
		In ECCV 2016 workshops
