from fastapi import APIRouter, HTTPException
from fastapi import HTTPException, status

from app.db.client import supabase
from app.schemas.auth import CreateUser, LoginUser, ResendConfirmation
from app.core.utils import serialize

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def create_user(user_data: CreateUser):
    """
    Endpoint para registrar un nuevo usuario.

    **Parámetros:**
    - user_data: objeto de tipo CreateUser
        - email (str): correo electrónico. Debe ser un email válido.
        - password (str): contraseña del usuario.

    **Retorna:**
    - `200 OK`: JSON con mensaje de éxito y los datos serializados del usuario.
    Ejemplo:

    ```
      {
          "message": "Usuario registrado exitosamente!",
          "data": {
              "id": "uuid-del-usuario",
              "email": "correo@ejemplo.com"
              ...
          }
      }
      ```

    - `400 Bad Request`: si hubo un error al registrar el usuario.
    - `500 Internal Server Error`: si ocurre un error interno en el servidor.

    **Nota:**
    - La contraseña se recibe en texto plano y se delega la gestión segura a Supabase Auth.
    """
    try:
        response = supabase.auth.sign_up(
            {"email": user_data.email, "password": user_data.password}
        )

        user = response.user

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Hubo un error al registrar el usuario.",
            )

        user_serialized = serialize(user)

        return {"message": "User registered successfully!", "data": user_serialized}

    except Exception as e:
        print(f"[ERROR] Hubo un error al registrar el usuario: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor.",
        )


@router.post("/login")
async def signin_user(user_data: LoginUser):
    """
    Endpoint para iniciar sesión de un usuario existente.

    **Parámetros:**
    - user_data: objeto de tipo LoginUser
        - email (str): correo electrónico del usuario. Debe ser un email válido.
        - password (str): contraseña del usuario.

        **Retorna:**
        - `200 OK`: JSON con mensaje de éxito y datos serializados del usuario y la sesión.
        Ejemplo:

        ```
        {
            "message": "Successfully signed in!",
            "data": {
                "user": {
                    "id": "uuid-del-usuario",
                    "email": "correo@ejemplo.com",
                    "email_confirmed_at": "2025-09-27T21:32:56.600687+00:00",
                    "role": "authenticated",
                    ...
                },
                "session: {
                    "access_token": "jwt-access-token",
                    "refresh_token": "refresh-token",
                    "expires_in": 3600,
                    ...
                }
            }
        }
        ```

    **Notas:**
    - La contraseña se recibe en texto plano y la autenticación se gestiona de forma segura a través de Supabase Auth.
    - El campo `data` incluye tanto el objeto `user` como el objeto `session` con los tokens de acceso y refresco.
    """
    try:
        response = supabase.auth.sign_in_with_password(
            {"email": user_data.email, "password": user_data.password}
        )

        response_serialized = serialize(response)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return {"message": "Successfully signed in!", "data": response_serialized}


@router.post("/resend-confirmation")
async def resend_confirmation(resend_data: ResendConfirmation):
    """
    Endpoint para reenviar un mensaje de confirmación al usuario.

    **Parámetros:**
    - `resend_data`: objeto de tipo ResendConfirmation.
        - type (str): tipo de confirmación a reenviar. Puede ser uno de:
            - `"signup"`: confirmación de registro por email.
            - `"email_change"`: confirmación de cambio de email.
            - `"phone_change"`: confirmación de cambio de teléfono.
            - `"sms"`: confirmación de registro por SMS.
        - email (str, opcional): correo electrónico del usuario. Requerido si el `type` es `"signup"` o `"email_change"`.
        - phone (str, opcional): número de teléfono del usuario. Requerido si el `type` es `"sms"` o `"phone_change"`.
        - options (dict, opcional): opciones adicionales, por ejemplo `{"email_redirect_to": "https://example.com/welcome"}` para redirigir al usuario tras la confirmación.

    **Retorna:**
    - `200 OK`: JSON con mensaje de éxito.
    Ejemplo:
    ```
    {
        "message": "¡Mensaje de confirmación reenviado correctamente!"
    }
    ```

    - `400 Bad Request`: si ocurre un error al intentar reenviar la confirmación.
    - `422 Unprocessable Entity`: si faltan campos obligatorios (`email` o `phone`) según el tipo de confirmación.

    **Notas:**
    - La validación principal de errores la gestiona Supabase. Este endpoint se encarga de construir el payload correcto y delegar el envío al servicio de Supabase.
    - El mensaje de éxito solo indica que la solicitud fue aceptada; Supabase enviará la confirmación al email o teléfono correspondiente.
    """
    try:
        payload = {"type": resend_data.type}

        if resend_data.type in ["signup", "email_change"]:
            if not resend_data.email:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="The 'email' fiel is required for this type of confirmation",
                )
            payload["email"] = resend_data.email

            if resend_data.type == "signup" and resend_data.options:
                payload["options"] = resend_data.options

        elif resend_data.type in ["sms", "phone_change"]:
            if not resend_data.phone:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="The 'phone' field is required for this type of confirmation",
                )
            payload["phone"] = resend_data.phone

        supabase.auth.resend(payload)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    return {"message": "Confirmation message resent successfully!"}
