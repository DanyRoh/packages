import pandas as pd

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
    Identifica los valores NA del dataframe y facilita un diccionario con los índices por cada variable
    :param df: dataframe de la librería Pandas
    :return: Devuelve un diccionario con las variables como claves y una lista con los registros agrupaodos
    """
    na_values = {}
    for col in df.columns:
        na_registers = df.index[df[col].isna()].tolist()
        if na_registers:
            na_values[col] = na_registers

    if not na_values:
        print('No hay valores NA')
    else:
        print('Recuento de registros NA por cada variable:\n')
        display(pd.DataFrame({'Variable': df.columns.to_list(),
                      'NA totales': df.isna().sum(),
                      '% del total': df.isna().sum()/len(df)}).set_index('Variable'))

        print('Detalle de las variables que contienen valores NA e índices donde se encuentran en el dataframe\n')
        display(na_values)

