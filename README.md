<p align="right"><b>English</b> | <a href="README.fr.md">Français</a></p>

# TP World3 (Adapted from Achille Baucher's TP)

A practical session modeling the interactions between population, resources, and industry using the World3 model.

## Provenance
Original TP authored and maintained by Achille Baucher. See the upstream reference and materials here:
- https://gitlab.inria.fr/abaucher/pydynamo/-/tree/TPworld3

This repository reorganises the TP, offers bilingual notebooks, and adds simple installers and Windows one-file executables.

## How to use
- **No Python installed**: download the Windows executable in "Releases" and run it. Two variants exist, one per language.
  - **TP-World3-FR.exe** for French
  - **TP-World3-EN.exe** for English
- **With Python**: use the installer in the `installers/` folder for your platform.
  - `setuponwindows.py` for Windows
  - `setuponlinux.py` for Linux/macOS

## Repository contents
- `notebooks/`
  - `TP.ipynb` - French notebook
  - `TP_en.ipynb` - English notebook
- `installers/`
  - `setuponwindows.py` - Windows installer/launcher
  - `setuponlinux.py` - Linux/macOS installer/launcher
  - `README.md` - README on how to use the installers (with an equivalent french version)
- `README.fr.md` - French README
-  `README.md` - English README
- `LICENSE` and metadata

## Notes
- The installers are designed to reuse existing files and avoid overwriting user work.

