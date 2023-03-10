import streamlit as st
from PIL import Image

import pickle
model = pickle.load(open('model1.pkl', 'rb'))


def run():
    img1 = Image.open('bank.jpeg')
    img1 = img1.resize((160, 160))
    imgg = '<img src="bank.jpeg">'
    title = '<b><p style="text-align:center;color:pink;font-size:50px;">Bank Loan Prediction</p></b> '
    st.image(img1, use_column_width=False)
    body = f'<style> </style>'
    st.markdown(title, unsafe_allow_html=True)
    st.markdown(body, unsafe_allow_html=True)

    account = st.text_input('Bank Account number')

    fullname = st.text_input('Full Name')

    gender = ('Female', 'Male')
    gender_options = list(range(len(gender)))
    gen = st.selectbox("Gender", gender_options,
                       format_func=lambda x: gender[x])

    education_display = ('Not Graduate', 'Graduate')
    education_options = list(range(len(education_display)))
    education = st.selectbox("Education", education_options,
                             format_func=lambda x: education_display[x])

    martial_display = ('No', 'Yes')
    martial_options = list(range(len(martial_display)))
    martial = st.selectbox("Martial Status", martial_options,
                           format_func=lambda x: martial_display[x])

    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",  dep_options,
                       format_func=lambda x: dep_display[x])

    employment_display = ('Job', 'Business')
    employment_options = list(range(len(employment_display)))
    employment = st.selectbox("Employment Status", employment_options,
                              format_func=lambda x: employment_display[x])

    property_display = ('Rural', 'Semi-Urban', 'Urban')
    property_options = list(range(len(property_display)))
    property = st.selectbox("Area of property", property_options,
                            format_func=lambda x: property_display[x])

    coappincome = st.number_input(
        "Co-Applicant's Monthly Income($)", value=0)

    credit_display = ('Between 300 to 500', 'Above 500')
    credit_options = list(range(len(credit_display)))
    credit = st.selectbox("Credit Score", credit_options,
                          format_func=lambda x: credit_display[x])

    monthly_income = st.number_input("Applicant's Monthly Income", value=0)

    loan_amt = st.number_input("Loan Amount", value=0)

    duration_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    duration_options = range(len(duration_display))
    dur = st.selectbox("Duration of loan", duration_options,
                       format_func=lambda x: duration_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        boxes = [[gen, martial, dep,  education, employment, monthly_income, coappincome,
                  loan_amt, duration, credit, property]]
        print(boxes)
        prediction = model.predict(boxes)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                ' you will not get a loan as per the calculations of the bank.'
            )
        else:
            st.success(
                ' Congratulations!! you will get the loan from Bank'
            )


run()
