# 🔬 Scientist Mode: Methods, Evidence Grading, OSF Pre-Registration & Limitations
**Features Covered:** C1, C2, C3, C4, C5, C6, C7, C9, C10

### 1. Pre-Registration of Hypotheses (OSF Template - Feature C7)
* **Primary Hypothesis (H1):** Polyphenolic aglycones isolated from *Cynodon dactylon* (*Luteolin*, *Apigenin*, *Quercetin*) achieve binding free energies ($\Delta G \le -8.5	ext{ kcal/mol}$) within the catalytic cleft of human **MMP-9 (`1GKC`)** and **COX-2 (`5IKR`)**, comparable to clinical positive controls (*Celecoxib*), while satisfying Lipinski/Veber passive permeability criteria.
* **Secondary Hypothesis (H2):** High-molecular-weight C-glycosides (*Orientin*, *Vitexin*, $	ext{TPSA} > 180	ext{ \AA}^2$) act locally on topical wound beds (stimulating VEGFR2/angiogenesis as observed at $10	ext{ }\mu	ext{g/mL}$ by Patil et al., 2025) rather than via passive systemic gastrointestinal absorption.

### 2. Figure-to-Script Reproducibility Map (Feature C9)
| Figure File | Generating Script / Notebook | Input Dataset |
| :--- | :--- | :--- |
| `figures/fig1_chemical_space_triage.png` | `notebooks/02_triage_admet_and_chemical_space.ipynb` | `data/durva_compounds_v1.csv` |
| `figures/fig2_docking_comparison.png` | `notebooks/04_docking_and_roc_benchmark.ipynb` | `data/durva_compounds_v1.csv` |
| `figures/fig3_roc_auc_benchmark.png` | `notebooks/04_docking_and_roc_benchmark.ipynb` | Active/Decoy Benchmark Set |

### 3. Negative Results & Nuanced Findings Log (Feature C10)
1. **Lauric Acid (`CD_008`):** Scored only `-5.9 kcal/mol` against MMP-9 and `-6.1 kcal/mol` against COX-2. We report this negative docking result transparently: Lauric acid's role in *Durva Taila* is primarily biophysical (lipid barrier and bacterial membrane disruption) rather than specific catalytic pocket inhibition.
2. **High-TPSA C-Glycosides (`CD_003` Orientin & `CD_004` Vitexin):** Flagged by our RDKit triage for high polar surface area (`201.28 Å²` and `181.05 Å²`), demonstrating why ADMET triage must always pair with docking so researchers do not falsely claim high oral bioavailability for intact glycosides.
