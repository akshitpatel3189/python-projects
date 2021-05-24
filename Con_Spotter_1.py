import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split,cross_val_predict,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,classification_report,f1_score,recall_score,precision_score,accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
import warnings
warnings.filterwarnings('ignore')
import random
random.seed(0)


def build_model_train_test(model,x_train,x_test,y_train,y_test):
    model.fit(x_train,y_train)

    y_pred = model.predict(x_train)
    
    print("\n----------Accuracy Scores on Train data------------------------------------")
    print("F1 Score: ", f1_score(y_train,y_pred))
    print("Precision Score: ", precision_score(y_train,y_pred))
    print("Recall Score: ", recall_score(y_train,y_pred))

    print("\n----------Accuracy Scores on Cross validation data------------------------------------")
    y_pred_cv = cross_val_predict(model,x_train,y_train,cv=5)
    print("F1 Score: ", f1_score(y_train,y_pred_cv))
    print("Precision Score: ", precision_score(y_train,y_pred_cv))
    print("Recall Score: ", recall_score(y_train,y_pred_cv))


    print("\n----------Accuracy Scores on Test data------------------------------------")
    y_pred_test = model.predict(x_test)
    print("F1 Score: ", f1_score(y_test,y_pred_test))
    print("Precision Score: ", precision_score(y_test,y_pred_test))
    print("Recall Score: ", recall_score(y_test,y_pred_test))

    plt.figure(figsize=(18,6))
    gs = gridspec.GridSpec(1,2)

    ax1 = plt.subplot(gs[0])
    cnf_matrix = confusion_matrix(y_train,y_pred,normalize='all')
    sns.heatmap(cnf_matrix,cmap='YlGnBu',annot=True)
    plt.title("Normalized Confusion Matrix - Train Data")

    ax3 = plt.subplot(gs[1])
    cnf_matrix = confusion_matrix(y_test,y_pred_test,normalize='all')
    sns.heatmap(cnf_matrix,cmap='YlGnBu',annot=True)
    plt.title("Normalized Confusion Matrix - Test Data")


def Print_Accuracy_Scores(y,y_pred):
    print("F1 Score: ", f1_score(y,y_pred))
    print("Precision Score: ", precision_score(y,y_pred))
    print("Recall Score: ", recall_score(y,y_pred))


cc_dataset = pd.read_csv("creditcard.csv")

X = cc_dataset.iloc[:,0:-1]
Y = cc_dataset.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


#Random forest
rnd_clf = RandomForestClassifier(bootstrap=True, class_weight='balanced',
            criterion='gini', max_depth=10, max_features='auto',
            max_leaf_nodes=None, min_impurity_decrease=0.0,
            min_impurity_split=None, min_samples_leaf=1,
            min_samples_split=5, min_weight_fraction_leaf=0.0,
            n_estimators=50, n_jobs=-1, oob_score=False, random_state=0,
            verbose=0, warm_start=False)
build_model_train_test(rnd_clf,x_train,x_test,y_train,y_test)


#Apply Knn Algorithm
knn_clf = KNeighborsClassifier(n_neighbors=3)
build_model_train_test(knn_clf,x_train,x_test,y_train,y_test)


#Apply AdaBoost classifier
ada_clf = AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=3,class_weight='balanced'), n_estimators=100,
        algorithm="SAMME.R", learning_rate=0.5, random_state=0
    )
build_model_train_test(ada_clf,x_train,x_test,y_train,y_test)


# Comparing all 3 alorithms with Voting Classifier
soft_voting_clf = VotingClassifier(
    estimators=[('rf', rnd_clf), ('ada', ada_clf), ('knn',knn_clf)], 
    voting='soft')
build_model_train_test(soft_voting_clf,x_train,x_test,y_train,y_test)
