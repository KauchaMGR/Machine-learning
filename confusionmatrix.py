import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

actual=np.random.binomial(1,0.9,1000)
predicted=np.random.binomial(1,0.9,1000)
confusion_matrix=metrics.confusion_matrix(actual,predicted)#It is a table that is used in classification problems to assess where errors in the model were made.
cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,display_labels=[0,1])

cm_display.plot()

plt.show()

#Now defining the accuracy ,sensitivity,precison,specificty,f_score
Accuracy = metrics.accuracy_score(actual, predicted)
Precision = metrics.precision_score(actual, predicted)
Sensitivity_recall = metrics.recall_score(actual, predicted)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)
F1_score = metrics.f1_score(actual, predicted)
print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})