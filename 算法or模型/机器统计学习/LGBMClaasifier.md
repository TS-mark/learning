# lgbm参数


## 固定参数
---

|参数| 分类器 |
|:--|---|
|max_depth| 给定树的深度，默认为3|
|learning_rate| 每个迭代产生的模型的权重、学习率，默认为0.1|
|n_estimators|子模型数量，默认为100|
|```objective```|给定损失函数，默认为："binary:logistic"，回归任务默认为:"reg:linear",还有例如"multi:softmax"，如果是softmax，需要设置num_class类别个数|
|boosting_type='gbdt'| ‘gbdt’, traditional Gradient Boosting Decision Tree. ‘dart’, Dropouts meet Multiple Additive Regression Trees. ‘goss’, Gradient-based One-Side Sampling. ‘rf’, Random Forest.|
|num_leaves = 31|树的最大叶子数，控制模型复杂性的最重要参数之一。对比在xgboost中，一般为2^(max_depth)<br>因LightGBM使用的是leaf-wise的算法，因此在调节树的复杂程度时，使用的是num_leaves而不是max_depth。它们之间大致换算关系：num_leaves = 2^(max_depth)。即它的值的设置应该小于2^(max_depth)，否则会进行警告，可能会导致过拟合。
|subsample_for_bin=200000|Number of samples for constructing bins.|
|objective|Specify the learning task and the corresponding learning objective or a custom objective function to be used (see note below).Default: ‘regression’ for LGBMRegressor, ‘binary’ or ‘multiclass’ for LGBMClassifier, ‘lambdarank’ for LGBMRanker.|
|silent=True|Whether to print messages while running boosting.|
|n_jobs = -1|Number of parallel threads.|
|subsample=1.0|训练样本采样率（行）|
|colsample_bytree=1.0 |训练特征采样率（列）|
|reg_alpha=0.0|L1 regularization term on weights.|
|reg_lambda=0.0|L2 regularization term on weights.|