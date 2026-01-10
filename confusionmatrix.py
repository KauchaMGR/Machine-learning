import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

actual=np.random.binomial(1,0.9,1000)
predicted=np.random.binomial(1,0.9,1000)
confusion_matrix=metrics.confusion_matrix(actual,predicted)
cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,display_labels=[0,1])

cm_display.plot()

plt.show()