import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# lode the data
oecd_bil = pd.read_csv("oced_bli_2020.csv", thousands=',')
