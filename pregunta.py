"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv('solicitudes_credito.csv',sep=";",index_col=0,encoding="utf8")
    df.dropna(inplace=True)
    for j in df.columns[0:4]:
        df[j]=df[j].str.lower()
    df["línea_credito"]=df.línea_credito.str.lower()
    df['fecha_de_beneficio']=pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    df["monto_del_credito"]=[line.replace("$","") for line in df["monto_del_credito"]]
    df["monto_del_credito"]=[line.replace(",","") for line in df["monto_del_credito"]]
    df["monto_del_credito"]=[line.replace(".00","") for line in df["monto_del_credito"]]
    df["monto_del_credito"]=df["monto_del_credito"].astype("float")
    df["barrio"]=df["barrio"].astype("str")
    df["barrio"]=[line.replace(" ","_") for line in df["barrio"]]
    df["barrio"]=[line.replace("-","_") for line in df["barrio"]]
    df["barrio"]=[line.replace("_"," ") for line in df["barrio"]]
    df["idea_negocio"]=df["idea_negocio"].astype("str")
    df["idea_negocio"]=[line.replace(" ","_") for line in df["idea_negocio"]]
    df["idea_negocio"]=[line.replace("-","_") for line in df["idea_negocio"]]
    df["idea_negocio"]=[line.replace("_"," ") for line in df["idea_negocio"]]
    df["línea_credito"]=[line.replace(" ","_") for line in df["línea_credito"]]
    df["línea_credito"]=[line.replace("-","_") for line in df["línea_credito"]]
    df["línea_credito"]=[line.replace("_"," ") for line in df["línea_credito"]]
    df.drop_duplicates(inplace=True)

    return df
