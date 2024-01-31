import streamlit as st
import pickle

# Load the .pkl file
with open('saved_data.pkl', 'rb') as f:
    data = pickle.load(f)

# Now you can use the loaded data in your Streamlit app
# For example, let's assume data is a dictionary
# You can display its contents using Streamlit widgets

# Display the contents of the loaded data
st.write("Loaded Data:")
st.write(data)

# Access specific elements of the loaded data
# For example, if data is a dictionary
# You can access its keys and values
st.write("Keys:")
st.write(list(data.keys()))

# Or display specific values
st.write("Value of 'key':")
st.write(data['key'])
