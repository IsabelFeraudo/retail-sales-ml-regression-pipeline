from pathlib import Path
import pandas as pd

try:
    BASE_DIR = Path(__file__).resolve().parent.parent
except NameError:
    BASE_DIR = Path().resolve()

DATA_DIR = BASE_DIR / "data"

def _read_excel_safe(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_excel(path)

def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def _resolve_price_column(df: pd.DataFrame) -> pd.DataFrame:
    if "precio_unitario" in df.columns:
        return df

    if "precio_unitario_x" in df.columns:
        df["precio_unitario"] = df["precio_unitario_x"]
    elif "precio_unitario_y" in df.columns:
        df["precio_unitario"] = df["precio_unitario_y"]
    else:
        raise ValueError(
            f"No price column found. Available columns: {df.columns.tolist()}"
        )

    df.drop(columns=["precio_unitario_x", "precio_unitario_y"], errors="ignore", inplace=True)
    return df

def load_data() -> pd.DataFrame:
    clientes = _normalize_columns(_read_excel_safe(DATA_DIR / "clientes.xlsx"))
    productos = _normalize_columns(_read_excel_safe(DATA_DIR / "productos.xlsx"))
    ventas = _normalize_columns(_read_excel_safe(DATA_DIR / "ventas.xlsx"))
    detalle = _normalize_columns(_read_excel_safe(DATA_DIR / "detalle_ventas.xlsx"))

    df = (
        detalle.merge(productos, on="id_producto", how="left")
        .merge(ventas, on="id_venta", how="left")
        .merge(clientes, on="id_cliente", how="left")
    )

    print("COLUMNAS DEL DATAFRAME:")
    print(df.columns.tolist())

    df = _resolve_price_column(df)

    df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce")
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")

    df["importe"] = df["cantidad"] * df["precio_unitario"]

    required = ["cantidad", "precio_unitario", "importe", "categoria"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.dropna(subset=required)

    return df
