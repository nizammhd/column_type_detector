import pandas as pd

def detect_column_types(df: pd.DataFrame, unique_threshold: int = 20) -> dict:
  
    col_types = {}
    
    for col in df.columns:
        series = df[col]
        dtype = series.dtype
        
        # If the column has numbers (int or float)
        if pd.api.types.is_numeric_dtype(dtype):
            # If only a few unique numbers -> treat as categories (like 0/1 or small set of codes)
            if series.nunique(dropna=True) <= unique_threshold:
                col_types[col] = "categorical"
            else:
                # Otherwise, it's a continuous number column
                col_types[col] = "numerical"
        
        # If the column has strings (text or words)
        elif pd.api.types.is_string_dtype(dtype):
            # Few unique values -> categories (like 'male', 'female')
            if series.nunique(dropna=True) <= unique_threshold:
                col_types[col] = "categorical"
            else:
                # Many unique values -> treat as free text
                col_types[col] = "text"
        
        # If the column has dates or times
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            col_types[col] = "datetime"
        
        # If none of the above, just assume it's a category
        else:
            col_types[col] = "categorical"
    
    return col_types
