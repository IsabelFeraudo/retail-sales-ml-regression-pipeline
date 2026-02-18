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


def load_data() -> pd.DataFrame:
    clientes = _read_excel_safe(DATA_DIR / "clientes.xlsx")
    productos = _read_excel_safe(DATA_DIR / "productos.xlsx")
    ventas = _read_excel_safe(DATA_DIR / "ventas.xlsx")
    detalle = _read_excel_safe(DATA_DIR / "detalle_ventas.xlsx")

    df = (
        detalle.merge(productos, on="id_producto", how="left")
        .merge(ventas, on="id_venta", how="left")
        .merge(clientes, on="id_cliente", how="left")
    )

    # Conversion
    df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce")
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")

    # Feature engineering
    df["importe"] = df["cantidad"] * df["precio_unitario"]

    # Cleaning
    df = df.dropna(subset=["cantidad", "precio_unitario", "importe", "categoria"])

    return df
