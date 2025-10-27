<p align="right"><a href="README.md">English</a> | <b>Français</b></p>

# TP World3 (adapté du TP d’Achille Baucher)

Séance pratique modélisant les interactions entre population, ressources et industrie à l’aide du modèle World3.

## Provenance
TP original conçu et maintenu par Achille Baucher. Référence amont et ressources :
- https://gitlab.inria.fr/abaucher/pydynamo/-/tree/TPworld3

Ce dépôt réorganise le TP, propose des notebooks bilingues et ajoute des installateurs simples ainsi que des exécutables Windows monofichier.

## Mode d’emploi
- **Sans Python installé** : téléchargez l’exécutable Windows dans « Releases » et lancez-le. Deux variantes existent, une par langue.
  - **TP-World3-FR.exe** pour le français
  - **TP-World3-EN.exe** pour l’anglais
- **Avec Python** : utilisez l’installateur adapté dans le répertoire `installers/`.
  - `setuponwindows.py` pour Windows
  - `setuponlinux.py` pour Linux/macOS

## Contenu du dépôt
- `notebooks/`
  - `TP.ipynb` - notebook en français
  - `TP_en.ipynb` - notebook en anglais
- `installers/`
  - `setuponwindows.py` - installeur/lanceur Windows
  - `setuponlinux.py` - installeur/lanceur Linux/macOS
  - `README.md` — guide d'utilisation des installateurs (avec une version française équivalente)
- `README.fr.md` - README en français
- `README.md` - README en anglais 
- `LICENSE` et métadonnées

## Notes
- Les installateurs réutilisent les fichiers existants et évitent d’écraser le travail utilisateur.
