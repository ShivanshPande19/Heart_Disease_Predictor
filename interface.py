import streamlit as st
import time
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Systolic Pressure:

# Normal Range: Typically less than 120 mm Hg
# Elevated Range: 120-129 mm Hg
# Hypertension Stage 1: 130-139 mm Hg
# Hypertension Stage 2: 140 mm Hg or higher 0 184
# Diastolic Pressure:


# Normal Range: Typically less than 80 mm Hg
# Elevated Range: 80-89 mm Hg
# Hypertension Stage 1: 90-99 mm Hg
# Hypertension Stage 2: 100 mm Hg or higher 0 112
st.title("HEART DISEASE PREDICTION")
st.divider()
with open('Heart_Predictor.pickle', 'rb') as model_file:
    model = pickle.load(model_file)
st.header('Question 1: Choose your gender')
gender = st.radio('Select your answer', ['Male', 'Female'])
st.write(gender)
def interpret_bmi(bmi):
    if bmi < 18.5:
        return st.error("Underweight")
    elif 18.5 <= bmi <=24.9:
        return st.info("Normal weight")
    elif 25 <= bmi < 29.9:
        return st.warning("Overweight")
    else:
        return st.warning("Obese")
def interpret_heartrate(rate):
    if rate<60:
        return st.warning('Your heart rate is too low')
    elif 60<=rate<=100:
        return st.info('Heart rate is in the normal range')
    else:
        return st.warning('Your heart rate is too high.Please take care')
def interpret_glucose(gluc):
    if(gluc<50):
        return st.warning('You may have hypogicemia ')
    elif(50<=gluc<70):
        return st.error('Your glucose is quite low')
    elif(70<=gluc<=110):
        return st.info('Your glucose level is normal')
    elif(110<gluc<=120):
        return st.error('Your glucose is quite high')
    elif(gluc>120):
        return st.warning('Your glucose level is extemely high. Please check for diabetes')

def get_systolic_category(systolic_bp):
    if(systolic_bp<110):
        return st.error("Low blood pressure")
    if 110<=systolic_bp < 130:
        return st.info("Normal")
    elif 130 <= systolic_bp <= 139:
        return st.error("Hypertensive Stage 1")
    elif 140 <= systolic_bp <= 159:
        return st.warning("Hypertensive Stage 2")
    elif systolic_bp >= 160:
        return st.warning("Hypertensive Stage 3")

def get_diastolic_category(diastolic_bp):
    if(diastolic_bp<70):
        return st.error("Low blood pressure")
    if 70<=diastolic_bp < 90:
        return st.info("Normal")
    elif 90 <= diastolic_bp <= 99:
        return st.warning("Hypertensive Stage 2")
    elif diastolic_bp >= 100:
        return st.warning("Hypertensive Stage 3")
    else:
        return "Invalid Diastolic Blood Pressure"
st.header('Question 2: How old are you?')
age = st.slider("Select your answer", 0, 130, 5)
st.write(f"You are {age} years old")

st.header('Question 3: Do you smoke?')
smoke = st.radio('Select your answer', ['Yes', 'No'])
message = 'You smoke.' if smoke == 'Yes' else "You don't smoke."
st.write(message)
cigs = 0 if smoke == "No" else 5

st.header('Question 4: Average number of cigarettes you smoke in a day. Select 0 if you don\'t.')
numberOfCigs = st.slider("Select your answer", 0, 100, cigs)
if numberOfCigs == 0:
    st.write('You don\'t smoke')
else:
    st.write(f"You smoke an average of {numberOfCigs} cigarettes in a day")

st.header('Question 5: Are you on BP Meds?')
BPMeds = st.radio('Select your answer', ['Yes I am on BP Meds', 'No I am not on it'])
st.write(BPMeds[0:3])
st.header('Question 6: Any history of stroke?')
stroke = st.radio('Select your answer', ['Yes, I had stroke in the past or in current feature', 'No I dont have any stroke history'])
st.write(stroke[0:3])
st.header('Question 7: Any history of HyperTension?')
hypertension = st.radio('Select your answer', ['Yes, I had  hypertension in the past or in current feature', 'No I dont have any hypertension history'])
st.write(hypertension[0:3])
st.header('Question 8: Any history of diabetes?')
diabetes=st.radio('Select your answer', ['Yes, I had  diabetes in the past or in current feature', 'No I dont have any diabetes history'])
st.write(diabetes[0:3])
st.header('Question 9 What is your cholestrol level?')
st.caption('Total normal cholestrol is less than 200 usually 150-200')
chol=st.number_input('Your cholestrol')
st.write(f"Your cholestrol is{chol}")
if chol:
    if(chol<200):
        st.info("An optimal range")
    elif(200<=chol<=250):
        st.error("Moderately high range")
    else:
        st.warning("Very high cholestrol")

st.header('Question 10 What is your BMI?')
st.caption('Normal is 18.5 to 24.9')
bmi=st.number_input('Your BMI')
st.write(f"Your BMI is{bmi}")
if bmi:
    interpret_bmi(bmi)

st.header('Question 11 What is your heart rate?')
st.caption('Normal range is 60-100')
heart_rate=st.number_input('Your heart rate')
st.write(f"Your heart rate is{heart_rate}")
if heart_rate:
    interpret_heartrate(heart_rate)

st.header('Question 12 What is your glucose level?')
st.caption('Normal is 70-110')
glucose=st.number_input('Your glucose level')
st.write(f"Your glucose level is{glucose}")
if glucose:
    interpret_glucose(glucose)

st.header('Question 13 What is your systolic blood pressure?')
st.caption("Normal range is 110-130")
syst=st.number_input('Your systolicBP')
st.write(f"Your systolicBP is{syst}")
if syst:
    get_systolic_category(syst)
st.header('Question 14 What is your diastolic blood pressure?')
st.caption("Normal is 70-90")
dias=st.number_input('Your diastolicBP')

st.write(f"Your diastolic BP is{dias}")
if dias:
    get_diastolic_category(dias)
# BEFORE DOING FURTHER ANALYSIS LET ME MAKE A BAR OF NORMAL VALUE
# SO THAT PERSON CAN BE KNOWN HOW MUCH CLOSE OF A VALUE HE I
smokestatus="❌AvoidIt"if smoke=="Yes" else "👍Good"
if(numberOfCigs==0):
    avaeragecl="Good"
elif(0<numberOfCigs<5):
    avaeragecl="Moderate"
elif(5<=numberOfCigs<=10):
    avaeragecl="High"
else:
    avaeragecl="Extreme"

if(chol<=200):
    cholll=0
elif(chol>200):
    cholll=chol-200
if(bmi<18.5):
    bmill="-underweight"
elif(18.5<=bmi<=24.9):
    bmill="normal weight"
elif(bmi>24.9):
    bmill="+over weight"
else:
    bmill="++obese"

# a very normal rate if 80
if(heart_rate<60):
    heartll=heart_rate-60
elif(60<=heart_rate<=100):
    heartll=0
elif(heart_rate>100):
    heartll=heart_rate-100

# coming upon to the glucose level now
if(glucose<70):
    glucosell=glucose-70
elif(70<=glucose<=110):
    glucosell=0
elif(glucose>110):
    glucosell=glucose-110
# coming upon to the systolic and diastolic pressure
if(syst<110):
    systll=syst-110
elif(110<=syst<=130):
    systll=0
elif(syst>130):
    systll=syst-130
if(dias<70):
    diasll=dias-70
elif(70<=dias<=90):
    diasll=0
elif(dias>90):
    diasll=dias-90



st.subheader("You have selected the following things")
col1,col2,col3,col4,col5,col6,col7=st.columns(7)
col1.metric("Gender", gender)
col2.metric("Age", age)
col3.metric("Smoke", smoke,smokestatus,)
col4.metric("AverageCigs",numberOfCigs,avaeragecl)
col5.metric("BPMeds?",BPMeds[0:3])
col6.metric("StrokeHistory",stroke[0:3])
col7.metric("HyperTension?",hypertension[0:3])

col8,col9,col10,col11,col12,col13,col14=st.columns(7)

col8.metric("Diabetes?",diabetes[0:3])
col9.metric("CholestrolLevel",chol,cholll)
col10.metric("BMI",bmi,bmill)
col11.metric("Heart_rate",heart_rate,heartll)
col12.metric("glucose level",glucose,glucosell)
col13.metric("systolic bp",syst,systll)
col14.metric("diastolicBP",dias,diasll)
# now there should be a submit button after which he will be shown the required things
progress_bar=st.progress(0)
if st.button("Submit"):
    # Collect user inputs
    new_sample = pd.DataFrame({
        'male': [1 if gender == 'Male' else 0],
        'age': [age],
        'currentSmoker': [1 if smoke == 'Yes' else 0],
        'cigsPerDay': [numberOfCigs],
        'BPMeds': [1 if BPMeds.startswith('Yes') else 0],
        'prevalentStroke': [1 if stroke.startswith('Yes') else 0],
        'prevalentHyp': [1 if hypertension.startswith('Yes') else 0],
        'diabetes': [1 if diabetes.startswith('Yes') else 0],
        'totChol': [chol],
        'BMI': [bmi],
        'heartRate': [heart_rate],
        'glucose': [glucose],
        'diaBP_2': [dias],
        'sysBP_2': [syst]
    })
    df=pd.read_csv('godcleanedData.csv')
    X=df.drop('TenYearCHD', axis = 'columns')
    y=df['TenYearCHD']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42,stratify=y)
    scaler=StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    new_scaler=scaler.transform(new_sample)
    with open('Heart_Predictor.pickle', 'rb') as model_file:
        model = pickle.load(model_file)
    probability = model.predict_proba(new_scaler)[:, 1]
    for percent_complete in range(100):
        time.sleep(0.01)  
        progress_bar.progress(percent_complete + 1,text='Calculating the probability')
    st.write(f'\nProbability of getting heart disease in the next 10 years: {probability[0]:.2%}')
    progress_bar.empty()



from sklearn.feature_selection import mutual_info_classif
import matplotlib.pyplot as plt

if st.button("Feature Classification"):
    
    with st.spinner('Loading data...'):
    
        
        df = pd.read_csv('godcleanedData.csv')

     
        df = df.drop(columns=['currentSmoker', 'BPMeds'])

  
        X = df.drop('TenYearCHD', axis=1)
        Y = df['TenYearCHD']

        importance = mutual_info_classif(X, Y, random_state=42)

        total_importance = sum(importance)
        normalized_importance = (importance / total_importance) * 100

        feat_importances = pd.DataFrame({'Feature': X.columns, 'Importance': normalized_importance})
        time.sleep(4)

    
    st.success('Data loaded successfully!')

 
    fig, ax = plt.subplots(figsize=(13, 13))
    ax.pie(feat_importances['Importance'], labels=feat_importances['Feature'], autopct='%1.1f%%')
    ax.set_title('Feature Importance using Mutual Information')

 
    st.pyplot(fig)

