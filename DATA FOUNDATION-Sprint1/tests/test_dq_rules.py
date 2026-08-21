import pandas as pd
import pytest
from rules import dq_rules

def test_pk_not_null():
    df = pd.DataFrame({"id":[1,None,3]})
    result = dq_rules.dq01_pk_not_null(df,"id")
    assert len(result)==1
    assert result.iloc[0]["severity"]=="CRITICAL"

def test_fk_exists():
    df = pd.DataFrame({"fund_id":[1,2,99]})
    ref = pd.DataFrame({"fund_id":[1,2]})
    result = dq_rules.dq02_fk_exists(df,"fund_id",ref,"fund_id")
    assert 99 in result["fund_id"].values
    assert result.iloc[0]["severity"]=="CRITICAL"

def test_opm_positive():
    df = pd.DataFrame({"opm":[10,-5,0]})
    result = dq_rules.dq03_opm_positive(df)
    assert -5 in result["opm"].values
    assert result.iloc[0]["severity"]=="WARNING"
