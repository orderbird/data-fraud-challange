
# Tech Challenge for Data Scientist Position

Welcome to our Data Science Tech Challenge.

In this assesment, you'll train a binary classifier to predict credit outcomes. 

We expect that you create python scripts or jupyter notebooks and 
be using popular python tools such as pandas, pySpark and scikit-learn. 
If you prefer any other tool, please explain why.
Finally, for a better understanding of your approachen and ideas 
as well as problems you faced, please comment your code. 

You should send your final submission via e-mail to us and avoid leaking 
your solution to other candidates on github or anywhere else.

In Task 1, you'll get familiar with the data-set, in task 2 you'll have to train 
some machine learning or statistical models. After that, you can decide weather 
you want to do Task 3 or Task 4, or you do both of them if you can.
Task 3 is about the overall optimization and Task 4 about productionizing your code.


## 1. Looking at the Data

Inside this repository, you an find a 
[file containing training data](data/credit-training-data.csv.gz) as well as a
[description of the file format](data-description.md):

 1. Load the data and replace codes with more meaningfull values.

 2. Visualize the distribution of the attributes inside the data.
    Do you see anything interresting there?


## 2. Predicting Credit Outcomes

 1. Develop at least two (a simple baseline and a one more sofisticateed) machine learning
    or statistical models, that can predict the result (good vs. bad) for a
    given credit based on the attributes of the credit/person.

 2. Compare and explain the outcomes of these models. 
    Which features are the most important ones for your models decision?


## 3. Dealing with the Risk

Consider the following:

 - giving out a credit that turns out to be good will give you 30% profit of the credit sum.
 - giving out a credit that turns out to be bad will cost you 90% of the credit sum.
 - losing a good customer will give you a bad reputation resulting in 5% of the credit sum in future loss.
 - rejecting a bad customer is the right thing to do and results in no loss at all.

1. How can you apply you're model to give a optimal recommandation for
   approving credits under these conditions?

2. What is the expected profit when using the model?


## 4. Automation

1. Finally, create a python scritp that will apply you're credit outcome prediction on a given input file.
   Your output file should contain the credit identifier and your models assesment of the credit (good vs. bad)

2. Create an airflow DAG that is able to apply your credit outcome prediction on a daily manner 
   and test it using our supplied airflow docker images. 
   <br/>
   You'll first have to initialize airflow with `docker-compose run airflow-init` 
   and then can start everything up with `docker-compose up`. 
   After a while, you should be able to log into http://localhost:8080 using airflow:airflow as credentials.
   For more documentation on running airflow inside docker, visit 
   [the official documentation](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html).



