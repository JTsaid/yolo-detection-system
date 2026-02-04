# 🎯 YOLO 智能目标检测系统

> 基于 YOLO11 深度学习模型的通用目标检测 Web 应用
> 
> **可检测 80 种常见物体**：人、车辆、动物、日常用品、食物等
> 
> 支持图片、视频、实时摄像头三种检测模式

---

## 📋 项目简介

这是一个基于最新 YOLO11 模型的智能目标检测系统，可以识别图片和视频中的多种物体（人、车辆、动物、日常用品等共80类）。系统提供了友好的 Web 界面，支持：

- **图片检测**：上传图片，快速标注所有检测到的物体
- **视频检测**：处理视频文件，输出完整标注的视频
- **摄像头检测**：实时调用摄像头进行目标检测和追踪

**应用场景**：
- 🚗 交通监控：车辆、行人检测与统计
- 🏭 工业质检：产品缺陷检测、物料识别
- 🏪 零售分析：客流统计、商品识别
- 🔒 安防监控：异常行为检测、入侵报警
- 📊 数据分析：视频内容自动标注与分析

## 📊 系统特点

### 🎯 核心功能
- ✅ **多模式检测**：支持图片、视频、实时摄像头三种输入方式
- ✅ **高精度识别**：基于 YOLO11 最新模型，识别准确率高
- ✅ **实时处理**：摄像头模式下可实时检测（300ms 响应）
- ✅ **参数可调**：支持调整置信度阈值，平衡速度与精度
- ✅ **结果可视化**：自动标注边界框和类别标签
- ✅ **统计分析**：自动统计检测结果，生成详细报告

### 🎨 界面设计
- 📱 **响应式布局**：适配各种屏幕尺寸
- 🎭 **专业主题**：深色主题，减少视觉疲劳
- 📊 **左右分屏**：原图与检测结果对比展示
- ⚡ **流畅体验**：Canvas 双缓冲技术，画面流畅无闪烁

### ⚙️ 技术优势
- 🚀 **性能优化**：异步处理、帧率控制、智能缓存
- 🔧 **易于部署**：一键启动脚本，无需复杂配置
- 📦 **轻量级**：使用 YOLO11n 模型，体积小速度快
- 🔌 **可扩展**：支持更换更大模型以提升精度

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

## 🎓 支持的检测类别（80种）

YOLO11 基于 COCO 数据集训练，可以检测以下类别：

### 👥 人物类（1种）
- person（人）

### 🚗 交通工具类（8种）
- bicycle（自行车）、car（汽车）、motorcycle（摩托车）、airplane（飞机）
- bus（公交车）、train（火车）、truck（卡车）、boat（船）

### 🐾 动物类（10种）
- bird（鸟）、cat（猫）、dog（狗）、horse（马）、sheep（羊）
- cow（牛）、elephant（大象）、bear（熊）、zebra（斑马）、giraffe（长颈鹿）

### 🪑 家具类（6种）
- chair（椅子）、couch（沙发）、bed（床）、dining table（餐桌）
- toilet（马桶）、potted plant（盆栽）

### 📱 电子设备类（6种）
- tv（电视）、laptop（笔记本电脑）、mouse（鼠标）、remote（遥控器）
- keyboard（键盘）、cell phone（手机）

### 🍎 食物类（11种）
- apple（苹果）、banana（香蕉）、orange（橙子）、sandwich（三明治）
- pizza（披萨）、donut（甜甜圈）、cake（蛋糕）、hot dog（热狗）
- broccoli（西兰花）、carrot（胡萝卜）、wine glass（酒杯）

### 🎾 运动用品类（10种）
- frisbee（飞盘）、skis（滑雪板）、snowboard（滑雪板）、sports ball（球）
- kite（风筝）、baseball bat（棒球棒）、baseball glove（棒球手套）
- skateboard（滑板）、surfboard（冲浪板）、tennis racket（网球拍）

### 🧳 日常用品类（28种）
- backpack（背包）、umbrella（雨伞）、handbag（手提包）、tie（领带）
- suitcase（行李箱）、bottle（瓶子）、cup（杯子）、fork（叉子）
- knife（刀）、spoon（勺子）、bowl（碗）、book（书）
- clock（时钟）、vase（花瓶）、scissors（剪刀）、teddy bear（泰迪熊）
- hair drier（吹风机）、toothbrush（牙刷）等

完整类别列表请参考 [COCO数据集官网](https://cocodataset.org/#explore)

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
