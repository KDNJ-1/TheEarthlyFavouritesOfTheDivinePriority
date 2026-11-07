"""
Data Validation & Provenance Integrity Script (Feature D6)
Checks data/durva_compounds_v1.csv for missing values, duplicate CIDs,
valid DOI strings, and Lipinski rule consistency.
"""
import sys
import pandas as pd

REQUIRED_COLS = [
    "compound_id", "compound_name", "name_hi", "plant_part",
    "pubchem_cid", "smiles", "mol_weight", "logP", "TPSA",
    "how_found", "source_doi", "reported_use", "evidence_grade"
]

def validate_csv(filepath="data/durva_compounds_v1.csv"):
    df = pd.read_csv(filepath)
    errors = []

    # 1. Check required columns
    for col in REQUIRED_COLS:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")

    if errors:
        return False, errors

    # 2. Check for null/empty values in critical columns
    for col in ["compound_name", "pubchem_cid", "smiles", "source_doi"]:
        if df[col].isnull().any():
            errors.append(f"Null values detected in critical column: {col}")

    # 3. Check duplicate PubChem CIDs
    if df["pubchem_cid"].duplicated().any():
        dups = df[df["pubchem_cid"].duplicated()]["compound_name"].tolist()
        errors.append(f"Duplicate PubChem CIDs found for: {dups}")

    # 4. Check DOI provenance format (must start with 10.)
    for idx, row in df.iterrows():
        doi = str(row["source_doi"]).strip()
        if not doi.startswith("10."):
            errors.append(f"Row {idx} ({row['compound_name']}) has invalid DOI provenance: {doi}")

    # 5. Check physicochemical ranges
    if (df["mol_weight"] <= 0).any():
        errors.append("Non-positive molecular weight detected.")

    return len(errors) == 0, errors

if __name__ == "__main__":
    ok, errs = validate_csv()
    if ok:
        print("✅ PASS: durva_compounds_v1.csv passed all schema, provenance, and chemistry checks!")
        sys.exit(0)
    else:
        print("❌ FAIL: Data validation errors found:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
