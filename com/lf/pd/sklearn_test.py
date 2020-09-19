#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-19 09:50
# @Author  : fei.liu


import pandas as pd

df_train = pd.read_csv(r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/titanic_train.csv')

feature_cols = ['Pclass', 'Parch']

X = df_train.loc[:, feature_cols]

y = df_train.Survived

from sklearn.linear_model import LogisticRegression

# 创建模型对象
logreg = LogisticRegression()

# 实现模型训练
logreg.fit(X, y)

# print(logreg.fit(X, y))

# 找一个历史数据中不存在的数据

X.drop_duplicates().sort_values(by=['Pclass', 'Parch'])
#
print(logreg.predict([[2, 4]]))
#
print(logreg.predict_proba([[2, 4]]))
