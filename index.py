#Project-2: Unit Converter App using Streamlit.

import streamlit as st

#Building profile:
st.sidebar.image("https://avatars.githubusercontent.com/u/170619187?s=400&u=f758c87ccd8a92db5993514049855df20f7d80aa&v=4", width=100)
st.sidebar.markdown("### Ekta Khatri")
st.sidebar.markdown("💼 **Developer**")
st.sidebar.markdown("[🔗 Streamlit] (https://share.streamlit.io/user/ektakhatri456)")
st.sidebar.markdown("[🔗 LinkedIn] (https://www.linkedin.com/in/ekta-khatri-7b6b4a1a8/)")


st.title("🚀Unit Converter using Streamlit")

st.markdown("###  Converts units from one form to another.")
st.write("Welcome! Please select the type of conversion you want to perform.")

# Conversion types:
category = st.selectbox("Select the Conversion type:", ["Length", "Time", "Weight","Temperature", "Volume"])

def convert_units(category,value,unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value * 1.60934
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Centimeters to Inches":
            return value * 0.393701
        elif unit == "Inches to Centimeters":
            return value / 0.393701


    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462 

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fareheit to Celsius":
            return (value - 32) * 5/9
        elif unit== "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32

    elif category == "Volume":
        if unit == "Liters to Milliliters":
            return value * 1000
        elif unit == "Milliliters to Liters":
            return value / 1000
        elif unit == "Liters to Gallons":
            return value * 0.264172
        elif unit == "Gallons to Liters":
            return value / 0.264172

#Conversions selected by user:

if category == "Length":
    unit = st.selectbox("Select the unit to convert from:", ["Kilometers to Miles", "Miles to kilometers", "Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeters"])

elif category == "Time":
    unit = st.selectbox("Select the unit to convert from:", ["Seconds to Minutes", "Minutes to seconds", "Minutes to Hours", "Hours to minutes", "Hours to Days", "Days to Hours"])

elif category == "Weight":
    unit = st.selectbox("Select the unit to convert from:", ["Kilograms to Pounds", "Pounds to Kilograms"])

elif category == "Temperature":
    unit = st.selectbox("Select the unit to convert from:", ["Celsius to Fahrenheit", "Fareheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius", "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"])

elif category == "Volume":
    unit = st.selectbox("Select the unit to convert from:", ["Liters to Milliliters", "Milliliters to Liters", "Liters to Gallons", "Gallons to Liters"])

value = st.number_input("Enter the value to convert:")
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.1f}") # The purpose of using '.1f' is to display one digit after the decimal point   

