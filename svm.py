import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import validation_curve
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

train_data = pd.read_csv("/content/train.csv") #reading the csv files using pandas
test_data = pd.read_csv("/content/test.csv")

train_data.shape # print the dimension or shape of train data

test_data.shape # print the dimension or shape of test data

train_data.head() # printing first five columns of train_data

test_data.head() # printing first five columns of test_data

train_data.isnull().sum().head(10) # không có giá trị nào bị thiếu trong tập dữ liệu

