# -*- coding: utf-8 -*-
"""
Created on Sat May 27 07:44:53 2023

@author: otusa
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv') 

##salary parsing

#This code helps us remove the -1 from the salary data 
df = df[df['Salary Estimate'] != '-1']

#This code helps us split the salary estimate column into two & appends the first one into the 
#the salary tab  
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#This code helps us remove the data from the k & the dollar signs from the salary  
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

#This code helps us take the first part of the salary estimate as minimum  
df['min_salary']= minus_Kd.apply(lambda x: int(x.split('-')[0]))

#This code helps us take the second part of the salary estimate as maximum 
df['max_salary']= minus_Kd.apply(lambda x: int(x.split('-')[1]))

df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name text only 
#This code removes all the numeric values from the company name,by returning the files    
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1 )

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if len(x.split(',')) > 1 else ( x.split(',')[2] if len(x.split(',')) > 2 else ''))
df['job_state'].replace(' Anne Arundel', ' MD', inplace = True)
df.job_state.value_counts()

#This code helps us check if the location of the job & the headquarters are the same.  
df['same state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

                                         
#age of company
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2023 - x)

#parsing of job description (python, etc.)

#python 
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

df['r studio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['r studio_yn'].value_counts()

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df.columns
df_out=df.drop(['index'], axis = 1)

df_out.to_csv('salary_data_cleaned.csv', index = False)

