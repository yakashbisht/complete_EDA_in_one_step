# -*- coding: utf-8 -*-
"""Untitled75.ipynb

Original file is located at
    https://colab.research.google.com/drive/1HyRxM5O0yNm9WDn8kK4vmcDasvTh0B_d
"""

!pip install ydata-profiling
from ydata_profiling import ProfileReport
import numpy as np
import pandas as pd
df = pd.read_csv("/content/diabetes.csv")
profile = ProfileReport(df, explorative=True)
profile.to_file("eda_report.html")

ProfileReport(df, minimal=True)

