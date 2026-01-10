import pandas as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
df=np.read_csv("data.csv")
features=['Age', 'Experience', 'Rank', 'Nationality']

d={'UK':0,'USA':1,'N':2}
df['Nationality']=df['Nationality'].map(d)
d= {'YES':1,'NO':0}
df['Go']=df['Go'].map(d)


x=df[features]
y=df['Go']
  
dtree=DecisionTreeClassifier().fit(x,y)
tree.plot_tree(dtree,feature_names=features)
