# 📊 Analyse des ventes – SQLite & Pandas

Ce projet réalise une **analyse commerciale complète** à partir du dataset Kaggle *Sample Sales Data*.  
Il combine **SQLite** pour la structure de données et **Pandas** pour la manipulation et la visualisation.

---

## 🚀 Installation et exécution

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/bachri31/Python-Pandas-SQL-Data-Analytics
cd Python-Pandas-SQL-Data-Analytics
```


Creer et activer l'environnement virtuel

Mac/Linux

```bash
python -m venv .sql_env
source sql_env/bin/activate
```

Sur Windows

```bash
python -m venv .sql_env
.\sql_env\Scripts\activate
```

Installer les dependances

```bash
pip install -r requirements.txt
```

Selectionenr le kernel (Jupyter Notebook)

```bash
python -m ipykernel install --user --name=.sql_env --display-name "Python (.sql_env)"
```

Utilisation 

Créer les table et inserer les valeurs dans SQLite en excutant le script suivant :

```bash
python src/set-up.py
```

Ce script est a excuter une seule fois pour initialiser la base de données.

Lancer Jupyter Notebook

```bash
jupyter notebook
```

Ouvrir `Sales_Analysis_SQL_Pandas.ipynb` et exécuter les cellules.

---

🧰 Outils utilisés

Python 3.12
SQLite3
Pandas
Matplotlib
KaggleHub
VS Code / Jupyter Notebook

📜 Licence

Projet personnel.
Données : Sample Sales Data © Kaggle — usage libre pour analyse non commerciale.
Voir les [termes de Kaggle](https://www.kaggle.com/terms) pour plus de détails.