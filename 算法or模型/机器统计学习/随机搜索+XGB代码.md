## 划分数据集
---
```python
# 使用训练集中前50000数据进行参数调优，从所有组合中选择40种参数组合进行3折交叉验证的训练，最终返回最佳参数列表
import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
from sklearn.model_selection import train_test_split
 
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=1)  #训练集和测试集    
x
X_train_ = np.array(X_train.values, dtype=float)
X_test_ = np.array(X_test.values, dtype=float)
```


## 随机搜索：
---
```python
clf = XGBClassifier(objective = 'binary:logistic')
param_dist = {
        'n_estimators':range(80,1000,100),
        'max_depth':range(2,15,1),
        'learning_rate':np.linspace(0.01,2,20),
        'subsample':np.linspace(0.7,0.9,20),
        'colsample_bytree':np.linspace(0.5,0.98,10),
        'min_child_weight':range(1,9,1),
        
        }
# scoring = "neg_log_loss"
grid = RandomizedSearchCV(clf,param_dist,cv = 3,scoring = 'roc_auc',n_jobs = 1,verbose=2,n_iter=20, return_train_score=True)
grid.fit(X_train_[:50000,:],y_train[:50000], eval_metric = ['error'])
grid.best_params_
```

## xgb  --->这是个二分类任务
---
```python
from xgboost.sklearn import XGBClassifier

params = grid.best_params_
xgb_t = XGBClassifier(n_estimators = params["n_estimators"],\
                      learning_rate = params["learning_rate"],\
                      max_depth = params["max_depth"],\
                      subsample = params["subsample"],\
                      colsample_bytree = params["colsample_bytree"],\
                      min_child_weight = params["min_child_weight"],\
                      use_label_encoder=False,\
                      objective = 'binary:logistic',\
                      scale_pos_weight = 10  #postive：negative = 1:10，可以设置scale_pos_weight=10
                   ) 
# xgb_t = XGBClassifier(params)

## eval_metric = ["logloss"]
xgb_t.fit(X_train, y_train, eval_set = [(X_test, y_test)], eval_metric = ['error'],\
          early_stopping_rounds = 20)
```