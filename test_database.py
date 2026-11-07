import os
import pandas as pd
from src.validate_data import validate_csv

def test_compounds_csv_exists():
    assert os.path.exists("data/durva_compounds_v1.csv")

def test_compounds_validation_passes():
    ok, errors = validate_csv("data/durva_compounds_v1.csv")
    assert ok, f"Validation failed: {errors}"

def test_positive_controls_included():
    df = pd.read_csv("data/durva_compounds_v1.csv")
    controls = df[df["role_type"] == "Positive Control"]
    assert len(controls) >= 2, "At least two clinical positive controls must be present."
