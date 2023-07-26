from turtle import st
import streamlit as st
import numpy as np
import sklearn
import tensorflow as tf

# Loading Model
model = tf.keras.models.load_model("F:/projects/Wine_Quality_Prediction_Web_App/Model/saved_model")

# creating a function for prediction
def Wine_Quality_prediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                            free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
    # Convert input data to float type
    input_data = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                           free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol], dtype=np.float32)
    input_data_as_numpy_array = np.expand_dims(input_data, axis=0)
    prediction = model.predict(input_data_as_numpy_array)
    prediction = np.argmax(prediction, axis=1)
    return f"The Wine Quality will be: {float(prediction):.6f}"


def convert_to_float_with_six_decimals(input_string):
    try:
        # Try converting the input string to a float and round to 6 decimal places
        return round(float(input_string), 6)
    except ValueError:
        # Return 0.0 if the conversion fails
        return 0.0

def main():
    # Add custom CSS styles
    st.markdown(
        """
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }

        h1 {
            color: #007bff;
            text-align: center;
            margin-bottom: 20px;
        }

        p {
            line-height: 1.6;
            margin-bottom: 10px;
        }

        .button-primary {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .button-primary:hover {
            background-color: #0056b3;
        }

        .result {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # giving a Title
    st.title('Wine Quality Prediction Web App')

    # Create the text input menu using streamlit
    fixed_acidity_str = st.text_input("Fixed Acidity", key='fixed_acidity')
    fixed_acidity = convert_to_float_with_six_decimals(fixed_acidity_str)

    # Create the text input menu using streamlit
    volatile_acidity_str = st.text_input("Volatile Acidity", key='volatile_acidity')
    volatile_acidity = convert_to_float_with_six_decimals(volatile_acidity_str)

    # Create the text input menu using streamlit
    citric_acid_str = st.text_input("Citric Acid", key='citric_acid')
    citric_acid = convert_to_float_with_six_decimals(citric_acid_str)

    # Create the text input menu using streamlit
    residual_sugar_str = st.text_input("Residual Sugar", key='residual_sugar')
    residual_sugar = convert_to_float_with_six_decimals(residual_sugar_str)

    # Create the text input menu using streamlit
    chlorides_str = st.text_input("Chlorides", key='chlorides')
    chlorides = convert_to_float_with_six_decimals(chlorides_str)

    # Create the text input menu using streamlit
    free_sulfur_dioxide_str = st.text_input("Free Sulfur Dioxide", key='free_sulfur_dioxide')
    free_sulfur_dioxide = convert_to_float_with_six_decimals(free_sulfur_dioxide_str)

    # Create the text input menu using streamlit
    total_sulfur_dioxide_str = st.text_input("Total Sulfur Dioxide", key='total_sulfur_dioxide')
    total_sulfur_dioxide = convert_to_float_with_six_decimals(total_sulfur_dioxide_str)

    # Create the text input menu using streamlit
    density_str = st.text_input("Density", key='density')
    density = convert_to_float_with_six_decimals(density_str)

    # Create the text input menu using streamlit
    pH_str = st.text_input("pH", key='pH')
    pH = convert_to_float_with_six_decimals(pH_str)

    # Create the text input menu using streamlit
    sulphates_str = st.text_input("Sulphates", key='sulphates')
    sulphates = convert_to_float_with_six_decimals(sulphates_str)

    # Create the text input menu using streamlit
    alcohol_str = st.text_input("Alcohol", key='alcohol')
    alcohol = convert_to_float_with_six_decimals(alcohol_str)

    # code for prediction
    prediction = ''

    # creating button for prediction
    if st.button('Result'):
        # Check if all input fields are filled
        if fixed_acidity and volatile_acidity and citric_acid and residual_sugar and chlorides and \
                free_sulfur_dioxide and total_sulfur_dioxide and density and pH and sulphates and alcohol:
            prediction = Wine_Quality_prediction(fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                                                 chlorides,
                                                 free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates,
                                                 alcohol)
            st.success(prediction)
        else:
            st.warning("Please fill all the input fields to get the prediction.")


if __name__ == '__main__':
    main()
