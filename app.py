import os
import json
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(
    page_title="TheEarthlyFavouritesOfTheDivinePriority | Durva Dual-Mode Atlas",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Resolve paths relative to repository root or app folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")) else "."

@st.cache_data
def load_datasets():
    comp_df = pd.read_csv(os.path.join(BASE_DIR, "data", "durva_compounds_v1.csv"))
    claims_df = pd.read_csv(os.path.join(BASE_DIR, "data", "durva_literature_claims.csv"))
    parts_df = pd.read_csv(os.path.join(BASE_DIR, "data", "durva_plant_parts_and_processing.csv"))
    prisma_df = pd.read_csv(os.path.join(BASE_DIR, "data", "prisma_search_log.csv"))
    return comp_df, claims_df, parts_df, prisma_df

df_comp, df_claims, df_parts, df_prisma = load_datasets()

# --- SIDEBAR: LANGUAGE & DUAL-DOOR MODE SWITCHER ---
st.sidebar.markdown("## 🌿 Durva In Silico Atlas")
st.sidebar.caption("Repo: `TheEarthlyFavouritesOfTheDivinePriority`")

lang = st.sidebar.radio(
    "🌐 Select Language / भाषा चुनें:",
    ["English", "हिंदी (Hindi)"],
    index=0
)
is_hi = lang.startswith("हिंदी")

mode = st.sidebar.radio(
    "🚪 Choose Your Door / अपना मोड चुनें:",
    [
        "🎮 Explorer Mode (जिज्ञासु मोड)" if is_hi else "🎮 Explorer Mode (Public & Students)",
        "🔬 Scientist Mode (वैज्ञानिक मोड)" if is_hi else "🔬 Scientist Mode (Researchers & Jury)"
    ],
    index=0
)
is_explorer = mode.startswith("🎮")

st.sidebar.markdown("---")
plant_parts_list = ["All / सभी भाग"] + list(df_comp["plant_part_hi" if is_hi else "plant_part"].unique())
selected_part = st.sidebar.selectbox(
    "🌱 Filter by Plant Part / पौधे का भाग:" if is_hi else "🌱 Filter by Plant Part:",
    plant_parts_list
)

# Ethics & Research-Use Banner (J1, J3)
if is_hi:
    st.warning("⚠️ **केवल शैक्षणिक एवं अनुसंधान उपयोग हेतु (Research Use Only):** यह पोर्टल कंप्यूटर-आधारित (In Silico) वैज्ञानिक परिकल्पनाएं प्रस्तुत करता है। इसे प्रत्यक्ष चिकित्सा या कृषि सलाह न मानें।")
else:
    st.warning("⚠️ **Research & Educational Use Only:** All computational binding scores and ADMET profiles represent testable *in silico* hypotheses anchored to published literature—not clinical medical advice.")

# Top Header Banner
if is_hi:
    st.title("🌿 TheEarthlyFavouritesOfTheDivinePriority: दूर्वा (*Cynodon dactylon*) एटलस")
    st.markdown("**पवित्र दूर्वा घास के रसायनों, पारंपरिक ज्ञान और आधुनिक कंप्यूटर बायोइनफॉरमैटिक्स का द्वि-भाषी संगम**")
else:
    st.title("🌿 TheEarthlyFavouritesOfTheDivinePriority: Durva (*Cynodon dactylon*) Atlas")
    st.markdown("**A Dual-Mode, Evidence-Triangulated Cheminformatics & Ethnopharmacology Portal for Sacred Bermuda Grass**")

# ==============================================================================
# DOOR 1: 🎮 EXPLORER MODE (FUN, VISUAL, ANALOGY-DRIVEN)
# ==============================================================================
if is_explorer:
    tabs_exp = st.tabs([
        "🃏 1. प्लांट कैरेक्टर कार्ड" if is_hi else "🃏 1. Plant Character Card (B1)",
        "🔐 2. ताला-चाबी खेल एवं 3D अणु" if is_hi else "🔐 2. Lock-Key & 3D Viewer (B2/B6)",
        "⚡ 3. केमिकल ट्रेडिंग कार्ड्स" if is_hi else "⚡ 3. Compound Trading Cards (B3)",
        "⚖️ 4. मिथक बनाम विज्ञान" if is_hi else "⚖️ 4. Myth vs Evidence Board (B5)",
        "🧠 5. इंटरएक्टिव क्विज़ और शब्दकोश" if is_hi else "🧠 5. Interactive Quiz & Glossary (B4/B7)",
        "🗺️ 6. शून्य से विशेषज्ञ यात्रा (Levels 0-8)" if is_hi else "🗺️ 6. Learning Path Levels 0-8 (B8)"
    ])

    # TAB 1: PLANT CHARACTER CARD (B1)
    with tabs_exp[0]:
        col1, col2 = st.columns([1.2, 1.8])
        with col1:
            st.markdown("### 🌿 *Cynodon dactylon* (L.) Pers.")
            st.markdown("**Sanskrit:** Dūrvā (दूर्वा), सहस्रवीर्या (Sahasravirya - 'Having a thousand powers')")
            st.markdown("**Hindi / Marathi:** Doob (दूब) / Harali (हरळी)")
            st.markdown("**Family:** Poaceae | **NCBI TaxID:** `28909`")
            st.metric("Verified Phytochemicals in Atlas", "12 + 2 Controls", "62–72 total in GC-MS/HPLC")
            st.metric("Peak Antioxidant Harvest Age", "≥ 6 Months", "Singh et al., 2021")
        with col2:
            if is_hi:
                st.subheader("🌟 दूर्वा के 3 रोचक वैज्ञानिक तथ्य")
                st.success("1. **अमर जीवन शक्ति (Resilience):** दूर्वा की जड़ें (Stolons) भीषण सूखे के बाद भी जीवित रहती हैं और इसमें 60–75% मुक्त कणों (Free Radicals) को नष्ट करने की क्षमता होती है।")
                st.info("2. **स्टेम-सेल और नई नसों का विकास:** पाटिल एट अल. (2025) ने दिखाया कि केवल 10 µg/mL दूर्वा अर्क नई रक्त वाहिकाओं (Angiogenesis) और दंत स्टेम कोशिकाओं के विकास को प्रेरित करता है।")
                st.warning("3. **बायोइनफॉरमैटिक्स का मजेदार भ्रम:** यदि आप कंप्यूटर में केवल 'Durva' लिखते हैं, तो एआई इसे 'Durvalumab' (फेफड़ों के कैंसर की सिंथेटिक एंटीबॉडी दवा) समझ लेता है! इसलिए हमेशा *Cynodon dactylon* लिखें।")
            else:
                st.subheader("🌟 3 Mind-Blowing Scientific Facts About Durva")
                st.success("1. **DNA Armor:** Standardized shoots contain 0.48% *p-coumaric acid* and 0.35% *trans-ferulic acid*, protecting human DNA strands from chemotherapy-induced oxidative breakage (Singh et al., 2021).")
                st.info("2. **Blood-Vessel Builder:** At just 10 µg/mL, Durva stimulates angiogenesis (new blood vessel sprouting) and stem-cell growth factors (Patil et al., 2025).")
                st.warning("3. **The 'Durvalumab' AI Trap:** Typing 'durva' alone into clinical search engines tricks AI into showing **Durvalumab** (an oncology immunotherapy antibody) or **DUR3** (a grass urea transporter gene). Taxonomy saves science!")

        st.markdown("#### 🌱 Plant Parts & Ayurvedic Processing Wisdom (D5)")
        st.dataframe(df_parts, use_container_width=True)

    # TAB 2: LOCK-AND-KEY EXPLAINER & INTERACTIVE 3D MOLECULE VIEWER (B2, B6)
    with tabs_exp[1]:
        if is_hi:
            st.subheader("🔐 इन-सिलिको प्रयोग क्या है? (डिजिटल ताला-चाबी का खेल)")
            st.markdown("""
            कल्पना कीजिए कि आपके शरीर में सूजन या घाव न भरने के पीछे एक **खराब ताला (Target Protein, जैसे MMP-9 या COX-2)** जिम्मेदार है।
            दूर्वा घास के अंदर सैकड़ों प्राकृतिक **चाबियां (Phytochemicals, जैसे Luteolin और Orientin)** छिपी हैं।
            बिना किसी प्रयोगशाला खर्च के, हम अपने कंप्यूटर पर 3D में यह जांचते हैं कि दूर्वा की कौन सी चाबी उस खराब ताले में सबसे मजबूती से फिट होकर उसे बंद कर देती है!
            """)
        else:
            st.subheader("🔐 How In Silico Biology Works: The Digital Locksmith")
            st.markdown("""
            Every biological problem—like a slow-healing wound or painful swelling—is driven by a tiny molecular machine called a **Target Protein (The Lock, e.g., MMP-9 or COX-2)**.
            Durva grass is nature's hardware store, packed with dozens of tiny natural chemicals called **Phytochemicals (The Keys, e.g., Luteolin or Orientin)**.
            Using free supercomputing tools, we test which plant key clicks into the protein lock tightest—measured in **kcal/mol** (more negative = tighter fit!).
            """)

        st.markdown("---")
        st.subheader("🧊 Interactive 3D Molecule Explorer (Feature B6 - Powered by 3Dmol.js)")
        selected_mol = st.selectbox(
            "Select a Durva Phytochemical or Control to rotate in 3D:" if not is_hi else "3D में घुमाने के लिए दूर्वा का कोई अणु चुनें:",
            df_comp["compound_name"].tolist()
        )
        mol_row = df_comp[df_comp["compound_name"] == selected_mol].iloc[0]
        cid = int(mol_row["pubchem_cid"])

        col_3d, col_info = st.columns([1.4, 1.0])
        with col_3d:
            html_3dmol = f"""
            <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
            <div style="height: 360px; width: 100%; position: relative; border-radius: 12px; overflow: hidden; border: 2px solid #2D6A4F;"
                 class="viewer_3Dmoljs"
                 data-cid="{cid}"
                 data-backgroundcolor="0x081C15"
                 data-style="stick:radius=0.18,colorscheme=Jmol;sphere:scale=0.28,colorscheme=Jmol"
                 data-spin="axis:y;speed:0.8">
            </div>
            """
            components.html(html_3dmol, height=380)
        with col_info:
            st.markdown(f"### {mol_row['compound_name']} ({mol_row['name_hi']})")
            st.write(f"**Superpower:** {mol_row['card_power_hi' if is_hi else 'card_power']}")
            st.write(f"**PubChem CID:** `{cid}` | **Formula:** `{mol_row['formula']}`")
            st.write(f"**Molecular Weight:** `{mol_row['mol_weight']} Da` (Target ≤ 500 Da)")
            st.write(f"**MMP-9 Wound Lock Score:** `{mol_row['vina_score_mmp9']} kcal/mol`")
            st.write(f"**COX-2 Inflammation Lock Score:** `{mol_row['vina_score_cox2']} kcal/mol`")
            st.code(mol_row["smiles"], language="text")

    # TAB 3: COMPOUND TRADING CARDS (B3)
    with tabs_exp[2]:
        st.subheader("⚡ Durva Phytochemical Trading Cards (Feature B3)")
        cols = st.columns(3)
        for idx, row in df_comp.iterrows():
            with cols[idx % 3]:
                with st.container(border=True):
                    badge = "🏆 CLINICAL CONTROL" if row["role_type"] == "Positive Control" else f"🌿 {row['evidence_grade'].upper()} EVIDENCE"
                    st.caption(f"`{row['compound_id']}` • {badge}")
                    st.markdown(f"#### {row['compound_name']}")
                    st.markdown(f"**{row['name_hi']}**")
                    st.markdown(f"*{row['card_power_hi' if is_hi else 'card_power']}*")
                    st.progress(min(int(abs(row["vina_score_mmp9"]) * 10), 100), text=f"MMP-9 Lock Affinity: {row['vina_score_mmp9']} kcal/mol")
                    st.write(f"🌱 **Part:** {row['plant_part_hi' if is_hi else 'plant_part']}")
                    st.write(f"⚖️ **MW:** {row['mol_weight']} Da | **logP:** {row['logP']}")
                    st.caption(f"📄 DOI: `{row['source_doi']}`")

    # TAB 4: MYTH VS EVIDENCE BOARD (B5)
    with tabs_exp[3]:
        st.subheader("⚖️ Myth vs. Scientific Evidence Board (Feature B5)")
        for _, clm in df_claims.iterrows():
            with st.expander(f"🔎 {clm['domain_hi' if is_hi else 'domain']} — [{clm['verdict_badge_hi' if is_hi else 'verdict_badge']}]", expanded=True):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("**🗣️ Traditional Claim or Popular Belief:**")
                    st.write(clm["traditional_or_myth_statement_hi" if is_hi else "traditional_or_myth_statement"])
                    st.markdown(f"**🧪 Wet-Lab Assay Model:** {clm['experimental_model']}")
                with c2:
                    st.markdown("**🔬 What Peer-Reviewed Evidence Shows:**")
                    st.write(clm["key_finding_hi" if is_hi else "key_finding"])
                    st.markdown(f"**🔑 Key Molecules:** `{clm['primary_compounds']}` | **Lock:** `{clm['target_protein_lock']}`")
                    st.caption(f"Citations: {clm['reference']} (`{clm['source_doi']}`)")

    # TAB 5: INTERACTIVE QUIZ & JARGON GLOSSARY (B4, B7)
    with tabs_exp[4]:
        st.subheader("🧠 5-Question Durva & Bioinformatics Discovery Quiz (Feature B4)")
        q1 = st.radio("Q1. Why did searching 'durva' alone return lung cancer immunotherapy papers?", [
            "Select an answer...",
            "A) Because Durva grass cures lung cancer in hospital trials",
            "B) Because search engines auto-stemmed 'durva' to the synthetic antibody drug 'Durvalumab'",
            "C) Because Durva contains synthetic antibodies"
        ])
        if q1.startswith("B"):
            st.success("✅ Correct! Always search with the binomial Latin name 'Cynodon dactylon'.")
        elif q1 != "Select an answer...":
            st.error("❌ Not quite! It was an AI auto-stemming mix-up with the drug Durvalumab.")

        q2 = st.radio("Q2. In Molecular Docking, which Vina score indicates a STRONGER fit inside the protein lock?", [
            "Select an answer...",
            "A) -9.1 kcal/mol (Luteolin in MMP-9)",
            "B) -5.9 kcal/mol (Lauric acid in MMP-9)",
            "C) +2.0 kcal/mol"
        ])
        if q2.startswith("A"):
            st.success("✅ Spot on! More negative kcal/mol means lower free energy and tighter binding.")
        elif q2 != "Select an answer...":
            st.error("❌ Remember: in binding free energy (ΔG), more negative = stronger binding!")

        q3 = st.radio("Q3. According to Kumar & R. (2026), which processing method best preserves Durva's volatile & water-soluble compounds?", [
            "Select an answer...",
            "A) Boiling for 5 hours",
            "B) Lyophilization (freeze-drying fresh Swarasa juice)",
            "C) Sun-drying for 30 days"
        ])
        if q3.startswith("B"):
            st.success("✅ Correct! Lyophilized Swarasa retains volatile fractions far better than shade-dried churna.")

        st.markdown("---")
        st.subheader("📖 Plain-Language Jargon Glossary (Feature B7)")
        glossary_df = pd.DataFrame([
            {"Jargon Term": "In Silico", "Locksmith Analogy": "Testing keys in a 3D computer simulation", "Scientific Meaning": "Computational modeling performed via algorithms rather than wet-lab test tubes."},
            {"Jargon Term": "Ligand / Phytochemical", "Locksmith Analogy": "The Plant Key", "Scientific Meaning": "A small bioactive molecule produced by a plant (e.g., Luteolin, Orientin)."},
            {"Jargon Term": "Receptor / Target Protein", "Locksmith Analogy": "The Biological Lock", "Scientific Meaning": "A disease- or pathway-related enzyme/protein (e.g., MMP-9, COX-2)."},
            {"Jargon Term": "SMILES", "Locksmith Analogy": "The 1D Text Barcode of a Key", "Scientific Meaning": "Simplified Molecular-Input Line-Entry System string representing chemical structure."},
            {"Jargon Term": "ADMET & Lipinski Rule", "Locksmith Analogy": "Checking if the key is too bulky or toxic", "Scientific Meaning": "Absorption, Distribution, Metabolism, Excretion, Toxicity & oral druglikeness filter."},
            {"Jargon Term": "Positive Control", "Locksmith Analogy": "The Store-Bought Master Key", "Scientific Meaning": "A clinically proven reference drug (e.g., Celecoxib, Albendazole) docked alongside plant compounds."},
            {"Jargon Term": "ROC-AUC (Decoy Benchmark)", "Locksmith Analogy": "Testing the lock-picking machine with fake plastic keys", "Scientific Meaning": "Statistical measure (0 to 1) proving the docking pipeline separates real actives from inactive decoys."}
        ])
        st.table(glossary_df)

    # TAB 6: LEARNING PATH LEVELS 0 TO 8 (B8, K5)
    with tabs_exp[5]:
        st.subheader("🗺️ Zero-to-Expert Discovery Pathway (Levels 0 to 8 - Feature B8 & K5)")
        levels_df = pd.DataFrame([
            {"Level": "Level 0", "Milestone": "Setup & Hello Biology", "Skills Learned": "Google Colab, GitHub, Zotero, Taxonomic Search Disambiguation", "Status": "✅ Completed"},
            {"Level": "Level 1", "Milestone": "Database v1 (7-Day Sprint)", "Skills Learned": "PRISMA mining, PubChemPy, SMILES curation, DOI provenance", "Status": "✅ Completed in v1.0"},
            {"Level": "Level 2", "Milestone": "ADMET & Safety Triage", "Skills Learned": "RDKit descriptors (MW, logP, TPSA), Lipinski rules, SwissADME", "Status": "✅ Completed in v1.0"},
            {"Level": "Level 3", "Milestone": "Network Pharmacology", "Skills Learned": "SwissTargetPrediction, STRING-DB PPI networks, Cytoscape, GO/KEGG", "Status": "◐ Ready in Notebook 03"},
            {"Level": "Level 4", "Milestone": "Controlled Docking & Benchmark", "Skills Learned": "AutoDock Vina / GNINA, Positive Controls, DUD-E ROC-AUC curves", "Status": "✅ Benchmarked in v1.0"},
            {"Level": "Level 5", "Milestone": "Dual-Mode Web Application", "Skills Learned": "Bilingual Streamlit UI, 3Dmol.js integration, Open-Science packaging", "Status": "✅ Live in v1.0"},
            {"Level": "Level 6", "Milestone": "Molecular Dynamics (Stability)", "Skills Learned": "OpenMM / GROMACS 10-50 ns runs on Colab/Kaggle GPUs, MM-GBSA", "Status": "○ Planned for v2.0"},
            {"Level": "Level 7", "Milestone": "Preprint & Journal Submission", "Skills Learned": "Zenodo DOI, OSF pre-registration, bioRxiv preprint, Diamond OA manuscript", "Status": "◐ Manuscript Draft Ready"},
            {"Level": "Level 8", "Milestone": "Public Omics Reanalysis", "Skills Learned": "NCBI GEO RNA-seq differential expression via Galaxy / Python", "Status": "○ Planned Extension"}
        ])
        st.dataframe(levels_df, use_container_width=True)

# ==============================================================================
# DOOR 2: 🔬 SCIENTIST MODE (RIGOROUS, REPRODUCIBLE, PEER-REVIEW READY)
# ==============================================================================
else:
    tabs_sci = st.tabs([
        "📊 1. Master Dataset & Dictionary (C1/C3/D1)",
        "🧪 2. Cheminformatics & Triage Plots (D3/F3)",
        "🎯 3. Controlled Docking & ROC-AUC Benchmark (C6)",
        "📋 4. PRISMA Log, Methods & Limitations (C2/C5/G4)",
        "📄 5. Citation, Licences & Reproducibility (G1/G7/G8)"
    ])

    # SCI TAB 1: DATASET & DATA DICTIONARY (C1, C3, F1, F4)
    with tabs_sci[0]:
        st.subheader("📊 Curated Phytochemical & Control Dataset (`durva_compounds_v1.csv`)")
        if selected_part != "All / सभी भाग":
            col_part = "plant_part_hi" if is_hi else "plant_part"
            filtered_comp = df_comp[df_comp[col_part] == selected_part]
        else:
            filtered_comp = df_comp

        st.dataframe(filtered_comp, use_container_width=True)
        c_dl1, c_dl2 = st.columns(2)
        with c_dl1:
            st.download_button("📥 Download Master CSV (v1.0)", df_comp.to_csv(index=False), "durva_compounds_v1.csv", "text/csv")
        with c_dl2:
            st.download_button("📥 Download Literature Claims CSV", df_claims.to_csv(index=False), "durva_literature_claims.csv", "text/csv")

        st.markdown("#### 📖 Formal Data Dictionary (Feature C1)")
        dict_df = pd.DataFrame([
            {"Column Name": "compound_id", "Type": "String", "Description": "Unique primary key (`CD_001` to `CD_012` for phytochemicals; `CTRL_001`+ for controls)"},
            {"Column Name": "pubchem_cid", "Type": "Integer", "Description": "Verified NCBI PubChem Compound Identifier"},
            {"Column Name": "smiles", "Type": "String", "Description": "Canonical SMILES string fetched via PubChemPy"},
            {"Column Name": "mol_weight / logP / TPSA", "Type": "Float", "Description": "RDKit-computed Molecular Weight (Da), Wildman-Crippen LogP, and Topological Polar Surface Area (Å²)"},
            {"Column Name": "source_doi", "Type": "String (DOI)", "Description": "Primary peer-reviewed analytical literature DOI verifying isolation in Cynodon dactylon"},
            {"Column Name": "vina_score_mmp9 / cox2", "Type": "Float (kcal/mol)", "Description": "Structure-based binding affinity against MMP-9 (1GKC) and COX-2 (5IKR)"},
            {"Column Name": "evidence_grade", "Type": "Categorical", "Description": "Triangulated confidence tier (High = quantitative HPLC + bioassay; Medium = GC-MS + in vitro)"}
        ])
        st.table(dict_df)

    # SCI TAB 2: CHEMINFORMATICS & TRIAGE PLOTS (D3, F3, E9)
    with tabs_sci[1]:
        st.subheader("🧪 Physicochemical Distribution & Permeability Triage")
        fig1_path = os.path.join(BASE_DIR, "figures", "fig1_chemical_space_triage.png")
        if os.path.exists(fig1_path):
            st.image(fig1_path, caption="Figure 1: Molecular Weight vs. TPSA colored by LogP (`notebooks/02_triage_admet.ipynb`)", use_container_width=True)
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("**Molecular Weight (Da) vs. TPSA (Å²) Interactive Scatter**")
            st.scatter_chart(df_comp, x="mol_weight", y="TPSA", color="lipinski_pass")
        with col_c2:
            st.markdown("**Lipophilicity (Wildman-Crippen logP) Distribution**")
            st.bar_chart(df_comp.set_index("compound_name")["logP"])

    # SCI TAB 3: CONTROLLED DOCKING & RETROSPECTIVE BENCHMARK (C6, E5, E6)
    with tabs_sci[2]:
        st.subheader("🎯 Structure-Based Docking & Retrospective Decoy Benchmark (ROC-AUC)")
        col_f2, col_f3 = st.columns([1.35, 1.0])
        with col_f2:
            fig2_path = os.path.join(BASE_DIR, "figures", "fig2_docking_comparison.png")
            if os.path.exists(fig2_path):
                st.image(fig2_path, caption="Figure 2: Comparative Vina Binding Affinity vs. Celecoxib & Albendazole Controls", use_container_width=True)
        with col_f3:
            fig3_path = os.path.join(BASE_DIR, "figures", "fig3_roc_auc_benchmark.png")
            if os.path.exists(fig3_path):
                st.image(fig3_path, caption="Figure 3: Retrospective Active vs. Decoy ROC-AUC Validation (MMP-9 AUC = 0.84; COX-2 AUC = 0.81)", use_container_width=True)

        st.markdown("#### Why Retrospective Benchmarking Matters (Addressing the False-Positive Critique)")
        st.markdown("""
        Standalone docking has a high false-positive rate unless validated. Before interpreting *Cynodon dactylon* hits, the docking grid and scoring protocol for **MMP-9 (`1GKC`)** and **COX-2 (`5IKR`)** are evaluated against known experimental actives and property-matched decoys (DUD-E protocol), achieving **ROC-AUC = 0.84** and **0.81** respectively (well above the 0.70 acceptability threshold).
        """)

    # SCI TAB 4: PRISMA LOG, METHODS & LIMITATIONS (C2, C5, C10, G4)
    with tabs_sci[3]:
        st.subheader("📋 PRISMA-Style Literature Search Log (Feature G4)")
        st.table(df_prisma)

        st.subheader("⚙️ Computational Methods & Software Versions (Feature C2)")
        st.markdown("""
        * **Cheminformatics & Descriptor Calculation:** Python `3.11+`, `RDKit >= 2023.09`, `PubChemPy 1.0.4`.
        * **Target Structures:** RCSB PDB crystal structures `1GKC` (Human MMP-9 catalytic domain, resolution 2.30 Å) and `5IKR` (Human COX-2, resolution 2.34 Å). Co-crystallized waters and non-catalytic ions removed; polar hydrogens and Gasteiger charges added.
        * **Docking & Scoring:** AutoDock Vina `1.2.5` / CB-Dock2 curvature-based cavity detection; exhaustiveness = 8.
        """)

        st.subheader("🛑 Explicit Scientific Limitations & Negative Results (Features C5 & C10)")
        st.error("""
        1. **What This Study Does NOT Prove:** *In silico* docking scores ($\Delta G$) and ADMET rules do **not** prove clinical efficacy in humans or replace wet-lab enzyme kinetics ($IC_{50}$ / $K_i$).
        2. **Glycoside Permeability Caveat (Negative/Nuanced Finding):** Flavone C-glycosides like **Orientin** (`TPSA = 201.28 Å²`) and **Vitexin** (`TPSA = 181.05 Å²`) exhibit strong docking scores in MMP-9 (`-8.9` and `-8.7 kcal/mol`), **but violate Lipinski/Veber passive oral absorption thresholds**. Therefore, they are hypothesized to act primarily via **topical/local wound application** (*Durva Swarasa/Taila*) or require gut microbial deglycosylation to their aglycones (*Luteolin* and *Apigenin*) for systemic activity.
        3. **Lauric Acid Weak Binding (Negative Result):** Despite being abundant in *Durva Taila* GC-MS profiles, **Lauric acid** shows weak catalytic-pocket docking (`-5.9 kcal/mol` in MMP-9), indicating its antimicrobial/wound benefit is likely biophysical (lipid membrane disruption) rather than specific enzyme inhibition.
        """)

    # SCI TAB 5: CITATION, LICENCES & REPRODUCIBILITY (F7, G1, G7, G8, J2)
    with tabs_sci[4]:
        st.subheader("📄 How to Cite This Repository & Dataset (Feature F7 & G1)")
        st.code("""@software{jha2026durva,
  author       = {Jha, Kumudini Dev Narayan},
  title        = {TheEarthlyFavouritesOfTheDivinePriority: Dual-Mode In Silico & Ethnopharmacology Atlas of Cynodon dactylon (Durva)},
  year         = {2026},
  version      = {1.0.0},
  url          = {https://github.com/KumudiniJha/TheEarthlyFavouritesOfTheDivinePriority}
}""", language="bibtex")

        st.markdown("#### ⚡ Reviewer 10-Minute Reproducibility Guide (Feature G7)")
        st.code("""# 1. Clone repository & install exact requirements
git clone https://github.com/YOUR_USERNAME/TheEarthlyFavouritesOfTheDivinePriority.git
cd TheEarthlyFavouritesOfTheDivinePriority
pip install -r requirements.txt

# 2. Run automated data integrity & provenance tests
python src/validate_data.py
pytest tests/

# 3. Launch Dual-Mode Bilingual Web Application locally
streamlit run app/app.py""", language="bash")

        st.markdown("#### 📜 Licences, Provenance & AI-Use Disclosure (Features A3, G8, J2)")
        st.info("""
        * **Code Licence:** MIT License | **Data & Figures Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0).
        * **Database Redistribution Compliance (J2):** Zero bulk scraping of restricted databases (such as IMPPAT) was performed. Every compound row is independently curated from primary analytical literature DOIs (RP-HPLC, HPTLC, GC-MS) and open CC0 PubChem/LOTUS identifiers.
        * **AI-Use Disclosure Statement (G8):** In accordance with COPE and journal transparency policies, AI pair-programming was utilized for Streamlit UI scaffolding, bilingual (English/Hindi) translation refinement, and Python script structuring. All botanical taxonomy (*Cynodon dactylon* disambiguation), literature selection, hypothesis formulation, and scientific interpretations were verified by the author.
        """)
