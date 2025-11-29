
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SRC_DATA_FILE_NAME = 'HR_Data_MNC_Data Science Lovers.csv'

def distribution_of_employee_status(hr_data_mnc_df):
    """ 1.) What is the distribution of Employee Status
    (Active, Resigned, Retired, Terminated) ?"""

    # Get count of unique occurrences in 'column_name'
    status_counts = hr_data_mnc_df['Status'].value_counts()
    # print(unique_counts)
    plt.figure(figsize=(6,4))
    plt.pie(status_counts,labels=status_counts.index,autopct='%1.1f%%',
            colors=sns.color_palette('crest'))
    plt.title('Distribution of Employee Status ')
    # plt.show()
    plt.savefig('Q001 Distribution of Employee Status.png',
                format='png', dpi=300)  # Save as PNG with 300 DPI
    plt.close()
    print('Distribution of Employee Status Done')

# -----------------------------------------------------------

def distribution_of_work_modes(hr_data_mnc_df):
    """Q.2) What is the distribution of work modes 
    (On-site, Remote) ?"""
    # Get count of unique occurrences in 'column_name'
    work_modes_counts = hr_data_mnc_df['Work_Mode'].value_counts()
    # print(unique_counts)
    plt.figure(figsize=(6,4))
    plt.pie(work_modes_counts,labels=work_modes_counts.index,autopct='%1.1f%%',
            colors=sns.color_palette('crest'))
    plt.title('Distribution of Employee Work Modes ')
    # plt.show()
    plt.savefig('Q002 Distribution of Employee Work modes.png',
                format='png', dpi=300)  # Save as PNG with 300 DPI
    plt.close()
    print('Distribution of work modes Done')

# -----------------------------------------------------------

def num_of_employees_in_each_dept(hr_data_mnc_df):
    """Q.3) How many employees are there in each department ?"""

   # Count the number of employees in each department using Employee_ID
    each_dept_employee_counts = hr_data_mnc_df.groupby('Department')['Employee_ID'].count()
    
    # Open the file for writing
    with open('Q003 Department-wise employee count.txt', 'w') as f:
        # Write the header
        f.write(f"{'Department':<15} : {'Number of Employees':<10}\n")
        
        # Write the employee counts department-wise
        for department, count in each_dept_employee_counts.items():
            f.write(f"{department:<15} : {count:<10}\n")

    print('Employee check in each department Done')

# -----------------------------------------------------------

def avg_dept_salary(hr_data_mnc_df):
    """Q.4) What is the average salary by Department ?
    """

   # Calculate the average salary department-wise
    average_salary_dept_wise = hr_data_mnc_df.groupby('Department')['Salary_INR'].mean()
    # Find the maximum average salary

    with open('Q004 Department-wise avg salary.txt', 'w') as f:
        # Write the header
        f.write(f"{'Department':<15} : {'Average Salary':<10} INR\n")
        # Write the average salary department-wise
        for department, average_salary in average_salary_dept_wise.items():
            f.write(f"{department:<15} : {average_salary:<10.2f} INR\n")
        f.write('\n.........................................................\n')

    print('Average salary department-wise check Done')

# -----------------------------------------------------------

def avg_job_title_salary(hr_data_mnc_df):
    """Q.5) Which job title has the highest average salary ?
       Q.6) What is the average salary in different Departments based on Job Title ?"""

   # Calculate the average salary job title-wise
    average_salary_job_title_wise = hr_data_mnc_df.groupby('Job_Title')['Salary_INR'].mean()
    average_salary_job_title_wise = average_salary_job_title_wise.round(2)
    average_salary_job_title_wise_sorted = average_salary_job_title_wise.sort_values(ascending=False)

    # Find the maximum salary
    max_salary = average_salary_job_title_wise_sorted.max()

    # Remove rows where the salary is not the maximum
    average_salary_job_title_wise_max = average_salary_job_title_wise_sorted[average_salary_job_title_wise_sorted == max_salary]

    with open('Q005 Job Title-wise highest avg salary.txt', 'w') as f:
        # Write the header
        f.write(f"{'Highest Salary Job Title':<26} : {'Average Salary':<10} INR\n")
        # Write the average salary department-wise
        for Job_Title, Salary_INR in average_salary_job_title_wise_max.items():
            f.write(f"{Job_Title:<26} : {Salary_INR:<10.2f} INR\n")
        f.write('\n.........................................................\n')

    print('Highest salary Job-title-wise check Done')

    # average_salary_job_title_wise = hr_data_mnc_df.groupby('Job_Title')['Salary_INR'].mean()
    with open('Q006 Job-title-wise avg salary.txt', 'w') as f:
        # Write the header
        f.write(f"{'Job_Title':<30} : {'Average Salary':<10} INR\n")
        # Write the average salary department-wise
        for job_title, average_salary in average_salary_job_title_wise.items():
            f.write(f"{job_title:<30} : {average_salary:<10.2f} INR\n")

    print('Average salary Job-title-wise check Done')

# -----------------------------------------------------------




# -----------------------------------------------------------

def main():
    'use as main enterance'
    print('\nHello from 002-data-analysis!')
    print('\tprogram by Jiya Mehta 24101077\n')

    print('wait . . . data csv file is loading . . .')
    hr_data_mnc_df = pd.read_csv(SRC_DATA_FILE_NAME)
    # print(hr_data_mnc_df.shape[0])
    print('Removing duplicate records')
    hr_data_mnc_df.drop_duplicates()
    # print(hr_data_mnc_df.shape[0])
    
    
    # Q.1) What is the distribution of Employee Status (Active, Resigned, Retired, Terminated) ?
    # distribution_of_employee_status(hr_data_mnc_df)

    # Q.2) What is the distribution of work modes (On-site, Remote)?
    # distribution_of_work_modes(hr_data_mnc_df)

    # Q.3) How many employees are there in each department ?
    # num_of_employees_in_each_dept(hr_data_mnc_df)

    # Q.4) What is the average salary by Department ? 
    # avg_dept_salary(hr_data_mnc_df)

    # Q.5) Which job title has the highest average salary ?
    # Q.6) What is the average salary in different Departments based on Job Title ?
    # avg_job_title_salary(hr_data_mnc_df)

# -----------------------------------------------------------
if __name__ == '__main__':
    main()
