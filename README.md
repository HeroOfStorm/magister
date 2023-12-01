

# Ocena wartości wynajmu mieszkania z użyciem modeli uczenia maszynowego
*PJATK - Demo modela opracowanego w ramach pracy magisterskiej*

Autor:
- Serhii Krasnoiarskyi (s18943)

Elementy wchodzące w skład projektu:
- Dokumentacja prototypu projektu
- Demo PoC (pokazanie część funkcjonalności prototypu)
- Model wytrenowany na realnych danych z strony otodom.pl


### Demo PoC
Ta aplikacja Streamlit wyświetla przykłady ofert wynajmu domów i pozwala użytkownikom przewidywać ceny wynajmu w oparciu o różne cechy nieruchomości. Aplikacja do tworzenia prognoz wykorzystuje model uczenia maszynowego który powstał w rezutacie pracy dyplomowej.
Po wprowadzeniu cech porządanego miszkania aplikacja wyświetla wyniki w postaci ceny i tego jak cena różni od śriedniej ceny mieszkania.
W ramach demo funkcjonalności prototypu dobrze by było, gdyby udało się zrobić:
- Wyświetlanie tabeli nieruchomości do wynajmu z możliwością wyboru wielu wierszy i wyświetlania odpowiedniej lokalizacji na mapie.
- Wybierz udogodnienia nieruchomości, dostosuj piętro, powierzchnię, liczbę pokoi, wiek i inne cechy, aby dokonać prognozy.
- Prześlij własne zdjęcia nieruchomości do wynajęcia, aby dodać je do wyświetlanych obrazów.
- Przewidywanie ceny na podstawi cech
- wizualizację wyników np. mapę wyświetlającą localizacje mieszkanie
- prosty interfejs graficzny np. do podania cech do analizy


#### Mapa zawierająca miejsce badanych mieszkań
W wersji podstawowej mapę można wygenerować po prostu w notatniku .ipynb.

W wersji bardziej interaktywnej mapę można dodać do interfejsu graficznego.

## Libraries Used
- Pandas
- Scikit-learn
#### Interfejs graficzny
W tym celu wykorzystać możemy:
- Streamlit - https://streamlit.io/
- Dash - https://dash.plotly.com/
- Folium



## Jak uruchomić
zainstaluj  requerments
uruchom stream_lit_app.py za pomocą polecenia:: 
    streamlit run stream_lit_app.py
-enjoy the demo

## Future Improvements
Planuje testowanie innych typów modeli i technik szkoleniowych w celu zwiększenia dokładności przewidywań.


*Enjoy!*

# Evaluating the rental value of an apartment using machine learning models
*PJATK - Demo of model developed as part of master's thesis*.

Author:
- Serhii Krasnoiarskyi (s18943)

Elements included in the project:
- Documentation of the project prototype
- PoC demo (showing some of the functionality of the prototype)
- Model trained on real data from otodom.pl website

## Overview
This Streamlit application displays examples of house rental offers and allows users to predict rental prices based on various features of the property. The app uses a machine learning model to make predictions and displays the results in a metric. 

## Features
This Streamlit app displays examples of home rental listings and allows users to predict rental prices based on various property characteristics. The application uses a machine learning model to make predictions, which was developed in a thesis resutation.
After entering the characteristics of the desired property, the app displays the results in the form of a price and how the price differs from the average price of the apartment.
As a demo of the prototype's functionality, it would be good to be able to do:
- Display a table of rental properties with the ability to select multiple rows and display the corresponding location on a map.
- Select property amenities, adjust floor, area, number of rooms, age and other features to make a prediction.
- Upload your own photos of rental properties to add them to the displayed images.
- Predict price based on features
- visualization of the results, e.g. a map displaying the localization of the apartment
- simple graphical interface, e.g. for specifying features for analysis

## Libraries Used
- Pandas
- Scikit-learn
#### Interfejs graficzny
W tym celu wykorzystać możemy:
- Streamlit - https://streamlit.io/
- Dash - https://dash.plotly.com/
- Folium

## How to Run
install requerments
run stream_lit_app.py by command: 
    streamlit run stream_lit_app.py
-enjoy the demo

## Future Improvements
Planning on testing other types of models and training techniques to enchance accuracy of prediactions.