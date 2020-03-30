import pandas as pd
import numpy as np

#Update display options to show more rows of data when executed
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1000)

#load in all datasources for H-1B Salaries
fb_h1b = pd.read_csv('Data/Facebook_Salaries_2018.csv')
ggle_h1b = pd.read_csv('Data/Google_Salaries_2018.csv')
sf_h1b = pd.read_csv('Data/SalesForce_Salaries_2018.csv')
wkd_h1b = pd.read_csv('Data/Workday_Salaries_2018.csv')

fb_h1b.head()
fb_h1b.dtypes
ggle_h1b.head()
sf_h1b.head()
wkd_h1b.head()

####################################################################
# FACEBOOK 
####################################################################
#add column for place of work
fb_h1b['Place_of_Work'] = 'Facebook' 
ggle_h1b['Place_of_Work'] = 'Google' 
sf_h1b['Place_of_Work'] = 'SalesForce'
wkd_h1b['Place_of_Work'] = 'Workday' 

#get job titles for FB Dataframe and start matching them to a Job Code (O-Net)
fb_h1b.head()

#let's see the value counts for each job!
fb_h1b['Job_Role'].value_counts()

#some duplicates, so have to clean the Job_Role's 
#get rid of trailing space 
fb_h1b['Job_Role'] = fb_h1b['Job_Role'].str.rstrip()

#get rid of leading 
fb_h1b['Job_Role'] = fb_h1b['Job_Role'].str.lstrip()

#Job Roles clean now
fb_h1b['Job_Role'].value_counts()


#we only really need jobs that have at least more than 10 ppl in the same position.But we can filter this out later. 
#from software engineer to Partner Engineer, we need the soc code for them 
#make a grouped dataframe and export it to excel. 

fb_job_counts = fb_h1b['Job_Role'].value_counts()
fb_h1b_grouped = fb_h1b.groupby(['Job_Role'])
fb_salary_avg = fb_h1b_grouped['Pay'].mean()

fb_salary_avg

#now make a dataframe 
#now make dataframe out of grouped information
fb_h1b_group = pd.DataFrame({'Job_Count': fb_job_counts,
                               'Salary': fb_salary_avg})

fb_h1b_group.head()

#reset_index
fb_h1b_group = fb_h1b_group.reset_index()

#change index column name to Job_Role
fb_h1b_group = fb_h1b_group.rename(columns={'index': 'Job_Role'})

#add fb column again. Try to make subset of data for the other tech company sheets
fb_h1b_group['Place_of_Work'] = 'Facebook' 
fb_h1b_group.head()

fb_h1b_group.sort_values(by='Job_Count', ascending=False)

#now do the same thing for the other worksheets


####################################################################
# GOOGLE 
####################################################################
#get job titles for FB Dataframe and start matching them to a Job Code (O-Net)
ggle_h1b.head()
#there are some nulls, let's see how many 
ggle_h1b.isnull().sum()

#only two nulls for the job roles. Have to get rid of them
        # test = ggle_h1b.dropna(axis = 0)
        # test.isnull().sum()
ggle_h1b = ggle_h1b.dropna(axis = 0)
ggle_h1b.isnull().sum()

#let's see the value counts for each job!
ggle_h1b['Job_Role'].value_counts()

#Make sure there aren't any duplicates, so have to clean the Job_Role's 
#get rid of trailing space 
ggle_h1b['Job_Role'] = ggle_h1b['Job_Role'].str.rstrip()

#get rid of leading 
ggle_h1b['Job_Role'] = ggle_h1b['Job_Role'].str.lstrip()

#Job Roles clean now
ggle_h1b['Job_Role'].value_counts()


#we only really need jobs that have at least more than 10 ppl in the same position.But we can filter this out later. 
#from software engineer to Partner Engineer, we need the soc code for them 
#make subset of data, then make a grouped dataframe and export it to excel.

ggle_h1b.head() 
ggle_h1b_sub = ggle_h1b.loc[:,['Job_Role', 'Pay', 'Place_of_Work']]
ggle_h1b_sub.head()
ggle_job_counts = ggle_h1b_sub['Job_Role'].value_counts()
ggle_h1b_grouped = ggle_h1b_sub.groupby(['Job_Role'])
ggle_salary_avg = ggle_h1b_grouped['Pay'].mean()

ggle_salary_avg
ggle_job_counts


#now make a dataframe 
#now make dataframe out of grouped information
ggle_h1b_group = pd.DataFrame({'Job_Count': ggle_job_counts,
                               'Salary': ggle_salary_avg})

ggle_h1b_group.head()

#reset_index
ggle_h1b_group = ggle_h1b_group.reset_index()

#change index column name to Job_Role
ggle_h1b_group = ggle_h1b_group.rename(columns={'index': 'Job_Role'})

ggle_h1b_group['Place_of_Work'] = 'Google' 
ggle_h1b_group.head()

ggle_h1b_group.sort_values(by='Job_Count', ascending=False)

####################################################################
# SALESFORCE
####################################################################
#get job titles for SF Dataframe and start matching them to a Job Code (O-Net)
sf_h1b.head()

#let's see if there are any nulls 
sf_h1b.isnull().sum()
#let's see the value counts for each job!
sf_h1b['Job_Role'].value_counts()

#in case of duplicates, have to clean the Job_Role's 
#get rid of trailing space 
sf_h1b['Job_Role'] = sf_h1b['Job_Role'].str.rstrip()

#get rid of leading 
sf_h1b['Job_Role'] = sf_h1b['Job_Role'].str.lstrip()

#Job Roles clean now
sf_h1b['Job_Role'].value_counts()

#we only really need jobs that have at least more than 10 ppl in the same position.But we can filter this out later. 
#from software engineer to Partner Engineer, we need the soc code for them 
#make a grouped dataframe and export it to excel. 

sf_h1b_job_counts = sf_h1b['Job_Role'].value_counts()
sf_h1b_grouped = sf_h1b.groupby(['Job_Role'])
sf_salary_avg = sf_h1b_grouped['Pay'].mean()

sf_salary_avg

#now make a dataframe 
#now make dataframe out of grouped information
sf_h1b_group = pd.DataFrame({'Job_Count': sf_h1b_job_counts,
                               'Salary': sf_salary_avg})

sf_h1b_group.head()

#reset_index
sf_h1b_group = sf_h1b_group.reset_index()

#change index column name to Job_Role
sf_h1b_group = sf_h1b_group.rename(columns={'index': 'Job_Role'})

#add fb column again. Try to make subset of data for the other tech company sheets
sf_h1b_group['Place_of_Work'] = 'SalesForce' 
sf_h1b_group.head()

sf_h1b_group.sort_values(by='Job_Count', ascending=False)

####################################################################
# WORKDAY 
####################################################################
#get job titles for FB Dataframe and start matching them to a Job Code (O-Net)
wkd_h1b.head()

#let's see if there are any nulls 
wkd_h1b.isnull().sum()
#let's see the value counts for each job!
wkd_h1b['Job_Role'].value_counts()

#in case of duplicates, have to clean the Job_Role's 
#get rid of trailing space 
wkd_h1b['Job_Role'] = wkd_h1b['Job_Role'].str.rstrip()

#get rid of leading 
wkd_h1b['Job_Role'] = wkd_h1b['Job_Role'].str.lstrip()

#Job Roles clean now
wkd_h1b['Job_Role'].value_counts()

#we only really need jobs that have at least more than 10 ppl in the same position.But we can filter this out later. 
#from software engineer to Partner Engineer, we need the soc code for them 
#make a grouped dataframe and export it to excel. 

wkd_h1b_job_counts = wkd_h1b['Job_Role'].value_counts()
wkd_h1b_grouped = wkd_h1b.groupby(['Job_Role'])
wkd_salary_avg = wkd_h1b_grouped['Pay'].mean()

wkd_salary_avg

#now make a dataframe 
#now make dataframe out of grouped information
wkd_h1b_group = pd.DataFrame({'Job_Count': wkd_h1b_job_counts,
                               'Salary': wkd_salary_avg})

wkd_h1b_group.head()

#reset_index
wkd_h1b_group = wkd_h1b_group.reset_index()

#change index column name to Job_Role
wkd_h1b_group = wkd_h1b_group.rename(columns={'index': 'Job_Role'})

#add fb column again. Try to make subset of data for the other tech company sheets
wkd_h1b_group['Place_of_Work'] = 'Workday' 
wkd_h1b_group.head()

wkd_h1b_group.sort_values(by='Job_Count', ascending=False)
#######################################################################
# EXPORT TO WORKBOOKS AND SPREADSHEETS

# fb_output = 'Data/FB_grouped.xlsx'
# ggle_output = 'Data/Ggle_grouped.xlsx'
# sf_output = 'Data/SF_grouped.xlsx'
# wkd_output = 'Data/Wkd_grouped.xlsx'

# fb_h1b_group.to_excel(fb_output, sheet_name = 'Data', index = False)
# ggle_h1b_group.to_excel(ggle_output, sheet_name = 'Data', index = False)
# sf_h1b_group.to_excel(sf_output, sheet_name = 'Data', index = False)
# wkd_h1b_group.to_excel(wkd_output, sheet_name = 'Data', index = False)

#########################################################################################
# 2015 - 2019 H1B Employer Data
#########################################################################################
h1b_15 = pd.read_csv('Data/h1b_datahubexport-2015.csv')
h1b_16 = pd.read_csv('Data/h1b_datahubexport-2016.csv')
h1b_17 = pd.read_csv('Data/h1b_datahubexport-2017.csv')
h1b_18 = pd.read_csv('Data/h1b_datahubexport-2018.csv')
h1b_19 = pd.read_csv('Data/h1b_datahubexport-2019.csv')

h1b_15.head()
h1b_15.dtypes

#make Zip, Tax ID, and NAICS Code into text for all dataframes 
h1b_15[["ZIP", "Tax ID", "NAICS"]] = h1b_15[["ZIP", "Tax ID", "NAICS"]].astype(str)
h1b_16[["ZIP", "Tax ID", "NAICS"]] = h1b_16[["ZIP", "Tax ID", "NAICS"]].astype(str)
h1b_17[["ZIP", "Tax ID", "NAICS"]] = h1b_17[["ZIP", "Tax ID", "NAICS"]].astype(str)
h1b_18[["ZIP", "Tax ID", "NAICS"]] = h1b_18[["ZIP", "Tax ID", "NAICS"]].astype(str)
h1b_19[["ZIP", "Tax ID", "NAICS"]] = h1b_19[["ZIP", "Tax ID", "NAICS"]].astype(str)

















