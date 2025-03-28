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
    10: {"yoruba": "Mẹwa", "breakdown": {"me": "to have", "wa": "ten"}, "pronunciation": "Meh-wah"},
    20: {"yoruba": "Ogun", "breakdown": "Basic Number", "pronunciation": "Oh-goon"}
}

st.title("Yoruba Number Breakdown App")

number = st.number_input("Enter a number:", min_value=1, step=1)

if number in yoruba_numbers:
    data = yoruba_numbers[number]
    st.subheader(f"Number: {number}")
    st.write(f"**Yoruba:** {data['yoruba']}")
    st.write(f"**Pronunciation:** {data['pronunciation']}")

    if 'breakdown' in data:
        st.write("**Breakdown:**")
        if not isinstance(data['breakdown'], dict):
             st.write(data['breakdown'])
        else:
            for key, value in data['breakdown'].items():
                st.write(f"- **{key}**: {value}")
else:
    st.warning(f"'{number}' is currently not available")
