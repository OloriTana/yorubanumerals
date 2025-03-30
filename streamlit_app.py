import streamlit as st
import json

# Yoruba numbers data
yoruba_numbers = { 
    1: {"yoruba": "(ọ̀)kan", "breakdown": "Base Numeral for 1", "pronunciation": "aw-kon"},
    2: {"yoruba": "èjì", "breakdown": "Base Numeral for 2", "pronunciation": "ay-jee"},
    3: {"yoruba": "ẹ̀ta", "breakdown": "Base Numeral for 3", "pronunciation": "eh-tah"},
    4: {"yoruba": "ẹ̀rin", "breakdown": "Base Numeral for 4", "pronunciation": "eh-reen"},
    5: {"yoruba": "àrún", "breakdown": "Base Numeral for 5", "pronunciation": "ah-roon"},
    6: {"yoruba": "ẹ̀fà", "breakdown": "Base Numeral for 6", "pronunciation": "eh-fah"},
    7: {"yoruba": "èje", "breakdown": "Base Numeral for 7", "pronunciation": "ay-jay"},
    8: {"yoruba": "ẹ̀jọ", "breakdown": "Base Numeral for 8", "pronunciation": "eh-jaw"},
    9: {"yoruba": "ẹ̀sán", "breakdown": "Base Numeral for 9", "pronunciation": "eh-sahn"},
    10: {"yoruba": "ẹ̀wá", "breakdown": "Base Numeral for 10", "pronunciation": "eh-wah"},
    11: {"yoruba": "ọ̀kànlá", "breakdown": {"Arithmetic breakdown": "ọ̀kan (1) + ẹ̀wá (ten)", "Explanation": "The syntax is 'ọ̀kan lé ẹ̀wá' (1 + 10). 'lé ẹ̀wá' becomes 'lá' by **deletion** and the low tone on ẹ̀ is transferred to the preceding vowel.", "Note": "This explanation applies to numerals 11 to 14."}},
    12: {"yoruba": "èjìlá", "breakdown": "èjì (2) + ẹ̀wá (ten)"},
    13: {"yoruba": "ẹ̀tàlá", "breakdown": "ẹ̀ta (3) + ẹ̀wá (ten)"},
    14: {"yoruba": "ẹ̀rìnlá", "breakdown": "ẹ̀rin (4) + ẹ̀wá (ten)"},
    15: {"yoruba": "àrúndínlógún", "breakdown": "àrún (5) - ogún (20)"},
    16: {"yoruba": "ẹ̀rindínlógún", "breakdown": "ẹ̀rin (4) - ogún (20)"},
    17: {"yoruba": "ẹ̀tadínlógún", "breakdown": "ẹ̀ta (3) - ogún (20)"},
    18: {"yoruba": "èjìdínlógún", "breakdown": "èjì (2) - ogún (20)"},
    19: {"yoruba": "ọ̀kandínlógún", "breakdown": "ọ̀kan (1) - ogún (20)"},
    20: {"yoruba": "Ogún", "breakdown": {"Note": "Base Numeral for 20", "Additional note": "Also called 'Okòó', a derivation of 'okùn owó' (a string of money)"}, "pronunciation": "oh-goon"},
    21: {"yoruba": "ọ̀kanlélógún", "breakdown": "ọ̀kan (1) + ogún (20)"},
    22: {"yoruba": "èjìlélógún", "breakdown": "èjì (2) + ogún (20)"},
    23: {"yoruba": "ẹ̀talélógún", "breakdown": "ẹ̀ta (3) + ogún (20)"},
    24: {"yoruba": "ẹ̀rinlélógún", "breakdown": "ẹ̀rin (4) + ogún (20)"},
    25: {"yoruba": "àrúndínlọ́gbọ̀n", "breakdown": "àrún (5) - ọgbọ̀n (30)"},
    26: {"yoruba": "ẹ̀rindínlọ́gbọ̀n", "breakdown": "ẹ̀rin (4) - ọgbọ̀n (30)"},
    27: {"yoruba": "ẹ̀tadínlọ́gbọ̀n", "breakdown": "ẹ̀ta (3) - ọgbọ̀n (30)"},
    28: {"yoruba": "èjìdínlọ́gbọ̀n", "breakdown": "èjì (2) - ọgbọ̀n (30)"},
    29: {"yoruba": "ọ̀kandínlọ́gbọ̀n", "breakdown": "ọ̀kan (1) - ọgbọ̀n (30)"},
    30: {"yoruba": "ọgbọ̀n", "breakdown": "Base numeral for 30"},
    31: {"yoruba": "ọ̀kanlélọ́gbọ̀n", "breakdown": "ọ̀kan (1) + ọgbọ̀n (30)"},
    32: {"yoruba": "èjìlélọ́gbọ̀n", "breakdown": "èjì (2) + ọgbọ̀n (30)"},
    33: {"yoruba": "ẹ̀talélọ́gbọ̀n", "breakdown": "ẹ̀ta (3) + ọgbọ̀n (30)"},
    34: {"yoruba": "ẹ̀rinlélọ́gbọ̀n", "breakdown": "ẹ̀rin (4) + ọgbọ̀n (30)"},
    35: {"yoruba": "àrúndínlógójì", "breakdown": "àrún (5) - ọgójì (40)"},
    36: {"yoruba": "ẹ̀rindínlógójì", "breakdown": "ẹ̀rin (4) - ọgójì (40)"},
    37: {"yoruba": "ẹ̀tadínlógójì", "breakdown": "ẹ̀ta (3) - ọgójì (40)"},
    38: {"yoruba": "èjìdínlógójì", "breakdown": "èjì (2) - ọgójì (40)"},
    39: {"yoruba": "ọ̀kandínlógójì", "breakdown": "ọ̀kan (1) - ọgójì (40)"},
    40: {"yoruba": "ogójì", "breakdown": "ogún (20) * èjì (2)"},
    50: {"yoruba": "àádọ́ta", "breakdown": {"Arithmetic breakdown": "àá (10) - ọgọ́ta (60)", "Explanation": "ẹ̀wá (10) becomes 'àá' by **deletion** and **assimilation**."}},
    60: {"yoruba": "ọgọ́ta", "breakdown": "ogún (20) * ẹ̀ta (3)"},
    70: {"yoruba": "àádọ́rin", "breakdown": "àá (10) - ọgọ́rin (80)"},
    80: {"yoruba": "ọgọ́rin", "breakdown": "ogún (20) * ẹ̀rin (4)"},
    90: {"yoruba": "àádọ́rùn-ún", "breakdown": "àá (10) - ọgọ́rùn-ún (100)"},
    100: {"yoruba": "ọgọ́rùn-ún", "breakdown": "ogún (20) * àrún (5)"},
    150: {"yoruba": "àádọ́jọ", "breakdown": "àá (10) - ọgọ́jọ (160)"},
    181: {"yoruba": "ọ̀kànlélọ́gọ́ọ̀sán", "breakdown": "ọ̀kàn (1) + ọgọ́sàn-án (180)"},
    182: {"yoruba": "èjìlélọ́gọ́ọ̀sán", "breakdown": "èjì (2) + ọgọ́sàn-án (180)"},
    183: {"yoruba": "ẹ̀tàlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀ta (3) + ọgọ́sàn-án (180)"},
    184: {"yoruba": "ẹ̀rinlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀rin (4) + ọgọ́sàn-án (180)"},
    185: {"yoruba": "àrúnlélọ́gọ́ọ̀sán", "breakdown": "àrún (5) + ọgọ́sàn-án (180)"},
    186: {"yoruba": "ẹ̀fàlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀fà (6) + ọgọ́sàn-án (180)"},
    187: {"yoruba": "èjelélọ́gọ́ọ̀sán", "breakdown": "èje (7) + ọgọ́sàn-án (180)"},
    188: {"yoruba": "ẹ̀jọlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀jọ (8) + ọgọ́sàn-án (180)"},
    189: {"yoruba": "ẹ̀sánlélọ́gọ́ọ̀sán", "breakdown": "ẹ̀sán (9) + ọgọ́sàn-án (180)"},
    190: {"yoruba": "ẹ̀wádínlúgba", "breakdown": "ẹ̀wá (10) + ọgọ́sàn-án (180)"},
    191: {"yoruba": "ẹ̀sándínlúgba", "breakdown": "ẹ̀sán (9) - igba (200)"},
    192: {"yoruba": "ẹ̀jọdínlúgba", "breakdown": "ẹ̀jọ (8) - igba (200)"},
    193: {"yoruba": "èjedínlúgba", "breakdown": "èje (7) - igba (200)"},
    194: {"yoruba": "ẹ̀fàdínlúgba", "breakdown": "ẹ̀fà (6) - igba (200)"},
    195: {"yoruba": "àrúndínlúgba", "breakdown": "àrún (5) - igba (200)"},
    196: {"yoruba": "ẹ̀rindínlúgba", "breakdown": "ẹ̀rin (4) - igba (200)"},
    197: {"yoruba": "ẹ̀tadínlúgba", "breakdown": "ẹ̀tà (3) - igba (200)"},
    198: {"yoruba": "èjìdínlúgba", "breakdown": "èjì (2) - igba (200)"},
    199: {"yoruba": "ọ̀kandínlúgba", "breakdown": "ọ̀kan (1) + igba (200)"},
    200: {"yoruba": "igba", "breakdown": "Base numeral for 200"},
    210: {"yoruba": "ẹ̀wálérúgba", "breakdown": "ẹ̀wá (10) + igba (200)"},
    215: {"yoruba": "àrúndínlókòólérúgba", "breakdown": "àrún (5) + okòó (20) + igba (200)"},
    220: {"yoruba": "okòólérúgba", "breakdown": "okòó (20) + igba (200)"},
    221: {"yoruba": "ọ̀kanléokòólérúgba", "breakdown": "ọ̀kan (1) + okòólérúgba (220)"},
    225: {"yoruba": "àrúnléokòólérúgba", "breakdown": "àrún (5) + okòólérúgba (220)"},
    229: {"yoruba": "ẹ̀sánléokòólérúgba", "breakdown": "ẹ̀sán (9) + okòólérúgba (220)"},
    230: {"yoruba": "ẹ̀wádínlójìlérúgba", "breakdown": "ẹ̀wá (10) - òjìlérúgba (240)"},
    300: {"yoruba": "ọ̀ọ́dúnrún", "breakdown": "Base numeral for 300"},
    340: {"yoruba": "òjìlélọ́ọ̀dúnrún", "breakdown": {"Arithmetic breakdown": "òjì (40) + ọ̀ọ́dúnrún (300)", "Additional note": "'òjì' is the clipped form of 'ogójì' (40)"}},
    400: {"yoruba": "irinwó", "breakdown": "Base numeral for 400"},
    450: {"yoruba": "ẹ̀wádínlọ́talérinwó", "breakdown": "ẹ̀wá (10) - ọ̀ta (60) + irinwo (400)"},
    500: {"yoruba": "ẹ̀ẹ́dẹ́gbẹ̀ta", "breakdown": {"Arithmetic breakdown": "ẹ̀ẹ́ (100) - ẹgbẹ̀ta (600)", "Explanation": "ọgọ́rùn-ún (100) becomes 'ẹ̀ẹ́' by **deletion** and **assimilation**."}},
    600: {"yoruba": "ẹgbẹ̀ta", "breakdown": "igba (200) * ẹ̀ta (3)"},
    1000: {"yoruba": "ẹgbẹ̀rún", "breakdown": "igba (200) * àrún (5)"},
    2000: {"yoruba": "ẹgbàá", "breakdown": "igba (200) * ẹ̀wá (10)"},
    3000: {"yoruba": "ẹ̀ẹ́dẹ́gbàájì/ẹgbẹ̀ẹ̀dógún", "breakdown": {"Option 1": "ẹgbẹ̀rún (1,000) - ẹgbàájì (4,000)", "Option 2": "igba (200) * ẹ̀ẹ́dógún (15)"}},
    5000: {"yoruba": "ẹ̀ẹ́dẹ́gbàáta/ẹgbàáàrúndínlọ́gbọ̀n", "breakdown": {"Option 1": "ẹgbẹ̀rún (1,000) - ẹgbàáta (6,000)", "Option 2": "ẹgbàá (2,000) * àrúndínlọ́gbọ̀n (25)"}},
    10000: {"yoruba": "ẹgbàáàrún", "breakdown": "ẹgbàá (2,000) * àrún (5)"},
    20000: {"yoruba": "ẹgbàáwàá/ọ̀kẹ́ kan", "breakdown": {"Arithmetic breakdown": "ẹgbàá (2,000) * ẹ̀wá (10) = 20,000", "Cultural note": "'Ọ̀kẹ́' is the traditional name for 20,000"}, "pronunciation": "aw-keh"},
    100000: {"yoruba": "ẹgbàáàdọ́ta/ọ̀kẹ́ márùn-ún", "breakdown": {"Option 1": "ẹgbàá (2,000) * àádọ́ta (50)", "Option 2": "ọ̀kẹ́ (20,000) * márùn-ún (5)"}},
    150000: {"yoruba": "ẹgbàáàrúndínlọ́gọ́rin", "breakdown": "ẹgbàá (2,000) * àrúndínlọ́gọ́rin (75)"},
    1000000: {"yoruba": "ẹgbàáwàá/ọ̀kẹ́ àádọ́ta", "breakdown": "ẹgbàáwàá/ọ̀kẹ́ (20,000) * àádọ́ta (50)"},
    1000000000: {"yoruba": "ẹgbàáwàá/ọ̀kẹ́ ẹgbàáàrúndínlọ́gbọ̀n", "breakdown": "ẹgbàáwàá/ọ̀kẹ́ (20,000) * ẹgbàáàrúndínlọ́gbọ̀n (5,000)"}
}

st.title("Yoruba Numerals")
number = st.number_input("Enter a number:", min_value=1, step=1)

if number in yoruba_numbers:
    data = yoruba_numbers[number]
    st.markdown(
    """<p style="font-size:13px;">👉 <b>Arithmetic keys</b>:  
    <i>'+' : lé ní (added to),</i>  
    <i>'-' : dín ní (subtracted from)</i>  
    <i>'*' : lọ́nà (multiplied by)</i>  
    </p>""",
    unsafe_allow_html=True
)

    st.subheader(f"Number: {number:,.0f}")
    st.write(f"**Yoruba:** {data['yoruba']}")
    
    if 'breakdown' in data:
        st.write("**Breakdown:**")
        if not isinstance(data['breakdown'], dict):
             st.write(data['breakdown'])
        else:
            for key, value in data['breakdown'].items():
                st.write(f"- **{key}**: {value}")
    if 'pronunciation' in data:
        st.write("**Pronunciation:**")
        if not isinstance(data['pronunciation'], dict):
            st.write(data['pronunciation'])
        else:
             for key, value in data["pronunciation"].items():
                st.write(f"- **{key}**: {value}")
else:
    st.warning(f"'{number}' is currently not available")
