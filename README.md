# 🎯 YOLO目标检测系统

基于YOLO11的智能目标检测Web应用，支持图片、视频和实时摄像头检测。

## ✨ 功能特点

- 📷 **图片检测** - 支持常见图片格式，实时标注检测结果
- 🎬 **视频检测** - 逐帧处理视频，输出完整标注视频
- 📹 **摄像头检测** - 实时调用摄像头进行目标检测
- 🎚️ **参数调节** - 可调整检测置信度阈值
- 📊 **结果展示** - 左右分屏对比，实时显示检测统计
- 🎨 **专业界面** - 简洁专业的深色主题设计

## 🚀 快速开始

### Windows系统

双击运行 `start.bat` 即可启动

### Linux/Mac系统

```bash
bash start.sh
```

### 手动启动

1. **安装依赖**

```bash
pip install -r requirements.txt
```

2. **启动应用**

```bash
python app.py
```

3. **访问应用**

浏览器打开 http://127.0.0.1:7860

## 📖 使用说明

### 图片检测

1. 切换到"图片检测"标签
2. 点击"选择文件"上传图片
3. 调整置信度阈值（可选）
4. 点击"开始检测"
5. 左侧显示原图，右侧显示检测结果

### 视频检测

1. 切换到"视频检测"标签
2. 点击"选择文件"上传视频
3. 调整置信度阈值（可选）
4. 点击"开始检测"
5. 等待处理完成，右侧自动播放检测结果视频

### 摄像头检测

1. 切换到"摄像头检测"标签
2. 点击"启动摄像头"
3. 允许浏览器访问摄像头
4. 实时查看检测结果
5. 点击"停止检测"结束

## 📁 项目结构

```
.
├── app.py              # 主应用程序
├── requirements.txt    # Python依赖
├── yolo11n.pt         # YOLO11模型文件
├── start.bat          # Windows启动脚本
├── start.sh           # Linux/Mac启动脚本
├── download_videos.bat # 演示视频下载脚本
├── demo_videos.md     # 演示视频说明
├── logs/              # 日志目录
├── reports/           # 报告目录
└── README.md          # 项目说明
```

## 🎬 演示视频

项目提供了演示视频下载脚本，运行 `download_videos.bat` 可自动下载测试视频。

详见 `demo_videos.md` 文件。

## 🔧 配置说明

### 修改端口

编辑 `app.py` 最后一行：

```python
app.run(host='127.0.0.1', port=7860, debug=False)  # 修改port参数
```

### 使用其他YOLO模型

编辑 `app.py` 中的模型加载部分：

```python
model = YOLO("yolo11n.pt")  # 可改为 yolo11s.pt, yolo11m.pt 等
```

可用模型：
- `yolo11n.pt` - Nano（最快，精度较低）
- `yolo11s.pt` - Small
- `yolo11m.pt` - Medium
- `yolo11l.pt` - Large
- `yolo11x.pt` - Extra Large（最慢，精度最高）

## 🎓 支持的检测类别

YOLO11可以检测80种常见物体，包括：

- 人、动物（猫、狗、鸟等）
- 交通工具（汽车、自行车、飞机等）
- 日常用品（椅子、桌子、手机等）
- 食物（苹果、香蕉、披萨等）

完整类别列表请参考 [COCO数据集](https://cocodataset.org/#explore)

## 🐛 常见问题

### 1. 端口被占用

修改 `app.py` 中的端口号，或关闭占用7860端口的程序

### 2. 模型下载失败

手动下载模型文件并放在项目根目录：
- [yolo11n.pt 下载地址](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt)

### 3. 摄像头无法访问

- 确保浏览器有摄像头权限
- 使用HTTPS或localhost访问
- 检查是否有其他程序占用摄像头

### 4. 视频处理速度慢

- 使用更小的模型（yolo11n.pt）
- 降低视频分辨率
- 使用GPU加速（需安装CUDA版PyTorch）

### 5. 依赖安装失败

建议使用国内镜像源：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 📝 技术栈

- **深度学习框架**: PyTorch
- **目标检测**: Ultralytics YOLO11
- **Web框架**: Flask
- **图像处理**: OpenCV, Pillow, NumPy
- **前端**: HTML5, CSS3, JavaScript (Canvas API, WebRTC)

## 🎯 性能优化

### 摄像头检测优化

- 使用requestAnimationFrame实现平滑渲染
- Canvas双缓冲技术减少闪烁
- 帧率控制（300ms间隔）平衡性能和流畅度
- 异步处理避免阻塞

### 视频检测优化

- H.264编码提升浏览器兼容性
- 逐帧处理并显示进度
- 自动循环播放便于演示

## 📄 许可证

本项目基于 AGPL-3.0 许可证开源

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📧 联系方式

如有问题或建议，请提交Issue

---

**⭐ 如果这个项目对你有帮助，请给个Star！**
