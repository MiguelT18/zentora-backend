from datetime import datetime


def serialize_user(user):
    """
    args: `user` (object): Objeto a serializar.

    Convierte un objeto en un diccionario serializable a JSON, transformando fechas a strings ISO y listas de objetos en listas de diccionarios.

    ### Ejemplo:
    ```python
    user_dict = serialize_user(user)
    print(user_dict)
    ```
    """
    user_dict = user.__dict__.copy()
    for k, v in list(user_dict.items()):
        if isinstance(v, datetime):
            user_dict[k] = v.isoformat()
        elif isinstance(v, list):
            user_dict[k] = [i.__dict__ for i in v]
    return user_dict
