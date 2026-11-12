---
title: Setup
nav_order: 2
---

# Setup

You need Python 3 with `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn`.

## On your own computer

1. Clone the course repository:

   ```bash
   git clone https://github.com/lilykoff/undergrad_ml.git
   cd undergrad_ml
   ```

2. Download the datasets. This fetches `data.zip` from [Zenodo](https://zenodo.org/records/18235955) and unpacks it into `data/` at the top of the repo:

   ```bash
   python get_data.py
   ```

3. Open any notebook in `lectures/` with Jupyter or VS Code. The notebooks read data from `../../data/`, so run them from inside their own folder.

## In Google Colab

Click a **Colab** link on the [schedule]({{ "/" | relative_url }}), then run this in the first cell. Change the last line to the lecture you opened.

```python
!git clone https://github.com/lilykoff/undergrad_ml.git
%cd undergrad_ml
!python get_data.py
%cd lectures/03_knn_classification
```

## Repository layout

```
undergrad_ml/
├── get_data.py          # downloads data/ from Zenodo
├── data/                # created by get_data.py (not in git)
└── lectures/
    └── 03_knn_classification/
        ├── 03_knn_classification.ipynb
        ├── 03_knn_classification.slides.html
        └── images/
```
