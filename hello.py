import streamlit as st #buat ke web dashboard
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# st.write(pd.DataFrame({
#     'c1': [1, 2, 3, 4],
#     'c2': [10, 20, 30, 40],
# }))

########## TEXTS #####
#1. Markdown
#  st.markdown( #output Argumen aja
#     """
#     #My first app
#     Hello, para calon praktisi data masa depan!
#     """
# )

#2. Text
# st.title('Analisis Data') #kae H1

#3. Header
st.header('Analisis Data 2') #Kae H2 Mungkin

#4. Subheader
st.subheader('Dashboard Data') #Kae H3 Mungkin

#5. Caption
st.caption('Berikut adalah dashboard') #Kae H4 Mungkin

#6. Code
st.code('Test Code') #kae p namun didalem border code line
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

#7. Text
st.text('Halo Calon Penghuni surga sekalian')

#8. Latex -> Buat MTK
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

########## Data Display #####
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

#1. DataFrame
st.dataframe(data=df, width=500, height=150)
#2. Table
st.table(data=df)
#3. Metric
st.metric(label="Suhu", value="28 °C", delta="1.4 °C")
#4. Json
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

########## Pyplot for CHART #####
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

##################################################### WIDGET #####
########## TEXT INPUT WIDGET #####
#1. Text Input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)
#2. Text Area
area = st.text_area(label='Alamat', value='')
st.write('Alamat: ', area)
#3. Number Input
number = st.number_input(label='No. Hp')
st.write('No. Hp: ', int(number), number)
#4. Date Input
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)
#5. upload data
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
#6. Kamera Input
# picture = st.camera_input('Take a picture')
# if picture:
#     st.image(picture)

########## BUTTON WIDGET INPUT #####
#1. Button Input Aja
if st.button('Say hello'):
    st.write('Hello there')
#2. Checkbox Input
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')
#3. Radio Button Input
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)
#4. Select Box Input
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
#5. Multiselect Box Input
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
#6. Slider Input
# values = st.slider(
#     label='Select a range of values',
#     min_value=0, max_value=100, value=(0, 100))
# st.write('Values:', values)


##################################################### LAYOUTING #####
########## SIDEBAR #####
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)

########## COLUMN #####
col1, col2, col3 = st.columns(3)
 
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")


########## TABS #####
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

########## CONTAINER #####
with st.container():
    st.write("Inside the container")
    
    x = np.random.normal(15, 5, 250)
 
    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig) 
 
st.write("Outside the container")

########## EXPANDER #####
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig) 

with st.expander("See explanation"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )