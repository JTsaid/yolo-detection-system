import numpy as np

# 原始矩阵（转置前）
matrix_baseline_original = np.array([
    [0.82, 0.35, 0.28, 0.04, 0.03, 0.00, 0.74], # Predict: Early Leaf Spot
    [0.00, 0.58, 0.00, 0.00, 0.01, 0.00, 0.13], # Predict: Early Rust
    [0.00, 0.00, 0.66, 0.00, 0.03, 0.02, 0.04], # Predict: Late Leaf Spot
    [0.00, 0.00, 0.00, 0.81, 0.00, 0.01, 0.00], # Predict: Nutrition
    [0.00, 0.00, 0.00, 0.00, 0.84, 0.00, 0.02], # Predict: Rust
    [0.01, 0.00, 0.00, 0.07, 0.00, 0.96, 0.07], # Predict: Healthy
    [0.01, 0.07, 0.06, 0.08, 0.08, 0.01, 0.00]  # Predict: Background
])

# 转置后的矩阵
matrix_baseline_transposed = matrix_baseline_original.T

labels = ['Early Leaf Spot', 'Early Rust', 'Late Leaf Spot', 
          'Nutrition Deficiency', 'Rust', 'Healthy', 'Background']

print("=" * 80)
print("转置前的矩阵（7x7）:")
print("=" * 80)
print("\n行标签（Predict）:")
for i, label in enumerate(labels):
    print(f"  {i}: {label}")
print("\n列标签（True）:")
for i, label in enumerate(labels):
    print(f"  {i}: {label}")

print("\n矩阵数据（转置前）:")
print(matrix_baseline_original)

print("\n" + "=" * 80)
print("转置后的矩阵（7x7）:")
print("=" * 80)
print("\n行标签（True）:")
for i, label in enumerate(labels):
    print(f"  {i}: {label}")
print("\n列标签（Predict）:")
for i, label in enumerate(labels):
    print(f"  {i}: {label}")

print("\n矩阵数据（转置后）:")
print(matrix_baseline_transposed)

print("\n" + "=" * 80)
print("转置后矩阵的详细说明:")
print("=" * 80)
print("\n转置后矩阵的含义:")
print("- 行（纵坐标）: True Label（真实标签）")
print("- 列（横坐标）: Predict Label（预测标签）")
print("\n例如：")
print(f"  matrix[0, 0] = {matrix_baseline_transposed[0, 0]} (True: Early Leaf Spot, Predict: Early Leaf Spot)")
print(f"  matrix[1, 0] = {matrix_baseline_transposed[1, 0]} (True: Early Rust, Predict: Early Leaf Spot)")
print(f"  matrix[0, 1] = {matrix_baseline_transposed[0, 1]} (True: Early Leaf Spot, Predict: Early Rust)")
