## ISM1636

### Introduction:
My name is Subash chandra Biswal (U77884251) and this repository is for Data Science Programming class with Professor Dr. Smith. The class comprises of quiet a good amount of handson coding assignments, weekly assignments, quizzes and in-class practice assignments. Th class covers many machine learning models for classification and regresiion. 

### About the repository:
The repository is arranged hierarchically in which one folder is created for each week of class which has all the study materials and assignment folder. Each assignment folder has both data file and code files.

The folders cover topics as mentioned below.

- $W01$ :  [Python Anaconda Installation and Jupyter lab run test.](https://github.com/sbiswal14/ISM1636/tree/main/W01)
- $W02$ :  [Regression models](https://github.com/sbiswal14/ISM1636/tree/main/W02) 
- $W03$ :  [Support Vector Machine models.](https://github.com/sbiswal14/ISM1636/tree/main/W03)
- $W04$ :  [Decision Tree Models.](https://github.com/sbiswal14/ISM1636/tree/main/W04)
- $W05$ :  [Ensemble Models.](https://github.com/sbiswal14/ISM1636/tree/main/W05)
- $W06$ :  [Spring Break Assignments.](https://github.com/sbiswal14/ISM1636/tree/main/W06)
- $W07$ :  [Text Mining and Data Imbalance.](https://github.com/sbiswal14/ISM1636/tree/main/W07)
- $W08$ :  [Neural Network.](https://github.com/sbiswal14/ISM1636/tree/main/W08)
- $W09$ :  [Deep Neural Network.](https://github.com/sbiswal14/ISM1636/tree/main/W09)
- $W10$ :  [Convolutional Neural Network.](https://github.com/sbiswal14/ISM1636/tree/main/W10)
- $W11$ :  [Recurring Neural Network.](https://github.com/sbiswal14/ISM1636/tree/main/W11)
- $W12$ :  [Autoencoder.](https://github.com/sbiswal14/ISM1636/tree/main/W12)
- $W13$ :  [Multivariate Autoendocder.](https://github.com/sbiswal14/ISM1636/tree/main/W13)
- $Bonus$ : [Bonus Programming Test.](https://github.com/sbiswal14/ISM1636/tree/main/Bonus)

### Assignments: ( Mini Projects)
There are three assignments which are like mini projects implementing knowledge from couple of weeks.

- $Assignment 1 :$
  The assignment was to analyse the cardiotocography data and classify each observation as suspect or normal.
  
  Author: J. P. Marques de Sá, J. Bernardes, D. Ayers de Campos.
  Source: UCI
  Please cite: Ayres de Campos et al. (2000) SisPorto 2.0 A Program for Automated Analysis of Cardiotocograms. J Matern Fetal Med 5:311-318, UCI

  2126 fetal cardiotocograms (CTGs) were automatically processed and the respective diagnostic features measured. The CTGs were also classified by three expert  obstetricians and a consensus classification label assigned to each of them. Classification was both with respect to a morphologic pattern (A, B, C. ...) and to a fetal state (N, S, P). Therefore the dataset can be used either for 10-class or 3-class experiments.
  
  You can find the data [here.](https://github.com/sbiswal14/ISM1636/blob/main/W06/cardiotocography_csv.csv)
  
  The code for preprocessing the data can be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W06/preprocessing%20_cardio.ipynb)
  
  The code for model fit and prediction can be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W06/modelfit_cardio.ipynb)
  
- $Assignment 2 :$
  Thenassignment was an enhancement of assignment 1 using neural network and comparing the predictions with normal classification models (Decision tree.)
  
  The code to fit neural network models and the comparision of performance can be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W08/Assignment/modelfit_cardio.ipynb)
  
- $Assignment 3 :$
  This assignment was on implementing Recurring Neural Network to process multivariate data to predict the time series data on traffic volume and predict.
  
  Hourly Interstate 94 Westbound traffic volume for MN DoT ATR station 301, roughly midway between Minneapolis and St Paul, MN. Hourly weather features and holidays  included for impacts on traffic volume.

  Attribute Information:

  - holiday : Categorical US National holidays plus regional holiday, Minnesota State Fair
  - temp : Numeric Average temp in kelvin
  - rain_1h : Numeric Amount in mm of rain that occurred in the hour
  - snow_1h : Numeric Amount in mm of snow that occurred in the hour
  - clouds_all : Numeric Percentage of cloud cover
  - weather_main : Categorical Short textual description of the current weather
  - weather_description : Categorical Longer textual description of the current weather
  - date_time : DateTime Hour of the data collected in local CST time
  - traffic_volume : Numeric Hourly I-94 ATR 301 reported westbound traffic volume
  - Source: UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume)

  The data can be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W13/Assignment/Metro_Interstate_Traffic_Volume.csv)

  The code to pre=process the data can be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W13/Assignment/Assignment_3_data_preprocessing.ipynb)

  The code to fit models cab be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W13/Assignment/Assignment_3_model_fit.ipynb)

### Python Flask Web Application: 

  The project is to predict the probability of lawn mower ownership by providing income and lawn lotsize. 

  The data can be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W03/Assignment/Data/RidingMowers.csv)

  The flask API can be found [here.](https://github.com/sbiswal14/ISM1636/blob/main/W03/flask_project/app.py)


  
  
