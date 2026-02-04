from ultralytics import YOLO

# 加载模型
model = YOLO('yolo11n.pt')

# 进行预测，使用较低的置信度阈值
image_path = r'D:\Research\ultralytics-main\ultralytics-main\images\image.png'
results = model(image_path, save=True, conf=0.1)

print(f"\n检测完成!")
print(f"检测到的对象数: {len(results[0].boxes)}")

if len(results[0].boxes) > 0:
    print("\n检测到的对象:")
    for i, box in enumerate(results[0].boxes):
        class_id = int(box.cls)
        confidence = float(box.conf)
        print(f"  对象 {i+1}: 类别ID={class_id}, 置信度={confidence:.2f}")
else:
    print("未检测到任何对象")

print(f"\n✓ 检测结果已保存到: runs/detect/predict/")
