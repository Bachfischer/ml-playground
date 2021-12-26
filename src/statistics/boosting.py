from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import QuantileTransformer
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import TransformedTargetRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRFRegressor

#generic function to fit model and return metrics for every algorithm
def boost_models(model):
    #transforming target variable through quantile transformer
    regr_trans = TransformedTargetRegressor(regressor=model, transformer=QuantileTransformer(output_distribution='normal'))
    regr_trans.fit(X, y)
    yhat = regr_trans.predict(X)
    algoname= model.__class__.__name__
    return algoname, round(r2_score(y, yhat),3), round(mean_absolute_error(y, yhat),2), round(np.sqrt(mean_squared_error(y, yhat)),2)

algo=[GradientBoostingRegressor(), LGBMRegressor(), XGBRFRegressor()]
score=[]
for model in algo:
    score.append(boost_models(model))

#Collate all scores in a table
pd.DataFrame(score, columns=['Model', 'Score', 'MAE', 'RMSE'])
