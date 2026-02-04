#!/usr/bin/env python
"""
Ultralytics YOLO 演示脚本
这个脚本展示了如何使用 YOLO 进行目标检测
"""

from ultralytics import YOLO
import sys

def main():
    print("=" * 60)
    print("Ultralytics YOLO 演示")
    print("=" * 60)
    
    # 显示可用的命令
    print("\n可用的命令:")
    print("1. python  detect <image_path>  - 进行目标检测")
    print("2. python  info                 - 显示项目信息")
    print("3. python  help                 - 显示帮助信息")
    
    if len(sys.argv) < 2:
        print("\n示例用法:")
        print("  python  info")
        print("  python  detect image.jpg")
        return
    
    command = sys.argv[1]
    
    if command == "info":
        show_info()
    elif command == "detect" and len(sys.argv) > 2:
        image_path = sys.argv[2]
        detect_objects(image_path)
    elif command == "help":
        show_help()
    else:
        print(f"未知命令: {command}")
        print("使用 'python  help' 获取帮助")

def show_info():
    """显示项目信息"""
    print("\n项目信息:")
    print("-" * 60)
    print("项目名称: Ultralytics YOLO")
    print("功能: 目标检测、分割、姿态估计、分类、追踪")
    print("支持的模型: YOLO11, YOLO10, YOLOv9, YOLOv8 等")
    print("Python 版本: >= 3.8")
    print("主要依赖: PyTorch, OpenCV, NumPy")
    print("-" * 60)
    
    # 尝试导入并显示版本
    try:
        from ultralytics import __version__
        print(f"Ultralytics 版本: {__version__}")
    except:
        pass
    
    print("\n✓ 项目已成功安装并准备就绪!")

def detect_objects(image_path):
    """进行目标检测"""
    print(f"\n正在加载模型...")
    try:
        model = YOLO('yolo11n.pt')
        print(f"正在检测: {image_path}")
        # 保存结果到 runs 文件夹
        results = model(image_path, save=True, conf=0.25)
        
        print(f"\n检测完成!")
        print(f"检测到的对象数: {len(results[0].boxes)}")
        
        # 显示检测结果
        if len(results[0].boxes) > 0:
            for i, box in enumerate(results[0].boxes):
                print(f"  对象 {i+1}: {box.cls} (置信度: {box.conf:.2f})")
        else:
            print("  未检测到任何对象")
        
        # 显示结果保存位置
        print(f"\n✓ 检测结果已保存到: runs/detect/predict/")
        print(f"  - 带标注的图片: runs/detect/predict/image.png")
        print(f"  - 标签文件: runs/detect/predict/labels/image.txt")
            
    except Exception as e:
        print(f"错误: {e}")
        print("提示: 确保图像文件存在且网络连接正常")

def show_help():
    """显示帮助信息"""
    print("\n帮助信息:")
    print("-" * 60)
    print("Ultralytics YOLO 是一个先进的计算机视觉框架")
    print("\n命令:")
    print("  info              - 显示项目信息")
    print("  detect <image>    - 对图像进行目标检测")
    print("  help              - 显示此帮助信息")
    print("\n示例:")
    print("  python  info")
    print("  python  detect photo.jpg")
    print("-" * 60)

if __name__ == "__main__":
    main()
