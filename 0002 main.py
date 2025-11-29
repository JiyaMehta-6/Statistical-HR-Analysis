
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


SRC_DATA_FILE_NAME = 'HR_Data_MNC_Data Science Lovers.csv'

# -----------------------------------------------------------
# 1
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
    print(' 1] Distribution of Employee Status Done')

# -----------------------------------------------------------
# 2
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
    print(' 2] Distribution of work modes Done')

# -----------------------------------------------------------
# 3
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

    print(' 3] Employee check in each department Done')

# -----------------------------------------------------------
# 4
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

    print(' 4] Average salary department-wise check Done')

# -----------------------------------------------------------
# 5,6
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

    print(' 5] Highest salary Job-title-wise check Done')

    # average_salary_job_title_wise = hr_data_mnc_df.groupby('Job_Title')['Salary_INR'].mean()
    with open('Q006 Job-title-wise avg salary.txt', 'w') as f:
        # Write the header
        f.write(f"{'Job_Title':<30} : {'Average Salary':<10} INR\n")
            # Write the average salary department-wise
        for job_title, average_salary in average_salary_job_title_wise.items():
            f.write(f"{job_title:<30} : {average_salary:<10.2f} INR\n")

    print(' 6] Average salary Job-title-wise check Done')

# -----------------------------------------------------------
# 7
def employee_Resigned_Terminated(hr_data_mnc_df):
    """Q.7) How many employees Resigned & Terminated in each department ?"""

    # Filter for resignations and terminations
    resigned = hr_data_mnc_df[hr_data_mnc_df['Status'] == 'Resigned']
    terminated = hr_data_mnc_df[hr_data_mnc_df['Status'] == 'Terminated']

    # Group by department and count
    resigned_count = resigned.groupby('Department').size()
    terminated_count = terminated.groupby('Department').size()

    # Merge the two counts into a DataFrame
    result = pd.DataFrame({
        'Department': resigned_count.index,
        'Resigned_Count': resigned_count.values
    }).merge(
        pd.DataFrame({
            'Department': terminated_count.index,
            'Terminated_Count': terminated_count.values
        }),
        on='Department',
        how='outer'
    ).fillna(0)

    # Convert counts to integers
    result['Resigned_Count'] = result['Resigned_Count'].astype(int)
    result['Terminated_Count'] = result['Terminated_Count'].astype(int)

    # Set the figure size
    plt.figure(figsize=(12, 6))

    # Melt the DataFrame for easier plotting
    result_melted = result.melt(id_vars='Department', value_vars=['Resigned_Count', 'Terminated_Count'],
                                 var_name='Status', value_name='Count')

    # Create a bar plot
    bar_plot = sns.barplot(data=result_melted, x='Department', y='Count', hue='Status', palette='Set2')

    # Add titles and labels
    plt.title('Employee Resignations and Terminations by Department', fontsize=16)
    plt.xlabel('Department', fontsize=14)
    plt.ylabel('Number of Employees', fontsize=14)
    plt.xticks(rotation=45)
    plt.legend(title='Status')

    # Annotate the bars with counts
    for p in bar_plot.patches:
        bar_plot.annotate(f'{int(p.get_height())}', 
                          (p.get_x() + p.get_width() / 2., p.get_height()), 
                          ha='center', va='bottom', 
                          fontsize=10, color='black', 
                          xytext=(0, 5),  # Offset the text slightly above the bar
                          textcoords='offset points')

    plt.tight_layout()

    # Show the plot
    # plt.show()
    # Save the figure as a PNG file
    plt.savefig('Q007 Distribution of Employee Resigned & Terminated.png', format='png', dpi=300)
    plt.close()
    print(' 7] Distribution of Employee Resigned/Terminated Done')

# -----------------------------------------------------------
# 8
def experience_avg_salary(hr_data_mnc_df):
    """Q.8) How does salary vary with years of experience ?"""

    # Group by 'Experience_Years' and calculate the average salary
    salary_experience = hr_data_mnc_df.groupby('Experience_Years')['Salary_INR'].mean()

    # Print the result
    # print(salary_experience)

    # Plotting the data
    plt.figure(figsize=(10, 6))
    sns.histplot(salary_experience, bins=30, kde=True, alpha=0.7, color='skyblue')
    plt.title('Average Salary Distribution by Years of Experience')
    plt.xlabel('Average Salary (INR)')
    plt.ylabel('Years of Experience')
    plt.grid()
    
    # Save as PNG with 300 DPI
    plt.savefig('Q008 Variation of salary with experience.png', format='png', dpi=300)
    plt.close()
    
    print(' 8] Variation of salary with experience check Done')

# -----------------------------------------------------------
# 9
def dept_avg_performance_rating(hr_data_mnc_df):
    """Q.9) What is the average performance rating by department ?
    """

   # Calculate the average performance rating department-wise
    average_performance_rating_dept_wise = hr_data_mnc_df.groupby('Department')['Performance_Rating'].mean()

    with open('Q009 Department-wise avg Performance Rating.txt', 'w') as f:
        # Write the header
        f.write(f"{'Department':<15} : {'Average Performance Rating':<10} INR\n")
        # Write the average salary department-wise
        for department, average_perf_rating in average_performance_rating_dept_wise.items():
            f.write(f"{department:<15} : {average_perf_rating:<10.2f}\n")

    print(' 9] Average Performance Rating department-wise check Done')

# -----------------------------------------------------------
# 10
def country_wise_employee_conc(hr_data_mnc_df):
    """Q.10) Which Country has the highest concentration of employees ?"""

    # Extract country from the Location column
    hr_data_mnc_df['Country'] = hr_data_mnc_df['Location'].str.split(',').str[1].str.strip()

    # Calculate the number of employees country-wise
    employees_country_wise = hr_data_mnc_df.groupby('Country')['Employee_ID'].count()
    # print(employees_country_wise)

    # Find the country with the maximum number of employees
    max_country = employees_country_wise.idxmax()
    max_count = employees_country_wise.max()
    
    with open('Q010 Country-wise Employee Concentration.txt', 'w') as f:
        # Print the country with the maximum employees
        f.write(f'The country that has maximum employees is {max_country} with {max_count} employees.\n')
        # Write the header
        f.write(f"{'Country':<30} : {'Employee Concentration':<10} \n")
        # Write the employee count country-wise
        for country, employees in employees_country_wise.items():
            f.write(f"{country:<30} : {employees:<10}\n")

    print('10] Employee concentration country-wise check Done')

# -----------------------------------------------------------
# 11
def correlation_performance_salary(hr_data_mnc_df):
    """Q.11) Is there a correlation between performance rating and salary ?"""
    
    # Ensure the relevant columns are numeric
    hr_data_mnc_df['Performance_Rating'] = pd.to_numeric(hr_data_mnc_df['Performance_Rating'], errors='coerce')
    hr_data_mnc_df['Salary_INR'] = pd.to_numeric(hr_data_mnc_df['Salary_INR'], errors='coerce')

    # Drop rows with NaN values in either column
    correlation_data = hr_data_mnc_df[['Performance_Rating', 'Salary_INR']].dropna()

    # Calculate the correlation
    correlation = correlation_data['Performance_Rating'].corr(correlation_data['Salary_INR'])

    # Interpret the correlation
   
    with open('Q011 Correlation between performance rating and salary.txt', 'w') as f:
        f.write(f'The correlation between performance rating and salary is: {correlation:.2f}\n')
        
        if correlation > 0:
            f.write("There is a positive correlation: as performance rating increases, salary tends to increase.\n")
        elif correlation < 0:
            f.write("There is a negative correlation: as performance rating increases, salary tends to decrease.\n")
        else:
            f.write("There is no correlation between performance rating and salary.\n")


    print('11] Correlation between performance rating and salary check Done')

# -----------------------------------------------------------
# 12
def hires_per_yr(hr_data_mnc_df):
    """Q.12) How has the number of hires changed over time (per year) ?"""

    # Extract the year from the Hire_Date column
    hr_data_mnc_df['Hire_Year'] = pd.to_datetime(hr_data_mnc_df['Hire_Date']).dt.year
    # Count the number of hires per year
    hires_per_year = hr_data_mnc_df.groupby('Hire_Year')['Employee_ID'].count()

    # Set the figure size
    plt.figure(figsize=(12, 6))
    # Create a line plot with markers
    sns.lineplot(data=hires_per_year, marker='o', color='blue', linewidth=2)

    # Add titles and labels
    plt.title('Number of Hires Per Year', fontsize=18, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Number of Hires', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Add grid lines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotate the points with the number of hires
    for x, y in zip(hires_per_year.index, hires_per_year):
        plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10, color='black')

    plt.tight_layout()

    # Save the figure as a PNG file
    plt.savefig('Q012 Hires Per Year.png', format='png', dpi=300)
    plt.close()
    print('12] Analysis of hires per year done.')

# -----------------------------------------------------------
# 13
def salary_compare_work_mode_wise(hr_data_mnc_df):
    # Descriptive statistics
    salary_summary = hr_data_mnc_df.groupby('Work_Mode')['Salary_INR'].agg(['mean', 'median', 'std'])

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Work_Mode', y='Salary_INR', data=hr_data_mnc_df)
    plt.title('Salary Distribution by Work Mode')
    plt.xlabel('Work Mode')
    plt.ylabel('Salary (INR)')
    plt.savefig('Q013 Comparing salaries of Remote vs. On-site employees.png', format='png', dpi=300)  # Save as PNG with 300 DPI
    plt.close()

    # Perform a Mann-Whitney U test
    remote_salaries = hr_data_mnc_df[hr_data_mnc_df['Work_Mode'] == 'Remote']['Salary_INR']
    onsite_salaries = hr_data_mnc_df[hr_data_mnc_df['Work_Mode'] == 'On-site']['Salary_INR']
    u_statistic, p_value = stats.mannwhitneyu(remote_salaries, onsite_salaries)

    # Prepare the output for the text file
    with open('Q013 Comparing salaries of Remote vs. On-site employees.txt', 'w') as f:
        # Write the salary summary
        f.write("Salary Summary:\n")
        f.write(salary_summary.to_string())  # Convert DataFrame to string for writing
        f.write("\n\n")  # Add a newline for better formatting

        # Output the results
        f.write(f'U-statistic: {u_statistic:.2f}\n')
        f.write(f'P-value    : {p_value:.2f}\n')

        # Determine significance
        alpha = 0.05  # significance level
        if p_value < alpha:
            f.write("There is a significant difference in salaries between Remote and On-site employees.\n")
        else:
            f.write("There is no significant difference in salaries between Remote and On-site employees.\n")
        print('13] Comparing salaries of Remote vs. On-site employees Done')

# -----------------------------------------------------------
# 14
def top_employees_by_department(hr_data_mnc_df):
    """Q.14) Find the top 10 employees with the highest salary in each department."""

    # Step 1: Sort the DataFrame by Department and Salary
    sorted_data = hr_data_mnc_df.sort_values(by=['Department', 'Salary_INR'], ascending=[True, False])

    # Step 2: Group by Department and get the top 10 employees
    top_10_employees = sorted_data.groupby('Department').head(10)

    # Optional: Reset index for better readability
    top_10_employees.reset_index(drop=True, inplace=True)

    with open('Q014 The top 10 employees with the highest salary in each department.txt', 'w') as f:
        # Write the salary summary
        # Convert DataFrame to string without index
        f.write(top_10_employees.to_string(index=False))  

    print('14] The top 10 employees with the highest salary in each department check Done.')

# -----------------------------------------------------------
# 15
def attrition_rate_by_department(hr_data_mnc_df):
    """Q.15) Identify departments with the highest attrition rate (Resigned %)."""

    # Step 1: Calculate total employees and resigned employees by department
    total_employees = hr_data_mnc_df.groupby('Department').size()
    resigned_employees = hr_data_mnc_df[hr_data_mnc_df['Status'] == 'Resigned'].groupby('Department').size()

    # Step 2: Calculate attrition rate
    attrition_rate = (resigned_employees / total_employees) * 100

    # Step 3: Create a DataFrame for the results
    attrition_df = pd.DataFrame(attrition_rate).reset_index()
    attrition_df.columns = ['Department', 'Attrition Rate (%)']

    # Step 4: Sort by attrition rate in descending order
    attrition_df = attrition_df.sort_values(by='Attrition Rate (%)', ascending=False)

    # Write the results to a text file
    with open('Q015 Departments with the highest attrition rate.txt', 'w') as f:
        f.write(attrition_df.to_string(index=False))  # Convert DataFrame to string without index

    print('15] Departments with the highest attrition rate check Done.')

# -----------------------------------------------------------

def main():
    'use as main enterance'
    print('\nHello from 002-data-analysis!')
    print('\tprogram by Jiya Mehta 24101077\n')

    print('wait . . . data csv file is loading . . .')
    hr_data_mnc_df = pd.read_csv(SRC_DATA_FILE_NAME)



# ========================================


    # Create a new DataFrame with at most 200 rows.
    # If the original file has fewer than 200 rows, this will just return the whole set.
    df_200 = hr_data_mnc_df.head(200).copy()          # or: df.sample(n=200, random_state=42) for a random subset

    # Optional: inspect the result
    print(df_200.shape)   # should be (200, number_of_columns)
    print(df_200.head())

    # Save the trimmed DataFrame if you need a separate file
    df_200.to_csv('HR_Data_MNC_subset_200.csv', index=False)


# =====================================================================


    # print(hr_data_mnc_df.shape[0])
    print('Removing duplicate records')
    hr_data_mnc_df.drop_duplicates()
    # print(hr_data_mnc_df.shape[0])
    
    
    # Q.1) What is the distribution of Employee Status (Active, Resigned, Retired, Terminated) ?
    distribution_of_employee_status(hr_data_mnc_df)

    # Q.2) What is the distribution of work modes (On-site, Remote)?
    distribution_of_work_modes(hr_data_mnc_df)

    # Q.3) How many employees are there in each department ?
    num_of_employees_in_each_dept(hr_data_mnc_df)

    # Q.4) What is the average salary by Department ? 
    avg_dept_salary(hr_data_mnc_df)

    # Q.5) Which job title has the highest average salary ?
    # Q.6) What is the average salary in different Departments based on Job Title ?
    avg_job_title_salary(hr_data_mnc_df)

    # Q.7) How many employees Resigned & Terminated in each department ?"""
    employee_Resigned_Terminated(hr_data_mnc_df)

    # Q.8) How does salary vary with years of experience ?
    experience_avg_salary(hr_data_mnc_df)

    # Q.9) What is the average performance rating by department ?
    dept_avg_performance_rating(hr_data_mnc_df)

    # Q.10) Which Country have the highest concentration of employees ?
    country_wise_employee_conc(hr_data_mnc_df)

    # Q.11) Is there a correlation between performance rating and salary ?
    correlation_performance_salary(hr_data_mnc_df)

    # Q.12) How has the number of hires changed over time (per year) ?
    hires_per_yr(hr_data_mnc_df)

    # Q.13) Compare salaries of Remote vs. On-site employees — is there a significant difference ?
    salary_compare_work_mode_wise(hr_data_mnc_df)

    # Q.14) Find the top 10 employees with the highest salary in each department.
    top_employees_by_department(hr_data_mnc_df)

    # Q.15) Identify departments with the highest attrition rate (Resigned %).
    attrition_rate_by_department(hr_data_mnc_df)

    print('==============================================================')
    print('The Statistical Analysis of HR DATASET of the MNC is completed!')
    print('==============================================================')

# -----------------------------------------------------------
if __name__ == '__main__':
    main()
