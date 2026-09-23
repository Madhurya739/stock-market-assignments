import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "data/bluestock_mf.db"  # adjust path as needed


def get_connection():
    """TODO: Add docstring."""
    return sqlite3.connect(DB_PATH)


@st.cache_data(ttl=600)
def get_companies():
    """TODO: Add docstring."""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM companies", conn)
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_ratios(ticker, year=None):
    """TODO: Add docstring."""
    conn = get_connection()
    query = "SELECT * FROM ratios WHERE ticker=?"
    params = [ticker]
    if year:
        query += " AND year=?"
        params.append(year)
    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_pl(ticker):
    """TODO: Add docstring."""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM profit_loss WHERE ticker=?", conn, params=[ticker])
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_bs(ticker):
    """TODO: Add docstring."""
    conn = get_connection()
    df = pd.read_sql(
        "SELECT * FROM balance_sheet WHERE ticker=?", conn, params=[ticker]
    )
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_cf(ticker):
    """TODO: Add docstring."""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM cash_flow WHERE ticker=?", conn, params=[ticker])
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_sectors():
    """TODO: Add docstring."""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM sectors", conn)
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_peers(group_name):
    """TODO: Add docstring."""
    conn = get_connection()
    df = pd.read_sql(
        "SELECT * FROM peers WHERE group_name=?", conn, params=[group_name]
    )
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_valuation(ticker):
    """TODO: Add docstring."""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM valuation WHERE ticker=?", conn, params=[ticker])
    conn.close()
    return df
