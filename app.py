"""
YOLO目标检测系统
支持图片和视频检测
"""
from flask import Flask, render_template_string, request, jsonify, send_file
from ultralytics import YOLO
import base64
import io
import os
import cv2
import numpy as np
import tempfile
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

logger.info("加载YOLO模型...")
model = YOLO("yolo11n.pt")
logger.info("模型加载完成！")

TEMP_DIR = tempfile.mkdtemp()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YOLO目标检测系统</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            background: #f5f5f5;
            height: 100vh;
            overflow: hidden;
        }
        
        .header {
            background: #2c3e50;
            color: white;
            padding: 15px 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            font-size: 1.3em;
            font-weight: 700;
            letter-spacing: 2px;
            font-family: 'Arial', sans-serif;
        }
        
        .main-container {
            display: flex;
            height: calc(100vh - 60px);
        }
        
        .left-panel {
            width: 50%;
            background: white;
            border-right: 1px solid #ddd;
            display: flex;
            flex-direction: column;
        }
        
        .right-panel {
            width: 50%;
            background: #fafafa;
            display: flex;
            flex-direction: column;
        }
        
        .controls {
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
            background: white;
        }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        
        .tab {
            padding: 8px 20px;
            border: 1px solid #ddd;
            background: white;
            cursor: pointer;
            border-radius: 4px;
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 1px;
            transition: all 0.2s;
        }
        
        .tab:hover {
            background: #f5f5f5;
        }
        
        .tab.active {
            background: #2c3e50;
            color: white;
            border-color: #2c3e50;
        }
        
        .control-row {
            display: flex;
            gap: 15px;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .control-row:last-child {
            margin-bottom: 0;
        }
        
        .file-input-wrapper {
            position: relative;
            flex: 1;
        }
        
        .file-input-btn {
            width: 100%;
            padding: 10px;
            background: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            cursor: pointer;
            text-align: left;
            font-size: 13px;
            font-weight: 600;
        }
        
        .file-input-btn:hover {
            background: #f5f5f5;
        }
        
        input[type="file"] {
            display: none;
        }
        
        .slider-group {
            flex: 1;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .slider-group label {
            font-size: 12px;
            color: #555;
            white-space: nowrap;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        input[type="range"] {
            flex: 1;
            height: 4px;
            border-radius: 2px;
            background: #ddd;
            outline: none;
            -webkit-appearance: none;
        }
        
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #2c3e50;
            cursor: pointer;
        }
        
        input[type="range"]::-moz-range-thumb {
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #2c3e50;
            cursor: pointer;
            border: none;
        }
        
        .value-display {
            font-size: 14px;
            font-weight: 600;
            color: #2c3e50;
            min-width: 40px;
        }
        
        .btn {
            padding: 10px 30px;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .btn-primary {
            background: #2c3e50;
            color: white;
        }
        
        .btn-primary:hover {
            background: #34495e;
        }
        
        .btn-primary:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .preview-area {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow: auto;
        }
        
        .preview-content {
            max-width: 100%;
            max-height: 100%;
        }
        
        .preview-content img,
        .preview-content video {
            max-width: 100%;
            max-height: 100%;
            display: block;
            margin: 0 auto;
        }
        
        .result-area {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 20px;
            overflow: hidden;
        }
        
        #resultContent {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 0;
            margin-bottom: 15px;
        }
        
        .result-video {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #000;
            border-radius: 4px;
        }
        
        .result-video video {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }
        
        .result-image {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .result-image img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }
        
        .stats-box {
            background: white;
            padding: 15px;
            border-radius: 4px;
            border: 1px solid #e0e0e0;
            max-height: 180px;
            overflow-y: auto;
            flex-shrink: 0;
        }
        
        .stats-box h3 {
            font-size: 12px;
            color: #555;
            margin-bottom: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stats-content {
            font-family: 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.6;
            white-space: pre-wrap;
            color: #333;
        }
        
        .loading {
            display: none;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1000;
        }
        
        .loading.show {
            display: block;
        }
        
        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #2c3e50;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .loading-text {
            font-size: 13px;
            color: #555;
            font-weight: 600;
            letter-spacing: 0.5px;
        }
        
        .progress-bar {
            width: 200px;
            height: 6px;
            background: #e0e0e0;
            border-radius: 3px;
            margin: 15px auto 10px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: #2c3e50;
            width: 0%;
            transition: width 0.3s;
        }
        
        .progress-text {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }
        
        .empty-state {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: #999;
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>YOLO 目标检测系统</h1>
    </div>
    
    <div class="main-container">
        <!-- 左侧面板 -->
        <div class="left-panel">
            <div class="controls">
                <div class="tabs">
                    <button class="tab active" onclick="switchTab('image')">图片检测</button>
                    <button class="tab" onclick="switchTab('video')">视频检测</button>
                    <button class="tab" onclick="switchTab('camera')">摄像头检测</button>
                </div>
                
                <div class="control-row">
                    <div class="file-input-wrapper" id="fileInputWrapper">
                        <button class="file-input-btn" onclick="document.getElementById('fileInput').click()">
                            <span id="fileLabel">选择文件</span>
                        </button>
                        <input type="file" id="fileInput" accept="image/*,video/*">
                    </div>
                    
                    <div class="file-input-wrapper" id="cameraControlWrapper" style="display:none;">
                        <button class="btn btn-primary" id="startCameraBtn" onclick="startCamera()">
                            启动摄像头
                        </button>
                        <button class="btn btn-primary" id="stopCameraBtn" onclick="stopCamera()" style="display:none;">
                            停止检测
                        </button>
                    </div>
                    
                    <div class="slider-group">
                        <label>置信度</label>
                        <input type="range" id="confSlider" min="0.1" max="0.9" step="0.05" value="0.25">
                        <span class="value-display" id="confValue">0.25</span>
                    </div>
                    
                    <button class="btn btn-primary" id="detectBtn" onclick="detect()" disabled>
                        开始检测
                    </button>
                </div>
            </div>
            
            <div class="preview-area">
                <div class="preview-content" id="preview">
                    <div class="empty-state">请选择文件</div>
                </div>
            </div>
        </div>
        
        <!-- 右侧面板 -->
        <div class="right-panel">
            <div class="result-area">
                <div id="resultContent">
                    <div class="empty-state">检测结果将显示在这里</div>
                </div>
                
                <div class="stats-box" id="statsBox" style="display:none;">
                    <h3>检测统计</h3>
                    <div class="stats-content" id="stats"></div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="loading" id="loading">
        <div class="spinner"></div>
        <div class="loading-text">正在处理中...</div>
        <div class="progress-bar">
            <div class="progress-fill" id="progressFill"></div>
        </div>
        <div class="progress-text" id="progressText">0%</div>
    </div>
    
    <script>
        let currentFile = null;
        let currentMode = 'image';
        let cameraStream = null;
        
        const fileInput = document.getElementById('fileInput');
        const fileLabel = document.getElementById('fileLabel');
        const preview = document.getElementById('preview');
        const detectBtn = document.getElementById('detectBtn');
        const confSlider = document.getElementById('confSlider');
        const confValue = document.getElementById('confValue');
        const resultContent = document.getElementById('resultContent');
        const statsBox = document.getElementById('statsBox');
        const stats = document.getElementById('stats');
        const loading = document.getElementById('loading');
        const fileInputWrapper = document.getElementById('fileInputWrapper');
        const cameraControlWrapper = document.getElementById('cameraControlWrapper');
        const startCameraBtn = document.getElementById('startCameraBtn');
        const stopCameraBtn = document.getElementById('stopCameraBtn');
        
        function switchTab(mode) {
            currentMode = mode;
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
            
            // 停止摄像头
            if (cameraStream) {
                stopCamera();
            }
            
            if (mode === 'camera') {
                fileInputWrapper.style.display = 'none';
                cameraControlWrapper.style.display = 'block';
                detectBtn.style.display = 'none';
            } else {
                fileInputWrapper.style.display = 'block';
                cameraControlWrapper.style.display = 'none';
                detectBtn.style.display = 'inline-block';
                fileInput.accept = mode === 'image' ? 'image/*' : 'video/*';
            }
            
            fileLabel.textContent = '选择文件';
            preview.innerHTML = '<div class="empty-state">请选择文件</div>';
            resultContent.innerHTML = '<div class="empty-state">检测结果将显示在这里</div>';
            statsBox.style.display = 'none';
            currentFile = null;
            detectBtn.disabled = true;
        }
        
        async function startCamera() {
            try {
                cameraStream = await navigator.mediaDevices.getUserMedia({ 
                    video: { width: 640, height: 480 } 
                });
                
                const video = document.createElement('video');
                video.srcObject = cameraStream;
                video.autoplay = true;
                video.style.width = '100%';
                preview.innerHTML = '';
                preview.appendChild(video);
                
                // 创建canvas用于显示检测结果（双缓冲技术）
                const resultCanvas = document.createElement('canvas');
                resultCanvas.width = 640;
                resultCanvas.height = 480;
                resultCanvas.style.width = '100%';
                resultCanvas.style.height = '100%';
                resultCanvas.style.objectFit = 'contain';
                resultCanvas.style.display = 'block';
                resultContent.innerHTML = '<div class="result-image"></div>';
                resultContent.querySelector('.result-image').appendChild(resultCanvas);
                const resultCtx = resultCanvas.getContext('2d');
                
                startCameraBtn.style.display = 'none';
                stopCameraBtn.style.display = 'inline-block';
                
                // 创建canvas用于捕获帧
                const captureCanvas = document.createElement('canvas');
                captureCanvas.width = 640;
                captureCanvas.height = 480;
                const captureCtx = captureCanvas.getContext('2d');
                
                // 优化canvas渲染质量
                resultCtx.imageSmoothingEnabled = true;
                resultCtx.imageSmoothingQuality = 'high';
                
                let isProcessing = false;
                let lastFrameTime = 0;
                const frameInterval = 300; // 300ms间隔，更平滑
                
                // 使用requestAnimationFrame实现平滑渲染
                function processFrame() {
                    if (!cameraStream) return;
                    
                    const now = Date.now();
                    if (now - lastFrameTime >= frameInterval && !isProcessing) {
                        lastFrameTime = now;
                        isProcessing = true;
                        
                        captureCtx.drawImage(video, 0, 0, 640, 480);
                        captureCanvas.toBlob(async (blob) => {
                            const formData = new FormData();
                            formData.append('frame', blob);
                            formData.append('conf', confSlider.value);
                            
                            try {
                                const response = await fetch('/detect_camera', {
                                    method: 'POST',
                                    body: formData
                                });
                                
                                const data = await response.json();
                                if (data.success) {
                                    // 创建新的Image对象并等待完全加载
                                    const img = new Image();
                                    img.onload = function() {
                                        // 使用requestAnimationFrame确保渲染同步
                                        requestAnimationFrame(() => {
                                            resultCtx.clearRect(0, 0, 640, 480);
                                            resultCtx.drawImage(img, 0, 0, 640, 480);
                                        });
                                    };
                                    img.src = 'data:image/jpeg;base64,' + data.image;
                                    
                                    stats.textContent = data.stats;
                                    statsBox.style.display = 'block';
                                }
                            } catch (error) {
                                console.error('检测失败:', error);
                            } finally {
                                isProcessing = false;
                            }
                        }, 'image/jpeg', 0.9);
                    }
                    
                    requestAnimationFrame(processFrame);
                }
                
                // 启动处理循环
                requestAnimationFrame(processFrame);
                
            } catch (error) {
                alert('无法访问摄像头: ' + error.message);
            }
        }
        
        function stopCamera() {
            if (cameraStream) {
                cameraStream.getTracks().forEach(track => track.stop());
                cameraStream = null;
            }
            preview.innerHTML = '<div class="empty-state">请选择文件</div>';
            resultContent.innerHTML = '<div class="empty-state">检测结果将显示在这里</div>';
            statsBox.style.display = 'none';
            startCameraBtn.style.display = 'inline-block';
            stopCameraBtn.style.display = 'none';
        }
        
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            currentFile = file;
            fileLabel.textContent = file.name;
            detectBtn.disabled = false;
            
            const url = URL.createObjectURL(file);
            
            if (currentMode === 'image') {
                preview.innerHTML = '<img src="' + url + '">';
            } else {
                preview.innerHTML = '<video src="' + url + '" controls autoplay muted loop></video>';
            }
        });
        
        confSlider.addEventListener('input', function() {
            confValue.textContent = this.value;
        });
        
        async function detect() {
            if (!currentFile) return;
            
            const formData = new FormData();
            formData.append('file', currentFile);
            formData.append('conf', confSlider.value);
            formData.append('mode', currentMode);
            
            loading.classList.add('show');
            detectBtn.disabled = true;
            
            try {
                const response = await fetch('/detect', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    if (currentMode === 'image') {
                        resultContent.innerHTML = '<div class="result-image"><img src="data:image/jpeg;base64,' + data.image + '"></div>';
                    } else {
                        resultContent.innerHTML = '<div class="result-video"><video src="/download_video/' + data.filename + '" controls autoplay loop></video></div>';
                    }
                    
                    stats.textContent = data.stats;
                    statsBox.style.display = 'block';
                } else {
                    alert('检测失败: ' + data.error);
                }
            } catch (error) {
                alert('请求失败: ' + error);
            } finally {
                loading.classList.remove('show');
                detectBtn.disabled = false;
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/detect', methods=['POST'])
def detect():
    try:
        file = request.files['file']
        conf = float(request.form.get('conf', 0.25))
        mode = request.form.get('mode', 'image')
        
        if mode == 'image':
            image = Image.open(file.stream)
            results = model(image, conf=conf)
            
            annotated = results[0].plot()
            annotated_image = Image.fromarray(annotated)
            
            buffered = io.BytesIO()
            annotated_image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            boxes = results[0].boxes
            detections = []
            for box in boxes:
                cls = int(box.cls[0])
                conf_val = float(box.conf[0])
                name = model.names[cls]
                detections.append(f"{name}: {conf_val:.2f}")
            
            stats = f"检测到 {len(boxes)} 个目标\n\n" + "\n".join(detections)
            
            return jsonify({
                'success': True,
                'image': img_str,
                'stats': stats
            })
        else:
            # 视频处理
            input_path = os.path.join(TEMP_DIR, 'input_' + file.filename)
            file.save(input_path)
            
            output_filename = 'output_' + file.filename
            output_path = os.path.join(TEMP_DIR, output_filename)
            
            cap = cv2.VideoCapture(input_path)
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # 使用H.264编码，更好的兼容性
            fourcc = cv2.VideoWriter_fourcc(*'avc1')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            frame_count = 0
            all_detections = []
            
            logger.info(f"开始处理视频，总帧数: {total_frames}")
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                results = model(frame, conf=conf, verbose=False)
                annotated_frame = results[0].plot()
                out.write(annotated_frame)
                
                boxes = results[0].boxes
                for box in boxes:
                    cls = int(box.cls[0])
                    name = model.names[cls]
                    all_detections.append(name)
                
                frame_count += 1
                
                # 每10帧记录一次进度
                if frame_count % 10 == 0:
                    progress = int((frame_count / total_frames) * 100)
                    logger.info(f"处理进度: {progress}% ({frame_count}/{total_frames})")
            
            cap.release()
            out.release()
            
            logger.info(f"视频处理完成，共处理 {frame_count} 帧")
            
            from collections import Counter
            detection_counts = Counter(all_detections)
            stats_lines = [
                f"总帧数: {total_frames}",
                f"处理帧数: {frame_count}",
                f"检测总数: {len(all_detections)}",
                "",
                "检测统计:"
            ]
            for obj, count in detection_counts.most_common():
                stats_lines.append(f"  {obj}: {count} 次")
            
            stats = "\n".join(stats_lines)
            
            return jsonify({
                'success': True,
                'filename': output_filename,
                'stats': stats
            })
        
    except Exception as e:
        logger.error(f"检测失败: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)})

@app.route('/detect_camera', methods=['POST'])
def detect_camera():
    try:
        frame_file = request.files['frame']
        conf = float(request.form.get('conf', 0.25))
        
        # 读取帧
        frame_bytes = frame_file.read()
        nparr = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # 检测
        results = model(frame, conf=conf, verbose=False)
        annotated_frame = results[0].plot()
        
        # 转换为JPEG
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        img_str = base64.b64encode(buffer).decode()
        
        # 统计
        boxes = results[0].boxes
        detections = []
        for box in boxes:
            cls = int(box.cls[0])
            conf_val = float(box.conf[0])
            name = model.names[cls]
            detections.append(f"{name}: {conf_val:.2f}")
        
        stats = f"检测到 {len(boxes)} 个目标\n\n" + "\n".join(detections) if detections else "未检测到目标"
        
        return jsonify({
            'success': True,
            'image': img_str,
            'stats': stats
        })
        
    except Exception as e:
        logger.error(f"摄像头检测失败: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download_video/<filename>')
def download_video(filename):
    try:
        file_path = os.path.join(TEMP_DIR, filename)
        return send_file(file_path, mimetype='video/mp4')
    except Exception as e:
        logger.error(f"视频下载失败: {e}")
        return "文件不存在", 404

if __name__ == '__main__':
    logger.info("=" * 60)
    logger.info("YOLO目标检测系统启动")
    logger.info("访问地址: http://127.0.0.1:7860")
    logger.info("=" * 60)
    
    os.makedirs('logs', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    
    app.run(host='127.0.0.1', port=7860, debug=False, threaded=True)
