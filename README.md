
# Tech Challenge for Data Scientist (Payment Fraut) 

Welcome to our Tech Challenge.
We have prepared a data-set and some tasks for you.

We expect that you create python scripts or jupyter notebooks for working with this data, 
using popular tools such as pandas, pySpark and scikit-learn. If you prefer another tool, please explain why.
Finally, for a better understanding of your approachen and ideas as well as problems you faced, please comment your code. 

You should send you final submission via e-mail to us and avoid leaking your solution to other candidates on github anywhere else.

## 1. Looking at the Data

Inside this repository, you an find a file containing data about credit alongside a description of the file format:

 1. Load the data/credit-training-data.csv and replace codes with more meaningfull values
 2. Visualize the distribution of the attributes inside the data

## 2. Predicting Credit Outcomes

 1. Develop at least two (a baseline and a more sofisticateed) machine learning
    or statistical models, that can predict the outcome (good vs. bad) for a
    given credit based on the attributes of the credit/person.
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
   Your output file should contain the credit identifier and your models assesment of the credit (good vs. bad)
2. Create an airflow DAG that is able to apply your credit outcome prediction on a daily manner 
   and test it using our supplied airflow docker images. 
   You'll first have to initialize airflow with `docker-compose run airflow-init` 
   and then can start everything up with `docker-compose up`. 
   After a while, you should be able to log into http://localhost:8080 using airflow:airflow as credentials.
   For more documentation on running airflow inside docker, visit 
   [the official documentation](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html).

