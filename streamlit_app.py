import streamlit as st
import json

# Yoruba numbers data
yoruba_numbers = {
    1: {"yoruba": "Ọkan", "breakdown": {"ọkà": "unit, one", "kan": "single"}, "pronunciation": "Oh-kan"},
    2: {"yoruba": "Meji", "breakdown": {"me": "to have", "ji": "double/two"}, "pronunciation": "Meh-jee"},
    3: {"yoruba": "Mẹta", "breakdown": {"me": "to have", "ta": "three"}, "pronunciation": "Meh-tah"},
    4: {"yoruba": "Mẹrin", "breakdown": {"me": "to have", "rin": "four"}, "pronunciation": "Meh-reen"},
    5: {"yoruba": "Marun", "breakdown": {"mar": "to be complete", "un": "five"}, "pronunciation": "Mah-roon"},
    6: {"yoruba": "Mẹfa", "breakdown": {"me": "to have", "fa": "six"}, "pronunciation": "Meh-fah"},
    7: {"yoruba": "Meje", "breakdown": {"me": "to have", "je": "seven"}, "pronunciation": "Meh-jeh"},
    8: {"yoruba": "Mẹjọ", "breakdown": {"me": "to have", "jọ": "eight"}, "pronunciation": "Meh-jaw"},
    9: {"yoruba": "Mẹsan", "breakdown": {"me": "to have", "san": "nine"}, "pronunciation": "Meh-sahn"},
    10: {"yoruba": "Mẹwa", "breakdown": {"me": "to have", "wa": "ten"}, "pronunciation": "Meh-wah"}
}

st.title("Yoruba Number Breakdown App")

number = st.number_input("Enter a number (1-10):", min_value=1, max_value=10, step=1)

if number in yoruba_numbers:
    data = yoruba_numbers[number]
    st.subheader(f"Number: {number}")
    st.write(f"**Yoruba:** {data['yoruba']}")
    st.write(f"**Pronunciation:** {data['pronunciation']}")
    st.write("**Breakdown:**")
    for key, value in data['breakdown'].items():
        st.write(f"- **{key}**: {value}")
else:
    st.warning("Please enter a number between 1 and 10.")
