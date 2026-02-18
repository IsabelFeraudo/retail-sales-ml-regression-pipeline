import pandas as pd

def load_data():
    clientes = pd.read_excel("data/clientes.xlsx")
    productos = pd.read_excel("data/productos.xlsx")
    ventas = pd.read_excel("data/ventas.xlsx")
    detalle = pd.read_excel("data/detalle_ventas.xlsx")

    df = (
        detalle.merge(productos, on="id_producto", how="left")
        .merge(ventas, on="id_venta", how="left")
        .merge(clientes, on="id_cliente", how="left")
    )

    df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce")
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
    df["importe"] = df["cantidad"] * df["precio_unitario"]

    df = df.dropna(subset=["cantidad", "precio_unitario", "importe", "categoria"])

    return df
