import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Creating a simple App
# Title of the app
st.title('My First Streamlit App')

# Add a text input box
name = st.text_input('Enter your name:')

# Display the input text
if name:
    st.write(f'Hello, {name}!')



# Building Interactive Widgets

if st.button('Click Me'):
    st.write(f'Hello, {name}!')

number = st.slider('Select a number', 0, 100)
st.write(f'You selected: {number}')


option = st.selectbox('Choose an option', ['Mumbai', 'Pune', 'Jaipur'])
st.write(f'You selected: {option}')

agree = st.checkbox('I agree')
if agree:
    st.write('You agreed!')


#Displaying Data
st.write('## **Displaying Data**')


data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
df = pd.DataFrame(data)
st.write(df)


fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)

## **Customizing Your App**
st.write('## **Customizing Your App**')
st.sidebar.title('Sidebar')
st.sidebar.write('This is the sidebar')

st.markdown('### Markdown Title')
st.markdown('*This is italicized text*')


st.write('---')  # Creates a horizontal line
st.write('Footer content here')





