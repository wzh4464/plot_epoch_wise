# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

# 设置字体为 Times New Roman（若系统支持）
mpl.rcParams['font.family'] = 'Times New Roman'

# 加载 CSV 数据
dit_df = pd.read_csv('dit_cleansing_performance_001.csv')
sgd_df = pd.read_csv('sgd_cleansing_performance_001.csv')
relabel_df = pd.read_csv('relabel_030_pct_metrics_001.csv')

# 向右平移 DIT 和 SGD 的 epoch
dit_df['epoch'] += 1
sgd_df['epoch'] += 1

# 设置学术配色
academic_colors = {
    'blue': '#1f77b4',
    'brown': '#8c564b',
    'red': '#d62728',
    'green': '#4daf4a'
}

# 设置 epoch 显示范围与刻度标签
max_epoch = int(max(dit_df['epoch'].max(), sgd_df['epoch'].max(), relabel_df['epoch'].max()))
adjusted_xticks = np.arange(3, max_epoch + 1, 2)               # 原始 epoch 刻度
adjusted_tick_labels = adjusted_xticks - 3                     # 实际显示标签减去 3（从 0 开始）

# 开始绘图
plt.figure(figsize=(10, 6))

# 绘制 DIT 曲线（绿色菱形）
plt.plot(
    dit_df['epoch'], dit_df['test_accuracy'],
    label='Per-epoch TIM prune', color=academic_colors['green'],
    marker='s', markersize=10, linestyle='-', zorder=10
)

# 绘制 SGD 曲线 （蓝色倒三角）
plt.plot(
    sgd_df['epoch'], sgd_df['test_accuracy'],
    label='Full-training TIM prune', color=academic_colors['blue'],
    marker='v', markersize=10, linestyle='-'
)

# 绘制 corrupted 曲线（红色圆圈）
plt.plot(
    relabel_df['epoch'], relabel_df['val_accuracy'],
    label='Train with corrupted data', color=academic_colors['red'],
    marker='o', markersize=10, linestyle='-'
)

# 设置坐标轴标签和图例
plt.xlabel('Epoch', fontsize=28)
plt.ylabel('Test Accuracy', fontsize=28)
plt.legend(fontsize=22)

# 设置刻度与标签
plt.xticks(adjusted_xticks, labels=adjusted_tick_labels, fontsize=24)
plt.yticks(fontsize=24)
plt.xlim(left=3)
plt.ylim(0.5, 1.0)

# 添加网格线
plt.grid(True)

# 添加黑色边框
for spine in plt.gca().spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.5)
    spine.set_edgecolor('black')

# 自动布局与保存图像
plt.tight_layout()
plt.savefig('epoch_wise_paper_figure.png', dpi=300)
# %%
