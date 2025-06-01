
# 🤖 Weather Shopper - Tests Automatisés avec Pytest & Selenium

Ce projet contient une suite de tests automatisés pour le site [Weather Shopper](https://weathershopper.pythonanywhere.com), développée en 🐍 Python avec Selenium et Pytest.

---

## 🔧 Configuration (pytest.ini)

```ini
[pytest]
addopts = --html=report.html --self-contained-html
testpaths = tests
pythonpath = .
```

✅ Génère automatiquement `report.html` dans le dossier racine  
✅ Tous les tests sont recherchés dans le dossier `tests/`  
✅ Accès simplifié aux modules internes grâce à `pythonpath = .`

---

## 📦 Installation des dépendances

Assure-toi d’activer ton environnement virtuel, puis installe :

```bash
pip install -r requirements.txt
```

---

## 🚀 Lancer les tests

```bash
pytest
```

## 🧪 Que testons-nous ?

- 🌡️ Redirection automatique selon la température (moisturizers ou sunscreens)
- 💰 Sélection des produits les moins chers avec mots-clés spécifiques (aloe, almond, spf-30, spf-50)
- 🛒 Ajout au panier et vérification du total
- 🔄 Comportements dynamiques du site

---

## 📊 Rapport de tests

Un fichier `report.html` est généré automatiquement après chaque test.  

---

## 👩‍💻 Par

Chaima Agoumi – Nelle Kelly Bouanga - Fekni Safaa - Bachri Fatima Ez-zahra

