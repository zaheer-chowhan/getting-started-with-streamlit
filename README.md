# Getting started with Streamlit


## **Introduction**

Streamlit is a powerful and user-friendly framework for creating interactive web applications with Python. It’s especially useful for data scientists and machine learning practitioners who want to visualize their data or share their models with minimal coding effort.

This tutorial helps you to understand the basics of Streamlit or get started with Streamlit. I have included only app.py file, where you can find the code.

## **Prerequisites**

- Basic knowledge of Python programming.
- Familiarity with data manipulation and visualization libraries (e.g., Pandas, Matplotlib).
- Python installed on your system (Python 3.6+ recommended).

## Description

In this tutorial we will understand the basics of streamlit where we will try to explore different components of streamlit with practical implementation.

## Dependencies

* Create Virtual Environment
* Install all the dependencies from requirements.txt

## Let's Get Started

## **Installation**

1. **Install Streamlit**:
   Open your terminal or command prompt and run:
   ```bash
   pip install streamlit
   ```

2. **Verify Installation**:
   To ensure Streamlit is installed correctly, run:
   ```bash
   streamlit --version
   ```

## **Creating a Simple Streamlit App**

1. **Set Up Your Project**:
   Create a new directory for your project and navigate into it:
   ```bash
   mkdir streamlit_app
   cd streamlit_app
   ```

2. **Create a Python Script**:
   Create a new Python file named `app.py`:
   ```bash
   touch app.py
   ```

3. **Write Your First App**:
   Open `app.py` in your favorite text editor and add the following code:
   ```python
   import streamlit as st

   # Title of the app
   st.title('My First Streamlit App')

   # Add a text input box
   name = st.text_input('Enter your name:')

   # Display the input text
   if name:
       st.write(f'Hello, {name}!')
   ```

4. **Run Your Streamlit App**:
   Back in your terminal, run:
   ```bash
   streamlit run app.py
   ```

   This command will start a local server and open the app in your default web browser.

## **Building Interactive Widgets**

Streamlit provides a variety of widgets to make your app interactive. Here’s how to use some of them:

1. **Button**:
   ```python
   if st.button('Click Me'):
       st.write('Button clicked!')
   ```

2. **Slider**:
   ```python
   number = st.slider('Select a number', 0, 100)
   st.write(f'You selected: {number}')
   ```

3. **Select Box**:
   ```python
   option = st.selectbox('Choose an option', ['Option 1', 'Option 2', 'Option 3'])
   st.write(f'You selected: {option}')
   ```

4. **Checkbox**:
   ```python
   agree = st.checkbox('I agree')
   if agree:
       st.write('You agreed!')
   ```

## **Displaying Data**

Streamlit makes it easy to display data and visualizations:

1. **Displaying a DataFrame**:
   ```python
   import pandas as pd

   data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
   df = pd.DataFrame(data)
   st.write(df)
   ```

2. **Displaying Charts**:
   ```python
   import matplotlib.pyplot as plt

   fig, ax = plt.subplots()
   ax.plot([1, 2, 3], [4, 5, 6])
   st.pyplot(fig)
   ```

## **Customizing Your App**

1. **Add Sidebar**:
   ```python
   st.sidebar.title('Sidebar')
   st.sidebar.write('This is the sidebar')
   ```

2. **Add a Markdown**:
   ```python
   st.markdown('### Markdown Title')
   st.markdown('*This is italicized text*')
   ```

3. **Add a Footer**:
   ```python
   st.write('---')  # Creates a horizontal line
   st.write('Footer content here')
   ```

## **Deploying Your App**

1. **Deploy to Streamlit Sharing**:
   - Push your code to a GitHub repository.
   - Go to [Streamlit Sharing](https://share.streamlit.io/) and sign in with GitHub.
   - Click on "New app" and select your repository and branch.

2. **Deploy to Heroku or Other Platforms**:
   Follow platform-specific instructions for deploying Python apps, ensuring that your `requirements.txt` includes `streamlit`.



## **Conclusion**

Congratulations! You’ve just created and deployed your first Streamlit app. With Streamlit, you can easily build interactive data applications and share your work with others.

Feel free to explore more Streamlit widgets and features in the [official documentation](https://docs.streamlit.io/).


## Authors

Mohammed Zaheeruddin Chowhan

