
def describe_df(df):
    """
    Facilita la informació necesario para conocer el contenido del dataframe
    :param df: dataframe de la librería Pandas
    :return: imprime diferentes descripciones del dataframe
    """

    print(f'El dataframe tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n\n')

    print(f'Datos estadísticos:\n\n')
    display(df.describe(include="all"))
    print('\n\n')

    print(f'Primeros 5 registros:\n\n')
    display(df.head())
    print('\n\n')

    print(f'Últimos 5 registros:\n\n')
    display(df.tail())
    print('\n\n')


def identify_na_values(df):
    """
    Identifica los valores susceptibles de ser tratados para mejorar la calidad del dataframe antes del análisis
    :param df: dataframe de la librería Pandas
    :return: Devuelve un diccionario con las variables como claves y una lista con los registros agrupaods
        en base a la incidencia detectada en el dataframe
    """
    print('Recuento de registros NA por cada variable:\n\n')
    display(df.isna().sum())

    na_values = {}

    for col in df.columns:
        na_registers = df[df[col].isna()]
        na_values[col] = na_registers

    return na_values
