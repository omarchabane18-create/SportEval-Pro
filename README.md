# 🏃 SportEval Pro

**AI-Powered Physical Education Assessment Platform**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python%203.9%2B-blue)](https://www.python.org/)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-brightgreen)]()

---

## 📋 À propos

**SportEval Pro** est une plateforme intelligente de **gestion et d'évaluation des performances physiques** pour les établissements scolaires marocains. Elle permet aux enseignants d'EPS de :

- 📊 Évaluer les élèves selon les **barèmes officiels marocains**
- 🧮 Calculer automatiquement les indices de performance (SPAS Engine)
- 🤖 Utiliser l'IA pour générer des rapports et recommandations
- 📈 Créer des statistiques et classements
- 📄 Exporter en PDF, Excel, Word
- ☁️ Synchroniser les données en cloud

---

## ✨ Fonctionnalités principales

### **Phase 1 (V1) - MVP**
- ✅ Gestion multi-établissements
- ✅ Gestion des enseignants EPS
- ✅ Gestion des classes et élèves
- ✅ Gestion des épreuves (Athlétisme, Sports collectifs, Gymnastique)
- ✅ Saisie des évaluations
- ✅ Calcul automatique des scores
- ✅ Classement des élèves
- ✅ Export PDF/Excel

### **Phases futures**
- 🔮 SPAS Engine (6 indices de performance)
- 🤖 Assistant IA conversationnel
- ☁️ Cloud sync (Google Drive, OneDrive)
- 📱 Application mobile (Android/iOS)
- 🎥 IA Vision (analyse vidéo)

---

## 🎯 Épreuves supportées

### **Athlétisme**
- Courses : 100m, 600m, 1000m
- Sauts : Saut en longueur, saut en hauteur
- Lancers : Lancer du poids

### **Sports Collectifs**
- Football
- Basketball
- Handball
- Volleyball

### **Gymnastique**
- Enchaînements acrobatiques
- Positions d'équilibre
- Souplesse

---

## 🛠️ Stack Technique

| Composant | Technologie |
|-----------|-------------|
| **Backend** | Python 3.9+ |
| **Framework Web** | Flask / Django |
| **Base de données** | SQLite (Dev) → PostgreSQL (Prod) |
| **Frontend** | HTML5 + CSS3 + JavaScript |
| **Desktop GUI** | PyQt6 / Tkinter |
| **IA** | OpenAI API / Hugging Face |
| **Export** | ReportLab (PDF), openpyxl (Excel) |
| **Cloud** | Google Drive API, OneDrive API |

---

## 📦 Structure du projet

```
SportEval-Pro/
├── README.md                          # Ce fichier
├── ARCHITECTURE.md                    # Documentation architecture
├── INSTALLATION.md                    # Guide d'installation
├── requirements.txt                   # Dépendances Python
├── .gitignore                         # Fichiers à ignorer
├── .env.example                       # Variables d'environnement
│
├── src/                               # Code source
│   ├── __init__.py
│   ├── main.py                        # Point d'entrée
│   ├── config.py                      # Configuration
│   │
│   ├── database/                      # Gestion base de données
│   │   ├── __init__.py
│   │   ├── models.py                  # Modèles SQLAlchemy
│   │   ├── connection.py              # Connexion DB
│   │   └── migrations/
│   │
│   ├── models/                        # Modèles métier
│   │   ├── __init__.py
│   │   ├── establishment.py           # Établissements
│   │   ├── teacher.py                 # Enseignants
│   │   ├── class_model.py             # Classes
│   │   ├── student.py                 # Élèves
│   │   ├── event.py                   # Épreuves
│   │   └── evaluation.py              # Évaluations
│   │
│   ├── services/                      # Logique métier
│   │   ├── __init__.py
│   │   ├── evaluation_service.py      # Calculs d'évaluation
│   │   ├── scoring_service.py         # Système de notation
│   │   ├── stats_service.py           # Statistiques
│   │   ├── export_service.py          # Exports
│   │   └── ai_service.py              # IA
│   │
│   ├── ui/                            # Interface utilisateur
│   │   ├── __init__.py
│   │   ├── main_window.py             # Fenêtre principale
│   │   ├── widgets/                   # Composants réutilisables
│   │   ├── dialogs/                   # Fenêtres de dialogue
│   │   └── assets/                    # Images, icônes
│   │
│   └── utils/                         # Utilitaires
│       ├── __init__.py
│       ├── validators.py              # Validation
│       ├── helpers.py                 # Fonctions d'aide
│       └── constants.py               # Constantes
│
├── tests/                             # Tests unitaires
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_ui.py
│
├── docs/                              # Documentation
│   ├── api.md                         # Documentation API
│   ├── database_schema.md             # Schéma DB
│   ├── user_guide.md                  # Guide utilisateur
│   └── developer_guide.md             # Guide développeur
│
├── data/                              # Données (à ne pas versionner)
│   ├── database.db                    # SQLite
│   ├── exports/                       # Fichiers exportés
│   └── imports/                       # Fichiers importés
│
└── scripts/                           # Scripts utiles
    ├── setup_db.py                    # Initialisation DB
    ├── seed_data.py                   # Données de test
    └── backup.py                      # Sauvegarde

```

---

## 🚀 Installation rapide

### **Prérequis**
- Python 3.9+
- pip
- Git

### **Étapes**

```bash
# 1. Cloner le dépôt
git clone https://github.com/omarchabane18-create/SportEval-Pro.git
cd SportEval-Pro

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement
# Sur Windows
venv\Scripts\activate
# Sur macOS/Linux
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Initialiser la base de données
python scripts/setup_db.py

# 6. Lancer l'application
python src/main.py
```

Pour plus de détails, voir [INSTALLATION.md](INSTALLATION.md)

---

## 📚 Documentation

- 📖 [Architecture](ARCHITECTURE.md) - Vue d'ensemble technique
- 📖 [Guide d'Installation](INSTALLATION.md) - Installer et configurer
- 📖 [Guide Utilisateur](docs/user_guide.md) - Comment utiliser l'app
- 📖 [Guide Développeur](docs/developer_guide.md) - Contribuer au projet
- 📖 [Schéma Base de Données](docs/database_schema.md) - Structure des données

---

## 📊 Roadmap

| Version | Statut | Contenu |
|---------|--------|---------|
| **V1** | 🟡 En cours | Interface, Gestion élèves/classes, Évaluations, Export |
| **V2** | 🟠 Planifié | SPAS Engine, Statistiques, Graphiques |
| **V3** | 🟠 Planifié | Assistant IA, Cloud, Multi-utilisateurs |
| **V4** | 🔴 Futur | Synchronisation, API, App mobile |
| **V5** | 🔴 Futur | IA avancée, Prédictions |
| **V6** | 🔴 Futur | Version professionnelle commerciale |

---

## 🤝 Contribution

Les contributions sont bienvenues ! Pour contribuer :

1. Fork le projet
2. Crée une branche (`git checkout -b feature/AmazingFeature`)
3. Commit tes changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvre une Pull Request

---

## 📝 Licence

Ce projet est sous licence **MIT** - voir [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Omar Chabane**
- 📧 Email : omarchabane18@gmail.com
- 🐙 GitHub : [@omarchabane18-create](https://github.com/omarchabane18-create)
- 📍 Maroc 🇲🇦

---

## 📞 Support

Pour toute question ou problème :
- 📤 Ouvre une [Issue](https://github.com/omarchabane18-create/SportEval-Pro/issues)
- 💬 Contacte-moi sur GitHub

---

## ⭐ Si le projet t'a plu, n'oublie pas de lui donner une star ! ⭐

**Dernière mise à jour** : Juillet 2026
**Version** : V1 (En développement)
