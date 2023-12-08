# xgboost参数

|参数| 分类器 |
|:--|---|
|max_depth| 给定树的深度，默认为3|
|learning_rate| 每个迭代产生的模型的权重、学习率，默认为0.1|
|n_estimators|子模型数量，默认为100|
|```objective```|给定损失函数，默认为："binary:logistic"，回归任务默认为:"reg:linear",还有例如"multi:softmax"，如果是softmax，需要设置num_class类别个数|
|booster|给定模型求解方式，默认为：gbtree，可选：gbtree、gblinear、dart|
|n_jobs = -1|使用多少线性并行构建XGBoost，默认为1，直接让他等于-1全跑就完事了|
|reg_alpha|l1正则项的权重，默认为0|
|reg_lambda|l2正则项的权重，默认为1|
|subsample|这个参数控制对于每棵树，随机采样的比例。减小这个参数的值，算法会更加保守，避免过拟合。但是，如果这个值设置得过小，它可能会导致欠拟合。|
|colsample_bytree|系统默认值为1。我们一般设置成0.8左右。用来控制每棵随机采样的列数的占比(每一列是一个特征)。 典型值：0.5-1范围: (0,1]|