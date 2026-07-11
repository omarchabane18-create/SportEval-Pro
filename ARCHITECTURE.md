# 🏗️ Architecture SportEval Pro

## Vue d'ensemble

**SportEval Pro** est une application multi-couches avec séparation des responsabilités :

```
┌─────────────────────────────────────┐
│   Interface Utilisateur (UI)        │
│   (PyQt6 / Web Django)              │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│   Couche Services (Business Logic)  │
│   - Évaluations                     │
│   - Scoring                         │
│   - Statistiques                    │
│   - Export                          │
│   - IA                              │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│   Couche Modèles (Data Models)      │
│   - Établissements                  │
│   - Enseignants                     │
│   - Classes                         │
│   - Élèves                          │
│   - Épreuves                        │
│   - Évaluations                     │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│   Base de Données                   │
│   SQLite (Dev) → PostgreSQL (Prod)  │
└─────────────────────────────────────┘
```

---

## 📁 Structure des dossiers

### `/src` - Code source principal

```
src/
├── __init__.py
├── main.py                    # Point d'entrée de l'application
├── config.py                  # Configuration globale
│
├── database/
│   ├── __init__.py
│   ├── connection.py          # Gestion de la connexion DB
│   ├── models.py              # Modèles SQLAlchemy
│   └── migrations/            # Scripts de migration
│
├── models/
│   ├── __init__.py
│   ├── establishment.py       # Modèle Établissement
│   ├── teacher.py             # Modèle Enseignant
│   ├── class_model.py         # Modèle Classe
│   ├── student.py             # Modèle Élève
│   ├── event.py               # Modèle Épreuve
│   └── evaluation.py          # Modèle Évaluation
│
├── services/
│   ├── __init__.py
│   ├── evaluation_service.py  # Logique d'évaluation
│   ├── scoring_service.py     # Calcul des scores
│   ├── stats_service.py       # Statistiques et graphiques
│   ├── export_service.py      # Export PDF/Excel
│   └── ai_service.py          # Services IA
│
├── ui/
│   ├── __init__.py
│   ├── main_window.py         # Fenêtre principale
│   ├── widgets/               # Composants réutilisables
│   │   ├── dashboard.py
│   │   ├── table_widget.py
│   │   └── chart_widget.py
│   ├── dialogs/               # Fenêtres de dialogue
│   │   ├── add_student.py
│   │   ├── add_evaluation.py
│   │   └── export_dialog.py
│   └── assets/                # Ressources (images, icônes)
│
└── utils/
    ├── __init__.py
    ├── validators.py          # Validation des données
    ├── helpers.py             # Fonctions utilitaires
    ├── constants.py           # Constantes de l'app
    └── decorators.py          # Décorateurs réutilisables
```

### `/docs` - Documentation

```
docs/
├── database_schema.md         # Schéma complet de la BD
├── user_guide.md              # Guide utilisateur
├── developer_guide.md         # Guide développeur
├── api_reference.md           # Référence API
└── algorithms.md              # Documentations des algorithmes
```

### `/tests` - Tests unitaires

```
tests/
├── __init__.py
├── test_models.py             # Tests des modèles
├── test_services.py           # Tests des services
├── test_ui.py                 # Tests de l'interface
└── fixtures.py                # Données de test
```

### `/scripts` - Scripts utiles

```
scripts/
├── setup_db.py                # Initialiser la BD
├── seed_data.py               # Peupler avec des données test
├── backup.py                  # Sauvegarder la BD
└── migrate.py                 # Migration de la BD
```

---

## 🗄️ Architecture Base de Données

### Entités principales

```sql
-- Établissements
Establishment (id, name, address, phone, email, director)

-- Enseignants
Teacher (id, first_name, last_name, email, specialty, establishment_id)

-- Classes
Class (id, name, level, year, establishment_id, teacher_id)

-- Élèves
Student (id, first_name, last_name, gender, birth_date, height, weight, massar_code, class_id)

-- Épreuves
Event (id, name, category, type, unit, gender, level, description)

-- Évaluations
Evaluation (id, student_id, event_id, score, date, teacher_id)

-- Scores calculés
Score (id, evaluation_id, ranking, percentile, grade, notes)

-- Historique
AuditLog (id, table_name, action, old_value, new_value, user_id, timestamp)
```

### Relations

- `Teacher` → `Establishment` (Many-to-One)
- `Class` → `Establishment` (Many-to-One)
- `Class` → `Teacher` (Many-to-One)
- `Student` → `Class` (Many-to-One)
- `Evaluation` → `Student` (Many-to-One)
- `Evaluation` → `Event` (Many-to-One)
- `Evaluation` → `Teacher` (Many-to-One)

---

## 🔄 Flux de données

### Processus d'évaluation

```
1. Enseignant crée une évaluation
   └─→ student_id, event_id, score

2. Service de scoring calcule
   ├─→ Score brut
   ├─→ Ranking (classement)
   ├─→ Percentile
   └─→ Grade (A, B, C, etc.)

3. Service IA (optionnel)
   ├─→ Détecte anomalies
   ├─→ Génère commentaires
   └─→ Fait des recommandations

4. Sauvegarde en base de données
   └─→ Évaluation + Scores

5. Mise à jour des statistiques
   ├─→ Classement de la classe
   ├─→ Statistiques élève
   └─→ Progression temporelle
```

---

## 🔐 Architecture sécurité

### Authentification

```python
class AuthService:
    - login(username, password) → Token
    - verify_token(token) → User
    - logout(token)
    - change_password(user_id, old_pwd, new_pwd)
```

### Autorisation par rôles

| Rôle | Permissions |
|------|-------------|
| **Admin** | Tous les droits |
| **Director** | Gestion établissement, rapports |
| **Teacher EPS** | Gestion classe/élèves, évaluations |
| **Inspector** | Lecture/statistiques |
| **Student** | Consultation (futur) |

### Audit

Toutes les modifications sont enregistrées :
- Qui ? (user_id)
- Quoi ? (table, id, colonne)
- Avant/Après ? (old_value, new_value)
- Quand ? (timestamp)

---

## 🔗 Intégrations externes

### Cloud Sync

```python
class CloudService:
    - sync_to_google_drive()
    - sync_to_onedrive()
    - auto_backup()
```

### IA & APIs

```python
class AIService:
    - analyze_performance() → OpenAI
    - generate_report()
    - predict_improvement()
```

### Export

```python
class ExportService:
    - export_pdf(data, template)
    - export_excel(data)
    - export_csv(data)
    - export_json(data)
```

---

## 📊 Modules clés

### 1. **Évaluation Service**
- Créer/modifier/supprimer évaluations
- Valider les données
- Déclencher les calculs

### 2. **Scoring Service**
- Calculer score brut vs barème
- Ranking (position dans la classe)
- Grade (A, B, C, D, F)
- Percentile

### 3. **Stats Service**
- Agrégations (moyenne, médiane, std dev)
- Graphiques (histogramme, courbe, radar)
- Comparaisons (intra-classe, inter-classe)
- Progressions temporelles

### 4. **Export Service**
- Générer PDF avec signature
- Excel avec formules
- CSV pour import ailleurs
- JSON pour API

### 5. **IA Service** (V3+)
- Analyse contextuelle
- Détection anomalies
- Suggestions pédagogiques
- Prédictions de performance

---

## 🚀 Patterns de développement

### MVC (Model-View-Controller)

```python
# Model
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Service (Business Logic)
class StudentService:
    def get_student_ranking(self, student_id):
        # Calcul du ranking
        pass

# UI (View + Controller)
class StudentWindow:
    def display_students(self):
        students = StudentService.get_all()
        # Afficher dans la UI
```

### Dependency Injection

```python
class EvaluationService:
    def __init__(self, db: Database, ai_service: AIService):
        self.db = db
        self.ai = ai_service
    
    def create_evaluation(self, data):
        # Utiliser self.db et self.ai
        pass
```

### Singleton (pour DB)

```python
class Database:
    _instance = None
    
    @staticmethod
    def get_instance():
        if Database._instance is None:
            Database._instance = Database()
        return Database._instance
```

---

## 📈 Scalabilité

### Phase 1 (MVP)
- SQLite (fichier local)
- 1 établissement
- UI desktop (PyQt6)

### Phase 2-3
- PostgreSQL (serveur)
- Multi-établissements
- Web app (Django)

### Phase 4+
- Microservices
- API REST
- Mobile apps
- Cloud infrastructure

---

## 🔄 CI/CD (Future)

```yaml
# .github/workflows/ci.yml
- Tests unitaires
- Linting (flake8, black)
- Coverage (>80%)
- Build docker
- Deploy staging
```

---

**Pour plus de détails, consulte les fichiers spécifiques dans `/docs`**
