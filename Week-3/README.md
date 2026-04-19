
# Week 03 - Semantic Segmentation & Video Stacking

## 📌 Objective

To perform **semantic segmentation** on extracted video frames using YOLOv8 and visualize results by reconstructing videos and stacking outputs for comparison.

---

## 🔹 Semantic Segmentation

* Used YOLOv8 segmentation model: `yolov8n-seg.pt`
* Applied segmentation on all extracted frames
* Generated pixel-wise object masks (colored overlays)
* Output stored in:

```
runs/segment/predict/
```

---

## 🎬 Video Generation

1. **Segmented Video**

```bash
ffmpeg -framerate 30 -i runs/segment/predict/frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p segmented_video.mp4
```

2. **Added Audio**

```bash
ffmpeg -stream_loop -1 -i "C:\Users\Vinod\Downloads\trimmed_audio.mp3" -i segmented_video.mp4 -c:v copy -c:a aac -shortest final_segmented_output.mp4
```

---

## 📊 Performance Metrics (Model Evaluation)

Metrics obtained by training YOLOv8n on the **coco8 dataset**:

* **Precision:** 0.71
* **Recall:** 0.75
* **mAP@0.5:** 0.76
* **mAP@0.5:0.95:** 0.59

📈 Refer to `results.png` for training curves.

> Note: These metrics are derived from training on a sample dataset and not directly from the input video.

---

## 🎥 Stacked Video (Final Output)

The final video combines:

1. Raw video (`videoplayback.mp4`)
2. Object detection output (`detected_video.mp4`)
3. Semantic segmentation output (`final_segmented_output.mp4`)

### 🔧 Stacking Command

```bash
ffmpeg -i videoplayback.mp4 -i detected_video.mp4 -i final_segmented_output.mp4 -filter_complex "vstack=inputs=3" -an stacked_video.mp4
```

### 🔧 Adding Audio

```bash
ffmpeg -stream_loop -1 -i "C:\Users\Vinod\Downloads\trimmed_audio.mp3" -i stacked_video.mp4 -c:v copy -c:a aac -shortest final_stacked_output.mp4
```


---

## 🔍 Observations

* Segmentation provides **pixel-level accuracy** compared to bounding box detection
* Works well for clearly visible objects
* Performance reduces slightly in:

  * Low lighting
  * Motion blur
* Stacked video helps visualize model improvements effectively

---

## 📁 Files (Week-3)

```
Week-3/
 ├── segment.py
 ├── train.py
```

---

## 🚀 Conclusion

Semantic segmentation improves object localization by identifying exact object boundaries. This technique is useful in applications like medical imaging, autonomous driving, and surveillance systems.
