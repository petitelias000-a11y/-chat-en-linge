<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat System - Elias</title>
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1a1a1a; color: white; display: flex; justify-content: center; padding: 20px; }
        #main-card { background: #2d2d2d; width: 100%; max-width: 500px; padding: 20px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h1, h2 { text-align: center; color: #00d4ff; }
        input, button, select { width: 100%; padding: 12px; margin: 8px 0; border-radius: 8px; border: none; box-sizing: border-box; }
        input { background: #3d3d3d; color: white; }
        button { background: #00d4ff; color: #1a1a1a; font-weight: bold; cursor: pointer; transition: 0.3s; }
        button:hover { background: #0099bb; transform: scale(1.02); }
        .log { background: #1a1a1a; padding: 10px; border-radius: 5px; height: 150px; overflow-y: auto; font-family: monospace; font-size: 0.9em; border: 1px solid #444; margin-top: 10px; }
        .hidden { display: none; }
    </style>
</head>
<body>

<div id="main-card">
    <h1>💬 CHAT SYSTEM</h1>
    
    <div id="menu-principal">
        <button py-click="show_create">1. Créer compte</button>
        <button py-click="show_login">2. Connexion</button>
        <button py-click="show_parent">3. Mode Parent</button>
    </div>

    <div id="screen-create" class="hidden">
        <h2>Créer un compte</h2>
        <input type="text" id="reg-name" placeholder="Pseudo">
        <input type="password" id="reg-pass" placeholder="Mot de passe">
        <p style="font-size: 0.8em;">Admins peuvent voir messages. Accepter ?</p>
        <button py-click="logic_create">Accepter et Créer</button>
        <button style="background:#555" py-click="back_to_main">Retour</button>
    </div>

    <div id="screen-login" class="hidden">
        <h2>Connexion</h2>
        <input type="text" id="log-name" placeholder="Pseudo">
        <input type="password" id="log-pass" placeholder="Mot de passe">
        <button py-click="logic_login">Se connecter</button>
        <button style="background:#555" py-click="back_to_main">Retour</button>
    </div>

    <div id="screen-user" class="hidden">
        <h2 id="user-title">Menu</h2>
        <button py-click="logic_send_msg">Envoyer un message</button>
        <button py-click="logic_read_msg">Lire mes messages</button>
        <button style="background:#ff4b4b" py-click="back_to_main">Déconnexion</button>
    </div>

    <div id="console-output" class="log">Bienvenue... En attente d'action.</div>
</div>

<script type="py">
from pyscript import document
import time

# Simulation des fichiers (en mémoire vive)
db = {
    "accounts": {"elias": "lolola"},
    "messages": [],
    "bans": {},
    "admins": ["elias"],
    "parents": {}
}

def log(txt):
    out = document.querySelector("#console-output")
    out.innerHTML = f"> {txt}<br>" + out.innerHTML

# NAVIGATION
def back_to_main(event):
    for s in ["create", "login", "user"]:
        document.querySelector(f"#screen-{s}").classList.add("hidden")
    document.querySelector("#menu-principal").classList.remove("hidden")

def show_create(event):
    document.querySelector("#menu-principal").classList.add("hidden")
    document.querySelector("#screen-create").classList.remove("hidden")

def show_login(event):
    document.querySelector("#menu-principal").classList.add("hidden")
    document.querySelector("#screen-login").classList.remove("hidden")

# LOGIQUE
def logic_create(event):
    name = document.querySelector("#reg-name").value
    pwd = document.querySelector("#reg-pass").value
    if name and pwd:
        db["accounts"][name] = pwd
        log(f"Compte {name} créé avec succès !")
        back_to_main(None)

def logic_login(event):
    name = document.querySelector("#log-name").value
    pwd = document.querySelector("#log-pass").value
    
    if name in db["accounts"] and db["accounts"][name] == pwd:
        log(f"Connecté en tant que {name}")
        document.querySelector("#screen-login").classList.add("hidden")
        document.querySelector("#screen-user").classList.remove("hidden")
        document.querySelector("#user-title").innerText = f"Salut {name}"
    else:
        log("Erreur : Identifiants incorrects")

def logic_send_msg(event):
    dest = prompt("Envoyer à qui ?")
    txt = prompt("Message :")
    if dest and txt:
        db["messages"].append({"from": "Utilisateur", "to": dest, "text": txt})
        log(f"Message envoyé à {dest}")

def logic_read_msg(event):
    log("Affichage des messages (Simulé)")
    for m in db["messages"]:
        log(f"De {m['from']}: {m['text']}")

# Fonction prompt pour les tests rapides
from js import prompt
</script>

</body>
</html>