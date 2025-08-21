import streamlit as st
from PIL import Image


st.set_page_config(page_title='Somesh Tak Resume', page_icon='dashboard', layout="wide", initial_sidebar_state="auto", menu_items=None)

image=Image.open('Somesh T.jpg')

col1, col2=st.columns(2)
col1.write('# Somesh Tak')
col1.info('Python-Data Science- Streamlit, Pandas, SQL, Power BI, PySpark')
col1.write('##### Contact: +91 99 75 26 89 45')
col1.write('##### Place: Pune')
col1.info('Seeking challenging assignments in Data Science, Reporting and Business Analysis with an organisation of repute')
with open("Somesh Tak Resume.pdf", "rb") as pdf_file:
        PDFbytes = pdf_file.read()
col1.download_button(
        label="Download Resume",
        data=PDFbytes,
        file_name="Somesh Tak Resume.pdf",
        mime="application/pdf",
        icon="⬇️"
    )
#col2.image(image)
with col2:
    sub_col_left, sub_col_center, sub_col_right = st.columns([1, 2, 1]) # Adjust ratios as needed

    with sub_col_center:
        st.image(image) # Replace with your image path

custom_css = """
    <style>
    .streamlit-expanderHeader {
        background-color: #f0f2f6; /* Light gray background for header */
        color: black;
    }
    .streamlit-expanderContent {
        background-color: #e0e2e6; /* Slightly darker gray for content */
        color: black;
    }
    </style>
    """
st.markdown(custom_css, unsafe_allow_html=True)
with st.expander('Professional Brief',expanded=False):
    st.write('''
-	Seasoned finance professional transitioned into Python Data science, bringing 15 years of analytical expertise and a proven track record of data-driven decision-making.
-	Hands on experience of Python, SQL, Big Data (Hadoop), PySpark, Oracle and other coding languages.
-	Good understanding of Banking and US mortgage industry.
-   Hands on experience and knowledge in Generative AI, Agentic AI, LLM models
-	Demonstrated ability to quickly learn organizational processes, workflows, policies & procedures.
-	Proficient in interacting with multiple levels of organisation, management & staff from different locations. 
-	Sound in conducting Equity Analysis and Industry Analysis aided by good understanding of capital markets, financial modelling/ forecasting techniques.
-	Exceptionally well organised with a track record that demonstrates self motivation, creativity, and initiative to achieve both personal & corporate goals.
    ''')

with st.expander('Competency Matrix',expanded=False):
    st.write('''
-   Worked on Python- Pandas, Streamlit, Plotly, SQLAlchemy etc. libraries
-   Worked on descriptive statistics, analytics and reporting using various tools
-   Created and published dashboards using Power BI
-   Created SQL stored procedures, Functions, Triggers, Cursors etc. and also worked on query optimization to improve performance in MS SQL
-   Created packages to automate the workflow in SSIS
-   Worked on Generative AI- Google Gemini, LLM models, Agentic AI applications

    ''')
with st.expander('Professional Summary',expanded=False):
    st.write('''
    ### Tata Consultancy Services                              (Apr'15 - till date)
    ##### Python Data Science & Automation (Citi)- Team Leader ( Jan’ 23 – till date)
    -    Leading team spread across geographies to deliver data analysis for Trade domain
    -    Worked on Data Quality Analytics Dashboard using Generative AI
    -    Automated Production Validation process to eliminate human error and reduced time from 2 hours to 2 mins per associate using Pandas, PySpark etc
    -    Created dashboard in Python to show recon of source to destination table ingestion data quality
    -    Created user interface using Streamlit and automated process of creating data catalog for ingested table using requests, pandas, json module
    -    Implemented and automated data quality checks (recon reports) for table ingestion at source side to avoid downstream impact
    -    Worked on regulatory reporting projects for multiple countries using Bigdata
    -    Successfully migrated reports from SAP BO to Python using Pandas, Pyspark OpenPyXL and PyFPDF
    -    Worked on model data lineage using json, pandas, requests module 
    -    Captured data lineage of Java UI application using Python
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
    
    ###  Homeward Residential India Pvt. Ltd., Pune as Business Analyst	(Aug’12-Mar'15)
    -    Own Daily, Weekly, Monthly and Quarterly Reports of the Company Portfolio Performance which are sent to the top management.
    -    Created/worked on performance dashboards for Foreclosure and Bankruptcy.
    -    Extensively worked on Risk management by creating reports on Foreclosure, Bankruptcy and Special Servicing.
    -    Automated Scheduled reports/Models using excel, VBA & SQL.
    -    Studied Industry research reports and compared the performance of the firm’s portfolio against the Industry.
    -    Worked with Rating Agencies like CITI, S&P, Fitch by providing the numbers related to the firm which helps them in rating the firm and the industry.
    -    Worked on other Ad-hoc Analysis requests from the Senior Management.
    ###  Synygy India Pvt. Ltd., Pune as Financial Reporting Associate	(Jul’11-Jun’12 )
    -    Projected & reported revenues on a weekly, monthly, quarterly and yearly basis.
    -    Analysed and reported:
        o	Revenue productivity on departmental basis and at company level.
        o	Expenses at departmental and company level.
    -    Co-ordinated with different departments to create the accurate reports. 
    -    Presented reports to Account Executives and Directors on their revenue accounts.
    -    Helped HR team in recruiting right positions at right location to minimize the cost and lowering attrition by creating accurate reports.
    -    Helped sales team in improving their productivity by creating accurate and meaningful reports. 
    -    Optimized the reports by using Macros or other coding techniques.
    
    ###  Fountain / Capstone Securities Analysis Pvt. Ltd., Pune/Mumbai as Associate (Proprietary Trader)	(May’09-Jul’11)
    -    Conducted analysis on trends in securities of DOW and NASDAQ Indices.
    -    Placed the orders through various Electronic Communication Networks (ECNs) and executed complete trade. 
    -    Took corrective action by analyzing market and stock condition with proper risk to reward ratio.
    -    Followed various strategies like hedging and exit strategies to operate the open position.


    ''')
with st.expander('Education',expanded=False):
    st.write('''
    ##### Education
    - MBA (Finance) from ICFAI University in 2009 with CGPA of 6.83.
    - B.Tech. (Computer Engineering) from Dr. B.A.T. University, Lonere in 2007 with 61.12%.
    - 12th from Maharashtra State Board in 2003 with 80.33% marks.       
    - 10th from Maharashtra State Board in 2001 with 88.80% marks.  \n     

    ##### Additional Qualification:
    - Certified Associate Python Programmer (PCAP)
    - Certified Microsoft Power BI Developer (PL300)
    - Cygnus Certification Course on EIC Analysis and Company Evaluation from Cygnus India in 09.
    - Completed Python-Data Science course from Datalogy \n


    ##### IT Skills:
    - Well versed with Python, SQL, Microsoft Office, Power BI, R, SPSS, Oracle, MicroStrategy and other useful Tools & Internet Applications
    ''')    
