import streamlit as st
import pandas as pd
import time

# Configuration de la page
st.set_page_config(page_title="Mon Système de Chat", layout="centered")
st.title("💬 Mon Système de Chat")

# Initialisation de la base de données en mémoire (Pour le test)
if 'db_accounts' not in st.session_state:
    st.session_state.db_accounts = {"elias": "lolola"} # Admin par défaut
if 'db_messages' not in st.session_state:
    st.session_state.db_messages = []

# --- INTERFACE ---
menu = ["Connexion", "Créer un compte", "Mode Parent"]
choix = st.sidebar.selectbox("Menu Principal", menu)

if choix == "Créer un compte":
    st.subheader("Création de compte")
    new_user = st.text_input("Pseudo")
    new_pwd = st.text_input("Mot de passe", type='password')
    agree = st.checkbox("J'accepte que les admins voient mes messages")
    
    if st.button("S'inscrire"):
        if agree and new_user not in st.session_state.db_accounts:
            st.session_state.db_accounts[new_user] = new_pwd
            st.success("Compte créé ! Connectez-vous à gauche.")
        else:
            st.error("Erreur : Pseudo déjà pris ou accord refusé.")

elif choix == "Connexion":
    st.subheader("Se connecter")
    user = st.text_input("Pseudo")
    pwd = st.text_input("Mot de passe", type='password')
    
    if st.button("Lancer la session"):
        if user in st.session_state.db_accounts and st.session_state.db_accounts[user] == pwd:
            st.success(f"Bienvenue {user} !")
            st.session_state.logged_in_user = user
        else:
            st.error("Identifiants incorrects")

    # Si connecté, afficher les options de message
    if 'logged_in_user' in st.session_state:
        st.write("---")
        dest = st.text_input("Envoyer à (destinataire)")
        msg = st.text_area("Votre message")
        if st.button("Envoyer"):
            st.session_state.db_messages.append({"de": st.session_state.logged_in_user, "a": dest, "txt": msg})
            st.info("Message envoyé !")
            
        st.subheader("Mes messages reçus")
        for m in st.session_state.db_messages:
            if m['a'] == st.session_state.logged_in_user:
                st.write(f"**De {m['de']} :** {m['txt']}")

elif choix == "Mode Parent":
    st.subheader("Contrôle Parental")
    child = st.text_input("Nom de l'enfant")
    if st.button("Voir l'activité"):
        messages_trouves = [m for m in st.session_state.db_messages if m['de'] == child or m['a'] == child]
        if messages_trouves:
            st.table(messages_trouves)
        else:
            st.write("Aucun message trouvé.")
