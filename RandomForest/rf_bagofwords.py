from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


df = pd.read_csv('./fake_jobs_dataset_v2.csv')

fake = df.loc[df['fraudulent'] == 1]
print(df.head())
print(fake)


df['company_profile'].head()


vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None)


from sklearn.model_selection import train_test_split


X = vectorizer.fit_transform(df['company_profile'].values.astype('U'))
Y = df[['fraudulent']].values
print(X)


np.asarray(X)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8)


print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)


forest = RandomForestClassifier(n_estimators = 100)


forest = forest.fit(X_train, Y_train.ravel())


Y_pred = forest.predict(X_test)


Y_test = Y_test.flatten()
Y_pred = Y_pred.flatten()
print(Y_pred)


df_rfc = pd.DataFrame({'Y_test': Y_test, 'Y_pred': Y_pred})
pd.set_option('display.max_rows', 60)
#pd.set_option("min_rows", 4470)
print(df_rfc)


from sklearn.metrics import accuracy_score


print(accuracy_score(Y_pred, Y_test))


tester = ['We are a food company that serve food from a truck']
testing = vectorizer.transform(tester)
np.asarray(testing)


result = forest.predict(testing)
if result:
    print('Fake')
else:
    print('Real')
print(result)
