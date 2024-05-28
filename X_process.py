import pandas as pd
import joblib

pipeline_num = joblib.load('./model_files/pipeline_num.save')

def X_process(cat_inp, num_data):

    #categorical data
    job_choice = ['blue-collar', 'management', 'technician', 'admin.', 'services',
         'retired', 'self-employed', 'entrepreneur', 'unemployed',
         'housemaid', 'student', 'nan']
    marital_choice = ['married', 'single', 'divorced']
    education_choice = ['secondary', 'tertiary', 'primary', 'nan']
    default_choice = ['no', 'yes']
    housing_choice = ['no', 'yes']
    loan_choice = ['no', 'yes']
    contact_choice = ['cellular', 'telephone']
    month_choice = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep',
         'oct', 'nov', 'dec']

    job_choicex = job_choice.copy()
    marital_choicex = marital_choice.copy()
    education_choicex = education_choice.copy()
    default_choicex = default_choice.copy()
    housing_choicex = housing_choice.copy()
    loan_choicex = loan_choice.copy()
    contact_choicex = contact_choice.copy()
    month_choicex = month_choice.copy()

    option_list = [job_choicex, marital_choicex, education_choicex, default_choicex, housing_choicex, loan_choicex, contact_choicex, month_choicex]
    remove_option_list = ['admin.', 'divorced', 'primary', 'no', 'no', 'no', 'cellular', 'apr']

    for i, x in zip(option_list, remove_option_list):
        i.remove(x)
        i.sort()
    
    cols = pd.concat([
    pd.Series(['job_' + x for x in job_choicex]),
    pd.Series(['marital_' + x for x in marital_choicex]),
    pd.Series(['education_' + x for x in education_choicex]),
    pd.Series(['default_' + x for x in default_choicex]),
    pd.Series(['housing_' + x for x in housing_choicex]),
    pd.Series(['loan_' + x for x in loan_choicex]),
    pd.Series(['contact_' + x for x in contact_choicex]),
    pd.Series(['month_' + x for x in month_choicex])
    ])

    data = pd.DataFrame({x: 0 for x in cols}, index=[0])

    for i in cat_inp:
        change_col = cols[cols.str.contains(i)]
        data[change_col] = 1
        
    #numeric data
    num_data = pipeline_num.transform(num_data)
    num_data = pd.DataFrame(data=num_data, columns=['age', 'balance', 'day_of_week', 'campaign', 'pdays', 'previous'])
 
    data = pd.concat([num_data, data], axis=1)
        
    return data
