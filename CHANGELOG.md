# Changelog & Versioned Data Releases (Feature C8)

## [v1.0.0] - 2026-11-07
### Added
- **Database v1 (`data/durva_compounds_v1.csv`):** 12 literature-verified *Cynodon dactylon* phytochemicals + 2 clinical Positive Controls (`Celecoxib`, `Albendazole`) with 100% DOI provenance (2009–2026).
- **Taxonomic Disambiguation Protocol:** Documented and prevented the `"durva" -> "Durvalumab" / "DUR3"` auto-stemming search artifact.
- **Dual-Mode Bilingual Streamlit App (`app/app.py`):** Full English and Hindi (`हिंदी`) interface switching between 🎮 Explorer Mode and 🔬 Scientist Mode, with interactive `3Dmol.js` molecular rendering.
- **Retrospective Benchmarking:** Added active-vs-decoy ROC-AUC curves (`MMP-9 AUC = 0.84`, `COX-2 AUC = 0.81`).
- **Agronomic & Processing Layer:** Added comparative data for fresh *Swarasa*, Lyophilized juice (Kumar & R., 2026), *Bhavitha Choorna* (P et al., 2026), *Durva Taila* (Santosh et al., 2026), and *Durva Ghrita* (Waghmare et al., 2025).
