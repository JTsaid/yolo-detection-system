# 🚀 快速开始指南

> 给其他开发者的快速上手指南

## 📦 一分钟快速启动

### 1️⃣ 克隆项目
```bash
git clone https://github.com/JTsaid/yolo-detection-system.git
cd yolo-detection-system
```

### 2️⃣ 安装依赖
```bash
# 推荐使用国内镜像源（更快）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 3️⃣ 启动应用
```bash
# Windows 用户
start.bat

# Linux/Mac 用户
chmod +x start.sh
./start.sh

# 或直接运行
python app.py
```

### 4️⃣ 访问应用
打开浏览器访问：http://127.0.0.1:7860

---

## 🎯 三步测试

### 第一步：测试图片检测（5秒）
1. 点击"选择文件"上传一张图片
2. 点击"开始检测"
3. 查看右侧检测结果

### 第二步：测试视频检测（1分钟）
1. 切换到"视频检测"标签
2. 上传一个短视频（10-30秒）
3. 等待处理完成

### 第三步：测试摄像头（实时）
1. 切换到"摄像头检测"标签
2. 点击"启动摄像头"
3. 允许浏览器访问摄像头

---

## 📋 系统要求

- ✅ Python 3.8+
- ✅ 2GB+ 可用内存
- ✅ 现代浏览器（Chrome/Edge/Firefox）
- ⚡ （可选）NVIDIA GPU 用于加速

---

## 🔧 依赖说明

项目会自动安装以下依赖：

| 依赖包 | 用途 | 大小 |
|--------|------|------|
| ultralytics | YOLO11 模型 | ~50MB |
| torch | PyTorch 框架 | ~200MB |
| flask | Web 服务器 | ~2MB |
| opencv-python | 图像处理 | ~50MB |

**首次安装约需 5-10 分钟**（取决于网速）

---

## ⚠️ 常见问题速查

### 问题1：端口被占用
```bash
# 修改 app.py 最后一行的端口号
app.run(host='127.0.0.1', port=8080)  # 改为 8080
```

### 问题2：依赖安装失败
```bash
# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题3：模型下载失败
```bash
# 手动下载模型文件
wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt
# 放到项目根目录
```

### 问题4：摄像头无法访问
- 使用 `http://localhost:7860` 或 `http://127.0.0.1:7860`
- 检查浏览器摄像头权限
- 确保没有其他程序占用摄像头

---

## 🎬 演示视频

运行以下命令下载测试视频：
```bash
# Windows
download_videos.bat

# Linux/Mac
bash download_videos.bat
```

---

## 📚 更多信息

- 📖 完整文档：[README.md](README.md)
- 🎬 演示视频说明：[demo_videos.md](demo_videos.md)
- 🐛 问题反馈：[GitHub Issues](https://github.com/JTsaid/yolo-detection-system/issues)

---

## 💡 提示

- 首次运行会自动下载模型文件（约 6MB）
- 建议先用图片测试，再测试视频
- 视频处理时间约为视频时长的 2-3 倍
- 使用 GPU 可显著提升处理速度

---

**🎉 祝你使用愉快！如有问题欢迎提 Issue！**
