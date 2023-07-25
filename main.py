import streamlit as st

st.set_page_config(page_title="Core Quality Concepts", page_icon=":bookmark_tabs:", layout="wide")

header = st.container()
table_header = st.container()

with header:
    st.subheader("Welcome to Core Quality Concepts page :wave:")
    st.title("Here you can find useful materials regarding quality related topics")
    # st.write("All topics as a single paper")
    # st.write("[Go to >](https://lkqeurope.sharepoint.com/:w:/r/sites/LKQE-QualityManagementTeamComponents/"
             # "_layouts/15/Doc.aspx?sourcedoc=%7B86C3C686-1DED-4C41-9C76-6FA3D2312E54%7D&file=Introduction%20to%20Quality%20-%20Guidebook.docx&action=default&mobileredirect=true)")

with table_header:
    st.write("---")
    st.write('<style>div.stTitle {text-align: center; font-size: 48px; font-weight: bold;}</style>',
             unsafe_allow_html=True)
    st.markdown('<div class="stTitle">Table of content</div>', unsafe_allow_html=True)
    st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Category")
    st.write("---")
    for _ in range (8):
        st.write("Quality Method")
    for _ in range (5):
        st.write("ISO")
    for _ in range (3):
        st.write("Other Standard")


with col2:
    st.subheader("Topic")
    st.write("---")
    st.write("5 Why")
    st.write("8D")
    st.write("Ishikawa")
    st.write("APQP - Advanced Product Quality Planning")
    st.write("FMEA - Failure Mode and Effects Analysis")
    st.write("MSA - Measurement System Analysis")
    st.write("PPAP - Production Part Approval Process")
    st.write("SPC - Statistical Process Control")
    st.write("ISO 9001:2015 - Quality Management System")
    st.write("ISO 14001:2015 - Environmental Management System")
    st.write("ISO 27001:2015 - Information Security Management System")
    st.write("ISO 45001:2018 - Occ. Heath & Safety Management System")
    st.write("ISO 50001:2018 - Energy Management System")
    st.write("IMS - Integrated Management System")
    st.write("VDA 6.3 - Verband der Automobilindustrie")
    st.write("IATF 16949 - International Automotive Task Force")

with col3:
    st.subheader("Youtube Webinar")
    st.write("---")
    st.write("[Go to YT 📽️ >](https://youtu.be/RaD9UKn2ijM)")
    st.write("[Go to YT 📽️ >](https://youtu.be/Rn9PfV8E2ew)")
    st.write("[Go to YT 📽️ >](https://youtu.be/DZwajTjyPmA)")
    st.write("[Go to YT 📽️ >](https://youtu.be/d5vYGiJvg5s)")
    st.write("[Go to YT 📽️ (Part1) >](https://youtu.be/Y9apjfb-u3o) [Go to YT 📽️ (Part2) >](https://youtu.be/THO9syzEVYk)")
    st.write("[Go to YT 📽️ >](https://youtu.be/GJFLIGmnpzI)")
    st.write("[Go to YT 📽️ >](https://youtu.be/gymZIVqXrPI)")
    st.write("[Go to YT 📽️ >](https://youtu.be/lOEqli-YV2I)")
    st.write("[Go to YT 📽️ >](https://youtu.be/lJqqM-bdDMI)")
    st.write("[Go to YT 📽️ >](https://youtu.be/2f4pBIvXkBs)")
    st.write("[Go to YT 📽️ >](https://youtu.be/Vs_jXSKByq4)")
    st.write("[Go to YT 📽️ >](https://youtu.be/OoNg4EwlfUk)")
    st.write("[Go to YT 📽️ >](https://youtu.be/tlsicPWFeek)")
    st.write("[Go to YT 📽️ >](https://youtu.be/b5jx86x8nXM)")
    st.write("[Go to YT 📽️ >](https://youtu.be/jKRZKYGWckU)")
    st.write("[Go to YT 📽️ >](https://youtu.be/YDQfr9A2o14)")


