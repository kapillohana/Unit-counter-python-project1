import streamlit as st


# Title of the app
st.title("Unit Converter")

# Select the type of conversion
conversion_type = st.selectbox(
    "Select conversion type:",
    ["Length", "Weight", "Temperature", "Volume"]
)

if conversion_type == "Length":
    # Length conversions
    col1, col2 = st.columns(2)
    
    with col1:
        length_value = st.number_input("Enter value:", min_value=0.0)
        from_unit = st.selectbox("From:", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    
    with col2:
        to_unit = st.selectbox("To:", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    
    # Conversion logic for length
    if st.button("Convert"):
        # Convert to meters first
        if from_unit == "meters":
            meters = length_value
        elif from_unit == "kilometers":
            meters = length_value * 1000
        elif from_unit == "centimeters":
            meters = length_value / 100
        elif from_unit == "millimeters":
            meters = length_value / 1000
        elif from_unit == "inches":
            meters = length_value * 0.0254
        elif from_unit == "feet":
            meters = length_value * 0.3048
        elif from_unit == "yards":
            meters = length_value * 0.9144
        elif from_unit == "miles":
            meters = length_value * 1609.344
        
        # Convert from meters to target unit
        if to_unit == "meters":
            result = meters
        elif to_unit == "kilometers":
            result = meters / 1000
        elif to_unit == "centimeters":
            result = meters * 100
        elif to_unit == "millimeters":
            result = meters * 1000
        elif to_unit == "inches":
            result = meters / 0.0254
        elif to_unit == "feet":
            result = meters / 0.3048
        elif to_unit == "yards":
            result = meters / 0.9144
        elif to_unit == "miles":
            result = meters / 1609.344
        
        st.success(f"{length_value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    # Weight conversions
    col1, col2 = st.columns(2)
    
    with col1:
        weight_value = st.number_input("Enter value:", min_value=0.0)
        from_unit = st.selectbox("From:", ["grams", "kilograms", "milligrams", "pounds", "ounces"])
    
    with col2:
        to_unit = st.selectbox("To:", ["grams", "kilograms", "milligrams", "pounds", "ounces"])
    
    # Conversion logic for weight
    if st.button("Convert"):
        # Convert to grams first
        if from_unit == "grams":
            grams = weight_value
        elif from_unit == "kilograms":
            grams = weight_value * 1000
        elif from_unit == "milligrams":
            grams = weight_value / 1000
        elif from_unit == "pounds":
            grams = weight_value * 453.592
        elif from_unit == "ounces":
            grams = weight_value * 28.3495
        
        # Convert from grams to target unit
        if to_unit == "grams":
            result = grams
        elif to_unit == "kilograms":
            result = grams / 1000
        elif to_unit == "milligrams":
            result = grams * 1000
        elif to_unit == "pounds":
            result = grams / 453.592
        elif to_unit == "ounces":
            result = grams / 28.3495
        
        st.success(f"{weight_value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    # Temperature conversions
    col1, col2 = st.columns(2)
    
    with col1:
        temp_value = st.number_input("Enter value:")
        from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    with col2:
        to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    # Conversion logic for temperature
    if st.button("Convert"):
        # Convert to Celsius first
        if from_unit == "Celsius":
            celsius = temp_value
        elif from_unit == "Fahrenheit":
            celsius = (temp_value - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = temp_value - 273.15
        
        # Convert from Celsius to target unit
        if to_unit == "Celsius":
            result = celsius
        elif to_unit == "Fahrenheit":
            result = (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            result = celsius + 273.15
        
        st.success(f"{temp_value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Volume":
    # Volume conversions
    col1, col2 = st.columns(2)
    
    with col1:
        volume_value = st.number_input("Enter value:", min_value=0.0)
        from_unit = st.selectbox("From:", ["liters", "milliliters", "cubic meters", "cubic centimeters", 
                                         "gallons (US)", "gallons (UK)", "quarts", "pints", "cups", "fluid ounces"])
    
    with col2:
        to_unit = st.selectbox("To:", ["liters", "milliliters", "cubic meters", "cubic centimeters", 
                                     "gallons (US)", "gallons (UK)", "quarts", "pints", "cups", "fluid ounces"])
    
    # Conversion logic for volume
    if st.button("Convert"):
        # Convert to liters first
        if from_unit == "liters":
            liters = volume_value
        elif from_unit == "milliliters":
            liters = volume_value / 1000
        elif from_unit == "cubic meters":
            liters = volume_value * 1000
        elif from_unit == "cubic centimeters":
            liters = volume_value / 1000
        elif from_unit == "gallons (US)":
            liters = volume_value * 3.78541
        elif from_unit == "gallons (UK)":
            liters = volume_value * 4.54609
        elif from_unit == "quarts":
            liters = volume_value * 0.946353
        elif from_unit == "pints":
            liters = volume_value * 0.473176
        elif from_unit == "cups":
            liters = volume_value * 0.24
        elif from_unit == "fluid ounces":
            liters = volume_value * 0.0295735
        
        # Convert from liters to target unit
        if to_unit == "liters":
            result = liters
        elif to_unit == "milliliters":
            result = liters * 1000
        elif to_unit == "cubic meters":
            result = liters / 1000
        elif to_unit == "cubic centimeters":
            result = liters * 1000
        elif to_unit == "gallons (US)":
            result = liters / 3.78541
        elif to_unit == "gallons (UK)":
            result = liters / 4.54609
        elif to_unit == "quarts":
            result = liters / 0.946353
        elif to_unit == "pints":
            result = liters / 0.473176
        elif to_unit == "cups":
            result = liters / 0.24
        elif to_unit == "fluid ounces":
            result = liters / 0.0295735
        
        st.success(f"{volume_value} {from_unit} = {result:.4f} {to_unit}")