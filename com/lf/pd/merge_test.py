#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-09-14 14:24
# @Author  : fei.liu

import pandas as pd

df_ratings = pd.read_csv(
    r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/ratings.dat',
    sep='::', engine='python', names='UserID::MovieID::Rating::Timestamp'.split('::'))

df_users = pd.read_csv(
    r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/users.dat',
    sep='::', engine='python', names='UserID::Gender::Age::Occupation::Zip-code'.split('::'))

df_movies = pd.read_csv(
    r'/Users/apple/Documents/git-source/python-source/my-python-project/resources/movies.dat',
    sep='::', engine='python', names='MovieID::Title::Genres'.split('::'))

df_ratings_users = pd.merge(df_ratings, df_users, left_on="UserID", right_on="UserID", how='inner')

df_ratings_users_movies = pd.merge(df_ratings_users, df_movies, left_on='MovieID', right_on='MovieID', how='inner')

# print(df_ratings_users_movies.head())

# 1-1 merge
left = pd.DataFrame({'sno':[11, 12, 13, 14], 'name':['name_a', 'name_b', 'name_c', 'name_d']})

right = pd.DataFrame({'sno':[11, 12, 13, 14], 'age':['21', '22', '23', '24']})

result = pd.merge(left, right, on='sno')
# print(result)

# 1-多 merge
left = pd.DataFrame({'sno':[11, 12, 13, 14], 'name':['name_a', 'name_b', 'name_c', 'name_d']})

right = pd.DataFrame({'sno':[11, 11, 11, 12, 12, 13], 'grade':['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']})

result = pd.merge(left, right, on='sno')

# 多-多 merge
left = pd.DataFrame({'sno':[11, 11, 12, 12, 12], '爱好':['篮球', '羽毛球', '乒乓球', '篮球', '足球']})

right = pd.DataFrame({'sno':[11, 11, 11, 12, 12, 13], 'grade':['语文88', '数学90', '英语75', '语文66', '数学55', '英语29']})

result = pd.merge(left, right, on = 'sno')

print(result)