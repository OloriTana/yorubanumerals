import streamlit as st
import json

# Yoruba numbers data
yoruba_numbers = { 
    1: {"yoruba": "(Ọ̀)kan", "breakdown": "Base Numeral for 1", "pronunciation": "aw-kan"},
    2: {"yoruba": "Èjì", "breakdown": "Base Numeral for 2", "pronunciation": "ey-jee"},
    3: {"yoruba": "Ẹ̀ta", "breakdown": "Base Numeral for 3", "pronunciation": "eh-tah"},
    4: {"yoruba": "Ẹ̀rin", "breakdown": "Base Numeral for 4", "pronunciation": "eh-reen"},
    5: {"yoruba": "Àrún", "breakdown": "Base Numeral for 5", "pronunciation": "ah-roon"},
    6: {"yoruba": "Ẹ̀fà", "breakdown": "Base Numeral for 6", "pronunciation": "eh-fah"},
    7: {"yoruba": "Èje", "breakdown": "Base Numeral for 7", "pronunciation": "ay-jay"},
    8: {"yoruba": "Ẹ̀jọ", "breakdown": "Base Numeral for 8", "pronunciation": "eh-jaw"},
    9: {"yoruba": "Ẹ̀sán", "breakdown": "Base Numeral for 9", "pronunciation": "eh-sahn"},
    10: {"yoruba": "Ẹ̀wá", "breakdown": "Base Numeral for 10", "pronunciation": "eh-wah"},
    11: {"yoruba": "ọ̀kànlá", "breakdown": "ọ̀kan (1) + lé (added to) + ẹ̀wá (ten)"},
    12: {"yoruba": "èjìlá", "breakdown": "èjì (2) + lé (added to) + ẹ̀wá (ten)"},
    13: {"yoruba": "ẹ̀tàlá", "breakdown": "ẹ̀ta (3) + lé (added to) + ẹ̀wá (ten)"},
    14: {"yoruba": "ẹ̀rìnlá", "breakdown": "ẹ̀rin (4) + lé (added to) + ẹ̀wá (ten)"},
    15: {"yoruba": "àrúndínlógún", "breakdown": "àrún (5) + dín (subtracted from) + ogún (20)"},
    16: {"yoruba": "ẹ̀rindínlógún", "breakdown": "ẹ̀rin (4) + dín (subtracted from) + ogún (20)"},
    17: {"yoruba": "ẹ̀tadínlógún", "breakdown": "ẹ̀ta (3) + dín (subtracted from) + ogún (20)"},
    18: {"yoruba": "èjìdínlógún", "breakdown": "èjì (2) + dín (subtracted from) + ogún (20)"},
    19: {"yoruba": "ọ̀kandínlógún", "breakdown": "ọ̀kan (1) + dín (subtracted from) + ogún (20)"},
    20: {"yoruba": "Ogún", "breakdown": {"Note": "Base Numeral for 20", "Additional note": "Also called 'Okòó', a derivation of 'okùn owó' (a string of money)"}, "pronunciation": "oh-goon"},
    21: {"yoruba": "ọ̀kanlélógún", "breakdown": "ọ̀kan (1) + lé (added to) + ogún (20)"},
    22: {"yoruba": "èjìlélógún", "breakdown": "èjì (2) + lé (added to) + ogún (20)"},
    23: {"yoruba": "ẹ̀talélógún", "breakdown": "ẹ̀ta (3) + lé (added to) + ogún (20)"},
    24: {"yoruba": "ẹ̀rinlélógún", "breakdown": "ẹ̀rin (4) + lé (added to) + ogún (20)"},
    25: {"yoruba": "àrúndínlọ́gbọ̀n", "breakdown": "àrún (5) + dín (subtracted from) + ọgbọ̀n (30)"},
    26: {"yoruba": "ẹ̀rindínlọ́gbọ̀n", "breakdown": "ẹ̀rin (4) + dín (subtracted from) + ọgbọ̀n (30)"},
    27: {"yoruba": "ẹ̀tadínlọ́gbọ̀n", "breakdown": "ẹ̀ta (3) + dín (subtracted from) + ọgbọ̀n (30)"},
    28: {"yoruba": "èjìdínlọ́gbọ̀n", "breakdown": "èjì (2) + dín (subtracted from) + ọgbọ̀n (30)"},
    29: {"yoruba": "ọ̀kandínlọ́gbọ̀n", "breakdown": "ọ̀kan (1) + dín (subtracted from) + ọgbọ̀n (30)"},
    30: {"yoruba": "ọgbọ̀n", "breakdown": "Base numeral for 30"},
    31: {"yoruba": "ọ̀kanlélọ́gbọ̀n", "breakdown": "ọ̀kan (1) + lé (added to) + ọgbọ̀n (30)"},
    32: {"yoruba": "èjìlélọ́gbọ̀n", "breakdown": "èjì (2) + lé (added to) + ọgbọ̀n (30)"},
    33: {"yoruba": "ẹ̀talélọ́gbọ̀n", "breakdown": "ẹ̀ta (3) + lé (added to) + ọgbọ̀n (30)"},
    34: {"yoruba": "ẹ̀rinlélọ́gbọ̀n", "breakdown": "ẹ̀rin (4) + lé (added to) + ọgbọ̀n (30)"},
    35: {"yoruba": "àrúndínlógójì", "breakdown": "àrún (5) + dín (subtracted from) + ọgójì (40)"},
    36: {"yoruba": "ẹ̀rindínlógójì", "breakdown": "ẹ̀rin (4) + dín (subtracted from) + ọgójì (40)"},
    37: {"yoruba": "ẹ̀tadínlógójì", "breakdown": "ẹ̀ta (3) + dín (subtracted from) + ọgójì (40)"},
    38: {"yoruba": "èjìdínlógójì", "breakdown": "èjì (2) + dín (subtracted from) + ọgójì (40)"},
    39: {"yoruba": "ọ̀kandínlógójì", "breakdown": "ọ̀kan (1) + dín (subtracted from) + ọgójì (40)"},
    40: {"yoruba": "ogójì", "breakdown": "ogún (20) + lọ́nà (multiplied by) + èjì (2)"},
    50: {"yoruba": "àádọ́ta", "breakdown": "àá (10) + dín (subtracted from) + ọgọ́ta (60)"},
    60: {"yoruba": "ọgọ́ta", "breakdown": "ogún (20) + lọ́nà (multiplied by) + ẹ̀ta (3)"},
    70: {"yoruba": "àádọ́rin", "breakdown": "àá (10) + dín (subtracted from) + ọgọ́rin (80)"},
    80: {"yoruba": "ọgọ́rin", "breakdown": "ogún (20) + lọ́nà (multiplied by) + ẹ̀rin (4)"},
    90: {"yoruba": "àádọ́rùn-ún", "breakdown": "àá (10) + dín (subtracted from) + ọgọ́rùn-ún (100)"},
    100: {"yoruba": "ọgọ́rùn-ún", "breakdown": "ogún (20) + lọ́nà (multiplied by) + àrún (5)"},
    181: {"yoruba": "ọ̀kànlélọ́gọ́ọ̀sán", "breakdown": "ọ̀kàn (one) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    182: {"yoruba": "èjìlélọ́gọ́ọ̀sán", "breakdown": "èjì (two) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    183: {"yoruba": "ẹ̀tàlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀ta (three) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    184: {"yoruba": "ẹ̀rinlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀rin (four) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    185: {"yoruba": "àrúnlélọ́gọ́ọ̀sán", "breakdown": "àrún (four) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    186: {"yoruba": "ẹ̀fàlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀fà (four) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    187: {"yoruba": "èjelélọ́gọ́ọ̀sán", "breakdown": "èje (four) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    188: {"yoruba": "ẹ̀jọlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀jọ (four) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    189: {"yoruba": "ẹ̀sánlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀sán (four) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    190: {"yoruba": "ẹ̀wádínlúgba", "breakdown": "ẹ̀wá (four) + lé ní (added to) + ọgọ́ọ̀sán (180)"},
    191: {"yoruba": "ẹ̀sándínlúgba", "breakdown": "ẹ̀sán (nine) + dín ní (subtracted from) + igba (200)"},
    192: {"yoruba": "ẹ̀jọdínlúgba", "breakdown": "ẹ̀jọ (nine) + dín ní (subtracted from) + igba (200)"},
    193: {"yoruba": "èjedínlúgba", "breakdown": "èje (nine) + dín ní (subtracted from) + igba (200)"},
    194: {"yoruba": "ẹ̀fàdínlúgba", "breakdown": "ẹ̀fà (nine) + dín ní (subtracted from) + igba (200)"},
    195: {"yoruba": "àrúndínlúgba", "breakdown": "àrún (nine) + dín ní (subtracted from) + igba (200)"},
    196: {"yoruba": "ẹ̀rindínlúgba", "breakdown": "ẹ̀rin (nine) + dín ní (subtracted from) + igba (200)"},
    197: {"yoruba": "ẹ̀tadínlúgba", "breakdown": "ẹ̀tà (nine) + dín ní (subtracted from) + igba (200)"},
    198: {"yoruba": "èjìdínlúgba", "breakdown": "èjì (nine) + dín ní (subtracted from) + igba (200)"},
    199: {"yoruba": "ọ̀kandínlúgba", "breakdown": "ọ̀kan (nine) + dín ní (subtracted from) + igba (200)"},
    200: {"yoruba": "igba", "breakdown": "Base numeral for 200"},
    210: {"yoruba": "ẹ̀wálérúgba", "breakdown": "ẹ̀wá (10) + lé (added to) + igba (200)"},
    215: {"yoruba": "àrúndínlókòólérúgba", "breakdown": "àrún (five) + dín ní (subtracted from) + okòólérúgba (two hundred and twenty)"},
    220: {"yoruba": "okòólérúgba", "breakdown": "okòó (twenty) + lé ní (added to) + igba (two hundred)"},
    221: {"yoruba": "ọ̀kanléokòólérúgba", "breakdown": "ọ̀kan (twenty-one) + lé ní (added to) + okòólérúgba (two hundred and twenty)"},
    225: {"yoruba": "àrúnléokòólérúgba", "breakdown": "àrún (twenty-five) + lé ní (added to) + okòólérúgba (two hundred and twenty)"},
    229: {"yoruba": "ẹ̀sánléokòólérúgba", "breakdown": "ẹ̀sán (twenty-nine) + lé ní (added to) + okòólérúgba (two hundred and twenty)"},
    230: {"yoruba": "ẹ̀wádínlójìlérúgba", "breakdown": "ẹ̀wá (ten) + dín ní (subtracted from) + òjìlérúgba (two hundred and forty)"},
    340: {"yoruba": "òjìlélọ́ọ̀dúnrún", "breakdown": "òjì (40) + lé ní (added to) + ọ̀dúnrún (300)"},
    450: {"yoruba": "ẹ̀wádínlọ́talérinwó", "breakdown": "ẹ̀wá (10) + dín (subtracted from) + ọ̀ta (60) + lé ní (added to) irinwo (400)"},
    600: {"yoruba": "ẹgbẹ̀ta", "breakdown": "igba (200) lọ́nà (multiplied by) + ẹ̀ta (3)"},
    1000: {"yoruba": "ẹgbẹ̀rún", "breakdown": "igba (200) lọ́nà (multiplied by) + àrún (5)"},
    5000: {"yoruba": "ẹ̀ẹ́dẹ́gbàáta", "breakdown": "ẹgbẹ̀rún (1000) + dín (subtracted from) + ẹgbẹ̀ta (6000)"},
    20000: {"yoruba": "ẹgbàáwàá/ọ̀kẹ́ kan", "breakdown": "ẹgbàá (2000) lọ́nà (multiplied by) + ẹ̀wá (10)", "Additional note": "'Ọ̀kẹ́' is the traditional name for 20,000"},
    1000000: {"yoruba": "ẹgbàáwàá/ọ̀kẹ́ àádọ́ta", "breakdown": "ẹgbàáwàá/ọ̀kẹ́ (20,000) lọ́nà (multiplied by) + àádọ́ta (50)"},
    1000000000: {"yoruba": "ẹgbàáwàá/ọ̀kẹ́ ẹgbàáàrúndínlọ́gbọ̀n", "breakdown": "ẹgbàáwàá/ọ̀kẹ́ (20,000) lọ́nà (multiplied by) + ẹgbàáàrúndínlọ́gbọ̀n (5000)"}
}

st.title("Yoruba Number Breakdown App")

number = st.number_input("Enter a number:", min_value=1, step=1)

if number in yoruba_numbers:
    data = yoruba_numbers[number]
    st.subheader(f"Number: {number}")
    st.write(f"*Yoruba:* {data['yoruba']}")
    
    if 'breakdown' in data:
        st.write("*Breakdown:*")
        if not isinstance(data['breakdown'], dict):
             st.write(data['breakdown'])
        else:
            for key, value in data['breakdown'].items():
                st.write(f"- *{key}*: {value}")
    if 'pronunciation' in data:
        st.write("*Pronunciation:*")
        if not isinstance(data['pronunciation'], dict):
            st.write(data['pronunciation'])
        else:
             for key, value in data("pronunciation", "Pronunciation not available"):
                st.write(f"*{Pronunciation}*: {data[pronunciation]}")
else:
    st.warning(f"'{number}' is currently not available")
