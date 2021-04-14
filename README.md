
# Tech Challenge for Data Scientist Position

Welcome to our Data Science Tech Challenge.

In this assessment, your mission is, if you accept the challenge, to train a model for predicting credit outcomes. 
More specifically, we would like you to train a classifier to decide if it is a good idea 
to give a credit to customer (in that case the customer is a called a good customer) or not (bad customer).

Since we are great Python lovers, we ask you to implement your approach in Python. Of course, you can make use of 
popular python tools such as pandas, pySpark and scikit-learn. If you prefer any other (Python) tool, please explain why.
Finally, for a better understanding of your approach and ideas as well as problems you might have faced, 
please comment your code. 

You should send your final submission via e-mail to us. We kindly ask you to not leak your solution to other 
candidates on github or anywhere else. Thanks!

What is the mission?
As a warm-up, in Task 1 we ask you to get familiar with the data-set. The actual challenge takes place in Task 2: 
solving an inverse problem via machine learning or statistical techniques. Since we don't want you to spend days 
or weeks on completing the assessment, next we let you decide if you want to complete the assessment by 
either solving Task 3 or Task 4: Task 3 is about the overall optimization and Task 4 about putting your code in production.
Of course, we don't keep you from solving both :-)


## 1. Looking at the Data

Inside this repository, you'll find a 
[file containing training data](data/credit-training-data.csv.gz) as well as a
[description of the file format](data-description.md):

 1. Load the data and replace codes with more meaningful values.

 2. Visualize the distribution of the attributes inside the data.
    Do you see anything interesting there?


## 2. Predicting Credit Outcomes

 1. Train two different models that can predict the result (good vs. bad) for a
    given credit based on the attributes of the credit/person.

 2. Compare them and explain the outcomes of these models. Which one is better than the other one and why?
    Which features are the most important ones for your models decision?
    
    
## 3. Dealing with the Risk

Consider the following:

 - giving out a credit that turns out to be good will give you 30% profit of the credit sum.
 - giving out a credit that turns out to be bad will cost you 90% of the credit sum.
 - losing a good customer will give you a bad reputation resulting in 5% of the credit sum in future loss.
 - rejecting a bad customer is the right thing to do and results in no loss at all.

1. How can you apply you're model to give an optimal recommendation for
   approving credits under these conditions?

2. What is the expected profit when using the optimized model?


## 4. Automation

1. Create a Python script that applies your credit outcome prediction on a given input file.
   Your output file should contain the credit identifier and your models assessment of the credit (good vs. bad)

2. Create an airflow DAG that is able to apply your credit outcome prediction on a daily manner 
   and test it using our supplied airflow docker images. 
   <br/>
   You'll first have to initialize airflow with `docker-compose run airflow-init` 
   and then can start everything up with `docker-compose up`. 
   After a few minutes, you should be able to log into http://localhost:8080 using airflow:airflow as credentials.
   For more documentation on running airflow inside docker, please visit 
   [the official documentation](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html).
