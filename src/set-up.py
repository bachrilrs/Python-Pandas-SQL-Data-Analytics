#!/usr/bin/env python3

# author : Laroussi Bachri



import sqlite3
import csv
import pandas as pd
from datetime import datetime
from pprint import pprint
from pathlib import Path


import sqlite3





csv_path = "./data/sales_data_sample.csv"
db_path = "./main.db"

df = pd.read_csv(csv_path)

def to_int(x):
    try:
        return int(str(x).strip())
    except:
        return None

def to_float(x):
    try:
        return float(str(x).strip())
    except:
        return None
    
def to_iso_date(s):
    if not s:
        return None
    s = str(s).strip()

    for fmt in ("%m/%d/%Y %H:%M","%m/%d/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s,fmt).strftime
        except ValueError:
            pass
    return s


if __name__ == '__main__': 

    con = sqlite3.connect('./main.db')
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS ventes (
    orderID             INTEGER      NOT NULL,
    orderlinenumber     INTEGER      NOT NULL,                   
    quantity            INTEGER      NOT NULL CHECK (quantity >= 0),
    price               REAL         NOT NULL CHECK (price >= 0),
    sales               REAL         NOT NULL CHECK (sales >= 0),
    date                TEXT         NOT NULL,                   
    status              TEXT         NOT NULL,                   
    QTR_ID              INTEGER      CHECK (QTR_ID BETWEEN 1 AND 4),
    month               INTEGER      CHECK (month BETWEEN 1 AND 12),
    year                INTEGER      CHECK (year BETWEEN 1900 AND 2100),

    product_category    TEXT,                                    
    prix_ref            REAL         CHECK (prix_ref >= 0),      
    ref_prod            TEXT,                                    
    company_name        TEXT,
    phone               TEXT,
    adress              TEXT,                                    
    adress_comp         TEXT,                                    
    city                TEXT,
    state               TEXT,
    zipcode             TEXT,
    country             TEXT,
    territory           TEXT,                                    
    contact_last_name   TEXT,
    contact_first_name  TEXT,
    taille              TEXT CHECK (taille IN ('Small','Medium','Large')),

    
    PRIMARY KEY (orderID, orderlinenumber)
    );
    """)

    con.commit()

    # Vérifie la structure de 'ventes'
    cur.execute("PRAGMA table_info(ventes);")
    for col in cur.fetchall():
        print(col)
    con.close()


    table_cols = ["orderID",
        "quantity",
        "price",
        "orderlinenumber",
        "sales",
        "date",
        "status",
        "QTR_ID",
        "month",
        "year",
        "product_category",
        "prix_ref",
        "ref_prod",
        "company_name",
        "phone",
        "adress",
        "adress_comp",
        "city",
        "state",
        "zipcode",
        "country",
        "territory",
        "contact_last_name",
        "contact_first_name",
        "taille"
    ]

    con = sqlite3.connect('./main.db')
    cur = con.cursor()

    with open(csv_path,'r',encoding='utf-8' , newline="")as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            values = tuple(row.get(col,"").strip() for col in table_cols)
            rows.append(values)

    placeholders = ', '.join(["?"]*len(table_cols))
    sql = f"INSERT INTO ventes ({', '.join(table_cols)}) VALUES ({placeholders})"
    # print(sql)
    # print(sql)

    cur.executemany(sql, rows) #a faire une fois 
    con.commit()
    cur.execute('Select * FROM ventes') # execute ne renvoie rien tout seul faut utiliser fetchall et print
    orders = [r for r in cur.fetchall()] # on ameliore la lisbilite avec une liste
    pprint(orders[:5])
    con.close()