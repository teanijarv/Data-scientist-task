# Data-scientist-task
 By Toomas Erik Anijärv

Most of the comments and workflow can be read from the code
but in here there are some more important points and conclusions.

Task 1 - ML analysis on EMG data
-
- The data was split by the usual 80/20 split for training and testing
- Normalization was not needed with this dataset as the value ranges were quite consistent
- Logistic regression was not good method for solving this multi-class classification problem
- K-nearest neighbors was the best classifier due to its non-linearity (unlike LR)
- LR accuracy was ~ 64%; KNN accuracy was ~ 99%
- The trained model (KNN) was also tested with other subject's data and performed well

Task 2 - Mathematical exercise
-
- Each neuron was calculated Euclidean distance with every other neuron
- Neurons with distances which indicated conflict where added to list of conflicted neurons
- Each unique neuron with a conflicted state was counted
- The algorithm is quite slow (~ 1-2min) but indicates on the terminal its progress