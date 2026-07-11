# 📖 Guide d'Installation - SportEval Pro

## 🔧 Prérequis

Avant de commencer, assure-toi d'avoir installé :

- **Python 3.9+** ([télécharger](https://www.python.org/downloads/))
- **Git** ([télécharger](https://git-scm.com/))
- **pip** (inclus avec Python)

### Vérifier l'installation

```bash
# Vérifier Python
python --version
# ou
python3 --version

# Vérifier pip
pip --version

# Vérifier Git
git --version
```

---

## 📥 Installation

### **Étape 1 : Cloner le dépôt**

```bash
# Via HTTPS
git clone https://github.com/omarchabane18-create/SportEval-Pro.git

# Ou via SSH (si tu as configuré les clés SSH)
git clone git@github.com:omarchabane18-create/SportEval-Pro.git

# Accéder au dossier
cd SportEval-Pro
```

### **Étape 2 : Créer un environnement virtuel**

L'environnement virtuel isole les dépendances du projet.

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**Sur macOS / Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

Tu devrais voir `(venv)` au début de ton terminal si c'est activé ✅

### **Étape 3 : Installer les dépendances**

```bash
pip install -r requirements.txt
```

Cela installera tous les packages nécessaires (Flask/Django, SQLAlchemy, etc.)

### **Étape 4 : Configurer l'environnement**

```bash
# Copier le fichier d'exemple
cp .env.example .env

# Ouvrir .env et ajuster les paramètres si nécessaire
```

### **Étape 5 : Initialiser la base de données**

```bash
# Créer les tables
python scripts/setup_db.py

# (Optionnel) Peupler avec des données de test
python scripts/seed_data.py
```

### **Étape 6 : Lancer l'application**

```bash
python src/main.py
```

L'application devrait démarrer ! 🎉

---

## 🐛 Dépannage

### ❌ `python: command not found`

**Solution :** Python n'est pas installé ou pas dans le PATH
```bash
# Sur macOS, essaie
python3 -m venv venv
source venv/bin/activate
python3 --version
```

### ❌ `ModuleNotFoundError: No module named 'flask'`

**Solution :** Les dépendances ne sont pas installées
```bash
# Vérifier que l'environnement virtuel est activé (voir (venv) dans le terminal)
pip install -r requirements.txt
```

### ❌ `Permission denied` (sur macOS/Linux)

**Solution :** Ajouter les permissions d'exécution
```bash
chmod +x scripts/setup_db.py
python scripts/setup_db.py
```

### ❌ Base de données verrouillée (`database is locked`)

**Solution :** Fermer l'application et supprimer le fichier `.db`
```bash
rm data/database.db
python scripts/setup_db.py
```

---

## 📁 Structure après installation

```
SportEval-Pro/
├── venv/                    # ← Environnement virtuel
├── src/                     # Code source
├── data/
│   └── database.db          # ← Base de données créée
├── requirements.txt
├── .env                     # Configuration locale
└── scripts/
```

---

## 🚀 Commandes utiles

### **Activer l'environnement virtuel**

**Windows :**
```bash
venv\Scripts\activate
```

**macOS / Linux :**
```bash
source venv/bin/activate
```

### **Désactiver l'environnement virtuel**

```bash
deactivate
```

### **Installer un nouveau package**

```bash
pip install package-name
# Puis mettre à jour requirements.txt
pip freeze > requirements.txt
```

### **Lancer les tests**

```bash
pytest tests/ -v
```

### **Supprimer et réinitialiser**

```bash
# Supprimer l'environnement virtuel
rm -rf venv

# Supprimer la base de données
rm data/database.db

# Recommencer from scratch
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt
python scripts/setup_db.py
```

---

## ☁️ Installation avec Docker (Optionnel)

Si tu préfères utiliser Docker :

```bash
# Construire l'image
docker build -t sporteval-pro .

# Lancer le conteneur
docker run -p 8000:8000 sporteval-pro
```

---

## 📚 Prochaines étapes

1. ✅ Lire le [README.md](README.md) pour comprendre le projet
2. ✅ Consulter le [ARCHITECTURE.md](ARCHITECTURE.md) pour la structure technique
3. ✅ Voir [docs/user_guide.md](docs/user_guide.md) pour utiliser l'app
4. ✅ Lire [docs/developer_guide.md](docs/developer_guide.md) pour contribuer

---

## 💬 Aide et support

Si tu rencontres des problèmes :

1. **Vérifier les logs** dans le terminal
2. **Consulter la section Dépannage** ci-dessus
3. **Ouvrir une Issue** sur GitHub : [Issues](https://github.com/omarchabane18-create/SportEval-Pro/issues)
4. **Me contacter** : omarchabane18@gmail.com

---

**Bienvenue sur SportEval Pro ! 🎉**
