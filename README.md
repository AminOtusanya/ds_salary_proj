# Data Science Salary Estimator: Project Overview
* Created a tool that estimates data science salaries (MAE -$27k) to help data scinetists negotiate thier income when they get a job. 
* Collected from Kaggle
* Engineered features from the text of each job description to quantify the value compnies put on python, excel, aws, and spark.
* Optimized Linear, Lasso, Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

# Code and Resources Used
**Python Version:** 3.10.9
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
**For Web Framework Requiremnts:** '''pip install -r requiremnts.txt'''
**YouTube Tutorial:** https://www.youtube.com/watch?v=agHKuUoMwvY&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=7

# Data Collected
For each job scrapper we got this from the entire dataset:
* Job title
* Salary Estimate
* Job Description
* Rating
* Company Name 
* Location
* Headquarters
* Size
* Founded
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors


# Data Cleaning
After collecting the data from kaggle, I needed to clean up the data so it will be usable for my model. 
In the process created the following variables. 
* Parsed numeric data out of salary 
* Made columns for employer provided salary 
* Removed rows without salary
* Parsed rating out of company text
* Made a new column for company state
* Added a new column for if the job was at the company's headquaters
* Transformed founded date into age of company
* Made columns for if diffferent skills were listed in the job description: 
  * Python 
  * R
  * Excel
  * AWS
  * Spark
* Column for simplified job title and seniority
* Column for description length

# EDA
I looked at the distribution of the data and the value counts for teh various categorical variables. 

# Model Bulding
First I tranformed the categorical variable into dummy variables, then I split the data into train aand tests sets with a test size of 20%

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE beacuse it is easy to interpret and outliers aren't 
particularly bad in for this tpe of model. 

Different model: 
  * **Multiple Linear Regression** - Baseline for the model
  * **Lasso Regression** - Because the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
  * **Random Forest** - Again, with the sparsity associated with the data, I thought that this would be a good fit.

# Model Perfomance:  
  The Lasso regression outperforms the other approaches when measuring with MAE
     * Lasso Regression: MAE = 26.594997703695352
     * Random Forest Regression: MAE = 27.486068958219423
     * Multiple Linear Regression: MAE = 78930099.30502017    

# Productionization 
  In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorail in youtube reference above.
  The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 





   
