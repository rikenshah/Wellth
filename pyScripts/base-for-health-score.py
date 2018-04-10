import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
#from sklearn.preprocessing import LabelEncoder

## Loading data and preprocessing
data = pd.read_csv('../datasets/merged.csv')
train_data=data.iloc[:,0:10]
data["Individual_Rate"] = (data["Individual_Rate"]-data["Individual_Rate"].min())/(data["Individual_Rate"].max()-data["Individual_Rate"].min())

Y=data.iloc[:,10]

#test_data = pd.read_csv('../datasets/merged.csv')
features=['Ins_Age','BMI','Individual_Rate']

##Linear Regression

LinReg_model = LinearRegression()
LinReg_model.fit(train_data[features], Y)
linReg_score = cross_val_score(LinReg_model, train_data[features], Y, cv=10,scoring='r2').mean()
print("R2 score using Linear Regression is ",linReg_score*100)

##Random Forest Regressor
##
##RanForest_model = RandomForestRegressor( random_state=0)
##RanForest_model.fit(train_data[features], Y)
##ranForest_score = cross_val_score(RanForest_model, train_data[features], Y, cv=10,scoring='r2').mean()
##print("R2 score using Random Forest Regression is ",ranForest_score*100)

##Gradient Boosting Regressor

GradBoost_model = GradientBoostingRegressor(max_depth=3, random_state=0,learning_rate=0.1,n_estimators=200)
GradBoost_model.fit(train_data[features], Y)
GradBoost_model.apply(train_data[features])
gradBoost_score = cross_val_score(GradBoost_model, train_data[features], Y, cv=10,scoring='r2').mean()
print("Feature Importance ",GradBoost_model.feature_importances_)
print("R2 score using Gradient Boosting Regressor is ",gradBoost_score*100)


