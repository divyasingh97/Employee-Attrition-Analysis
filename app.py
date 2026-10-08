import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("models/employee_attrition_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Employee Attrition Analysis",
    page_icon="👨‍💼",
    layout="wide"
)


# Title
st.title("👨‍💼 Employee Attrition Analysis")
st.write("Predict whether an employee is likely to leave the company.")


st.divider()


# Employee information
st.header("Enter Employee Information")


col1, col2, col3 = st.columns(3)


with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    business_travel = st.selectbox(
        "Business Travel",
        ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
    )

    daily_rate = st.number_input(
        "Daily Rate",
        min_value=100,
        max_value=1500,
        value=800
    )

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=30,
        value=5
    )

    education = st.selectbox(
        "Education Level",
        [1, 2, 3, 4, 5],
        index=1
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

    environment_satisfaction = st.selectbox(
        "Environment Satisfaction",
        [1, 2, 3, 4],
        index=2
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    hourly_rate = st.number_input(
        "Hourly Rate",
        min_value=30,
        max_value=100,
        value=60
    )


with col2:
    job_involvement = st.selectbox(
        "Job Involvement",
        [1, 2, 3, 4],
        index=2
    )

    job_level = st.selectbox(
        "Job Level",
        [1, 2, 3, 4, 5],
        index=0
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [1, 2, 3, 4],
        index=2
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=20000,
        value=5000
    )

    monthly_rate = st.number_input(
        "Monthly Rate",
        min_value=2000,
        max_value=27000,
        value=14000
    )

    num_companies_worked = st.number_input(
        "Number of Companies Worked",
        min_value=0,
        max_value=10,
        value=1
    )

    overtime = st.selectbox(
        "OverTime",
        ["Yes", "No"]
    )

    percent_salary_hike = st.number_input(
        "Percent Salary Hike",
        min_value=10,
        max_value=30,
        value=15
    )


with col3:
    performance_rating = st.selectbox(
        "Performance Rating",
        [3, 4],
        index=0
    )

    relationship_satisfaction = st.selectbox(
        "Relationship Satisfaction",
        [1, 2, 3, 4],
        index=2
    )

    stock_option_level = st.selectbox(
        "Stock Option Level",
        [0, 1, 2, 3],
        index=0
    )

    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=40,
        value=8
    )

    training_times_last_year = st.number_input(
        "Training Times Last Year",
        min_value=0,
        max_value=10,
        value=3
    )

    work_life_balance = st.selectbox(
        "Work Life Balance",
        [1, 2, 3, 4],
        index=2
    )

    years_at_company = st.number_input(
        "Years At Company",
        min_value=0,
        max_value=40,
        value=5
    )

    years_in_current_role = st.number_input(
        "Years In Current Role",
        min_value=0,
        max_value=20,
        value=3
    )

    years_since_last_promotion = st.number_input(
        "Years Since Last Promotion",
        min_value=0,
        max_value=15,
        value=1
    )

    years_with_curr_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        max_value=20,
        value=3
    )


# Create input dataframe
input_data = pd.DataFrame({
    "Age": [age],
    "BusinessTravel": [business_travel],
    "DailyRate": [daily_rate],
    "Department": [department],
    "DistanceFromHome": [distance_from_home],
    "Education": [education],
    "EducationField": [education_field],
    "EnvironmentSatisfaction": [environment_satisfaction],
    "Gender": [gender],
    "HourlyRate": [hourly_rate],
    "JobInvolvement": [job_involvement],
    "JobLevel": [job_level],
    "JobRole": [job_role],
    "JobSatisfaction": [job_satisfaction],
    "MaritalStatus": [marital_status],
    "MonthlyIncome": [monthly_income],
    "MonthlyRate": [monthly_rate],
    "NumCompaniesWorked": [num_companies_worked],
    "OverTime": [overtime],
    "PercentSalaryHike": [percent_salary_hike],
    "PerformanceRating": [performance_rating],
    "RelationshipSatisfaction": [relationship_satisfaction],
    "StockOptionLevel": [stock_option_level],
    "TotalWorkingYears": [total_working_years],
    "TrainingTimesLastYear": [training_times_last_year],
    "WorkLifeBalance": [work_life_balance],
    "YearsAtCompany": [years_at_company],
    "YearsInCurrentRole": [years_in_current_role],
    "YearsSinceLastPromotion": [years_since_last_promotion],
    "YearsWithCurrManager": [years_with_curr_manager]
})


st.divider()


# Prediction button
if st.button("🔍 Predict Employee Attrition", use_container_width=True):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Prediction: Employee is likely to leave.")
    else:
        st.success("✅ Prediction: Employee is likely to stay.")