from urllib.parse import urlparse

def is_url(url):
    """
    Verifica si una cadena tiene formato de url
        Comprueba que el esquema y el netloc no estén vacíos
        Esquema: protocolo de comunicación (p.e.: http, https, ftp, mailto, etc
        Netloc: identifica la ubicación de red (nombre de dominio o dirección IP del servidor
    :param url: la cadena a verificar
    :return: True o False
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False