from RandomForest import random_forest_model as rf
from googletrans import Translator
import pandas as pd
import csv
import os


def add_to_csv(new_data):
    original_file = 'RandomForest/fake_jobs_dataset_v2.csv'

    # New CSV file
    new_file = 'new_job.csv'

    # Read the original CSV file into a DataFrame
    df = pd.read_csv(original_file)

    # Create a new row of data
    new_row = new_data

    # Append the new row to the DataFrame
    df = df.append(new_row, ignore_index=True)

    # Save the DataFrame to a new CSV file
    df.to_csv(new_file, index=False)


def prediction(a=None,b=None,c=None,d=None,e=None,f=None,g=None,h=None,i=None,j=None,k=None,l=None,m=None,n=None,o=None,p=None):
    language = [a,c,e,f,g,h,l,m,n,o,p]
    language_not_none = []
    for lang in language:
        if lang is None:
            print('None')
        else:
            language_not_none.append(lang)
            print('added to language check')
    print(language_not_none)
    if language_check(language_not_none) == 1:
        return 1
    predict = {
        'title': a,
        'location': b,
        'department': c,
        'salary_range': d,
        'company_profile': e,
        'description': f,
        'requirements': g,
        'benefits': h,
        'telecommuting': i,
        'has_company_logo': j,
        'has_questions': k,
        'employment_type': l,
        'required_experience': m,
        'required_education': n,
        'industry': o,
        'function': p
    }

    add_to_csv(predict)
    df_ = pd.read_csv('new_job.csv')
    df_ = df_[['title', 'location', 'department', 'salary_range', 'company_profile', 'description', 'requirements',
               'benefits', 'telecommuting', 'has_company_logo', 'has_questions', 'employment_type',
               'required_experience', 'required_education', 'industry', 'function']]
    predict_ = rf.label_encoder(df_)
    test = predict_.tail(1)
    print(test, "tail")
    last_row_list = test.values.tolist()[0]
    print(last_row_list, "list")
    result = rf.rfc.predict([last_row_list])
    print("Prediction new csv:", result)
    print("Working")
    result = str(result)
    print(result)
    file_path = 'new_job.csv'
    os.remove(file_path)
    if result == "[0]":
        return 0
    else:
        return 1


def language_check(language):
    detector = Translator()
    languages = language
    fraud = 0

    dec_lan = detector.detect(languages)
    for dec in dec_lan:
        print(dec.lang)

        if dec.lang == 'en':
            print("working")
            fraud = 0
        else:
            print("stopped")
            fraud = 1
            break
    print(fraud)
    if fraud == 1:
        return 1


def setup():
    rf.main()
    # prediction('Financing Auto(car) sales','US, IL, hazelcrest','hr',35000-73000,'Looking for adventurous people to join a thriving industry.  We offer training and competitive earnings.  Find out why imports are the way to go and view our cars at our website.','If you have experience in financing for auto sales and a great attitude you can work in our Hazelcrest office.  From $500 top $1000 a week by contract.','prior car sales expprior car loan financing exp','profit sharingcar allowancecompany car',0,0,0,'Contract','Associate',None,"Automotive",None)
    print(prediction(0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1))


if __name__ == "__main__":
    setup()
    # language_check(['Hello', 'Hi', 'Hejsan svejsan'])
    # rf.main()
    # prediction()
