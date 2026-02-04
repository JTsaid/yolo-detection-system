# 🎬 演示视频下载链接

## 推荐演示视频

### 1. 交通场景视频（推荐）
**适合展示**: 车辆、行人、交通标志检测

```bash
# 下载命令
curl -L -o traffic.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/car-detection.mp4"
```

**直接下载链接**:
- https://github.com/intel-iot-devkit/sample-videos/raw/master/car-detection.mp4

---

### 2. 人员检测视频
**适合展示**: 人员追踪、行为分析

```bash
# 下载命令
curl -L -o people.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4"
```

**直接下载链接**:
- https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4

---

### 3. 监控场景视频
**适合展示**: 工业场景、物体检测

```bash
# 下载命令
curl -L -o monitoring.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/bolt-detection.mp4"
```

**直接下载链接**:
- https://github.com/intel-iot-devkit/sample-videos/raw/master/bolt-detection.mp4

---

### 4. 行人检测视频
**适合展示**: 密集人群检测

```bash
# 下载命令
curl -L -o pedestrian.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4"
```

**直接下载链接**:
- https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4

---

### 5. 商场场景视频
**适合展示**: 多目标追踪

```bash
# 下载命令
curl -L -o mall.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/face-demographics-walking.mp4"
```

**直接下载链接**:
- https://github.com/intel-iot-devkit/sample-videos/raw/master/face-demographics-walking.mp4

---

## 其他优质视频源

### Pexels（免费高质量视频）
- 网站: https://www.pexels.com/videos/
- 搜索关键词: traffic, people, street, city, cars

### Pixabay（免费视频）
- 网站: https://pixabay.com/videos/
- 搜索关键词: traffic, pedestrian, urban, vehicles

---

## 快速下载所有演示视频

### Windows (PowerShell)
```powershell
# 创建demo_videos目录
New-Item -ItemType Directory -Force -Path demo_videos

# 下载视频
Invoke-WebRequest -Uri "https://github.com/intel-iot-devkit/sample-videos/raw/master/car-detection.mp4" -OutFile "demo_videos/traffic.mp4"
Invoke-WebRequest -Uri "https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4" -OutFile "demo_videos/people.mp4"
Invoke-WebRequest -Uri "https://github.com/intel-iot-devkit/sample-videos/raw/master/bolt-detection.mp4" -OutFile "demo_videos/monitoring.mp4"
```

### Linux/Mac
```bash
# 创建demo_videos目录
mkdir -p demo_videos

# 下载视频
curl -L -o demo_videos/traffic.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/car-detection.mp4"
curl -L -o demo_videos/people.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4"
curl -L -o demo_videos/monitoring.mp4 "https://github.com/intel-iot-devkit/sample-videos/raw/master/bolt-detection.mp4"
```

---

## 使用建议

### 年底汇报演示顺序

1. **traffic.mp4** (30秒)
   - 展示车辆检测能力
   - 说明: "系统可以实时识别道路上的车辆、行人等目标"

2. **people.mp4** (20秒)
   - 展示人员追踪
   - 说明: "可以应用于人流统计、安全监控等场景"

3. **monitoring.mp4** (15秒)
   - 展示工业场景
   - 说明: "支持工业生产线的质量检测和监控"

### 演示技巧

- 先用图片快速展示检测效果（5秒出结果）
- 再用短视频展示实时处理能力（选择10-30秒的片段）
- 调整置信度阈值展示参数调优效果
- 强调检测速度和准确率

---

## 视频规格建议

- **分辨率**: 720p 或 1080p
- **时长**: 10-60秒（演示用）
- **格式**: MP4（兼容性最好）
- **大小**: < 50MB（处理速度快）

---

## 注意事项

1. 视频文件较大，下载可能需要几分钟
2. 建议使用有线网络下载
3. 如果GitHub下载慢，可以使用镜像站点
4. 演示前先测试一遍，确保流畅

---

**提示**: 这些视频都是开源免费的，可以放心使用！
