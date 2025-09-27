from datetime import datetime


def serialize(obj):
    """
    args: `obj` (object): Objeto a serializar.

    Convierte un objeto en un diccionario serializable a JSON:
    - Transforma datetime a strings ISO.
    - Convierte listas de objetos en listas de diccionarios.
    - Maneja objetos anidados recursivamente.

    ### Ejemplo:
    ```python
    user_dict = serialize(user)
    print(user_dict)
    ```
    """
    if isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [serialize(item) for item in obj]
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif hasattr(obj, "__dict__"):
        return serialize(obj.__dict__)
    else:
        return obj
