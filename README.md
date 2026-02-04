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

### 前置要求

- Python 3.8 或更高版本
- pip 包管理器
- （可选）CUDA 支持的 GPU（用于加速）

### 方法一：一键启动（推荐）

#### Windows 系统
```bash
# 双击运行
start.bat
```

#### Linux/Mac 系统
```bash
# 添加执行权限（首次运行）
chmod +x start.sh

# 启动应用
./start.sh
```

### 方法二：手动启动

#### 1. 克隆项目
```bash
git clone https://github.com/JTsaid/yolo-detection-system.git
cd yolo-detection-system
```

#### 2. 创建虚拟环境（推荐）
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. 安装依赖
```bash
# 使用国内镜像源（推荐，速度更快）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用默认源
pip install -r requirements.txt
```

**依赖说明**：
- `ultralytics` - YOLO11 模型库
- `flask` - Web 框架
- `torch` & `torchvision` - PyTorch 深度学习框架
- `opencv-python` - 图像处理
- `pillow` - 图像读取
- `numpy` - 数值计算

#### 4. 下载模型文件（自动）

首次运行时，程序会自动下载 `yolo11n.pt` 模型文件（约 6MB）。

如果自动下载失败，可手动下载：
```bash
# 方法1：使用 wget
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt

# 方法2：使用 curl
curl -L -o yolo11n.pt https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt
```

将下载的 `yolo11n.pt` 文件放在项目根目录。

#### 5. 启动应用
```bash
python app.py
```

#### 6. 访问应用

启动成功后，在浏览器中打开：
```
http://127.0.0.1:7860
```

你会看到类似以下的启动信息：
```
============================================================
YOLO目标检测系统启动
访问地址: http://127.0.0.1:7860
============================================================
```

### 🎬 下载演示视频（可选）

运行以下脚本下载测试视频：

```bash
# Windows
download_videos.bat

# Linux/Mac
bash download_videos.bat
```

演示视频会保存在 `demo_videos/` 目录中。

## 📖 使用说明

### 快速测试

**首次使用建议流程**：

1. **测试图片检测**（最快，5秒出结果）
   - 切换到"图片检测"标签
   - 上传一张包含人、车辆或动物的图片
   - 点击"开始检测"
   - 查看右侧标注结果

2. **测试视频检测**（需要1-2分钟）
   - 切换到"视频检测"标签
   - 上传一个短视频（建议10-30秒）
   - 等待处理完成
   - 播放查看标注视频

3. **测试摄像头检测**（实时）
   - 切换到"摄像头检测"标签
   - 点击"启动摄像头"
   - 允许浏览器访问摄像头
   - 实时查看检测效果

### 图片检测

1. 切换到"图片检测"标签
2. 点击"选择文件"上传图片（支持 JPG、PNG、BMP 等格式）
3. 调整置信度阈值（可选，默认 0.25）
   - 值越高，检测越严格，误报越少
   - 值越低，检测越宽松，可能漏检
4. 点击"开始检测"
5. 左侧显示原图，右侧显示检测结果
6. 查看底部统计信息（检测到的物体及置信度）

**推荐测试图片**：
- 街道场景（检测车辆、行人）
- 室内场景（检测家具、电子设备）
- 动物照片（检测猫、狗等宠物）

### 视频检测

1. 切换到"视频检测"标签
2. 点击"选择文件"上传视频（支持 MP4、AVI、MOV 等格式）
3. 调整置信度阈值（可选）
4. 点击"开始检测"
5. 等待处理完成（处理时间取决于视频长度）
   - 10秒视频约需 30-60 秒
   - 30秒视频约需 1-2 分钟
6. 右侧自动播放检测结果视频
7. 查看底部统计信息（总帧数、检测统计）

**视频处理提示**：
- 建议使用 10-60 秒的短视频测试
- 视频分辨率建议 720p 或 1080p
- 文件大小建议 < 50MB

### 摄像头检测

1. 切换到"摄像头检测"标签
2. 点击"启动摄像头"
3. 允许浏览器访问摄像头（首次使用会弹出权限请求）
4. 左侧显示摄像头画面，右侧实时显示检测结果
5. 调整置信度阈值可实时改变检测灵敏度
6. 点击"停止检测"结束

**摄像头检测特点**：
- ⚡ 实时检测，300ms 响应速度
- 🎯 自动追踪移动物体
- 📊 实时更新检测统计
- 🎨 流畅渲染，无闪烁

**最佳实践**：
- 确保光线充足
- 保持摄像头稳定
- 物体距离适中（1-5米）
- 避免背景过于复杂

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

**错误信息**：`Address already in use` 或 `端口 7860 已被占用`

**解决方法**：
```bash
# 方法1：修改端口
# 编辑 app.py 最后一行，将 7860 改为其他端口（如 8080）
app.run(host='127.0.0.1', port=8080, debug=False)

# 方法2：关闭占用端口的程序
# Windows
netstat -ano | findstr :7860
taskkill /PID <进程ID> /F

# Linux/Mac
lsof -i :7860
kill -9 <进程ID>
```

### 2. 模型下载失败

**错误信息**：`Failed to download yolo11n.pt`

**解决方法**：
```bash
# 手动下载模型文件
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt

# 或使用浏览器下载后放到项目根目录
```

**备用下载地址**：
- [GitHub Release](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt)
- [百度网盘](https://pan.baidu.com) - 搜索 "yolo11n.pt"

### 3. 依赖安装失败

**错误信息**：`pip install` 超时或失败

**解决方法**：
```bash
# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用阿里云镜像
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 如果 torch 安装失败，单独安装 CPU 版本
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### 4. 摄像头无法访问

**错误信息**：`无法访问摄像头` 或 `Permission denied`

**解决方法**：
- ✅ 确保浏览器有摄像头权限（浏览器设置 → 隐私 → 摄像头）
- ✅ 使用 `http://localhost:7860` 或 `http://127.0.0.1:7860` 访问
- ✅ 检查是否有其他程序占用摄像头（如 Zoom、Teams）
- ✅ 尝试使用 Chrome 或 Edge 浏览器

### 5. 视频处理速度慢

**现象**：视频检测需要很长时间

**优化方法**：
```python
# 方法1：使用更小的模型（编辑 app.py）
model = YOLO("yolo11n.pt")  # 最快（当前使用）
# model = YOLO("yolo11s.pt")  # 较快
# model = YOLO("yolo11m.pt")  # 中等

# 方法2：降低视频分辨率
# 在上传前使用视频编辑工具将分辨率降至 720p

# 方法3：使用 GPU 加速（需要 NVIDIA GPU）
# 安装 CUDA 版本的 PyTorch
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### 6. 内存不足

**错误信息**：`Out of memory` 或 `MemoryError`

**解决方法**：
- 使用更小的模型（yolo11n.pt）
- 减小输入图片/视频的分辨率
- 关闭其他占用内存的程序
- 增加系统虚拟内存

### 7. Python 版本不兼容

**错误信息**：`SyntaxError` 或版本相关错误

**解决方法**：
```bash
# 检查 Python 版本（需要 3.8+）
python --version

# 如果版本过低，安装新版本
# Windows: 从 python.org 下载安装
# Linux: sudo apt install python3.10
# Mac: brew install python@3.10
```

### 8. 检测结果不准确

**优化建议**：
- 📊 调整置信度阈值（默认 0.25，可调至 0.3-0.5）
- 🎯 使用更大的模型（yolo11m.pt 或 yolo11l.pt）
- 💡 确保图片/视频光线充足、清晰度高
- 🔍 对于小目标，使用更高分辨率的输入

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
