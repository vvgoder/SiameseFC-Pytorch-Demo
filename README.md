# Pytorch implementation of SiamFC 

## Declaration
I can't find the original version of this code(maybe the author had deleted it or i am blind).
If anyone find the original version,please give me the link in ISSUES,thank you!
I have added some code about DEMO ON YOUR OWN VIDEO,see in demo_online_video.py

## How to run SiamseFC on your own video
I have put the weight-file in folder "models",as you can see in  *'models\siamfc_pretrained.pth'*
if you want to  run SiamseFC on your own video
just modify the below code in **demo_online_video.py**
**Put your video path in video_dir value**

```
if __name__ == "__main__":
    # Fire(main)
    video_dir = ''
    gpu_id = 0
    model_path = 'models\siamfc_pretrained.pth'
    main(video_dir, gpu_id, model_path)

```

```
## Reference
[1] Bertinetto, Luca and Valmadre, Jack and Henriques, Joo F and Vedaldi, Andrea and Torr, Philip H S
		Fully-Convolutional Siamese Networks for Object Tracking
		In ECCV 2016 workshops
