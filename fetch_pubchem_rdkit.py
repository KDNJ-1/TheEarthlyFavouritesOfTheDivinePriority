"""
Automated PubChem & RDKit Property Calculator (Features D2 & D3)
Fetches Canonical SMILES, CID, and computes Lipinski Rule-of-5 descriptors.
"""
import pandas as pd

def compute_rdkit_properties(smiles_str):
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors
        mol = Chem.MolFromSmiles(smiles_str)
        if mol is None:
            return None
        mw = round(Descriptors.MolWt(mol), 2)
        logp = round(Descriptors.MolLogP(mol), 2)
        tpsa = round(Descriptors.TPSA(mol), 2)
        hbd = Descriptors.NumHDonors(mol)
        hba = Descriptors.NumHAcceptors(mol)
        rot = Descriptors.NumRotatableBonds(mol)
        violations = sum([mw > 500, logp > 5, hbd > 5, hba > 10])
        return {
            "mol_weight": mw,
            "logP": logp,
            "TPSA": tpsa,
            "H_donors": hbd,
            "H_acceptors": hba,
            "rotatable_bonds": rot,
            "lipinski_violations": violations,
            "lipinski_pass": "Pass" if violations <= 1 else "Check"
        }
    except ImportError:
        print("Install rdkit via: pip install rdkit")
        return None

if __name__ == "__main__":
    print("Run inside Google Colab or local environment with RDKit and PubChemPy installed.")
