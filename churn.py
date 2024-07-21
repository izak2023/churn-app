import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the Streamlit app
st.title("Churn web app")

# Load the CSV data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Path to the CSV file
csv_file_path = "C:\\Users\\HP\\Downloads\\churn\\churn_data.csv"

# Load data
data = load_data(csv_file_path)

# Display the data in a table
st.write("### Churn Data")
st.write(data)

# Add a dropdown to filter the data based on a column value
column_to_filter = st.selectbox("Select Column to Filter", data.columns)
unique_values = data[column_to_filter].unique()
selected_value = st.selectbox(f"Select {column_to_filter} Value", unique_values)

# Filter data based on the selected value
filtered_data = data[data[column_to_filter] == selected_value]

# Display filtered data
st.write(f"### Filtered Data by {column_to_filter} = {selected_value}")
st.write(filtered_data)

# Summary statistics
st.write("### Summary Statistics")
st.write(filtered_data.describe())

# Display data in a chart
st.write("### Data Chart")
chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])

if chart_type == "Line Chart":
    st.line_chart(filtered_data)
elif chart_type == "Bar Chart":
    fig = px.bar(filtered_data, x=filtered_data.columns[0], y=filtered_data.columns[1])
    st.plotly_chart(fig)
elif chart_type == "Scatter Plot":
    fig = px.scatter(filtered_data, x=filtered_data.columns[0], y=filtered_data.columns[1])
    st.plotly_chart(fig)

# Input fields for features
st.write("### Input Features")

# Create input fields for each feature
input_data = {}
for column in data.columns:
    input_value = st.text_input(f"Enter {column}", "")
    input_data[column] = input_value

# Add a validation button
if st.button("Validate"):
    # Display the entered data
    st.write("### Entered Data")
    st.write(input_data)
    
    # Optionally, add more validation logic here
    st.success("Validation successful!")

# Add a prediction button
if st.button("Predict"):
    # Convert input data to a DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Ensure all input values are numeric, converting if necessary
    input_df = input_df.apply(pd.to_numeric, errors='coerce')
    
    # Check for missing values
    if input_df.isnull().values.any():
        st.error("Please provide valid numeric inputs for all features.")
    else:
        # Make prediction
        prediction = model.predict(input_df)
        
        # Display the prediction
        st.write("### Prediction")
        st.write(f"The predicted value is: {prediction[0]}")