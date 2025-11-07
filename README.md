# Awesome NCNN Collection

A curated collection of high-quality NCNN resources, projects, and implementations for mobile and edge AI deployment. Updated for 2025 with the latest trending projects and optimization techniques.

## Table of Contents
- [Official NCNN Resources](#official-ncnn-resources)
- [Latest YOLO Implementations (2024-2025)](#latest-yolo-implementations-2024-2025)
- [Object Detection](#object-detection)
- [Image Classification](#image-classification)
- [Image Segmentation](#image-segmentation)
- [Super Resolution & Image Enhancement](#super-resolution--image-enhancement)
- [Face & Biometrics](#face--biometrics)
- [Pose Estimation & Human Tracking](#pose-estimation--human-tracking)
- [Speech Recognition & ASR](#speech-recognition--asr)
- [OCR & Text Recognition](#ocr--text-recognition)
- [Video Processing](#video-processing)
- [Stable Diffusion & Generative Models](#stable-diffusion--generative-models)
- [Model Collections & Zoo](#model-collections--zoo)
- [Platform-Specific Deployment](#platform-specific-deployment)
- [Optimization & Quantization](#optimization--quantization)
- [Tools & Utilities](#tools--utilities)
- [Tutorials & Documentation](#tutorials--documentation)
- [Benchmarks & Performance](#benchmarks--performance)

---

## Official NCNN Resources

### Core Framework
- [Tencent/ncnn](https://github.com/Tencent/ncnn) - Official high-performance neural network inference framework optimized for mobile platforms (22k+ stars)
- [NCNN Official Documentation](https://ncnn.readthedocs.io/en/latest/) - Comprehensive documentation with tutorials and API reference
- [NCNN DocsForge](https://ncnn.docsforge.com/) - Alternative documentation portal
- [NCNN Vulkan FAQ](https://github.com/Tencent/ncnn/wiki/FAQ-ncnn-vulkan) - Vulkan acceleration guide and troubleshooting
- [NCNN Official Benchmarks](https://github.com/Tencent/ncnn/tree/master/benchmark) - Performance benchmarks for various models

### Python Integration
- [NCNN Python Wrapper](https://github.com/Tencent/ncnn/tree/master/python) - Official Python bindings for NCNN

---

## Latest YOLO Implementations (2024-2025)

### YOLOv11 (Latest - 2024)
- [Ultralytics YOLO11 NCNN Export Guide](https://docs.ultralytics.com/integrations/ncnn/) - Official guide for exporting YOLO11 to NCNN format
- [zhouweigogogo/yolo11-ncnn](https://github.com/zhouweigogogo/yolo11-ncnn) - C++ implementation with YOLO11n running at ~48ms
- [taiji1985/yolo11-ncnn](https://github.com/taiji1985/yolo11-ncnn) - NCNN YOLO11 without magic operations
- [gaoxumustwin/ncnn-android-yolov11](https://github.com/gaoxumustwin/ncnn-android-yolov11) - YOLO11 NCNN Android optimization deployment
- [Abandon-ht/ncnn-android-yolo11](https://github.com/Abandon-ht/ncnn-android-yolo11) - Real-time YOLO11 Android demo
- [mlim97/yolo_ros](https://github.com/mlim97/yolo_ros) - YOLOv8/v9/v10/v11 for ROS 2 with NCNN

### YOLOv10 & YOLOv9 (2024)
- [Ultralytics YOLO Comparison](https://www.ultralytics.com/blog/comparing-ultralytics-yolo11-vs-previous-yolo-models) - Performance comparison of YOLO versions

### YOLOv8 & Earlier Versions
- [FeiGeChuanShu/ncnn-android-yolov8](https://github.com/FeiGeChuanShu/ncnn-android-yolov8) - YOLOv8 Android implementation
- [FeiGeChuanShu/ncnn-android-yolov6](https://github.com/FeiGeChuanShu/ncnn-android-yolov6) - YOLOv6 Android implementation
- [FeiGeChuanShu/yolov5-seg-ncnn](https://github.com/FeiGeChuanShu/yolov5-seg-ncnn) - YOLOv5 segmentation with NCNN
- [DataXujing/ncnn_android_yolov6](https://github.com/DataXujing/ncnn_android_yolov6) - YOLOv6 NCNN Android with conversion guide
- [cmdbug/YOLOv5_NCNN](https://github.com/cmdbug/YOLOv5_NCNN) - YOLOv5 deployment on Android and iOS
- [triple-Mu/YOLOv8-TensorRT](https://github.com/triple-Mu/YOLOv8-TensorRT) - YOLOv8 with TensorRT (comparison framework)

### Other YOLO Variants
- [meituan/YOLOv6](https://github.com/meituan/YOLOv6) - Official YOLOv6 by Meituan
- [tinyvision/DAMO-YOLO](https://github.com/tinyvision/DAMO-YOLO) - DAMO-YOLO for industrial applications
- [jizhishutong/YOLOU](https://github.com/jizhishutong/YOLOU) - YOLO-Universal

---

## Object Detection

### NanoDet (Lightweight Detection)
- [RangiLyu/nanodet](https://github.com/RangiLyu/nanodet) - Super fast and lightweight anchor-free object detection model
- [nihui/ncnn-android-nanodet](https://github.com/nihui/ncnn-android-nanodet) - Official NCNN Android NanoDet demo

### BlazeFace
- [FeiGeChuanShu/ncnn_Android_blazeface](https://github.com/FeiGeChuanShu/ncnn_Android_blazeface) - BlazeFace for face detection on Android

### General Detection
- [DefTruth/lite.ai.toolkit](https://github.com/DefTruth/lite.ai.toolkit) - Comprehensive lite AI toolkit with NCNN support
- [WongKinYiu/yolor](https://github.com/wkt/YoloMobile) - YOLO Mobile implementation

---

## Image Classification

- [nihui/ncnn-android-squeezenet](https://github.com/nihui/ncnn-android-squeezenet) - SqueezeNet image classification demo
- [Revo-Future/ncnn_mobileNet](https://github.com/Revo-Future/ncnn_mobileNet) - MobileNet implementation
- [linguanghan/ncnn_mobilenetv2_andriod](https://github.com/linguanghan/ncnn_mobilenetv2_andriod) - MobileNetV2 for Android

---

## Image Segmentation

### Portrait & Semantic Segmentation
- [leeys888/ncnn-portrait-segmentation](https://github.com/leeys888/ncnn-portrait-segmentation) - Portrait segmentation
- [FeiGeChuanShu/ncnn_Android_RobustVideoMatting](https://github.com/FeiGeChuanShu/ncnn_Android_RobustVideoMatting) - Real-time human video matting on Android
- [slz929/SAM-Android-ncnn](https://github.com/slz929/SAM-Android-ncnn) - Segment Anything Model (SAM) on Android with NCNN
- [xuduo35/unet_mxnet2ncnn](https://github.com/xuduo35/unet_mxnet2ncnn) - U-Net implementation
- [CoinCheung/BiSeNet](https://github.com/CoinCheung/BiSeNet/blob/master/ncnn/segment.cpp) - BiSeNet segmentation

---

## Super Resolution & Image Enhancement

### Real-ESRGAN & Waifu2x
- [xinntao/Real-ESRGAN-ncnn-vulkan](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan) - Real-ESRGAN with NCNN and Vulkan acceleration
- [tumuyan/RealSR-NCNN-Android](https://github.com/tumuyan/RealSR-NCNN-Android) - Comprehensive Android app with RealSR, SRMD, RealCUGAN, Real-ESRGAN, Waifu2x, Anime4k
- [AaronFeng753/Waifu2x-Extension-GUI](https://github.com/AaronFeng753/Waifu2x-Extension-GUI) - GUI for video/image upscaling with multiple SR models
- [nagadomi/waifu2x](https://github.com/nagadomi/waifu2x) - Original Waifu2x for anime-style art
- [nihui/srmd-ncnn-vulkan](https://github.com/nihui/srmd-ncnn-vulkan) - SRMD super resolution

### Other Enhancement
- [jixiaozhong/RealSR](https://github.com/jixiaozhong/RealSR) - Real-world super resolution
- [JuZiSYJ/ncnn-picture-enhancement](https://github.com/JuZiSYJ/ncnn-picture-enhancement) - General picture enhancement
- [FeiGeChuanShu/GFPGAN-ncnn](https://github.com/FeiGeChuanShu/GFPGAN-ncnn) - GFPGAN face restoration with NCNN

---

## Face & Biometrics

### Face Detection & Recognition
- [Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB) - Ultra-lightweight 1MB face detector
- [polarisZhao/PFLD-pytorch](https://github.com/polarisZhao/PFLD-pytorch) - PFLD facial landmark detection

### Other Biometrics
- [digital-nomad-cheng/Iris_Landmarks_PyTorch](https://github.com/digital-nomad-cheng/Iris_Landmarks_PyTorch) - Iris landmark detection

---

## Pose Estimation & Human Tracking

### RTMPose & Pose Estimation
- **RTMPose with NCNN** - RTMPose models deployed and tested on Snapdragon 865 using NCNN for efficient mobile inference
- **YOLOv8-pose** - Enhanced real-time human pose estimation based on modified YOLOv8 framework
- **MoveNet, PoseNet, BlazePose** - Popular models compatible with mobile/edge deployment

### Resources
- [Best Human Pose Estimation Models 2024](https://www.posetracker.com/news/best-human-pose-estimation-models-for-mobile-app-in-2024) - Comprehensive comparison of mobile pose estimation models

---

## Speech Recognition & ASR

### Sherpa-NCNN
- [k2-fsa/sherpa-ncnn](https://github.com/k2-fsa/sherpa-ncnn) - Real-time speech recognition and VAD using next-gen Kaldi with NCNN
- [Sherpa-NCNN Documentation](https://k2-fsa.github.io/sherpa/ncnn/) - Complete documentation and pre-trained models
- Supports: iOS, Android, Linux, macOS, Windows, Raspberry Pi, VisionFive2, LicheePi4A
- Multilingual support: Chinese, English, Japanese, Korean, Cantonese

---

## OCR & Text Recognition

### Lightweight OCR
- **chineseocr_lite** - Super lightweight OCR for Chinese characters with NCNN inference support
- [sunsean21/ncnn_ocr-master](https://github.com/sunsean21/ncnn_ocr-master) - NCNN OCR profiling tool
- **ncnn-webassembly-ocrlite** - OCR deployment in web browsers using NCNN and WebAssembly

### Resources
- [10 Awesome OCR Models for 2025](https://www.kdnuggets.com/10-awesome-ocr-models-for-2025) - Latest OCR model comparison

---

## Video Processing

### Frame Interpolation & Optical Flow
- **RIFE-ncnn-vulkan** - Real-Time Intermediate Flow Estimation for video frame interpolation
- [hzwer/ECCV2022-RIFE](https://github.com/hzwer/ECCV2022-RIFE) - RIFE for video frame interpolation

---

## Stable Diffusion & Generative Models

### Stable Diffusion
- [EdVince/Stable-Diffusion-NCNN](https://github.com/EdVince/Stable-Diffusion-NCNN) - Stable Diffusion in NCNN with C++, supports txt2img and img2img
- [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) - Popular Stable Diffusion WebUI (reference)

---

## Model Collections & Zoo

### Curated Model Collections
- [Baiyuetribe/ncnn-models](https://github.com/Baiyuetribe/ncnn-models) - Awesome AI models with NCNN and conversion guides
- [nilseuropa/ncnn_models](https://github.com/nilseuropa/ncnn_models) - Collection of NCNN models
- [nihui/ncnn-assets](https://github.com/nihui/ncnn-assets/tree/master/models) - Official NCNN model assets
- [zchrissirhcz/awesome-ncnn](https://github.com/zchrissirhcz/awesome-ncnn) - Comprehensive awesome-ncnn collection

---

## Platform-Specific Deployment

### Android
- [NCNN Android Deployment Guide](https://medium.com/@freshtechyy/deployment-of-pytorch-model-using-ncnn-for-mobile-devices-part-2-ff28e9aaf0d6) - Complete PyTorch to NCNN Android deployment tutorial
- [dangbo/ncnn-mobile](https://github.com/dangbo/ncnn-mobile) - NCNN usage in Android and iOS

### iOS
- [anuragajwani/consume-c-in-swift](https://anuragajwani.medium.com/how-to-consume-c-code-in-swift-b4d64a04e989) - Using C++ (NCNN) in Swift
- [zhuzilin/ncnn-swift](https://github.com/zhuzilin/ncnn-swift) - NCNN Swift wrapper

### WebAssembly
- [nihui/ncnn-webassembly-portrait-segmentation](https://github.com/nihui/ncnn-webassembly-portrait-segmentation) - NCNN WebAssembly demo

### OpenCV Integration
- [nihui/opencv-mobile](https://github.com/nihui/opencv-mobile) - Minimal OpenCV for mobile deployment with NCNN

---

## Optimization & Quantization

### INT8 Quantization
- [NCNN Quantized INT8 Inference Guide](https://github.com/Tencent/ncnn/blob/master/docs/how-to-use-and-FAQ/quantized-int8-inference.md) - Official post-training quantization guide
- [BUG1989/caffe-int8-convert-tools](https://github.com/BUG1989/caffe-int8-convert-tools) - Caffe INT8 conversion tools
- [ChenShisen/ncnnqat](https://github.com/ChenShisen/ncnnqat) - NCNN quantization-aware training

### Optimization Resources
- [Understanding NCNN Machine Vision Systems 2025](https://www.unitxlabs.com/resources/ncnn-machine-vision-system-2025/) - Latest optimization techniques
- [NCNN Vulkan Optimization Notes](https://github.com/Tencent/ncnn/wiki/vulkan-notes) - Vulkan-specific optimizations

---

## Tools & Utilities

### Model Conversion & Editing
- [daquexian/onnx-simplifier](https://github.com/daquexian/onnx-simplifier) - ONNX model simplification tool
- [convertmodel.com](https://convertmodel.com/) - Online model conversion platform
- [scarsty/ncnn-editor](https://github.com/scarsty/ncnn-editor) - Visual NCNN model editor
- [nihui/ncnn-small-board](https://github.com/nihui/ncnn-small-board) - NCNN model visualization tool

### Inference Helpers
- [iwatake2222/InferenceHelper](https://github.com/iwatake2222/InferenceHelper) - Unified inference interface for multiple frameworks
- [iwatake2222/InferenceHelper_Sample](https://github.com/iwatake2222/InferenceHelper_Sample) - InferenceHelper sample projects

### CMake Examples
- [zchrissirhcz/cmake_examples](https://github.com/zchrissirhcz/cmake_examples) - CMake examples for NCNN integration

---

## Tutorials & Documentation

### Official Documentation
- [NCNN Wiki](https://github.com/Tencent/ncnn/wiki) - Official wiki with comprehensive guides
- [NCNN How to Build](https://github.com/Tencent/ncnn/wiki/how-to-build) - Building NCNN for different platforms

### Chinese Language Resources
- [Zhengtq/ncnn_breakdown](https://github.com/Zhengtq/ncnn_breakdown) - NCNN source code analysis (Chinese)
- [NCNN Understanding (Zhihu)](https://www.zhihu.com/column/c_1320446932913762304) - NCNN technical articles
- [NCNN Analysis Blog](https://blog.csdn.net/just_sort/article/details/111403398) - Detailed NCNN analysis
- [NCNN Deep Dive](https://blog.csdn.net/sinat_31425585/category_9312419.html) - Comprehensive NCNN series

### English Tutorials
- [PyTorch to NCNN Deployment Part 1](https://medium.com/@freshtechyy/deployment-of-pytorch-model-using-ncnn-bceff5d846b0) - Model conversion guide
- [PyTorch to NCNN Deployment Part 2](https://medium.com/@freshtechyy/deployment-of-pytorch-model-using-ncnn-for-mobile-devices-part-2-ff28e9aaf0d6) - Mobile deployment tutorial
- [PyTorch vs ONNX vs NCNN](https://medium.com/@nadirapovey/pytorch-vs-onnx-vs-ncnn-ee50115b6263) - Framework comparison
- [NCNN Getting Started](https://www.deepchecks.com/llm-tools/ncnn/) - Features and getting started guide

---

## Benchmarks & Performance

### Official Benchmarks
- [NCNN Official Benchmarks](https://github.com/Tencent/ncnn/blob/master/benchmark/README.md) - Comprehensive benchmark results
- [NCNN OpenBenchmarking](https://openbenchmarking.org/test/pts/ncnn) - Public benchmark database
- **Latest Results (Dec 2024)**: 58.54% lower latency vs GPU for matrix-vector multiplication, 3.2× faster LLM inference, 2× higher throughput than NPUs

### Framework Comparisons
- [embedded-ai.bench](https://github.com/AI-performance/embedded-ai.bench) - NCNN vs TNN vs MNN vs TFLite benchmarks
- [Xiaomi Mobile AI Bench](https://github.com/XiaoMi/mobile-ai-bench) - Benchmarking neural network inference on mobile devices
- [NCNN vs TensorRT Comparison](https://medium.com/@reza_mahmoudi/the-difference-between-ncnn-and-tensorrt-9e869390fe00) - Detailed comparison

---

## Research Papers & Articles (2024-2025)

### YOLO Comparisons
- [YOLOv8/v9/v10/v11 Performance Comparison](https://www.mdpi.com/2076-3417/15/6/3154) - Comprehensive evaluation
- [YOLOv11 Architectural Enhancements](https://arxiv.org/html/2410.17725v1) - Key improvements overview
- [A Comparative Analysis for Smoke/Fire Detection](https://www.mdpi.com/2571-6255/8/1/26) - YOLOv9/v10/v11 comparison

### Mobile AI Trends
- [NCNN Machine Vision 2025](https://www.unitxlabs.com/resources/ncnn-machine-vision-system-2025/) - Latest trends and techniques
- [Review of Post-Transformer Architectures 2024](https://www.latent.space/p/2024-post-transformers) - State Space Models, RWKV

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest high-quality NCNN resources.

## License

This collection is provided as-is for educational and reference purposes.

## Last Updated

**January 2025** - Continuously updated with the latest NCNN projects and resources.
