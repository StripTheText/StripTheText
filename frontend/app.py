# Import of libraries
import streamlit as st
import pandas as pd
import numpy as np
import pathlib

# Definition of global variables
root_path = pathlib.Path(__file__).cwd().parent  # Path to the root folder
data_path = root_path.joinpath('data')  # Path to the data folder


# Definition of functions
def test_paths():
    print(root_path)
    print(data_path)


# Building the app
def main():
    st.title('Strip the Text')

    st.markdown("""
    
    ## Ein Universitätsprojekt von Studierenden der Dualen Hochschule Baden-Württemberg Mannheim
    
    ### Projektteam:
    - [**Daniel Schmitz - **]()
    - [**Tobias Kister - 9416513**](contact@tksiter.de)
    - [**Jan Neilfeld - **]()
    - [**Michel Medved - **]()
    
    ### Projektbeschreibung: 
    
    Bei den Projekt handelt es sich um die Realisierung eines Web-Tools, welches es ermöglicht, Texte von unnötigen 
    Informationen zu befreien und die zentralen Punkte der Englischsprachigen Texte zu erfassen. Des Weiteren bildet 
    das nachfolgende Projekt die Möglichkeit die vorliegenden Texte anhand ihres Inhaltes zu einer bestimmten 
    Kategorie von Dokumenten zu klassifizieren.

    """)


if __name__ == '__main__':
    # test_paths()
    main()
