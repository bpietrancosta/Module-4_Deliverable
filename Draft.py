from statistics import mean
import pandas as pd
import os

cwd = os.getcwd() + '\\new_full_student_data.csv'
student_df = pd.read_csv(cwd)

null_values = student_df.isna().sum()


student_df = student_df.dropna()
null_values2 = student_df.isna().sum()


duplicate_count = student_df.duplicated().sum()


student_df = student_df.drop_duplicates()


duplicate_count2 = student_df.duplicated().sum()


student_df['grade'] = student_df['grade'].str.replace("th", "")

student_df['grade'] = student_df['grade'].astype('int64')


student_mean_math = student_df['math_score'].mean()

min_reading_score = student_df['reading_score'].min()

student_df.loc[:, 'grade']

student_df.iloc[:3, [3,4,5]]

summ_stats_grade_9 = student_df.loc[student_df['grade'] == 9].describe()

min_reading_score_row = student_df.loc[student_df['reading_score'] == min_reading_score]

read_scores_from_Dixon_and_10 = student_df.loc[(student_df['school_name'] == 'Dixon High School') & (student_df['grade'] == 10), ['school_name', 'reading_score']]

mean_11_and_12_reading = student_df.loc[(student_df['grade'] == 11) | (student_df['grade'] == 12), ['reading_score']].mean()

group_df = student_df.groupby('school_type')['reading_score', 'math_score'].mean()

group_df2 = student_df.groupby('school_name')['student_id'].count().sort_values(ascending=False)

group_df3 = student_df.groupby(['school_type', 'grade'])['math_score'].mean().round(0)

