import streamlit as st
from PIL import Image

######
st.title("Python 🐍 for Renewable ♻️ Energy ⚡️  | Data Processing 📊📈")

# Add logo
logo_filePath = "/workspaces/blank-app/images/eagelogo2.png"
eage_logo = Image.open(logo_filePath)

st.sidebar.image(eage_logo, width=250)

######
courseInfo = st.Page(
    title="Course Info",
    page="views/courseInfo.py",
    icon=":material/info:",
    default=True
)
pythonBasics = st.Page(
    title="Python Basics",
    page="views/pythonBasics.py",
    icon=":material/code:",
)
    
    
eolic = st.Page(
    title="Eolic",
    page="views/eolic.py",
    icon=":material/wb_sunny:",
)
hydroelectric = st.Page(
    title="Hydroelectric",
    page="views/hydroelectric.py",
    icon=":material/waves:",
)
geothermal = st.Page(
    title="Geothermal",
    page="views/geothermal.py",
    icon=":material/whatshot:",
)
solar = st.Page(
    title="Solar",
    page="views/solar.py",
    icon=":material/brightness_5:",
)
###### Build Navigation Menu
pg = st.navigation(
    {
        "Course Information": [courseInfo],
        "Python Basics": [pythonBasics],
        "Renewable Energy Content": [eolic, hydroelectric, geothermal, solar],
    }
)
pg.run()


# Add EAGE logo
eage_logo_filePath = "/workspaces/blank-app/images/eagelogo.png"
st.logo(eage_logo_filePath, link="https://eage.org")