import pandas as pd
import numpy as np
import sklearn 
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from backend.db_connection import db
import logging

logger = logging.getLogger()



def add_bias_column(X):
    """
    Args:
        X (array): can be either 1-d or 2-d
    
    Returns:
        Xnew (array): the same array, but 2-d with a column of 1's in the first spot
    """
    
    if len(X.shape) == 1:
        Xnew = np.column_stack([np.ones(X.shape[0]), X])
    
    elif len(X.shape) == 2:
        bias_col = np.ones((X.shape[0], 1))
        Xnew = np.hstack([bias_col, X])
        
    else:
        raise ValueError("Input array must be either 1-d or 2-d")

    return Xnew

def line_of_best_fit(X, y):
    '''
    Arguments:
        X: 1-d or 2-d array with all predictor values without bias term
        y: 1-d array with corresponding response values to x 
        
    Returns: 
        a vector with the coefficients of the line of best fit + intercept 
    '''
    X_with_bias = add_bias_column(X)
    
    # computing the coefficients with (X^T * X)^(-1) * X^T * y
    XtX = np.dot(X_with_bias.T, X_with_bias)
    XtX_inv = np.linalg.inv(XtX)
    Xty = np.dot(X_with_bias.T, y)
    coefficients = np.dot(XtX_inv, Xty)
    
    return coefficients

def linreg_predict(Xnew, ynew, line):
    '''
    Arguments:
        Xnew: 1-d or 2-d array with all p predictor features except bias term
        ynew: 1-d array with all corresponding response values to Xnew
        m: 1-d array of length p + 1 with the coefficents from the line_of_best_fit function
    
    Returns:
        dc: dictionary with predicted y values, residuals, mean squared error, and r squared
    '''
    
    Xnew_with_bias = add_bias_column(Xnew)
    
    # computing results
    ypreds = np.dot(Xnew_with_bias, line)
    resids = ynew - ypreds
    mse = np.mean(resids ** 2)
    r2 = r2_score(ynew, ypreds)
    
    # creating result dictionary 
    dc = {
        'ypreds': ypreds,
        'resids': resids,
        'mse': mse,
        'r2': r2
    }
    
    return dc

def train2(): 
# call database to make array of hotel prices
    cursor = db.get_db().cursor()
    cursor.execute("""SELECT flight_price FROM main_df""")
    rows = cursor.fetchall()
    temp = [row['flight_price'] for row in rows]

    y = np.array(temp)

# call database to make dataframe of flight prices, hotel ratings, gdp, dummies
    cursor = db.get_db().cursor()
    res = cursor.execute("""SELECT hotel_price, hotel_rating, gdp, 
                         city_origin_Madrid, city_origin_Paris, city_origin_Rome, 
                         city_destination_Madrid, city_destination_Paris, 
                         city_destination_Rome, quarter_Q2, quarter_Q3, quarter_Q4
 FROM main_df""")
    rows = cursor.fetchall()
    df = pd.DataFrame.from_dict(rows)
    
#collecting numerical data
    X_num = np.array([df['hotel_price'], df['hotel_rating'], df['gdp']])

# standardizing data
    X_stand = (X_num.T - np.mean(X_num.T, axis=0)) / np.std(X_num.T, axis=0)

# making dummies 
    dummies_array = np.array([df['city_origin_Madrid'], df['city_origin_Paris'], df['city_origin_Rome'], df['city_destination_Madrid'], df['city_destination_Paris'], df['city_destination_Rome'], df['quarter_Q2'], df['quarter_Q3'], df['quarter_Q4']]).astype('int')


#concatenating
    X = np.concatenate([X_stand, dummies_array.T], axis=1)

# training model
    crossval = train_test_split(X, y, test_size=0.3)

    Xtrain, Xtest, ytrain, ytest = crossval

    train_line = line_of_best_fit(Xtrain, ytrain)
    test_line = linreg_predict(Xtest, ytest, train_line)

# finding line (parameter array) for whole dataset
    line = line_of_best_fit(X, y)

    intercept = line[0]
    slope1 = line[1]
    slope2 = line[2]
    slope3 = line[3]
    slope4 = line[4]
    slope5 = line[5]
    slope6 = line[6]
    slope7 = line[7]
    slope8 = line[8]
    slope9 = line[9]
    slope10 = line[10]
    slope11 = line[11]
    slope12 = line[12]

# storing line of best fit in database
    cursor = db.get_db().cursor()
    cursor.execute(f"""INSERT INTO flight_params VALUES 
                         ({0}, {intercept}, {slope1}, {slope2},
                          {slope3}, {slope4},  {slope5}, {slope6},
                           {slope7}, {slope8},  {slope9}, {slope10},
                            {slope11}, {slope12})""")
    db.get_db().commit()
    return 'Model trained!'


def predict2(var01, var02, var03, var04, var05):
    # call database to make dataframe of flight prices, hotel ratings, gdp, dummies
    cursor = db.get_db().cursor()
    cursor.execute("""SELECT hotel_price, hotel_rating, gdp, 
                         city_origin_Madrid, city_origin_Paris, city_origin_Rome, 
                         city_destination_Madrid, city_destination_Paris, 
                         city_destination_Rome, quarter_Q2, quarter_Q3, quarter_Q4
    FROM main_df""")
    rows = cursor.fetchall()
    df = pd.DataFrame.from_dict(rows)

    #getting params for model from db as a dictionary
    cursor = db.get_db().cursor()
    cursor.execute(f"""SELECT * from flight_params""")
    rows_params = cursor.fetchall()

    # changing dictionary to array 
    params_array = np.array(list(rows_params[0].values())[1:]) 

    # finding means and stds for standardization
    mean_flights = np.mean(df['hotel_price'])
    std_flights = np.std(df['hotel_price'])
    mean_ratings = np.mean(df['hotel_rating'])
    std_ratings = np.std(df['hotel_rating'])
    mean_gdp = np.mean(df['gdp'])
    std_gdp = np.std(df['gdp'])
    
    # standardizing
    hotel = (float(var01) - mean_flights)/std_flights
    rating = (float(var02)  - mean_ratings)/std_ratings
    
    # changing user inputs into usable values
    if var03 == 'London':
        co = np.array([0,0,0])
    if var03 == 'Madrid':
        co = np.array([1,0,0])
    if var03 == 'Paris':
        co = np.array([0,1,0])
    if var03 == 'Rome':
        co = np.array([0,0,1])

    if var04 == 'London':
        gdp = 51070
        cd = np.array([0,0,0])
    if var04 == 'Madrid':
        gdp = 34050
        cd = np.array([1,0,0])
    if var04 == 'Paris':
        gdp = 47360
        cd = np.array([0,1,0])
    if var04 == 'Rome':
        gdp = 39580
        cd = np.array([0,0,1])
  
    if var05 in ('January', 'February', 'March'):
        quarter = np.array([0,0,0])
    if var05 in ('April', 'May', 'June'):
        quarter = np.array([1,0,0])
    if var05 in ('July', 'August', 'September'):
        quarter = np.array([0,1,0])
    if var05 in ('October', 'November', 'December'):
        quarter = np.array([0,0,1])

    # standardizing   
    gdp = (gdp - mean_gdp)/std_gdp

    # creating array of converted user inputs 
    numerical_values = np.array([1.0, hotel, rating, gdp])
    input_array = np.concatenate((numerical_values, co, cd, quarter))
  
    # predicting using our line of best fit
    prediction = np.dot(params_array, input_array)

    return prediction

