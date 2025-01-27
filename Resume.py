import streamlit as st
from PIL import Image
# import pandas as pd
# import numpy as np

st.set_page_config(page_title='Somesh Tak Resume', page_icon='home_with_garden', layout="wide", initial_sidebar_state="auto", menu_items=None)

# image=Image.open('Somesh_Tak.JPG')

col1, col2=st.columns(2)
col1.write('# Somesh Tak')
col1.info('Python-Data Science- Streamlit, Pandas, SQL, Power BI, PySpark')
col1.write('##### Contact: +91 99 75 26 89 45')
col1.write('##### Place: Pune')
col1.info('Seeking challenging assignments in Data Science, Reporting and Business Analysis with an organisation of repute')
# col2.image(image, width=250)


with st.expander('Professional Brief'):
    st.write('''
-	Seasoned finance professional transitioned into Python Data science, bringing 14 years of analytical expertise and a proven track record of data-driven decision-making.
-	Hands on experience of Python, SQL, Big Data (Hadoop), PySpark, Oracle and other coding languages.
-	Good understanding of Banking and US mortgage industry.
-	Demonstrated ability to quickly learn organizational processes, workflows, policies & procedures.
-	Proficient in interacting with multiple levels of organisation, management & staff from different locations. 
-	Sound in conducting Equity Analysis and Industry Analysis aided by good understanding of capital markets, financial modelling/ forecasting techniques.
-	Exceptionally well organised with a track record that demonstrates self motivation, creativity, and initiative to achieve both personal & corporate goals.
    ''')

with st.expander('Competency Matrix'):
    st.write('''
-   Worked on Python- Pandas, Streamlit, Plotly, SQLAlchemy etc. libraries
-   Worked on descriptive statistics, analytics and reporting using various tools
-   Created and published dashboards using Power BI
-   Created SQL stored procedures, Functions, Triggers, Cursors etc. and also worked on query optimization to improve performance in MS SQL
-   Created packages to automate the workflow in SSIS

    ''')
with st.expander('TCS Professional Summary'):
    st.write('''
    ##### Python Data Science & Automation (Citi)- Team Leader ( Jan’ 23 – till date)
    -    Leading team spread across geographies to deliver data analysis for Trade domain
    -    Automated Production Validation process to eliminate human error and reduced time from 2 hours to 2 mins per associate
    -    Created dashboard to show recon of source to destination table ingestion data quality
    -    Created user interface and automated process of creating data catalogue for ingested table
    -    Implemented and automated data quality checks for table ingestion at source side to avoid downstream impact
    -    Analysed the various production issues, performed RCA and took various steps to avoid them
    -    Worked on regulatory reporting projects for multiple countries
    -    Successfully migrated reports from SAP BO to Python using Pandas, Pyspark OpenPyXL and PyFPDF
    ##### Loan Boarding Automation (Rushmore)- Team Leader ( Jan’ 21 – Sept' 22)
    -    Successfully lead short term fixed priced consulting project using just in time resource allocation
    -    Automated loan boarding process end to end using Python(Streamlit, Pandas, SQL Alchemy, Pyodbc, NumPy libraries) and SQL. 
    -     Developed User Interface (Multi Page Offline Web App) using Python’s Streamlit package to facilitate below operations:
            - Database operations on SQL server like table creation, upload, delete, drop, run stored procedure, run SQL functions etc
            - Run NLP model to predict the mapping of the fields
            - Create logic rules using drop downs, python code was generated in the background and was saved in rules engine repository.
            - Work on excel files like merging files, splitting into individual files, data cleaning & data manipulation etc.
            - View descriptive statistics report of the provided file
        - Create basic plots on the screen by changing data points
    - Developed SQL stored procedures, functions catering to different business needs
    - Developed data quality dashboards in Power BI to show data quality, exceptions, monthly trend for senior management, provided drill down functionalities as well for business use.
    - Developed Power BI dashboards for various business KPI for business teams.
    ### 
    ##### Risk Reporting & Analytics (Mr. Cooper)- Team Leader (Apr’ 18 – Dec’ 20)
    -    Helped and developed methods to quantify enterprise & operational risk.
    -    Helped and developed Key Risk Indicators (KRI) in mortgage originations and servicing process.
    -    Done analysis on various portfolio key metrics and risk areas using Excel, SQL, Python & R.
    -    Developed dashboards in Excel and Power BI for better view of the process to the senior management, provided functionalities to drill down to record level for business use as well.
    -    Automated and optimized the process by eliminating repeated and manual steps using SQL, SSIS packages, Excel and VBA Macros.
    -    Analysed & measured mortgage tools created against compliance, accuracy & risk.
    -    Helped other teams to bring efficiency and streamline the processes, provided training on mortgage processes.
    -    Worked on Ad-hoc Analysis requests from the Senior Management with time constraints
    ### 
    ##### Servicing Acquisition (Mr. Cooper)- Team Leader (Apr’ 15 – Mar’ 18)
    -    Developed stored procedures, functions, views, Cursors, etc. in Microsoft SQL./CVEDY
    -    Automated and optimized the process by eliminating repeated and manual steps using SQL, SSIS packages, Excel and VBA Macros.
    -    Created complex Monarch models to extract the data from raw source files.
    -    Extensively worked on data quality by creating a large number of edit checks using MS-SQL, Procedures and VBA.
    -    Consistently maintained the SLA (99%) since the inception of the project by achieving >99% quality score in mapping and SQL.
    -    Served as a mentor and reviewer to junior specialists in providing training on Process, Monarch, Mortgage, SQL, SSIS, SSRS & VBA.

    ''')
with st.expander('Education'):
    st.write('''
    ##### Education
    - MBA (Finance) from ICFAI University in 2009 with CGPA of 6.83.
    - B.Tech. (Computer Engineering) from Dr. B.A.T. University, Lonere in 2007 with 61.12%.
    - 12th from Maharashtra State Board in 2003 with 80.33% marks.       
    - 10th from Maharashtra State Board in 2001 with 88.80% marks.  \n     
    
    ### 
    ##### Additional Qualification:
    - Cygnus Certification Course on EIC Analysis and Company Evaluation from Cygnus India in 09.
    - Completed Python-Data Science course from Datalogy \n

    ### 
    ##### IT Skills:
    - Well versed with Python, SQL, Microsoft Office, Power BI, R, SPSS, Oracle, MicroStrategy and other useful Tools & Internet Applications
    ''')    
