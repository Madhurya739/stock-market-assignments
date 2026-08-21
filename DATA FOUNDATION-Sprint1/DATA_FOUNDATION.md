```python

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[1], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
cd C:\Users\srisa\Desktop\Week_2 Stock Market\project
```

    C:\Users\srisa\Desktop\Week_2 Stock Market\project
    


```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[3], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[4], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[5], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[6], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
with open(r"C:\Users\Madhurya\Projects\schema.sql", "r") as f:
    cursor.executescript(f.read())

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[7], line 1
    ----> 1 with open(r"C:\Users\Madhurya\Projects\schema.sql", "r") as f:
          2     cursor.executescript(f.read())
    

    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Madhurya\\Projects\\schema.sql'



```python
with open(r"C:\Users\srisa\Desktop\Week_2 Stock Market\schema.sql", "r") as f:
    cursor.executescript(f.read())

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[8], line 1
    ----> 1 with open(r"C:\Users\srisa\Desktop\Week_2 Stock Market\schema.sql", "r") as f:
          2     cursor.executescript(f.read())
    

    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\srisa\\Desktop\\Week_2 Stock Market\\schema.sql'



```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[9], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
cd C:\Users\srisa\Desktop\Week_2 Stock Market\project
```

    C:\Users\srisa\Desktop\Week_2 Stock Market\project
    


```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[11], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[12], line 10
          6 conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
          7 cursor = conn.cursor()
          8 
          9 # Load schema
    ---> 10 with open("schema.sql", "r") as f:
         11     cursor.executescript(f.read())
         12 
         13 # Example: load CSV into table
    

    FileNotFoundError: [Errno 2] No such file or directory: 'schema.sql'



```python
import os
print(os.getcwd())

```

    C:\Users\srisa\Desktop\Week_2 Stock Market\project
    


```python
with open(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\schema.sql", "r") as f:
    cursor.executescript(f.read())

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[14], line 1
    ----> 1 with open(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\schema.sql", "r") as f:
          2     cursor.executescript(f.read())
    

    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\srisa\\Desktop\\Week_2 Stock Market\\project\\schema.sql'



```python
with open(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\schema.sql", "r") as f:
    cursor.executescript(f.read())
```


```python
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

cursor.execute("PRAGMA foreign_keys;")
print(cursor.fetchone())  # should print (1,)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    Cell In[16], line 6
          2 conn.execute("PRAGMA foreign_keys = ON;")
          3 cursor = conn.cursor()
          4 
          5 with open("schema.sql", "r") as f:
    ----> 6     cursor.executescript(f.read())
          7 
          8 cursor.execute("PRAGMA foreign_keys;")
          9 print(cursor.fetchone())  # should print (1,)
    

    OperationalError: table dim_fund already exists



```python
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

cursor.execute("PRAGMA foreign_keys;")
print(cursor.fetchone())  # should print (1,)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    Cell In[17], line 6
          2 conn.execute("PRAGMA foreign_keys = ON;")
          3 cursor = conn.cursor()
          4 
          5 with open("schema.sql", "r") as f:
    ----> 6     cursor.executescript(f.read())
          7 
          8 cursor.execute("PRAGMA foreign_keys;")
          9 print(cursor.fetchone())  # should print (1,)
    

    OperationalError: table dim_fund already exists



```python
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

cursor.execute("PRAGMA foreign_keys;")
print(cursor.fetchone())  # should print (1,)
```

    (1,)
    


```python
audit = []
audit.append({"file":"companies.csv","rows":load_csv("companies.csv","dim_company")})
audit.append({"file":"prices.csv","rows":load_csv("prices.csv","fact_prices")})
audit.append({"file":"pl.csv","rows":load_csv("pl.csv","fact_pl")})
audit.append({"file":"bs.csv","rows":load_csv("bs.csv","fact_bs")})
audit.append({"file":"cf.csv","rows":load_csv("cf.csv","fact_cf")})

pd.DataFrame(audit).to_sql("load_audit", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[19], line 2
          1 audit = []
    ----> 2 audit.append({"file":"companies.csv","rows":load_csv("companies.csv","dim_company")})
          3 audit.append({"file":"prices.csv","rows":load_csv("prices.csv","fact_prices")})
          4 audit.append({"file":"pl.csv","rows":load_csv("pl.csv","fact_pl")})
          5 audit.append({"file":"bs.csv","rows":load_csv("bs.csv","fact_bs")})
    

    NameError: name 'load_csv' is not defined



```python
import sqlite3, pandas as pd

conn = sqlite3.connect("market.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

def load_csv(csv_file, table_name):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"{table_name}: {len(df)} rows loaded")
    return len(df)

audit = []
audit.append({"file":"companies.csv","rows":load_csv("companies.csv","dim_company")})
audit.append({"file":"pl.csv","rows":load_csv("pl.csv","fact_pl")})
audit.append({"file":"bs.csv","rows":load_csv("bs.csv","fact_bs")})
audit.append({"file":"cf.csv","rows":load_csv("cf.csv","fact_cf")})

pd.DataFrame(audit).to_sql("load_audit", conn, if_exists="append", index=False)

cursor.execute("PRAGMA foreign_key_check;")
print(cursor.fetchall())  # should be []

```

    dim_company: 93 rows loaded
    fact_pl: 1277 rows loaded
    fact_bs: 1313 rows loaded
    fact_cf: 1188 rows loaded
    []
    


```python
import sqlite3, pandas as pd

conn = sqlite3.connect("market.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

def load_csv(csv_file, table_name):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"{table_name}: {len(df)} rows loaded")
    return len(df)

audit = []

# 1. Parent table first
audit.append({"file":"companies.csv","rows":load_csv("companies.csv","dim_company")})

# 2. Child fact tables next
audit.append({"file":"pl.csv","rows":load_csv("pl.csv","fact_pl")})
audit.append({"file":"bs.csv","rows":load_csv("bs.csv","fact_bs")})
audit.append({"file":"cf.csv","rows":load_csv("cf.csv","fact_cf")})

# 3. Audit table
pd.DataFrame(audit).to_sql("load_audit", conn, if_exists="append", index=False)

# 4. FK check
cursor.execute("PRAGMA foreign_key_check;")
print(cursor.fetchall())  # should be []

```

    dim_company: 93 rows loaded
    fact_pl: 1277 rows loaded
    fact_bs: 1313 rows loaded
    fact_cf: 1188 rows loaded
    []
    


```python
SELECT company_id, COUNT(DISTINCT year) AS years
FROM fact_pl
WHERE company_id IN (
    SELECT company_id FROM dim_company ORDER BY RANDOM() LIMIT 5
)
GROUP BY company_id;

```


      Cell In[22], line 1
        SELECT company_id, COUNT(DISTINCT year) AS years
                                 ^
    SyntaxError: invalid syntax. Perhaps you forgot a comma?
    



```python
load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\projectcompanies.csv","dim_company")

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[23], line 1
    ----> 1 load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\projectcompanies.csv","dim_company")
    

    Cell In[21], line 8, in load_csv(csv_file, table_name)
          7 def load_csv(csv_file, table_name):
    ----> 8     df = pd.read_csv(csv_file)
          9     df.to_sql(table_name, conn, if_exists="append", index=False)
         10     print(f"{table_name}: {len(df)} rows loaded")
         11     return len(df)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:873, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, skip_blank_lines, parse_dates, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, low_memory, memory_map, float_precision, storage_options, dtype_backend)
        861 kwds_defaults = _refine_defaults_read(
        862     dialect,
        863     delimiter,
       (...)    869     dtype_backend=dtype_backend,
        870 )
        871 kwds.update(kwds_defaults)
    --> 873 return _read(filepath_or_buffer, kwds)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:300, in _read(filepath_or_buffer, kwds)
        297 _validate_names(kwds.get("names", None))
        299 # Create the parser.
    --> 300 parser = TextFileReader(filepath_or_buffer, **kwds)
        302 if chunksize or iterator:
        303     return parser
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1645, in TextFileReader.__init__(self, f, engine, **kwds)
       1642     self.options["has_index_names"] = kwds["has_index_names"]
       1644 self.handles: IOHandles | None = None
    -> 1645 self._engine = self._make_engine(f, self.engine)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1904, in TextFileReader._make_engine(self, f, engine)
       1902     if "b" not in mode:
       1903         mode += "b"
    -> 1904 self.handles = get_handle(
       1905     f,
       1906     mode,
       1907     encoding=self.options.get("encoding", None),
       1908     compression=self.options.get("compression", None),
       1909     memory_map=self.options.get("memory_map", False),
       1910     is_text=is_text,
       1911     errors=self.options.get("encoding_errors", "strict"),
       1912     storage_options=self.options.get("storage_options", None),
       1913 )
       1914 assert self.handles is not None
       1915 f = self.handles.handle
    

    File ~\anaconda3\Lib\site-packages\pandas\io\common.py:930, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        925 elif isinstance(handle, str):
        926     # Check whether the filename is to be opened in binary mode.
        927     # Binary mode does not support 'encoding' and 'newline'.
        928     if ioargs.encoding and "b" not in ioargs.mode:
        929         # Encoding
    --> 930         handle = open(
        931             handle,
        932             ioargs.mode,
        933             encoding=ioargs.encoding,
        934             errors=errors,
        935             newline="",
        936         )
        937     else:
        938         # Binary mode
        939         handle = open(handle, ioargs.mode)
    

    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\srisa\\Desktop\\Week_2 Stock Market\\projectcompanies.csv'



```python
load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv","dim_company")
```

    dim_company: 93 rows loaded
    




    93




```python
load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv","dim_company")
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named Unnamed: 12

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[25], line 1
    ----> 1 load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv","dim_company")
    

    Cell In[21], line 9, in load_csv(csv_file, table_name)
          7 def load_csv(csv_file, table_name):
          8     df = pd.read_csv(csv_file)
    ----> 9     df.to_sql(table_name, conn, if_exists="append", index=False)
         10     print(f"{table_name}: {len(df)} rows loaded")
         11     return len(df)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv","dim_company")
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named Unnamed: 12

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[26], line 1
    ----> 1 load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv","dim_company")
    

    Cell In[21], line 9, in load_csv(csv_file, table_name)
          7 def load_csv(csv_file, table_name):
          8     df = pd.read_csv(csv_file)
    ----> 9     df.to_sql(table_name, conn, if_exists="append", index=False)
         10     print(f"{table_name}: {len(df)} rows loaded")
         11     return len(df)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

df = pd.read_csv("companies.csv")

# Drop any columns starting with "Unnamed"
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Check columns
print(df.columns)

df.to_sql("dim_company", conn, if_exists="append", index=False)

```

    Index(['Mkt Fintech — Nifty 100  |  Companies  |  92 records'], dtype='str')
    




    93




```python
load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv","dim_company")
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named Unnamed: 12

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[28], line 1
    ----> 1 load_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv","dim_company")
    

    Cell In[21], line 9, in load_csv(csv_file, table_name)
          7 def load_csv(csv_file, table_name):
          8     df = pd.read_csv(csv_file)
    ----> 9     df.to_sql(table_name, conn, if_exists="append", index=False)
         10     print(f"{table_name}: {len(df)} rows loaded")
         11     return len(df)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

df = pd.read_csv("companies.csv")

# Keep only the columns you need
df = df[['company_id','company_name','year']]

# Rename company_id → ticker
df = df.rename(columns={'company_id':'ticker'})

print(df.head())  # sanity check

df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[29], line 6
          2 
          3 df = pd.read_csv("companies.csv")
          4 
          5 # Keep only the columns you need
    ----> 6 df = df[['company_id','company_name','year']]
          7 
          8 # Rename company_id → ticker
          9 df = df.rename(columns={'company_id':'ticker'})
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['company_id', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

df = pd.read_csv("companies.csv")

# Keep only the columns you need
df = df[['ticker','company_name','year']]

# Rename company_id → ticker
df = df.rename(columns={'company_id':'ticker'})

print(df.head())  # sanity check

df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[30], line 6
          2 
          3 df = pd.read_csv("companies.csv")
          4 
          5 # Keep only the columns you need
    ----> 6 df = df[['ticker','company_name','year']]
          7 
          8 # Rename company_id → ticker
          9 df = df.rename(columns={'company_id':'ticker'})
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

df = pd.read_csv("companies.csv")

# Keep only the columns you need
df = df[['company_id','company_name','year']]

# Rename company_id → ticker
df = df.rename(columns={'company_id':'ticker'})

print(df.head())  # sanity check

df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[31], line 6
          2 
          3 df = pd.read_csv("companies.csv")
          4 
          5 # Keep only the columns you need
    ----> 6 df = df[['company_id','company_name','year']]
          7 
          8 # Rename company_id → ticker
          9 df = df.rename(columns={'company_id':'ticker'})
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['company_id', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

df = pd.read_csv("companies.csv")

# Keep only the columns you need
df = df[['company_id','company_name','year']]

# Rename company_id → ticker
df = df.rename(columns={'company_id':'ticker'})

print(df.head())  # sanity check

df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[32], line 6
          2 
          3 df = pd.read_csv("companies.csv")
          4 
          5 # Keep only the columns you need
    ----> 6 df = df[['company_id','company_name','year']]
          7 
          8 # Rename company_id → ticker
          9 df = df.rename(columns={'company_id':'ticker'})
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['company_id', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

df = pd.read_csv("companies.csv")

# Show actual column names
print(df.columns.tolist())

```

    ['Mkt Fintech — Nifty 100  |  Companies  |  92 records', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']
    


```python
# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only the columns you need
df = df[['company_id','company_name','year']]

# Rename company_id → ticker
df = df.rename(columns={'company_id':'ticker'})

print(df.head())

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[34], line 5
          1 # Drop any Unnamed columns
          2 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          3 
          4 # Keep only the columns you need
    ----> 5 df = df[['company_id','company_name','year']]
          6 
          7 # Rename company_id → ticker
          8 df = df.rename(columns={'company_id':'ticker'})
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['company_id', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
df.to_sql("dim_company", conn, if_exists="append", index=False)

```




    93




```python
df = pd.read_csv("companies.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[['company_id','company_name','year']]
df = df.rename(columns={'company_id':'ticker'})
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[36], line 3
          1 df = pd.read_csv("companies.csv")
          2 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    ----> 3 df = df[['company_id','company_name','year']]
          4 df = df.rename(columns={'company_id':'ticker'})
          5 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['company_id', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
df = pd.read_csv("companies.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[['ticker','company_name','year']]
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[37], line 3
          1 df = pd.read_csv("companies.csv")
          2 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    ----> 3 df = df[['ticker','company_name','year']]
          4 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
df = pd.read_csv("companies.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[['company_id','company_name','year']]
df = df.rename(columns={'company_id':'ticker'})
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[38], line 3
          1 df = pd.read_csv("companies.csv")
          2 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    ----> 3 df = df[['company_id','company_name','year']]
          4 df = df.rename(columns={'company_id':'ticker'})
          5 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['company_id', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

# Read CSV
df = pd.read_csv("companies.csv")

# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file
df.to_csv("companies_clean.csv", index=False)

print(df.head())

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[39], line 10
          6 # Drop any Unnamed columns
          7 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          8 
          9 # Keep only ticker, company_name, year
    ---> 10 df = df[['ticker','company_name','year']]
         11 
         12 # Save cleaned file
         13 df.to_csv("companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

# Read CSV
df = pd.read_csv("companies.csv")

# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file
df.to_csv("companies_clean.csv", index=False)

print(df.head())

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[40], line 10
          6 # Drop any Unnamed columns
          7 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          8 
          9 # Keep only ticker, company_name, year
    ---> 10 df = df[['ticker','company_name','year']]
         11 
         12 # Save cleaned file
         13 df.to_csv("companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

# Read CSV
df = pd.read_csv("companies.csv")

# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file
df.to_csv("companies_clean.csv", index=False)

print(df.head())

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[41], line 10
          6 # Drop any Unnamed columns
          7 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          8 
          9 # Keep only ticker, company_name, year
    ---> 10 df = df[['ticker','company_name','year']]
         11 
         12 # Save cleaned file
         13 df.to_csv("companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

# Read CSV
df = pd.read_csv("companies.csv")

# Drop any columns with 'Unnamed' or empty names
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only the essential columns
df = df[['ticker','company_name','year']]

# Save cleaned file
df.to_csv("companies_clean.csv", index=False)

print(df.head())

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[42], line 11
          7 df = df.loc[:, df.columns.notnull()]
          8 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          9 
         10 # Keep only the essential columns
    ---> 11 df = df[['ticker','company_name','year']]
         12 
         13 # Save cleaned file
         14 df.to_csv("companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

# Read CSV
df = pd.read_csv("companies1.csv")

# Drop any columns with 'Unnamed' or empty names
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only the essential columns
df = df[['ticker','company_name','year']]

# Save cleaned file
df.to_csv("companies_clean.csv", index=False)

print(df.head())

```

           ticker                company_name  year
    0         ABB            Abbott India Ltd  2019
    1  ADANIENSOL  Adani Energy Solutions Ltd  2020
    2    ADANIENT       Adani Enterprises Ltd  2021
    3  ADANIGREEN      Adani Green Energy Ltd  2022
    4  ADANIPORTS       Adani Ports & SEZ Ltd  2025
    


```python
df = pd.read_csv("companies1_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[45], line 2
          1 df = pd.read_csv("companies1_clean.csv")
    ----> 2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
df = pd.read_csv("companies1_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[46], line 1
    ----> 1 df = pd.read_csv("companies1_clean.csv")
          2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:873, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, skip_blank_lines, parse_dates, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, low_memory, memory_map, float_precision, storage_options, dtype_backend)
        861 kwds_defaults = _refine_defaults_read(
        862     dialect,
        863     delimiter,
       (...)    869     dtype_backend=dtype_backend,
        870 )
        871 kwds.update(kwds_defaults)
    --> 873 return _read(filepath_or_buffer, kwds)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:300, in _read(filepath_or_buffer, kwds)
        297 _validate_names(kwds.get("names", None))
        299 # Create the parser.
    --> 300 parser = TextFileReader(filepath_or_buffer, **kwds)
        302 if chunksize or iterator:
        303     return parser
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1645, in TextFileReader.__init__(self, f, engine, **kwds)
       1642     self.options["has_index_names"] = kwds["has_index_names"]
       1644 self.handles: IOHandles | None = None
    -> 1645 self._engine = self._make_engine(f, self.engine)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1904, in TextFileReader._make_engine(self, f, engine)
       1902     if "b" not in mode:
       1903         mode += "b"
    -> 1904 self.handles = get_handle(
       1905     f,
       1906     mode,
       1907     encoding=self.options.get("encoding", None),
       1908     compression=self.options.get("compression", None),
       1909     memory_map=self.options.get("memory_map", False),
       1910     is_text=is_text,
       1911     errors=self.options.get("encoding_errors", "strict"),
       1912     storage_options=self.options.get("storage_options", None),
       1913 )
       1914 assert self.handles is not None
       1915 f = self.handles.handle
    

    File ~\anaconda3\Lib\site-packages\pandas\io\common.py:930, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        925 elif isinstance(handle, str):
        926     # Check whether the filename is to be opened in binary mode.
        927     # Binary mode does not support 'encoding' and 'newline'.
        928     if ioargs.encoding and "b" not in ioargs.mode:
        929         # Encoding
    --> 930         handle = open(
        931             handle,
        932             ioargs.mode,
        933             encoding=ioargs.encoding,
        934             errors=errors,
        935             newline="",
        936         )
        937     else:
        938         # Binary mode
        939         handle = open(handle, ioargs.mode)
    

    FileNotFoundError: [Errno 2] No such file or directory: 'companies1_clean.csv'



```python
df = pd.read_csv("companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[47], line 1
    ----> 1 df = pd.read_csv("companies_clean.csv")
          2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:873, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, skip_blank_lines, parse_dates, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, low_memory, memory_map, float_precision, storage_options, dtype_backend)
        861 kwds_defaults = _refine_defaults_read(
        862     dialect,
        863     delimiter,
       (...)    869     dtype_backend=dtype_backend,
        870 )
        871 kwds.update(kwds_defaults)
    --> 873 return _read(filepath_or_buffer, kwds)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:300, in _read(filepath_or_buffer, kwds)
        297 _validate_names(kwds.get("names", None))
        299 # Create the parser.
    --> 300 parser = TextFileReader(filepath_or_buffer, **kwds)
        302 if chunksize or iterator:
        303     return parser
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1645, in TextFileReader.__init__(self, f, engine, **kwds)
       1642     self.options["has_index_names"] = kwds["has_index_names"]
       1644 self.handles: IOHandles | None = None
    -> 1645 self._engine = self._make_engine(f, self.engine)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1904, in TextFileReader._make_engine(self, f, engine)
       1902     if "b" not in mode:
       1903         mode += "b"
    -> 1904 self.handles = get_handle(
       1905     f,
       1906     mode,
       1907     encoding=self.options.get("encoding", None),
       1908     compression=self.options.get("compression", None),
       1909     memory_map=self.options.get("memory_map", False),
       1910     is_text=is_text,
       1911     errors=self.options.get("encoding_errors", "strict"),
       1912     storage_options=self.options.get("storage_options", None),
       1913 )
       1914 assert self.handles is not None
       1915 f = self.handles.handle
    

    File ~\anaconda3\Lib\site-packages\pandas\io\common.py:930, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        925 elif isinstance(handle, str):
        926     # Check whether the filename is to be opened in binary mode.
        927     # Binary mode does not support 'encoding' and 'newline'.
        928     if ioargs.encoding and "b" not in ioargs.mode:
        929         # Encoding
    --> 930         handle = open(
        931             handle,
        932             ioargs.mode,
        933             encoding=ioargs.encoding,
        934             errors=errors,
        935             newline="",
        936         )
        937     else:
        938         # Binary mode
        939         handle = open(handle, ioargs.mode)
    

    FileNotFoundError: [Errno 2] No such file or directory: 'companies_clean.csv'



```python
df = pd.read_csv("companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[48], line 2
          1 df = pd.read_csv("companies_clean.csv")
    ----> 2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

# Read original file
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv")

# Drop any blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file in the same folder
df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)

print("Cleaned file saved successfully")

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[49], line 11
          7 df = df.loc[:, df.columns.notnull()]
          8 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          9 
         10 # Keep only ticker, company_name, year
    ---> 11 df = df[['ticker','company_name','year']]
         12 
         13 # Save cleaned file in the same folder
         14 df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
cd C:\Users\srisa\Desktop\Week_2 Stock Market\project
```

    C:\Users\srisa\Desktop\Week_2 Stock Market\project
    


```python
import pandas as pd

# Read original file
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv")

# Drop any blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file in the same folder
df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)

print("Cleaned file saved successfully")

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[51], line 11
          7 df = df.loc[:, df.columns.notnull()]
          8 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          9 
         10 # Keep only ticker, company_name, year
    ---> 11 df = df[['ticker','company_name','year']]
         12 
         13 # Save cleaned file in the same folder
         14 df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

# Read original file
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv")

# Drop any blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file in the same folder
df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)

print("Cleaned file saved successfully")

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[52], line 11
          7 df = df.loc[:, df.columns.notnull()]
          8 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          9 
         10 # Keep only ticker, company_name, year
    ---> 11 df = df[['ticker','company_name','year']]
         12 
         13 # Save cleaned file in the same folder
         14 df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

# Read original file
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv")

# Drop any blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file in the same folder
df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)

print("Cleaned file saved successfully")
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[53], line 11
          7 df = df.loc[:, df.columns.notnull()]
          8 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          9 
         10 # Keep only ticker, company_name, year
    ---> 11 df = df[['ticker','company_name','year']]
         12 
         13 # Save cleaned file in the same folder
         14 df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'company_name', 'year'], dtype='str')] are in the [columns]"



```python
import pandas as pd

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv")
print(df.columns.tolist())

```

    ['Mkt Fintech — Nifty 100  |  Companies  |  92 records', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10']
    


```python
import pandas as pd

# Skip the first row (metadata), use the second row as header
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)

# Drop any blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file
df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)

print(df.head())

```

           ticker                               company_name  year
    0         ABB                           Abbott India Ltd  2019
    1  ADANIENSOL                 Adani Energy Solutions Ltd  2020
    2    ADANIENT                      Adani Enterprises Ltd  2021
    3  ADANIGREEN                     Adani Green Energy Ltd  2022
    4  ADANIPORTS  Adani Ports & Special Economic Zone Ltd\n  2025
    


```python
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[56], line 2
          1 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[57], line 2
          1 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[58], line 2
          1 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[59], line 2
          1 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

# Skip the first row (metadata), use the second row as header
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)

# Drop any blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only ticker, company_name, year
df = df[['ticker','company_name','year']]

# Save cleaned file
df.to_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv", index=False)

print(df.head())


```

           ticker                               company_name  year
    0         ABB                           Abbott India Ltd  2019
    1  ADANIENSOL                 Adani Energy Solutions Ltd  2020
    2    ADANIENT                      Adani Enterprises Ltd  2021
    3  ADANIGREEN                     Adani Green Energy Ltd  2022
    4  ADANIPORTS  Adani Ports & Special Economic Zone Ltd\n  2025
    


```python
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[61], line 2
          1 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 2 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")

# If table expects company_id instead of ticker
df = df.rename(columns={'ticker':'company_id'})

df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named company_id

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[62], line 6
          2 
          3 # If table expects company_id instead of ticker
          4 df = df.rename(columns={'ticker':'company_id'})
          5 
    ----> 6 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[63], line 4
          1 import pandas as pd
          2 
          3 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 4 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[64], line 4
          1 import pandas as pd
          2 
          3 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 4 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[65], line 4
          1 import pandas as pd
          2 
          3 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 4 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
df.to_sql("dim_company", conn, if_exists="append", index=False)

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[66], line 4
          1 import pandas as pd
          2 
          3 df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies_clean.csv")
    ----> 4 df.to_sql("dim_company", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# --- Helper function to clean CSVs ---
def clean_and_load(file_path, table_name, keep_cols):
    # Skip metadata row if present
    df = pd.read_csv(file_path, skiprows=1)

    # Drop blank/Unnamed columns
    df = df.loc[:, df.columns.notnull()]
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Keep only required columns
    df = df[keep_cols]

    # Load into SQLite
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Load dimension table ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
    "dim_company",
    ["ticker", "company_name", "year"]
)

# --- Load fact tables ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv",
    "fact_pl",
    ["ticker", "year", "revenue", "expenses", "profit"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv",
    "fact_bs",
    ["ticker", "year", "assets", "liabilities", "equity"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_cf.csv",
    "fact_cf",
    ["ticker", "year", "operating_cf", "investing_cf", "financing_cf"]
)

# --- Audit ---
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("dim_company rows:", cur.fetchone()[0])

cur.execute("PRAGMA foreign_key_check;")
print("Foreign key check:", cur.fetchall())

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[67], line 24
         20     df.to_sql(table_name, conn, if_exists="append", index=False)
         21     print(f"Loaded {len(df)} rows into {table_name}")
         22 
         23 # --- Load dimension table ---
    ---> 24 clean_and_load(
         25     r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
         26     "dim_company",
         27     ["ticker", "company_name", "year"]
    

    Cell In[67], line 20, in clean_and_load(file_path, table_name, keep_cols)
         16     # Keep only required columns
         17     df = df[keep_cols]
         18 
         19     # Load into SQLite
    ---> 20     df.to_sql(table_name, conn, if_exists="append", index=False)
         21     print(f"Loaded {len(df)} rows into {table_name}")
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# --- Helper function to clean CSVs ---
def clean_and_load(file_path, table_name, keep_cols):
    # Skip metadata row if present
    df = pd.read_csv(file_path, skiprows=1)

    # Drop blank/Unnamed columns
    df = df.loc[:, df.columns.notnull()]
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Keep only required columns
    df = df[keep_cols]

    # Load into SQLite
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Load dimension table ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
    "dim_company",
    ["ticker", "company_name", "year"]
)

# --- Load fact tables ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv",
    "fact_pl",
    ["ticker", "year", "revenue", "expenses", "profit"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv",
    "fact_bs",
    ["ticker", "year", "assets", "liabilities", "equity"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_cf.csv",
    "fact_cf",
    ["ticker", "year", "operating_cf", "investing_cf", "financing_cf"]
)

# --- Audit ---
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("dim_company rows:", cur.fetchone()[0])

cur.execute("PRAGMA foreign_key_check;")
print("Foreign key check:", cur.fetchall())

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[68], line 24
         20     df.to_sql(table_name, conn, if_exists="append", index=False)
         21     print(f"Loaded {len(df)} rows into {table_name}")
         22 
         23 # --- Load dimension table ---
    ---> 24 clean_and_load(
         25     r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
         26     "dim_company",
         27     ["ticker", "company_name", "year"]
    

    Cell In[68], line 20, in clean_and_load(file_path, table_name, keep_cols)
         16     # Keep only required columns
         17     df = df[keep_cols]
         18 
         19     # Load into SQLite
    ---> 20     df.to_sql(table_name, conn, if_exists="append", index=False)
         21     print(f"Loaded {len(df)} rows into {table_name}")
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# --- Helper function to clean CSVs ---
def clean_and_load(file_path, table_name, keep_cols):
    # Skip metadata row if present
    df = pd.read_csv(file_path, skiprows=1)

    # Drop blank/Unnamed columns
    df = df.loc[:, df.columns.notnull()]
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Keep only required columns
    df = df[keep_cols]

    # Load into SQLite
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Load dimension table ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
    "dim_company",
    ["ticker", "company_name", "year"]
)

# --- Load fact tables ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv",
    "fact_pl",
    ["ticker", "year", "revenue", "expenses", "profit"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv",
    "fact_bs",
    ["ticker", "year", "assets", "liabilities", "equity"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_cf.csv",
    "fact_cf",
    ["ticker", "year", "operating_cf", "investing_cf", "financing_cf"]
)

# --- Audit ---
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("dim_company rows:", cur.fetchone()[0])

cur.execute("PRAGMA foreign_key_check;")
print("Foreign key check:", cur.fetchall())

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[69], line 24
         20     df.to_sql(table_name, conn, if_exists="append", index=False)
         21     print(f"Loaded {len(df)} rows into {table_name}")
         22 
         23 # --- Load dimension table ---
    ---> 24 clean_and_load(
         25     r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
         26     "dim_company",
         27     ["ticker", "company_name", "year"]
    

    Cell In[69], line 20, in clean_and_load(file_path, table_name, keep_cols)
         16     # Keep only required columns
         17     df = df[keep_cols]
         18 
         19     # Load into SQLite
    ---> 20     df.to_sql(table_name, conn, if_exists="append", index=False)
         21     print(f"Loaded {len(df)} rows into {table_name}")
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

# Connect to your database
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Read CSV, skip metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)

# Drop blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only required columns
df = df[['ticker','company_name','year']]

# Load into SQLite
df.to_sql("dim_company", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[70], line 18
         14 # Keep only required columns
         15 df = df[['ticker','company_name','year']]
         16 
         17 # Load into SQLite
    ---> 18 df.to_sql("dim_company", conn, if_exists="append", index=False)
         19 
         20 # Audit
         21 cur = conn.cursor()
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Read CSV, skip metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)

# Drop blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only required columns
df = df[['ticker','company_name','year']]

# Load into SQLite
df.to_sql("dim_company", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[71], line 17
         13 # Keep only required columns
         14 df = df[['ticker','company_name','year']]
         15 
         16 # Load into SQLite
    ---> 17 df.to_sql("dim_company", conn, if_exists="append", index=False)
         18 
         19 # Audit
         20 cur = conn.cursor()
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Read CSV, skip metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)

# Drop blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only required columns
df = df[['ticker','company_name','year']]

# Load into SQLite
df.to_sql("dim_company", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[72], line 17
         13 # Keep only required columns
         14 df = df[['ticker','company_name','year']]
         15 
         16 # Load into SQLite
    ---> 17 df.to_sql("dim_company", conn, if_exists="append", index=False)
         18 
         19 # Audit
         20 cur = conn.cursor()
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)

# Drop blank/Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only required columns
df = df[['ticker','company_name','year']]

# Load into SQLite
df.to_sql("dim_company", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[73], line 16
         12 # Keep only required columns
         13 df = df[['ticker','company_name','year']]
         14 
         15 # Load into SQLite
    ---> 16 df.to_sql("dim_company", conn, if_exists="append", index=False)
         17 
         18 # Audit
         19 cur = conn.cursor()
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[['ticker','company_name','year']]

df.to_sql("dim_company", conn, if_exists="append", index=False)

cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

conn.close()

```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2571, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2570 try:
    -> 2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    

    OperationalError: table dim_company has no column named ticker

    
    The above exception was the direct cause of the following exception:
    

    DatabaseError                             Traceback (most recent call last)

    Cell In[74], line 11
          7 df = df.loc[:, df.columns.notnull()]
          8 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
          9 df = df[['ticker','company_name','year']]
         10 
    ---> 11 df.to_sql("dim_company", conn, if_exists="append", index=False)
         12 
         13 cur = conn.cursor()
         14 cur.execute("SELECT COUNT(*) FROM dim_company;")
    

    File ~\anaconda3\Lib\site-packages\pandas\core\generic.py:3052, in NDFrame.to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       3048         3
       3049         """  # noqa: E501
       3050         from pandas.io import sql
       3051 
    -> 3052         return sql.to_sql(
       3053             self,
       3054             name,
       3055             con,
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:841, in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method, engine, **engine_kwargs)
        836     raise NotImplementedError(
        837         "'frame' argument should be either a Series or a DataFrame"
        838     )
        840 with pandasSQL_builder(con, schema=schema, need_transaction=True) as pandas_sql:
    --> 841     return pandas_sql.to_sql(
        842         frame,
        843         name,
        844         if_exists=if_exists,
        845         index=index,
        846         index_label=index_label,
        847         schema=schema,
        848         chunksize=chunksize,
        849         dtype=dtype,
        850         method=method,
        851         engine=engine,
        852         **engine_kwargs,
        853     )
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2880, in SQLiteDatabase.to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method, engine, **engine_kwargs)
       2870 table = SQLiteTable(
       2871     name,
       2872     self,
       (...)   2877     dtype=dtype,
       2878 )
       2879 table.create()
    -> 2880 return table.insert(chunksize, method)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:1122, in SQLTable.insert(self, chunksize, method)
       1117     break
       1119 chunk_iter = zip(
       1120     *(arr[start_i:end_i] for arr in data_list), strict=True
       1121 )
    -> 1122 num_inserted = exec_insert(conn, keys, chunk_iter)
       1123 # GH 46891
       1124 if num_inserted is not None:
    

    File ~\anaconda3\Lib\site-packages\pandas\io\sql.py:2573, in SQLiteTable._execute_insert(self, conn, keys, data_iter)
       2571     conn.executemany(self.insert_statement(num_rows=1), data_list)
       2572 except Error as exc:
    -> 2573     raise DatabaseError("Execution failed") from exc
       2574 return conn.rowcount
    

    DatabaseError: Execution failed



```python
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

```


```python
cur = conn.cursor()
cur.execute("PRAGMA table_info(dim_company);")
print(cur.fetchall())

```

    [(0, 'Mkt Fintech — Nifty 100  |  Companies  |  92 records', 'TEXT', 0, None, 0), (1, 'Unnamed: 1', 'TEXT', 0, None, 0), (2, 'Unnamed: 2', 'TEXT', 0, None, 0), (3, 'Unnamed: 3', 'TEXT', 0, None, 0), (4, 'Unnamed: 4', 'TEXT', 0, None, 0), (5, 'Unnamed: 5', 'TEXT', 0, None, 0), (6, 'Unnamed: 6', 'TEXT', 0, None, 0), (7, 'Unnamed: 7', 'TEXT', 0, None, 0), (8, 'Unnamed: 8', 'TEXT', 0, None, 0), (9, 'Unnamed: 9', 'TEXT', 0, None, 0), (10, 'Unnamed: 10', 'TEXT', 0, None, 0), (11, 'Unnamed: 11', 'TEXT', 0, None, 0)]
    


```python
import sqlite3
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS dim_company;")
conn.commit()
conn.close()

```


```python
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE dim_company (
    ticker TEXT PRIMARY KEY,
    company_name TEXT NOT NULL,
    year INTEGER
);
""")
conn.commit()
conn.close()

```


```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Skip the metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv", skiprows=1)

# Drop Unnamed columns
df = df.loc[:, df.columns.notnull()]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Keep only the right columns
df = df[['ticker','company_name','year']]

# Load into SQLite
df.to_sql("dim_company", conn, if_exists="append", index=False)

cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

conn.close()

```

    Rows in dim_company: 92
    


```python
import sqlite3
import pandas as pd

db_path = r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# --- Drop and recreate tables ---
cur.execute("DROP TABLE IF EXISTS dim_company;")
cur.execute("DROP TABLE IF EXISTS fact_pl;")
cur.execute("DROP TABLE IF EXISTS fact_bs;")
cur.execute("DROP TABLE IF EXISTS fact_cf;")

cur.execute("""
CREATE TABLE dim_company (
    ticker TEXT PRIMARY KEY,
    company_name TEXT NOT NULL,
    year INTEGER
);
""")

cur.execute("""
CREATE TABLE fact_pl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year INTEGER NOT NULL,
    revenue REAL,
    expenses REAL,
    profit REAL,
    FOREIGN KEY (ticker) REFERENCES dim_company(ticker)
);
""")

cur.execute("""
CREATE TABLE fact_bs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year INTEGER NOT NULL,
    assets REAL,
    liabilities REAL,
    equity REAL,
    FOREIGN KEY (ticker) REFERENCES dim_company(ticker)
);
""")

cur.execute("""
CREATE TABLE fact_cf (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year INTEGER NOT NULL,
    operating_cf REAL,
    investing_cf REAL,
    financing_cf REAL,
    FOREIGN KEY (ticker) REFERENCES dim_company(ticker)
);
""")

conn.commit()

# --- Helper function to clean and load ---
def clean_and_load(file_path, table_name, keep_cols, skiprows=1):
    df = pd.read_csv(file_path, skiprows=skiprows)
    df = df.loc[:, df.columns.notnull()]
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df[keep_cols]
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Load dimension table ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
    "dim_company",
    ["ticker","company_name","year"]
)

# --- Load fact tables ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_pl.csv",
    "fact_pl",
    ["ticker","year","revenue","expenses","profit"],
    skiprows=0
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_bs.csv",
    "fact_bs",
    ["ticker","year","assets","liabilities","equity"],
    skiprows=0
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_cf.csv",
    "fact_cf",
    ["ticker","year","operating_cf","investing_cf","financing_cf"],
    skiprows=0
)

# --- Audit ---
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

cur.execute("PRAGMA foreign_key_check;")
print("Foreign key check:", cur.fetchall())

conn.close()

```

    Loaded 92 rows into dim_company
    


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    Cell In[80], line 77
         73     ["ticker","company_name","year"]
         74 )
         75 
         76 # --- Load fact tables ---
    ---> 77 clean_and_load(
         78     r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_pl.csv",
         79     "fact_pl",
         80     ["ticker","year","revenue","expenses","profit"],
    

    Cell In[80], line 62, in clean_and_load(file_path, table_name, keep_cols, skiprows)
         61 def clean_and_load(file_path, table_name, keep_cols, skiprows=1):
    ---> 62     df = pd.read_csv(file_path, skiprows=skiprows)
         63     df = df.loc[:, df.columns.notnull()]
         64     df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
         65     df = df[keep_cols]
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:873, in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, skip_blank_lines, parse_dates, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, low_memory, memory_map, float_precision, storage_options, dtype_backend)
        861 kwds_defaults = _refine_defaults_read(
        862     dialect,
        863     delimiter,
       (...)    869     dtype_backend=dtype_backend,
        870 )
        871 kwds.update(kwds_defaults)
    --> 873 return _read(filepath_or_buffer, kwds)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:300, in _read(filepath_or_buffer, kwds)
        297 _validate_names(kwds.get("names", None))
        299 # Create the parser.
    --> 300 parser = TextFileReader(filepath_or_buffer, **kwds)
        302 if chunksize or iterator:
        303     return parser
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1645, in TextFileReader.__init__(self, f, engine, **kwds)
       1642     self.options["has_index_names"] = kwds["has_index_names"]
       1644 self.handles: IOHandles | None = None
    -> 1645 self._engine = self._make_engine(f, self.engine)
    

    File ~\anaconda3\Lib\site-packages\pandas\io\parsers\readers.py:1904, in TextFileReader._make_engine(self, f, engine)
       1902     if "b" not in mode:
       1903         mode += "b"
    -> 1904 self.handles = get_handle(
       1905     f,
       1906     mode,
       1907     encoding=self.options.get("encoding", None),
       1908     compression=self.options.get("compression", None),
       1909     memory_map=self.options.get("memory_map", False),
       1910     is_text=is_text,
       1911     errors=self.options.get("encoding_errors", "strict"),
       1912     storage_options=self.options.get("storage_options", None),
       1913 )
       1914 assert self.handles is not None
       1915 f = self.handles.handle
    

    File ~\anaconda3\Lib\site-packages\pandas\io\common.py:930, in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        925 elif isinstance(handle, str):
        926     # Check whether the filename is to be opened in binary mode.
        927     # Binary mode does not support 'encoding' and 'newline'.
        928     if ioargs.encoding and "b" not in ioargs.mode:
        929         # Encoding
    --> 930         handle = open(
        931             handle,
        932             ioargs.mode,
        933             encoding=ioargs.encoding,
        934             errors=errors,
        935             newline="",
        936         )
        937     else:
        938         # Binary mode
        939         handle = open(handle, ioargs.mode)
    

    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\srisa\\Desktop\\Week_2 Stock Market\\project\\\\fact_pl.csv'



```python
import sqlite3
import pandas as pd

db_path = r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# --- Drop and recreate tables ---
cur.execute("DROP TABLE IF EXISTS dim_company;")
cur.execute("DROP TABLE IF EXISTS fact_pl;")
cur.execute("DROP TABLE IF EXISTS fact_bs;")
cur.execute("DROP TABLE IF EXISTS fact_cf;")

cur.execute("""
CREATE TABLE dim_company (
    ticker TEXT PRIMARY KEY,
    company_name TEXT NOT NULL,
    year INTEGER
);
""")

cur.execute("""
CREATE TABLE fact_pl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year INTEGER NOT NULL,
    revenue REAL,
    expenses REAL,
    profit REAL,
    FOREIGN KEY (ticker) REFERENCES dim_company(ticker)
);
""")

cur.execute("""
CREATE TABLE fact_bs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year INTEGER NOT NULL,
    assets REAL,
    liabilities REAL,
    equity REAL,
    FOREIGN KEY (ticker) REFERENCES dim_company(ticker)
);
""")

cur.execute("""
CREATE TABLE fact_cf (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year INTEGER NOT NULL,
    operating_cf REAL,
    investing_cf REAL,
    financing_cf REAL,
    FOREIGN KEY (ticker) REFERENCES dim_company(ticker)
);
""")

conn.commit()

# --- Helper function to clean and load ---
def clean_and_load(file_path, table_name, keep_cols, skiprows=1):
    df = pd.read_csv(file_path, skiprows=skiprows)
    df = df.loc[:, df.columns.notnull()]
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df[keep_cols]
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Load dimension table ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
    "dim_company",
    ["ticker","company_name","year"]
)

# --- Load fact tables ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_pl.csv",
    "fact_pl",
    ["ticker","year","revenue","expenses","profit"],
    skiprows=0
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_bs.csv",
    "fact_bs",
    ["ticker","year","assets","liabilities","equity"],
    skiprows=0
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_cf.csv",
    "fact_cf",
    ["ticker","year","operating_cf","investing_cf","financing_cf"],
    skiprows=0
)

# --- Audit ---
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("Rows in dim_company:", cur.fetchone()[0])

cur.execute("PRAGMA foreign_key_check;")
print("Foreign key check:", cur.fetchall())

conn.close()

```

    Loaded 92 rows into dim_company
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[81], line 77
         73     ["ticker","company_name","year"]
         74 )
         75 
         76 # --- Load fact tables ---
    ---> 77 clean_and_load(
         78     r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\\fact_pl.csv",
         79     "fact_pl",
         80     ["ticker","year","revenue","expenses","profit"],
    

    Cell In[81], line 65, in clean_and_load(file_path, table_name, keep_cols, skiprows)
         61 def clean_and_load(file_path, table_name, keep_cols, skiprows=1):
         62     df = pd.read_csv(file_path, skiprows=skiprows)
         63     df = df.loc[:, df.columns.notnull()]
         64     df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    ---> 65     df = df[keep_cols]
         66     df.to_sql(table_name, conn, if_exists="append", index=False)
         67     print(f"Loaded {len(df)} rows into {table_name}")
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6352, in Index._raise_if_missing(self, key, indexer, axis_name)
       6350 if nmissing:
       6351     if nmissing == len(indexer):
    -> 6352         raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354     not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
       6355     raise KeyError(f"{not_found} not in index")
    

    KeyError: "None of [Index(['ticker', 'year', 'revenue', 'expenses', 'profit'], dtype='str')] are in the [columns]"



```python
import pandas as pd

df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv", nrows=1)
print(df.columns.tolist())

```

    ['Bluestock Fintech — Nifty 100  |  Profit & Loss  |  1,276 records', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14']
    


```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Skip the metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv", skiprows=1)

# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Rename columns to match your schema
df = df.rename(columns={
    'company_id': 'ticker',
    'sales': 'revenue',
    'net_profit': 'profit'
})

# Keep only the needed columns
df = df[['ticker','year','revenue','expenses','profit']]

# Load into SQLite
df.to_sql("fact_pl", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM fact_pl;")
print("Rows in fact_pl:", cur.fetchone()[0])

conn.close()

```

    Rows in fact_pl: 1276
    


```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Skip the metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv", skiprows=1)

# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Rename columns to match your schema
df = df.rename(columns={
    'company_id': 'ticker',
    'sales': 'revenue',
    'net_profit': 'profit'
})

# Keep only the needed columns
df = df[['ticker','year','revenue','expenses','profit']]

# Load into SQLite
df.to_sql("fact_pl", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM fact_bs;")
print("Rows in fact_pl:", cur.fetchone()[0])

conn.close()
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[84], line 20
         16     'net_profit': 'profit'
         17 })
         18 
         19 # Keep only the needed columns
    ---> 20 df = df[['ticker','year','revenue','expenses','profit']]
         21 
         22 # Load into SQLite
         23 df.to_sql("fact_pl", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6355, in Index._raise_if_missing(self, key, indexer, axis_name)
       6352     raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354 not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
    -> 6355 raise KeyError(f"{not_found} not in index")
    

    KeyError: "['revenue', 'expenses', 'profit'] not in index"



```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Skip the metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv", skiprows=1)

# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Rename columns to match your schema
df = df.rename(columns={
    'company_id': 'ticker',
    'total_assets': 'assets',
    'total_liabilities': 'liabilities',
    'reserves': 'equity'
})

# Keep only the needed columns
df = df[['ticker','year','assets','liabilities','equity']]

# Load into SQLite
df.to_sql("fact_bs", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM fact_bs;")
print("Rows in fact_bs:", cur.fetchone()[0])

conn.close()

```

    Rows in fact_bs: 1312
    


```python
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# Skip the metadata row
df = pd.read_csv(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_cf.csv", skiprows=1)

# Drop any Unnamed columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Rename columns to match your schema
df = df.rename(columns={
    'company_id': 'ticker',
    'total_assets': 'assets',
    'total_liabilities': 'liabilities',
    'reserves': 'equity'
})

# Keep only the needed columns
df = df[['ticker','year','assets','liabilities','equity']]

# Load into SQLite
df.to_sql("fact_bs", conn, if_exists="append", index=False)

# Audit
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM fact_cf;")
print("Rows in fact_bs:", cur.fetchone()[0])

conn.close()

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[86], line 21
         17     'reserves': 'equity'
         18 })
         19 
         20 # Keep only the needed columns
    ---> 21 df = df[['ticker','year','assets','liabilities','equity']]
         22 
         23 # Load into SQLite
         24 df.to_sql("fact_bs", conn, if_exists="append", index=False)
    

    File ~\anaconda3\Lib\site-packages\pandas\core\frame.py:4384, in DataFrame.__getitem__(self, key)
       4380                 indexer = [indexer]
       4381         else:
       4382             if is_iterator(key):
       4383                 key = list(key)
    -> 4384             indexer = self.columns._get_indexer_strict(key, "columns")[1]
       4385 
       4386         # take() does not accept boolean indexers
       4387         if getattr(indexer, "dtype", None) == bool:
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6302, in Index._get_indexer_strict(self, key, axis_name)
       6299 else:
       6300     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
    -> 6302 self._raise_if_missing(keyarr, indexer, axis_name)
       6304 keyarr = self.take(indexer)
       6305 if isinstance(key, Index):
       6306     # GH 42790 - Preserve name from an Index
    

    File ~\anaconda3\Lib\site-packages\pandas\core\indexes\base.py:6355, in Index._raise_if_missing(self, key, indexer, axis_name)
       6352     raise KeyError(f"None of [{key}] are in the [{axis_name}]")
       6354 not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
    -> 6355 raise KeyError(f"{not_found} not in index")
    

    KeyError: "['assets', 'liabilities', 'equity'] not in index"



```python
import pandas as pd
import sqlite3

db_path = r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db"
conn = sqlite3.connect(db_path)

# --- Helper function ---
def clean_and_load(file_path, table_name, rename_map, keep_cols, skiprows=1):
    # Read CSV, skip metadata row
    df = pd.read_csv(file_path, skiprows=skiprows)
    # Drop Unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # Rename columns
    df = df.rename(columns=rename_map)
    # Keep only required columns
    df = df[keep_cols]
    # Load into SQLite
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Profit & Loss ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv",
    "fact_pl",
    rename_map={
        "company_id": "ticker",
        "sales": "revenue",
        "net_profit": "profit"
    },
    keep_cols=["ticker","year","revenue","expenses","profit"]
)

# --- Balance Sheet ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv",
    "fact_bs",
    rename_map={
        "company_id": "ticker",
        "total_assets": "assets",
        "total_liabilities": "liabilities",
        "reserves": "equity"
    },
    keep_cols=["ticker","year","assets","liabilities","equity"]
)

# --- Cash Flow ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_cf.csv",
    "fact_cf",
    rename_map={
        "company_id": "ticker",
        "operating_activity": "operating_cf",
        "investing_activity": "investing_cf",
        "financing_activity": "financing_cf"
    },
    keep_cols=["ticker","year","operating_cf","investing_cf","financing_cf"]
)

# --- Audit ---
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM fact_pl;")
print("Rows in fact_pl:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM fact_bs;")
print("Rows in fact_bs:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM fact_cf;")
print("Rows in fact_cf:", cur.fetchone()[0])

cur.execute("PRAGMA foreign_key_check;")
print("Foreign key check:", cur.fetchall())

conn.close()

```

    Loaded 1276 rows into fact_pl
    Loaded 1312 rows into fact_bs
    Loaded 1187 rows into fact_cf
    Rows in fact_pl: 2552
    Rows in fact_bs: 2624
    Rows in fact_cf: 1187
    Foreign key check: [('fact_cf', 127, 'dim_company', 0), ('fact_cf', 128, 'dim_company', 0), ('fact_cf', 129, 'dim_company', 0), ('fact_cf', 130, 'dim_company', 0), ('fact_cf', 131, 'dim_company', 0), ('fact_cf', 132, 'dim_company', 0), ('fact_cf', 133, 'dim_company', 0), ('fact_cf', 1099, 'dim_company', 0), ('fact_cf', 1100, 'dim_company', 0), ('fact_cf', 1101, 'dim_company', 0), ('fact_cf', 1102, 'dim_company', 0), ('fact_cf', 1103, 'dim_company', 0), ('fact_cf', 1104, 'dim_company', 0), ('fact_cf', 1105, 'dim_company', 0), ('fact_cf', 1106, 'dim_company', 0), ('fact_cf', 1107, 'dim_company', 0), ('fact_cf', 1108, 'dim_company', 0), ('fact_cf', 1109, 'dim_company', 0), ('fact_cf', 1110, 'dim_company', 0), ('fact_cf', 1111, 'dim_company', 0), ('fact_cf', 1112, 'dim_company', 0), ('fact_cf', 1113, 'dim_company', 0), ('fact_cf', 1114, 'dim_company', 0), ('fact_cf', 1115, 'dim_company', 0), ('fact_cf', 1116, 'dim_company', 0), ('fact_cf', 1117, 'dim_company', 0), ('fact_cf', 1118, 'dim_company', 0), ('fact_cf', 1119, 'dim_company', 0), ('fact_cf', 1120, 'dim_company', 0), ('fact_cf', 1121, 'dim_company', 0), ('fact_cf', 1122, 'dim_company', 0), ('fact_cf', 1123, 'dim_company', 0), ('fact_cf', 1124, 'dim_company', 0), ('fact_cf', 1125, 'dim_company', 0), ('fact_cf', 1126, 'dim_company', 0), ('fact_cf', 1127, 'dim_company', 0), ('fact_cf', 1128, 'dim_company', 0), ('fact_cf', 1129, 'dim_company', 0), ('fact_cf', 1130, 'dim_company', 0), ('fact_cf', 1131, 'dim_company', 0), ('fact_cf', 1132, 'dim_company', 0), ('fact_cf', 1133, 'dim_company', 0), ('fact_cf', 1134, 'dim_company', 0), ('fact_cf', 1135, 'dim_company', 0), ('fact_cf', 1136, 'dim_company', 0), ('fact_cf', 1137, 'dim_company', 0), ('fact_cf', 1138, 'dim_company', 0), ('fact_cf', 1139, 'dim_company', 0), ('fact_cf', 1140, 'dim_company', 0), ('fact_cf', 1141, 'dim_company', 0), ('fact_cf', 1142, 'dim_company', 0), ('fact_cf', 1143, 'dim_company', 0), ('fact_cf', 1144, 'dim_company', 0), ('fact_cf', 1145, 'dim_company', 0), ('fact_cf', 1146, 'dim_company', 0), ('fact_cf', 1147, 'dim_company', 0), ('fact_cf', 1148, 'dim_company', 0), ('fact_cf', 1149, 'dim_company', 0), ('fact_cf', 1150, 'dim_company', 0), ('fact_cf', 1151, 'dim_company', 0), ('fact_cf', 1152, 'dim_company', 0), ('fact_cf', 1153, 'dim_company', 0), ('fact_cf', 1154, 'dim_company', 0), ('fact_cf', 1155, 'dim_company', 0), ('fact_cf', 1156, 'dim_company', 0), ('fact_cf', 1157, 'dim_company', 0), ('fact_cf', 1158, 'dim_company', 0), ('fact_cf', 1159, 'dim_company', 0), ('fact_cf', 1160, 'dim_company', 0), ('fact_cf', 1161, 'dim_company', 0), ('fact_cf', 1162, 'dim_company', 0), ('fact_cf', 1163, 'dim_company', 0), ('fact_cf', 1164, 'dim_company', 0), ('fact_cf', 1165, 'dim_company', 0), ('fact_cf', 1166, 'dim_company', 0), ('fact_cf', 1167, 'dim_company', 0), ('fact_cf', 1168, 'dim_company', 0), ('fact_cf', 1169, 'dim_company', 0), ('fact_cf', 1170, 'dim_company', 0), ('fact_cf', 1171, 'dim_company', 0), ('fact_cf', 1172, 'dim_company', 0), ('fact_cf', 1173, 'dim_company', 0), ('fact_cf', 1174, 'dim_company', 0), ('fact_cf', 1175, 'dim_company', 0), ('fact_cf', 1176, 'dim_company', 0), ('fact_cf', 1177, 'dim_company', 0), ('fact_cf', 1178, 'dim_company', 0), ('fact_cf', 1179, 'dim_company', 0), ('fact_cf', 1180, 'dim_company', 0), ('fact_cf', 1181, 'dim_company', 0), ('fact_cf', 1182, 'dim_company', 0), ('fact_cf', 1183, 'dim_company', 0), ('fact_cf', 1184, 'dim_company', 0), ('fact_cf', 1185, 'dim_company', 0), ('fact_cf', 1186, 'dim_company', 0), ('fact_cf', 1187, 'dim_company', 0), ('fact_bs', 1034, 'dim_company', 0), ('fact_bs', 1035, 'dim_company', 0), ('fact_bs', 1036, 'dim_company', 0), ('fact_bs', 1037, 'dim_company', 0), ('fact_bs', 1038, 'dim_company', 0), ('fact_bs', 1039, 'dim_company', 0), ('fact_bs', 1040, 'dim_company', 0), ('fact_bs', 1041, 'dim_company', 0), ('fact_bs', 1042, 'dim_company', 0), ('fact_bs', 1043, 'dim_company', 0), ('fact_bs', 1044, 'dim_company', 0), ('fact_bs', 1045, 'dim_company', 0), ('fact_bs', 1046, 'dim_company', 0), ('fact_bs', 1060, 'dim_company', 0), ('fact_bs', 1061, 'dim_company', 0), ('fact_bs', 1062, 'dim_company', 0), ('fact_bs', 1063, 'dim_company', 0), ('fact_bs', 1064, 'dim_company', 0), ('fact_bs', 1065, 'dim_company', 0), ('fact_bs', 1066, 'dim_company', 0), ('fact_bs', 1067, 'dim_company', 0), ('fact_bs', 1068, 'dim_company', 0), ('fact_bs', 1069, 'dim_company', 0), ('fact_bs', 1070, 'dim_company', 0), ('fact_bs', 1071, 'dim_company', 0), ('fact_bs', 1072, 'dim_company', 0), ('fact_bs', 1073, 'dim_company', 0), ('fact_bs', 1074, 'dim_company', 0), ('fact_bs', 1075, 'dim_company', 0), ('fact_bs', 1076, 'dim_company', 0), ('fact_bs', 1077, 'dim_company', 0), ('fact_bs', 1078, 'dim_company', 0), ('fact_bs', 1079, 'dim_company', 0), ('fact_bs', 1080, 'dim_company', 0), ('fact_bs', 1081, 'dim_company', 0), ('fact_bs', 1082, 'dim_company', 0), ('fact_bs', 1083, 'dim_company', 0), ('fact_bs', 1084, 'dim_company', 0), ('fact_bs', 1085, 'dim_company', 0), ('fact_bs', 1086, 'dim_company', 0), ('fact_bs', 1087, 'dim_company', 0), ('fact_bs', 1088, 'dim_company', 0), ('fact_bs', 1089, 'dim_company', 0), ('fact_bs', 1090, 'dim_company', 0), ('fact_bs', 1091, 'dim_company', 0), ('fact_bs', 1092, 'dim_company', 0), ('fact_bs', 1093, 'dim_company', 0), ('fact_bs', 1119, 'dim_company', 0), ('fact_bs', 1120, 'dim_company', 0), ('fact_bs', 1121, 'dim_company', 0), ('fact_bs', 1122, 'dim_company', 0), ('fact_bs', 1123, 'dim_company', 0), ('fact_bs', 1124, 'dim_company', 0), ('fact_bs', 1125, 'dim_company', 0), ('fact_bs', 1126, 'dim_company', 0), ('fact_bs', 1127, 'dim_company', 0), ('fact_bs', 1128, 'dim_company', 0), ('fact_bs', 1129, 'dim_company', 0), ('fact_bs', 1130, 'dim_company', 0), ('fact_bs', 1131, 'dim_company', 0), ('fact_bs', 1132, 'dim_company', 0), ('fact_bs', 1133, 'dim_company', 0), ('fact_bs', 1134, 'dim_company', 0), ('fact_bs', 1135, 'dim_company', 0), ('fact_bs', 1136, 'dim_company', 0), ('fact_bs', 1137, 'dim_company', 0), ('fact_bs', 1138, 'dim_company', 0), ('fact_bs', 1139, 'dim_company', 0), ('fact_bs', 1140, 'dim_company', 0), ('fact_bs', 1141, 'dim_company', 0), ('fact_bs', 1142, 'dim_company', 0), ('fact_bs', 1143, 'dim_company', 0), ('fact_bs', 1157, 'dim_company', 0), ('fact_bs', 1158, 'dim_company', 0), ('fact_bs', 1159, 'dim_company', 0), ('fact_bs', 1160, 'dim_company', 0), ('fact_bs', 1161, 'dim_company', 0), ('fact_bs', 1162, 'dim_company', 0), ('fact_bs', 1163, 'dim_company', 0), ('fact_bs', 1164, 'dim_company', 0), ('fact_bs', 1165, 'dim_company', 0), ('fact_bs', 1166, 'dim_company', 0), ('fact_bs', 1167, 'dim_company', 0), ('fact_bs', 1168, 'dim_company', 0), ('fact_bs', 1169, 'dim_company', 0), ('fact_bs', 2346, 'dim_company', 0), ('fact_bs', 2347, 'dim_company', 0), ('fact_bs', 2348, 'dim_company', 0), ('fact_bs', 2349, 'dim_company', 0), ('fact_bs', 2350, 'dim_company', 0), ('fact_bs', 2351, 'dim_company', 0), ('fact_bs', 2352, 'dim_company', 0), ('fact_bs', 2353, 'dim_company', 0), ('fact_bs', 2354, 'dim_company', 0), ('fact_bs', 2355, 'dim_company', 0), ('fact_bs', 2356, 'dim_company', 0), ('fact_bs', 2357, 'dim_company', 0), ('fact_bs', 2358, 'dim_company', 0), ('fact_bs', 2372, 'dim_company', 0), ('fact_bs', 2373, 'dim_company', 0), ('fact_bs', 2374, 'dim_company', 0), ('fact_bs', 2375, 'dim_company', 0), ('fact_bs', 2376, 'dim_company', 0), ('fact_bs', 2377, 'dim_company', 0), ('fact_bs', 2378, 'dim_company', 0), ('fact_bs', 2379, 'dim_company', 0), ('fact_bs', 2380, 'dim_company', 0), ('fact_bs', 2381, 'dim_company', 0), ('fact_bs', 2382, 'dim_company', 0), ('fact_bs', 2383, 'dim_company', 0), ('fact_bs', 2384, 'dim_company', 0), ('fact_bs', 2385, 'dim_company', 0), ('fact_bs', 2386, 'dim_company', 0), ('fact_bs', 2387, 'dim_company', 0), ('fact_bs', 2388, 'dim_company', 0), ('fact_bs', 2389, 'dim_company', 0), ('fact_bs', 2390, 'dim_company', 0), ('fact_bs', 2391, 'dim_company', 0), ('fact_bs', 2392, 'dim_company', 0), ('fact_bs', 2393, 'dim_company', 0), ('fact_bs', 2394, 'dim_company', 0), ('fact_bs', 2395, 'dim_company', 0), ('fact_bs', 2396, 'dim_company', 0), ('fact_bs', 2397, 'dim_company', 0), ('fact_bs', 2398, 'dim_company', 0), ('fact_bs', 2399, 'dim_company', 0), ('fact_bs', 2400, 'dim_company', 0), ('fact_bs', 2401, 'dim_company', 0), ('fact_bs', 2402, 'dim_company', 0), ('fact_bs', 2403, 'dim_company', 0), ('fact_bs', 2404, 'dim_company', 0), ('fact_bs', 2405, 'dim_company', 0), ('fact_bs', 2431, 'dim_company', 0), ('fact_bs', 2432, 'dim_company', 0), ('fact_bs', 2433, 'dim_company', 0), ('fact_bs', 2434, 'dim_company', 0), ('fact_bs', 2435, 'dim_company', 0), ('fact_bs', 2436, 'dim_company', 0), ('fact_bs', 2437, 'dim_company', 0), ('fact_bs', 2438, 'dim_company', 0), ('fact_bs', 2439, 'dim_company', 0), ('fact_bs', 2440, 'dim_company', 0), ('fact_bs', 2441, 'dim_company', 0), ('fact_bs', 2442, 'dim_company', 0), ('fact_bs', 2443, 'dim_company', 0), ('fact_bs', 2444, 'dim_company', 0), ('fact_bs', 2445, 'dim_company', 0), ('fact_bs', 2446, 'dim_company', 0), ('fact_bs', 2447, 'dim_company', 0), ('fact_bs', 2448, 'dim_company', 0), ('fact_bs', 2449, 'dim_company', 0), ('fact_bs', 2450, 'dim_company', 0), ('fact_bs', 2451, 'dim_company', 0), ('fact_bs', 2452, 'dim_company', 0), ('fact_bs', 2453, 'dim_company', 0), ('fact_bs', 2454, 'dim_company', 0), ('fact_bs', 2455, 'dim_company', 0), ('fact_bs', 2469, 'dim_company', 0), ('fact_bs', 2470, 'dim_company', 0), ('fact_bs', 2471, 'dim_company', 0), ('fact_bs', 2472, 'dim_company', 0), ('fact_bs', 2473, 'dim_company', 0), ('fact_bs', 2474, 'dim_company', 0), ('fact_bs', 2475, 'dim_company', 0), ('fact_bs', 2476, 'dim_company', 0), ('fact_bs', 2477, 'dim_company', 0), ('fact_bs', 2478, 'dim_company', 0), ('fact_bs', 2479, 'dim_company', 0), ('fact_bs', 2480, 'dim_company', 0), ('fact_bs', 2481, 'dim_company', 0), ('fact_pl', 1165, 'dim_company', 0), ('fact_pl', 1166, 'dim_company', 0), ('fact_pl', 1167, 'dim_company', 0), ('fact_pl', 1168, 'dim_company', 0), ('fact_pl', 1169, 'dim_company', 0), ('fact_pl', 1170, 'dim_company', 0), ('fact_pl', 1171, 'dim_company', 0), ('fact_pl', 1172, 'dim_company', 0), ('fact_pl', 1173, 'dim_company', 0), ('fact_pl', 1174, 'dim_company', 0), ('fact_pl', 1175, 'dim_company', 0), ('fact_pl', 1176, 'dim_company', 0), ('fact_pl', 1177, 'dim_company', 0), ('fact_pl', 1178, 'dim_company', 0), ('fact_pl', 1179, 'dim_company', 0), ('fact_pl', 1180, 'dim_company', 0), ('fact_pl', 1181, 'dim_company', 0), ('fact_pl', 1182, 'dim_company', 0), ('fact_pl', 1183, 'dim_company', 0), ('fact_pl', 1184, 'dim_company', 0), ('fact_pl', 1185, 'dim_company', 0), ('fact_pl', 1186, 'dim_company', 0), ('fact_pl', 1187, 'dim_company', 0), ('fact_pl', 1188, 'dim_company', 0), ('fact_pl', 1189, 'dim_company', 0), ('fact_pl', 1190, 'dim_company', 0), ('fact_pl', 1191, 'dim_company', 0), ('fact_pl', 1192, 'dim_company', 0), ('fact_pl', 1193, 'dim_company', 0), ('fact_pl', 1194, 'dim_company', 0), ('fact_pl', 1195, 'dim_company', 0), ('fact_pl', 1196, 'dim_company', 0), ('fact_pl', 1197, 'dim_company', 0), ('fact_pl', 1198, 'dim_company', 0), ('fact_pl', 1199, 'dim_company', 0), ('fact_pl', 1200, 'dim_company', 0), ('fact_pl', 1201, 'dim_company', 0), ('fact_pl', 1202, 'dim_company', 0), ('fact_pl', 1203, 'dim_company', 0), ('fact_pl', 1204, 'dim_company', 0), ('fact_pl', 1205, 'dim_company', 0), ('fact_pl', 1206, 'dim_company', 0), ('fact_pl', 1207, 'dim_company', 0), ('fact_pl', 1208, 'dim_company', 0), ('fact_pl', 1209, 'dim_company', 0), ('fact_pl', 1210, 'dim_company', 0), ('fact_pl', 1211, 'dim_company', 0), ('fact_pl', 1212, 'dim_company', 0), ('fact_pl', 1213, 'dim_company', 0), ('fact_pl', 1214, 'dim_company', 0), ('fact_pl', 1215, 'dim_company', 0), ('fact_pl', 1216, 'dim_company', 0), ('fact_pl', 1217, 'dim_company', 0), ('fact_pl', 1218, 'dim_company', 0), ('fact_pl', 1219, 'dim_company', 0), ('fact_pl', 1220, 'dim_company', 0), ('fact_pl', 1221, 'dim_company', 0), ('fact_pl', 1222, 'dim_company', 0), ('fact_pl', 1223, 'dim_company', 0), ('fact_pl', 1224, 'dim_company', 0), ('fact_pl', 1225, 'dim_company', 0), ('fact_pl', 1226, 'dim_company', 0), ('fact_pl', 1227, 'dim_company', 0), ('fact_pl', 1228, 'dim_company', 0), ('fact_pl', 1229, 'dim_company', 0), ('fact_pl', 1230, 'dim_company', 0), ('fact_pl', 1231, 'dim_company', 0), ('fact_pl', 1232, 'dim_company', 0), ('fact_pl', 1233, 'dim_company', 0), ('fact_pl', 1234, 'dim_company', 0), ('fact_pl', 1235, 'dim_company', 0), ('fact_pl', 1236, 'dim_company', 0), ('fact_pl', 1237, 'dim_company', 0), ('fact_pl', 1238, 'dim_company', 0), ('fact_pl', 1239, 'dim_company', 0), ('fact_pl', 1240, 'dim_company', 0), ('fact_pl', 1241, 'dim_company', 0), ('fact_pl', 1242, 'dim_company', 0), ('fact_pl', 1243, 'dim_company', 0), ('fact_pl', 1244, 'dim_company', 0), ('fact_pl', 1245, 'dim_company', 0), ('fact_pl', 1246, 'dim_company', 0), ('fact_pl', 1247, 'dim_company', 0), ('fact_pl', 1248, 'dim_company', 0), ('fact_pl', 1249, 'dim_company', 0), ('fact_pl', 1250, 'dim_company', 0), ('fact_pl', 1251, 'dim_company', 0), ('fact_pl', 1252, 'dim_company', 0), ('fact_pl', 1253, 'dim_company', 0), ('fact_pl', 1254, 'dim_company', 0), ('fact_pl', 1255, 'dim_company', 0), ('fact_pl', 1256, 'dim_company', 0), ('fact_pl', 1257, 'dim_company', 0), ('fact_pl', 1258, 'dim_company', 0), ('fact_pl', 1259, 'dim_company', 0), ('fact_pl', 1260, 'dim_company', 0), ('fact_pl', 1261, 'dim_company', 0), ('fact_pl', 1262, 'dim_company', 0), ('fact_pl', 1263, 'dim_company', 0), ('fact_pl', 2441, 'dim_company', 0), ('fact_pl', 2442, 'dim_company', 0), ('fact_pl', 2443, 'dim_company', 0), ('fact_pl', 2444, 'dim_company', 0), ('fact_pl', 2445, 'dim_company', 0), ('fact_pl', 2446, 'dim_company', 0), ('fact_pl', 2447, 'dim_company', 0), ('fact_pl', 2448, 'dim_company', 0), ('fact_pl', 2449, 'dim_company', 0), ('fact_pl', 2450, 'dim_company', 0), ('fact_pl', 2451, 'dim_company', 0), ('fact_pl', 2452, 'dim_company', 0), ('fact_pl', 2453, 'dim_company', 0), ('fact_pl', 2454, 'dim_company', 0), ('fact_pl', 2455, 'dim_company', 0), ('fact_pl', 2456, 'dim_company', 0), ('fact_pl', 2457, 'dim_company', 0), ('fact_pl', 2458, 'dim_company', 0), ('fact_pl', 2459, 'dim_company', 0), ('fact_pl', 2460, 'dim_company', 0), ('fact_pl', 2461, 'dim_company', 0), ('fact_pl', 2462, 'dim_company', 0), ('fact_pl', 2463, 'dim_company', 0), ('fact_pl', 2464, 'dim_company', 0), ('fact_pl', 2465, 'dim_company', 0), ('fact_pl', 2466, 'dim_company', 0), ('fact_pl', 2467, 'dim_company', 0), ('fact_pl', 2468, 'dim_company', 0), ('fact_pl', 2469, 'dim_company', 0), ('fact_pl', 2470, 'dim_company', 0), ('fact_pl', 2471, 'dim_company', 0), ('fact_pl', 2472, 'dim_company', 0), ('fact_pl', 2473, 'dim_company', 0), ('fact_pl', 2474, 'dim_company', 0), ('fact_pl', 2475, 'dim_company', 0), ('fact_pl', 2476, 'dim_company', 0), ('fact_pl', 2477, 'dim_company', 0), ('fact_pl', 2478, 'dim_company', 0), ('fact_pl', 2479, 'dim_company', 0), ('fact_pl', 2480, 'dim_company', 0), ('fact_pl', 2481, 'dim_company', 0), ('fact_pl', 2482, 'dim_company', 0), ('fact_pl', 2483, 'dim_company', 0), ('fact_pl', 2484, 'dim_company', 0), ('fact_pl', 2485, 'dim_company', 0), ('fact_pl', 2486, 'dim_company', 0), ('fact_pl', 2487, 'dim_company', 0), ('fact_pl', 2488, 'dim_company', 0), ('fact_pl', 2489, 'dim_company', 0), ('fact_pl', 2490, 'dim_company', 0), ('fact_pl', 2491, 'dim_company', 0), ('fact_pl', 2492, 'dim_company', 0), ('fact_pl', 2493, 'dim_company', 0), ('fact_pl', 2494, 'dim_company', 0), ('fact_pl', 2495, 'dim_company', 0), ('fact_pl', 2496, 'dim_company', 0), ('fact_pl', 2497, 'dim_company', 0), ('fact_pl', 2498, 'dim_company', 0), ('fact_pl', 2499, 'dim_company', 0), ('fact_pl', 2500, 'dim_company', 0), ('fact_pl', 2501, 'dim_company', 0), ('fact_pl', 2502, 'dim_company', 0), ('fact_pl', 2503, 'dim_company', 0), ('fact_pl', 2504, 'dim_company', 0), ('fact_pl', 2505, 'dim_company', 0), ('fact_pl', 2506, 'dim_company', 0), ('fact_pl', 2507, 'dim_company', 0), ('fact_pl', 2508, 'dim_company', 0), ('fact_pl', 2509, 'dim_company', 0), ('fact_pl', 2510, 'dim_company', 0), ('fact_pl', 2511, 'dim_company', 0), ('fact_pl', 2512, 'dim_company', 0), ('fact_pl', 2513, 'dim_company', 0), ('fact_pl', 2514, 'dim_company', 0), ('fact_pl', 2515, 'dim_company', 0), ('fact_pl', 2516, 'dim_company', 0), ('fact_pl', 2517, 'dim_company', 0), ('fact_pl', 2518, 'dim_company', 0), ('fact_pl', 2519, 'dim_company', 0), ('fact_pl', 2520, 'dim_company', 0), ('fact_pl', 2521, 'dim_company', 0), ('fact_pl', 2522, 'dim_company', 0), ('fact_pl', 2523, 'dim_company', 0), ('fact_pl', 2524, 'dim_company', 0), ('fact_pl', 2525, 'dim_company', 0), ('fact_pl', 2526, 'dim_company', 0), ('fact_pl', 2527, 'dim_company', 0), ('fact_pl', 2528, 'dim_company', 0), ('fact_pl', 2529, 'dim_company', 0), ('fact_pl', 2530, 'dim_company', 0), ('fact_pl', 2531, 'dim_company', 0), ('fact_pl', 2532, 'dim_company', 0), ('fact_pl', 2533, 'dim_company', 0), ('fact_pl', 2534, 'dim_company', 0), ('fact_pl', 2535, 'dim_company', 0), ('fact_pl', 2536, 'dim_company', 0), ('fact_pl', 2537, 'dim_company', 0), ('fact_pl', 2538, 'dim_company', 0), ('fact_pl', 2539, 'dim_company', 0)]
    


```python
def log_audit(table_name, file_name, rows_loaded):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO load_audit (table_name, file_name, rows_loaded)
        VALUES (?, ?, ?)
    """, (table_name, file_name, rows_loaded))
    conn.commit()

```


```python
df.to_sql(table_name, conn, if_exists="append", index=False)
log_audit(table_name, file_path.split("\\")[-1], len(df))
print(f"Loaded {len(df)} rows into {table_name}")

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[89], line 1
    ----> 1 df.to_sql(table_name, conn, if_exists="append", index=False)
          2 log_audit(table_name, file_path.split("\\")[-1], len(df))
          3 print(f"Loaded {len(df)} rows into {table_name}")
    

    NameError: name 'table_name' is not defined



```python
import pandas as pd
import sqlite3

db_path = r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# --- Drop and recreate audit + fact tables ---
cur.execute("DROP TABLE IF EXISTS load_audit;")
cur.execute("""
CREATE TABLE load_audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    file_name TEXT NOT NULL,
    rows_loaded INTEGER,
    load_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

cur.execute("DROP TABLE IF EXISTS fact_pl;")
cur.execute("""
CREATE TABLE fact_pl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year TEXT NOT NULL,
    revenue REAL,
    expenses REAL,
    profit REAL
);
""")

cur.execute("DROP TABLE IF EXISTS fact_bs;")
cur.execute("""
CREATE TABLE fact_bs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year TEXT NOT NULL,
    assets REAL,
    liabilities REAL,
    equity REAL
);
""")

cur.execute("DROP TABLE IF EXISTS fact_cf;")
cur.execute("""
CREATE TABLE fact_cf (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    year TEXT NOT NULL,
    operating_cf REAL,
    investing_cf REAL,
    financing_cf REAL
);
""")

conn.commit()

# --- Audit logger ---
def log_audit(table_name, file_name, rows_loaded):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO load_audit (table_name, file_name, rows_loaded)
        VALUES (?, ?, ?)
    """, (table_name, file_name, rows_loaded))
    conn.commit()

# --- Loader function ---
def clean_and_load(file_path, table_name, rename_map, keep_cols, skiprows=1):
    df = pd.read_csv(file_path, skiprows=skiprows)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.rename(columns=rename_map)
    df = df[keep_cols]
    df.to_sql(table_name, conn, if_exists="append", index=False)
    log_audit(table_name, file_path.split("\\")[-1], len(df))
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Profit & Loss ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv",
    "fact_pl",
    rename_map={"company_id": "ticker","sales": "revenue","net_profit": "profit"},
    keep_cols=["ticker","year","revenue","expenses","profit"]
)

# --- Balance Sheet ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv",
    "fact_bs",
    rename_map={"company_id": "ticker","total_assets": "assets","total_liabilities": "liabilities","reserves": "equity"},
    keep_cols=["ticker","year","assets","liabilities","equity"]
)

# --- Cash Flow ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_cf.csv",
    "fact_cf",
    rename_map={"company_id": "ticker","operating_activity": "operating_cf","investing_activity": "investing_cf","financing_activity": "financing_cf"},
    keep_cols=["ticker","year","operating_cf","investing_cf","financing_cf"]
)

# --- Audit check ---
cur.execute("SELECT * FROM load_audit;")
for row in cur.fetchall():
    print(row)

conn.close()

```

    Loaded 1276 rows into fact_pl
    Loaded 1312 rows into fact_bs
    Loaded 1187 rows into fact_cf
    (1, 'fact_pl', 'fact_pl.csv', 1276, '2026-08-20 16:49:13')
    (2, 'fact_bs', 'fact_bs.csv', 1312, '2026-08-20 16:49:13')
    (3, 'fact_cf', 'fact_cf.csv', 1187, '2026-08-20 16:49:13')
    


```python
cur = conn.cursor()
cur.execute("""
SELECT table_name, file_name, rows_loaded, MAX(load_timestamp) AS last_loaded
FROM load_audit
GROUP BY table_name;
""")
for row in cur.fetchall():
    print(row)

```


    ---------------------------------------------------------------------------

    ProgrammingError                          Traceback (most recent call last)

    Cell In[91], line 1
    ----> 1 cur = conn.cursor()
          2 cur.execute("""
          3 SELECT table_name, file_name, rows_loaded, MAX(load_timestamp) AS last_loaded
          4 FROM load_audit
    

    ProgrammingError: Cannot operate on a closed database.



```python
import sqlite3

db_path = r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
SELECT table_name, file_name, rows_loaded, MAX(load_timestamp) AS last_loaded
FROM load_audit
GROUP BY table_name;
""")

rows = cur.fetchall()
for row in rows:
    print(f"Table: {row[0]} | File: {row[1]} | Rows: {row[2]} | Last Loaded: {row[3]}")

conn.close()

```

    Table: fact_bs | File: fact_bs.csv | Rows: 1312 | Last Loaded: 2026-08-20 16:49:13
    Table: fact_cf | File: fact_cf.csv | Rows: 1187 | Last Loaded: 2026-08-20 16:49:13
    Table: fact_pl | File: fact_pl.csv | Rows: 1276 | Last Loaded: 2026-08-20 16:49:13
    


```python

```
