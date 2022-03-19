# eXtreme Gradient Boosting (XGBoost)

# https://xgboost.readthedocs.io/en/latest/

# XGBoost is an optimized distributed gradient boost library designed
# to be highly efficient, flexible and portable. It implements algorithms
# machine learning under the Gradient Boosting framework. XGBoost provides a
# parallel tree augmentation (aka GBDT, GBM) that solves many
# Data Science problems quickly and accurately. The same code runs
# in the distributed environment (Hadoop, SGE, MPI) and can solve problems with data from
# billions of records.

# Widely used in Kaggle competitions.

# Note: If you have problems with accentuation, see this link:
# https://support.rstudio.com/hc/en-us/articles/200532197-Character-Encoding

# Setting the working directory
getwd()
setwd("~/Dropbox/DSA/MachineLearning2.0/Cap09/R")

# In this example, we intend to predict whether a mushroom can be eaten or not!

# packages
install.packages("xgboost")
install.packages("Ckmeans.1d.dp")
install.packages("DiagrammeR")
require(xgboost)
require(Ckmeans.1d.dp)
require(DiagrammeR)

# datasets
# https://archive.ics.uci.edu/ml/datasets/mushroom
?agaricus.train
data(agaricus.train, package = 'xgboost')
data(agaricus.test, package = 'xgboost')

# Collecting training and testing subsets
training_data <- agaricus.train
test_data <- agaricus.test

# Data summary
str(training_data)

# Viewing the dimensions
dim(training_data$date)
dim(test_data$date)

# Visualizing the data
View(training_data)
View(test_data)

# Classes to be predicted
class(training_data$data)[1]
class(training_data$label)

# Building the model
?xgboost
v1_model <- xgboost(data = training_data$date,
                    label = training_data$label,
                    max.depth = 2,
                    eta = 1,
                    nthread = 2,
                    nround = 2,
                    objective = "binary:logistic")

# Imprimindo o modelo
modelo_v1

# Matriz Densa
?xgb.DMatrix
dtrain <- xgb.DMatrix(data = dados_treino$data, label = dados_treino$label)
dtrain
class(dtrain)

# Modelo baseado em matriz densa
modelo_v2 <- xgboost(data = dtrain, 
                     max.depth = 2, 
                     eta = 1, 
                     nthread = 2, 
                     nround = 2, 
                     objective = "binary:logistic")

# Imprimindo o modelo
modelo_v2

# Criando um modelo e imprimindo as etapas realizadas
modelo_v3 <- xgboost(data = dtrain, 
                     max.depth = 2, 
                     eta = 1, 
                     nthread = 2, 
                     nround = 2, 
                     objective = "binary:logistic", 
                     verbose = 2)

# Printing the model
model_v3

# Making predictions
pred <- predict(model_v3, test_data$data)

# Size of the prediction vector
print(length(pred))

# Forecasts
print(head(pred))

# Transforming predictions into ranking
prediction <- as.numeric(pred > 0.5)
print(head(prediction))

# errors
err <- mean(as.numeric(pred > 0.5) != test_data$label)
print(paste("test-error = ", err))

# Creating 2 arrays
dtrain <- xgb.DMatrix(data = training_data$data, label = training_data$label)
dtest <- xgb.DMatrix(data = test_data$data, label = test_data$label)

# Creating a watchlist
watchlist <- list(train = dtrain, test = dtest)
watchlist

# Creating a model
?xgb.train
model_v4 <- xgb.train(data = dtrain,
                      max.depth = 2,
                      eta = 1,
                      nthread = 2,
                      nround = 2,
                      watchlist = watchlist,
                      objective = "binary:logistic")

# Getting the label
label = getinfo(dtest, "label")

# Making predictions
pred <- predict(model_v4, dtest)

# Error
err <- as.numeric(sum(as.integer(pred > 0.5) != label))/length(label)
print(paste("test-error = ", err))

# Creating the Attribute Importance Matrix
importance_matrix <- xgb.importance(model = model_v4)
print(importance_matrix)

# Plot
xgb.plot.importance(importance_matrix = importance_matrix)

# dump
xgb.dump(model_v4, with_stats = T)

# model plot
xgb.plot.tree(model = model_v4)

# Saving the model
xgb.save(model_v4, "xgboost.model")

# Loading the trained model
bst2 <- xgb.load("xgboost.model")

# Making predictions
pred2 <- predict(bst2, test_data$data)
pred2





