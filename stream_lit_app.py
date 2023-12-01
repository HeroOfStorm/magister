"""
This Streamlit application displays examples of house rental offers and allows users to predict rental prices based on various features of the property. The app uses a machine learning model to make predictions and displays the results in a metric. 

The app also includes a table of rental properties with the ability to select multiple rows and display the corresponding location on a map. Users can also select amenities of a property, adjust the floor, surface area, number of rooms, age, and other features to make a prediction.

The app also allows users to upload their own images of rental properties to add to the selection of images displayed.

The app uses various Python libraries including Streamlit, Pandas, Folium, and Scikit-learn.
"""

import streamlit as st
import os
import numpy as np
import pandas as pd
import folium
import base64
import joblib
from pipeline import ClusterSimilarity, TypeSelector
from streamlit_image_select import image_select
from streamlit_folium import st_folium
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

DEFAULT_HOUSE = "images/default_house.jpg"
location_info = pd.read_csv('data/Preprocessed_otodom_310823V2.csv')

if 'model' not in st.session_state:
    st.session_state['model'] = joblib.load('data/final_model.pkl')
    st.session_state['button_label'] = "Predict"
    st.session_state['button_state'] = False

def update_selector():
    list_imgs = [f"./images/{i}" for i in os.listdir("./images")]
    return list_imgs

list_imgs = update_selector()

@st.cache_resource
def prepare_data():
    data = pd.read_csv("data/Imputed_prep_otodom_310823.csv", index_col=0).sample(20).reset_index(drop=True)
    arr_loc = []
    for i in range(len(list_imgs)):
        row = data.loc[i]
        arr_loc.append([row['lat'], row['lng'], list_imgs[i]])
        data.loc[i, 'image_path'] = list_imgs[i]
    return data, arr_loc

data, arr_loc = prepare_data()

@st.cache_resource
def prepare_ag_settings():
    global data
    gb = GridOptionsBuilder.from_dataframe(data.iloc[:, :-1])
    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_side_bar()
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children")
    return gb.build()

gridOptions = prepare_ag_settings()

def create_marker_from_img(image_path, m, loc=[52.190348191, 20.416055962]):
    encoded = base64.b64encode(open(image_path, 'rb').read())
    html = '<img src="data:image/png;base64, {}" style="width:200px; height:auto;">'.format
    popup_content = html(encoded.decode('UTF-8'))
    marker = folium.Marker(
        loc,
        popup=popup_content,
        tooltip="OK",
        icon=folium.Icon(color='red')
    )
    marker.add_to(m)

def update_selection(select, m):
    for i in select:
        try:
            create_marker_from_img(i['image_path'], m, loc=[i['lat'], i['lng']])
        except (KeyError, TypeError):
            create_marker_from_img(DEFAULT_HOUSE, m, loc=[i['lat'], i['lng']])

st.title('Examples of House rental offers')

# Create a grid response using AgGrid
grid_response = AgGrid(
    data,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='streamlit', # Add theme color to the table
    enable_enterprise_modules=False,
    height=350, 
    width='100%',
    # reload_data=True
)

# Retrieve the updated data and selected rows from the grid response
data = grid_response['data']
selected = grid_response['selected_rows'] 

# Create a folium map
m = folium.Map(location=[52.190348191,20.916055962], zoom_start=6)

# Update the map with markers based on the selected rows
update_selection(selected, m)

# Display the folium map using st_folium
st_data = st_folium(m, width=725)

# Set the title for the section displaying apartment photos
st.title('Apartments photo examples')

# Update the selector
update_selector()
list_imgs = update_selector()

# Display the selected image
img = image_select("", list_imgs)

st.image(img)

# Select amenities of a property
amenities_selected = st.multiselect("Pick amenities of a property", ['taras', 'Winda', 'balkon', 'Miejsce parkingowe'], ['taras'])

# Select floor of apartment
floor = st.slider('Floor of apartment', 0, 30, 15)

# Select surface area of apartment
area = st.slider('Surface area of apartment', 10, 150, 15)

# Calculate maximum number of rooms based on surface area
max_rooms = (area // 10) + 1

# Select number of rooms in apartment
room_count = st.slider('Number of rooms in apartment', 1, max_rooms, 1)

# Select age of apartment
age = st.slider('Age of apartment', 1, 75, 15)

# Select apartment readiness
stan_wykonczenia = st.checkbox('Is apartment ready for use?')

# Select apartment type in offer
rodzaj_zabudowy = st.checkbox('Is apartment type in offer?')

# Select apartment material in offer
meterial_zabudowy = st.checkbox('Is apartment material in offer?')

# age = st.slider('Surface area of apartment', 10, 60, 15)
loaclisation = st.selectbox("Location:", location_info['localisation'].unique())


# Function to predict rental price
def predict():
    records = location_info[location_info['localisation'] == loaclisation].sample()
    categorycals = ['balkon', 'taras', 'Winda', 'Miejsce_parkingowe', 'Materiał_budynku', 'Stan_wykończenia', 'Rodzaj_zabudowy']
    input = {
        'Powierzchnia': [area],
        'Piętro': [floor],
        'room_count': [room_count],
        'lat': [records['lat'].values[0]],
        'lng': [records['lng'].values[0]],
        'Ludnosc': [records['Ludnosc'].values[0]],
        'age': [age],
        'balkon': [0],
        'taras': [0],
        'Winda': [0],
        'Miejsce_parkingowe': [0],
        'Materiał_budynku': [int(meterial_zabudowy)],
        'Stan_wykończenia': [int(stan_wykonczenia)],
        'Rodzaj_zabudowy': [int(rodzaj_zabudowy)]
    }
    for i in amenities_selected:
        input[i.replace(' ', '_')][0] = 1

    df = pd.DataFrame.from_dict(input)
    df[categorycals] = df[categorycals].astype(int).astype('category')

    st.session_state['button_label'] = "Predicting..."
    st.session_state['button_state'] = True
    st.session_state['result'] = st.session_state['model'].predict(df)[0]
    st.session_state['button_label'] = "Predict"
    st.session_state['button_state'] = False

# Button to predict rental price
predict_button = st.button(label=st.session_state['button_label'], on_click=predict, disabled=st.session_state['button_state'])

# Display the predicted rental price
if 'result' in st.session_state:
    st.metric(
        label="Rental price",
        value=np.round(st.session_state['result'], 2),
        delta=np.round(float(st.session_state['result']) - float(data['price'].mean()), 2),
        delta_color="inverse"
    )

# Function to save uploaded file
def save_uploadedfile(uploadedfile):
    path_new_file = os.path.join("images", uploadedfile.name)
    with open(path_new_file, "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File: {} to images".format(path_new_file.split('/')[-1]))

# Upload an image
image_file = st.file_uploader("Upload An Image", type=['png', 'jpeg', 'jpg', 'webp'])
if image_file is not None:
    save_uploadedfile(image_file)
    update_selector()
