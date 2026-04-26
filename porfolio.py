import streamlit as st

# configuration de la page

st.set_page_config("cv Fatimata Bassel Ba, layout=wide")

# titre

st.title ("Profil")

st.markdown("---")

# Informations personnelles
with st.sidebar:
    
    st.title("Fatimata Bassel Ba")
    st.header("Technicienne Supérieur en Géomatique")
    st.write("Email:fatimabasselb@gmail.com")
    st.write("Adresse:Dakar, Sénégal")
    st.markdown("---")

# Profils

st.write("### Technicienne de Terrain et Bureau d'Études. Spécialiste de la collecte de données et de la topographie ")

# Formations et Diplomes
st.header("Formations Académiques")
st.write(" *En cours*") 
st.write("*Master en Géographie*")
st.caption("Université Cheikh Anta Diop de Dakar (UCAD)")
st.write("---")
st.write("*2023*")
st.write(" *Brevet de Technicienne Supérieur en Géomatique*")
st.caption(" Centre d'Entreprenariat et de Développement Technique (G15)")
st.write("---") 
st.write("*2021*")
st.write("*Baccalauréat Scientifique*")
st.caption("lycée Blaise Diagne de Dakar")

# Compétences

st.header("Compétences")
st.markdown (".......")
st.write("*-Topographie & Levés*")
st.write("*Conception Cartographique*")
st.write("*-Analyse Spatiale (SIG)*")
st.write("*-Dessin Architectural*")
st.write("*-Gestion de Bases de Données*")

# OUtils à utiliser

st.header (" Maîtrise Logicielle & Technique")
st.markdown(".....")
st.write ("*-ArcGIS*")
st.write ("*-QGIS*")
st.write("*-AutoCAD*")
st.write("*-Sketchup (3D)*")
st.write("*-Python / Streamlit*")
st.write("*-Power AMC*")


# Projets
st.header("Réalisations & Projets Phares")
st.write("""
*   *-Application Web SIG :* Création d'interfaces interactives avec Streamlit.
*   *-Cartographie Thématique :* Conception de cartes complexes pour l'aide à la décision
*    *-Expertise Terrain :* Campagnes de levés topographiques et traitement de données de précision.

""")

