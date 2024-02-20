
def describe_df(df):
    """
    Facilita la informació necesario para conocer el contenido del dataframe
    :param df: dataframe de la librería Pandas
    :return: imprime diferentes descripciones del dataframe
    """
    print(f'El dataframe tiene {df.shape[0]} filas y {df.shape[1]} columnas.')
    print(df.describe())
    print(df.head())
    print(df.tail())
