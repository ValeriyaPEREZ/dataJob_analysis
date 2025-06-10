import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("kaggle_survey_2020_responses.csv", low_memory=False)


# Titre principal
st.title("Projet DATA JOB")
st.sidebar.title("Sommaire")
pages=["Le Projet DataJob","Dataset","Nettoyage des données","Analyse exploratoire","Compétences par poste","Conclusion"]
page=st.sidebar.radio("aller vers",pages)
if page == "Le Projet DataJob":

    

    with st.container():
        st.image("DataScientist.png", caption="Data Scientist")
        st.subheader("Projet réalisé par Valeriya PEREZ the best")
    st.subheader(" Objectif")
    st.markdown("""**Comprendre les différents profils techniques dans l'industrie de la Data** à partir du sondage Kaggle 2020.  
    Identifier les tâches effectuées et les outils utilisés globalement, puis les analyser selon les **postes occupés**, afin de construire un système simple de recommandation de poste pour les apprenants.)""")

    st.markdown("""
    ### Approche & Méthode : méthode cycle V
                

    - **Exploration** des données du sondage
    - **Analyse** des outils, compétences et tâches selon les postes
    - **Choix de recommandations** basées sur les similarités de compétences""")

    st.image("kaggle.png", caption="Kaggle")
    

   

elif page == "Dataset":
    st.subheader("Aperçu des 15 premières lignes")
    st.dataframe(df.head(15))

elif page == "Nettoyage des données":
    st.subheader("🧼 Nettoyage des données")

    # 1. Trouver les doublons et les supprimer
    nb_doublons = df.duplicated().sum()
    st.markdown(f"**🔁 Nombre de doublons trouvés :** {nb_doublons}")
    if nb_doublons > 0:
        st.write("Suppression des doublons...")
        df.drop_duplicates(inplace=True)
        st.markdown("Doublons supprimés ✅")
    else:
        st.info("Aucun doublon trouvé.")

    # 2. Identifier les NaN
    st.markdown("Identifier les NaN")
    nan_percent = df.isnull().mean().sort_values(ascending=False) * 100
    nan_percent = nan_percent[nan_percent > 0]
    st.dataframe(nan_percent.head(3))  # affiche les 10 colonnes les plus vides

    # 3. Justifier la décision de supprimer les colonnes « trop vides »
    st.markdown(f"🧹 Colonnes supprimées car >90% de NaN")
    st.markdown(f"Les autres NaN sont remplacés par O")

    # 4. Renommer les colonnes trop longues
    
    st.markdown("Gérer les colonnes avec des noms longs (Excel, renommer, regrouper)")
    st.image("questionsExcel.png")


elif page == "Analyse exploratoire":
    st.subheader("Analyse exploratoire (EDA)")

    st.markdown("L’analyse exploratoire a constitué le cœur de notre démarche, car elle nous a permis de dégager les grandes tendances qui caractérisent les professionnels de la data. " \
    "Cette étape a été conduite selon plusieurs axes, en partant " \
    "d’une vue globale des profils, " \
    "puis en s’intéressant plus précisément aux outils, langages et plateformes les plus répandus. " \
    "Et finalement, les compétences par le poste de travail occupé.")
    st.image("cycleV.png")

    st.markdown("### Présentation générale des profils de répondants")

    st.markdown("Les hommes sont nettement plus nombreux dans le secteur." \
    "Pour les deux genres, les diplômes de niveau master et bachelor sont majoritaires." \
    " Master (à 40%), Bachelor’s à (35,6%) ou d’un doctorat niveau (11%) , ce qui témoigne de l’exigence de formation dans les métiers de la data")
    st.image("genre_etudes.png")

    st.markdown("L’essentiel des répondants a entre 1 et 5 ans d’expérience, avec une décroissance marquée pour les tranches supérieures. " \
    "Plus de 3 000 personnes ont moins d’1 an d’expérience, ce qui compréhensible car majoritairement Kaggle est utiliser pour apprendre et les « seniors » ne l’utilise pas")
    st.image("agerepondants.png")

    st.markdown("Les pays les plus représentés dans l’échantillon sont l’Inde(44,2%), les États-Unis (16,93%), " \
    "le Brésil(5,25%), le Royaume-Uni et la Russie")
    st.image("pays.png")
    st.image("cartemonde.png")

    
    st.markdown("La répartition géographique et la présence de plus de 44 % de répondants venant d’Inde nous ont permis de comprendre les résultats extrêmement étranges au niveau salarial (« Q24 »)")
    st.image("salaires.png")

    st.markdown("Pour affiner l’analyse nous avons essayé présenter la répartition du salaire dans le top 5 pays représentés dans le questionnaire ")
    st.image("salairesparpays.png")


    
    st.markdown("### Affichage outils / langages / IDEs / ML etc.")

    st.markdown("Nous avons exploré les compétences techniques en étudiant les réponses aux questions sur les outils utilisés. " \
    "Concernant les langages de programmation (Q7), " \
    "Python arrive largement en tête et comme langages utilisé, mais également comme premier langage à apprendre (à plus de 83% répondants le conseillent), suivi de R et SQL.  ")
    st.image("TopLangagesConseillés.png")
    st.image("TopLangagesutilisés.png")

    st.markdown("En ce qui concerne les environnements de développement IDE (Q9):" \
    " Jupyter Notebook( à 30%) et Visual Studio Code( à 15.7%) sont les plus couramment cités, suivis par PyCharm (13,3%), Rstudio represente 10,2%, Spyder (8,8%), Notepad++ (8,4%), Sublime Text (6,6%)")
    st.image("IDE.png")

    st.markdown("En matière de visualisation de données à travers la question Q14." \
    " Les bibliothèques Matplotlib et Seaborn dominent largement, suivies de près par Plotly. Cette hiérarchie confirme la place centrale de Python dans l’écosystème de la data science, et notamment de ses bibliothèques de visualisation. ")
    st.image("visualisation.png")

    


elif page == "Compétences par poste":
    st.subheader("Identification des ensembles de compétences par poste")
    

    st.markdown("### Objectif : créer un Profil Type pour chaque poste")
    st.markdown("Etablissons un profil type pour chaque poste, en nous basant sur les compétences les plus fréquemment associées à ces rôles. " \
    "Variable Q5-DataJob nous a permis d’identifier les rôles les plus fréquents dans le sondage : Student, Data Scientist, Data Analyst, Software Engineer, Machine Learning Engineer et Research Scientist")
    st.image("NombreRepondants.png")

    st.markdown("### Analyser par langages et IDE utilisés")


    st.markdown("Nous avons commencé par croiser les réponses aux questions techniques (langages, IDEs, plateformes, tâches ML) " \
    "avec le poste déclaré, en choisissant les 4 profils types suivants : Data Analyst, Data Scientist, Data Engineer, Statisticien")
    st.image("LangagesparJob.png")


    st.markdown("Du côté des environnements de développement (Q9) pour ces 4 profils types suivants : Data Analyst, Data Scientist, Data Engineer, Statisticien")
    st.image("IDEparJob.png")

    st.markdown("L’analyse des outils de visualisation (Q14) grâce à ce diagramme en barres empilée a permis de confirmer ces tendances : " \
    "les Data Scientists et Data Analysts privilégient Matplotlib, Seaborn et Plotly. Et ils effectuent beaucoup plus de visuels alors que les Statisticiens n’utilise quasiment pas les rendus visuels.")
    st.image("visualisationparJob.png")


    
    st.markdown("### Decliner selon le type de taches au quotidien")
    st.markdown("Le barplot horizontal empilé ci-dessous présente les 5 principales activités professionnelles par profil métier")
    st.image("ActivitesparJob.png")


elif page == "Conclusion":
    st.subheader("Conclusion : vers un Système de Recommandation par Compétences")

    st.markdown("### Data Analyst ")
    st.markdown("La bulle la plus grande : c’est le trio central pour les Data Analysts : Python + Jupyter + Matplotlib cela présente la simplicité, l’accessibilité, et la force de Python pour la visualisation")
    st.image("DataAnalyst.png")

    st.markdown("### Data Scientist ")
    st.markdown("La grosse bulle Python + Jupyter + Matplotlib est sans surprise la signature du Data Scientist classique. " \
    "La richesse des outils montre la polyvalence de ces professionnels: usage de Python avec plusieurs IDE et bibliothèques")
    st.image("ProfilDataScientist.png")


    st.markdown("### Data Engineer ")
    st.markdown("Les Data Engineers ne sont pas les plus visuels, mais ils utilisent une variété d’outils selon leurs missions (dashboards, monitoring, EDA…). " \
    "Les bulles se concentrent autour de 3 langages : Python est ultra-dominant. C’est la base de travail des Data Engineers. SQL est très présent , également, ce qu’est cohérent avec leur rôle orienté bases de données. " \
    "R est présent mais secondaire,probablement, quelques profils hybrides ou analystes reconvertis. " \
    "IDEs les plus utilisés Jupyter (JupyterLab, Notebooks...) - Couplé à Python + Matplotlib représente la plus grosse bulle ce que montre une adoption forte des notebooks pour : l’exploration rapide, le prototypage, la documentation du code.")
    st.image("ProfilDataEngineer.png")

    st.markdown("### Statisticien ")
    st.markdown("Les statisticiens restent fortement ancrés dans R, ce qui est cohérent avec la tradition académique/statistique. " \
    "La bulle dominante R + RStudio + ggplot2. Pour les statisticiens modernisés vers la data science = Python + Jupyter + Matplotlib. Bulle R + VSCode + ggplot2 peut signaler une adoption progressive d'IDE plus généralistes ")
    st.image("ProfilStatisticien.png")


    st.markdown("### Proposition pour les 4 profils clés : Data Analyst, Data Scientist,Data Engineer et Statisticien ")
    st.markdown("### Les parcours recommandés pour les étudiants ")
 
    data = {
    "Profil": ["Data Analyst", "Data Scientist", "Data Engineer", "Statisticien"],
    "Bulle principale": [
        "Python + Jupyter + Matplotlib",
        "Python + Jupyter + Matplotlib",
        "Python + Jupyter + Matplotlib",
        "R + RStudio + ggplot2"
    ],
    "Autres combinaisons notables": [
        "R + RStudio + Seaborn\nSQL + VSCode + Plotly",
        "Python + PyCharm + Plotly\nR + RStudio + ggplot2",
        "SQL + VSCode + Plotly/Seaborn\nSQL + PyCharm + ggplot2",
        "Python + Jupyter + Matplotlib\nR + RStudio + Plotly"
    ],
    "Langages clés": [
        "Python, R, SQL",
        "Python, R",
        "Python, SQL, R",
        "R, Python, SQL"
    ],
    "IDEs utilisés": [
        "Jupyter, RStudio, VSCode, Visual Studio",
        "Jupyter, VSCode, PyCharm, RStudio",
        "Jupyter, VSCode, PyCharm, RStudio",
        "RStudio, Jupyter, VSCode"
    ],
    "Outils de visualisation": [
        "Matplotlib, Seaborn, Plotly, ggplot2",
        "Matplotlib, Seaborn, Plotly, ggplot2",
        "Matplotlib, Seaborn, Plotly, ggplot2",
        "ggplot2, Matplotlib, Plotly, Seaborn"
    ],
    "Profil métier / comportement": [
        "Hybride : business, stats, visualisation",
        "Très polyvalent, technique et exploratoire",
        "Moins visuel, usage pro et scripting",
        "Statistique classique, rigueur, modernisation"
    ]
}

# Conversion en DataFrame
    df_profil = pd.DataFrame(data)

# Affichage dans Streamlit
    st.subheader("Tableau récapitulatif des 4 profils Data")
    st.table(df_profil)
    

   
   
