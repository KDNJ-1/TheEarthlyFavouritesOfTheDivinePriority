# Contributing to TheEarthlyFavouritesOfTheDivinePriority (Features I1 & I7)

Welcome! Whether you are an undergraduate botany student, a computational chemist, or an Ayurvedic researcher, you can contribute to this open-science atlas—or **fork this repository as a template for your own plant species!**

### How to Add a New Compound to Database v1
1. Ensure the compound has been experimentally identified in *Cynodon dactylon* via GC-MS, LC-MS, HPTLC, or RP-HPLC in a peer-reviewed paper with a valid **DOI**.
2. Add the row to `data/durva_compounds_v1.csv` including `plant_part`, `how_found`, and `source_doi`.
3. Run `python src/validate_data.py` to verify schema integrity.
4. Submit a Pull Request!

### How to Fork This Repo as a Template for Another Plant (Feature I7)
1. Click **Fork** at the top right of GitHub.
2. Replace `data/durva_compounds_v1.csv` and `data/durva_literature_claims.csv` with your target species.
3. Run `notebooks/01_build_database_v1.ipynb` in Google Colab to auto-populate PubChem CIDs, SMILES, and RDKit descriptors.
