
import pandas as pd

def guardar_usuario(nombre, email, rol):
    nuevo = pd.DataFrame([[nombre, email, rol]], columns=["Nombre", "Email", "Rol"])
    try:
        df = pd.read_csv("data/users.csv")
        df = pd.concat([df, nuevo], ignore_index=True)
    except:
        df = nuevo
    df.to_csv("data/users.csv", index=False)
