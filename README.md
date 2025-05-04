# plot-epoch-wise

## Project Description

This project provides a Python script to visualize the performance of different training methods over epochs. It loads cleansing performance data from CSV files and plots test accuracy curves for three methods: DIT per epoch, SGD influence, and training with corrupted data. The plot uses academic-style colors and formatting to clearly compare the methods' accuracy trends over training epochs.

## Installation

This project requires Python 3.9 or higher. The dependencies can be installed via pip:

```bash
pip install daytime jupyter matplotlib numpy pandas
```

Alternatively, you can use the `pyproject.toml` file with a compatible package manager like Poetry or pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure the following CSV data files are present in the project directory:
   - `dit_cleansing_performance_001.csv`
   - `sgd_cleansing_performance_001.csv`
   - `relabel_030_pct_metrics_001.csv`

2. Run the main script to generate the accuracy comparison plot:

```bash
python main.py
```

3. The script will produce a plot image file named `epoch_wise_paper_figure.png` in the project directory.

## Plot Explanation

- The plot compares test accuracy across epochs for three training methods:
  - **DIT per epoch** (blue squares)
  - **SGD influence** (brown downward triangles)
  - **Train with corrupted data** (red circles)

- The x-axis shows the epoch number (adjusted for display), and the y-axis shows test accuracy ranging from 0.5 to 1.0.

- The plot includes grid lines and a black border for clarity, using Times New Roman font for academic presentation.

## License

This project is provided as-is without any warranty.
