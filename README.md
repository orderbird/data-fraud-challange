
# Tech Challange for Data Scientist (Payment Fraut) 

TODO: General into on how to work on the challange

## 1. Looking at the Data

Inside this repository, we provide you with a file containing data about credit defaults as well as a description of the file format.

 1. Loading the data/credit-training-data.csv and replace codes with more meaningfull values
 2. Visualize the distribution of the attributes inside the data

## 2. Predicting Credit Outcomes

 1. Develop at least two (a baseline and a more sofisticateed) Machine Learning or Statistical models, that can predict the outcome (Good vs. Bad) for a given credit based on the attributes of the credit/person.
 2. Compare and explain the outcomes of these models.

## 3. Dealing with the Risk

Consider the following:
 a. Giving out a credit that turns out to be good wil give you 30% profit of the credit sum.
 b. Giving out a credit that turns out to be bad will cost you 90% of the credit sum.
 c. Losing a good customer will give you a bad reputation resulting in 5% of the credit sum in future loss.
 d. Rejecting a bad customer is the right thing to do and results in no loss at all.

1. Tune your models accordingly to optimize you profit.
2. What's the expected profit when using the model

## 4. Fraud Automation

1. Finally, create a python scritp that will apply you're credit outcome prediction on a given input file.
2. Create an airflow DAG that is able to apply your credit outcome prediction on a daily manner 
   and test it using our supplied airflow docker base image.

