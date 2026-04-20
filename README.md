# Measurement Data Analyzer

# Measurement Data Analyzer

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A Python tool for automated analysis and visualization of electrical measurement data.
Designed to process CSV files exported from measurement devices and generate statistical reports and plots.

---

## Features

- Automatic loading of CSV measurement files
- Statistical analysis — min, max, mean, standard deviation for each channel
- Automatic plot generation for each measurement channel
- Export of a structured text report
- Modular and extensible architecture

---

## Concepts Covered

| Concept | Description |
|---|---|
| pandas | Data loading and manipulation from CSV files |
| matplotlib | Automatic plot generation and export |
| numpy | Statistical computations |
| File I/O | Structured report export to text file |
| Modular design | Each function has a single responsibility |

---

## Project Structure
measurement-data-analyzer/
├── data/
│   └── sample_data.csv       ← Sample electrical measurement data
├── src/
│   └── analyzer.py           ← Main analysis script
├── output/
│   ├── voltage_V.png         ← Generated plots
│   ├── current_A.png
│   ├── temperature_C.png
│   ├── power_W.png
│   └── report.txt            ← Generated statistical report
├── requirements.txt
└── README.md

---

## Getting Started

### Requirements

- Python 3.8 or higher
- pip

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
cd src
python analyzer.py
```

---

## Input Format

The tool expects a CSV file with the following structure :
timestamp,voltage_V,current_A,temperature_C,power_W
0.0,12.01,0.52,25.3,6.25
0.5,12.05,0.53,25.4,6.39
...

- First column must be `timestamp` (in seconds)
- Remaining columns are measurement channels — any name is supported

---

## Example Output
==================================================
MEASUREMENT DATA ANALYZER
[ 1/3 ] Loading data...
Data loaded successfully — 20 rows, 5 columns
[ 2/3 ] Analyzing data...
voltage_V — min: 11.95, max: 12.15, mean: 12.047, std: 0.0611
current_A — min: 0.5,   max: 0.55,  mean: 0.526,  std: 0.0157
temperature_C — min: 25.3, max: 29.1, mean: 27.175, std: 1.2126
power_W — min: 5.98, max: 6.68, mean: 6.3375, std: 0.2208
[ 3/3 ] Generating plots and report...
Plot saved: ../output/voltage_V.png
Plot saved: ../output/current_A.png
Plot saved: ../output/temperature_C.png
Plot saved: ../output/power_W.png
Report saved: ../output/report.txt
==================================================
Analysis complete!

---

## Future Improvements

- Support for multiple input files
- Interactive plots with plotly
- Anomaly detection on measurement channels
- Export report as PDF

---

## Author

**Regis Tsafack**
GitHub: [github.com/regis37](https://github.com/regis37)