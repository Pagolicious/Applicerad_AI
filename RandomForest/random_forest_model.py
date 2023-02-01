import pandas as pd

rfc = None
df = None


def main():
    global rfc
    global df
    df = pd.read_csv('RandomForest/fake_jobs_dataset_v2.csv')


    # df.head()


    # print(df.columns)


    # df.info()


    df.describe()


    # print(df.shape)


    df = df[['title', 'location', 'department', 'salary_range',
             'company_profile', 'description', 'requirements', 'benefits',
             'telecommuting', 'has_company_logo', 'has_questions', 'employment_type',
             'required_experience', 'required_education', 'industry', 'function',
             'fraudulent']]


    df.isna().apply(pd.value_counts)


    df.isnull().sum()


    df['fraudulent'].value_counts()


    fraud = df[df['fraudulent']== 1]
    # print(fraud.shape)


    not_fraud = df[df['fraudulent']== 0]
    # print(not_fraud.shape)


    fraud = fraud.sample(17014, replace=True)


    # print(fraud.shape, not_fraud.shape)


    df = fraud.append(not_fraud)
    df.reset_index()

    df = label_encoder(df)


    df = df.reset_index()
    df.head()


    from sklearn.model_selection import train_test_split


    X = df[['title', 'location', 'department', 'salary_range',
            'company_profile', 'description', 'requirements', 'benefits',
            'telecommuting', 'has_company_logo', 'has_questions', 'employment_type',
            'required_experience', 'required_education', 'industry', 'function']].values
    Y = df[['fraudulent']].values


    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)


    # print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)


    from sklearn.metrics import accuracy_score


    from sklearn.ensemble import RandomForestClassifier


    rfc = RandomForestClassifier(n_estimators=4)


    rfc.fit(X_train, Y_train)


    Y_pred = rfc.predict(X_test)


    Y_test = Y_test.flatten()
    Y_pred = Y_pred.flatten()


    df_rfc = pd.DataFrame({'Y_test': Y_test , 'Y_pred': Y_pred})
    # print(df_rfc)


    # print('Random Forest:', accuracy_score(Y_pred, Y_test))


    # print(rfc.predict([[10592,38,1337,874,1709,11720,5824,6205,0,0,0,3,7,13,131,37]]))


def label_encoder(df):
    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    df['title'] = le.fit_transform(df['title'])
    df['location'] = le.fit_transform(df['location'])
    df['department'] = le.fit_transform(df['department'])
    df['salary_range'] = le.fit_transform(df['salary_range'])
    df['company_profile'] = le.fit_transform(df['company_profile'])
    df['description'] = le.fit_transform(df['description'])
    df['requirements'] = le.fit_transform(df['requirements'])
    df['benefits'] = le.fit_transform(df['benefits'])
    df['telecommuting'] = le.fit_transform(df['telecommuting'])
    df['has_company_logo'] = le.fit_transform(df['has_company_logo'])
    df['has_questions'] = le.fit_transform(df['has_questions'])
    df['employment_type'] = le.fit_transform(df['employment_type'])
    df['required_experience'] = le.fit_transform(df['required_experience'])
    df['required_education'] = le.fit_transform(df['required_education'])
    df['industry'] = le.fit_transform(df['industry'])
    df['function'] = le.fit_transform(df['function'])

    return df


if __name__ == '__main__':
    main()
