import pandas as pd
import pytest

from src.extract.extract_data import extract_data

def test_extract_valid_file(tmp_path):
    file_path = tmp_path / "patients.csv"

    data = """patient_id,first_name,last_name,date_of_birth,gender,city
            P001,Rahul,Sharma,1990-01-01,M,Delhi
            P002,Priya,Singh,1992-02-02,F,Mumbai
            """

    file_path.write_text(data)

    df = extract_data(file_path)

    assert isinstance(df,pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == [
        "patient_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "city",
        ]



def test_extract_missing_file():
    file_path = "data/raw/does_not_exist.csv"

    with pytest.raises(FileNotFoundError):
        extract_data(file_path)

def test_extract_empty_file(tmp_path):
    file_path = tmp_path / "empty.csv"

    file_path.write_text("")

    with pytest.raises(ValueError):
        extract_data(file_path)

def test_extract_missing_columns(tmp_path):
    file_path = tmp_path / "bad_data.csv"

    data = """patient_id,first_name,last_name,gender
            P001,Rahul,Sharma,M
            """

    file_path.write_text(data)

    with pytest.raises(ValueError, match="Missing required columns"):
        extract_data(file_path)