from RandomForest import random_forest_model


def prediction():
    print(random_forest_model.rfc.predict([[17612,10592,38,1337,874,1709,11720,5824,6205,0,0,0,3,7,13,131,37]]))
    print("if [0] valid, else fraud")


def setup():
    random_forest_model.main()
    prediction()
