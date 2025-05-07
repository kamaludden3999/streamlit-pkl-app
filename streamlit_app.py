from pickle import dump
dump(logistic_model,open ('TITANIC_train.pkl','wb')
from pickle import load
loaded_logistic_model=load(open('TITANIC_train.pkl','wb'))
y_pred=loded_logistic_model.predict(x_test)
