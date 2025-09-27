from fastapi import APIRouter, HTTPException

from app.db.client import supabase
from app.schemas.auth import CreateUser
from app.core.utils import serialize_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def create_user(user_data: CreateUser):
    """
    Endpoint para registrar un nuevo usuario.
    """
    try:
        result = supabase.auth.sign_up(
            {"email": user_data.email, "password": user_data.password}
        )

        user = result.user

        if not user:
            raise HTTPException(
                status_code=400, detail="Hubo un error al registrar el usuario."
            )

        user_serialized = serialize_user(user)

        return {"message": "Usuario registrado exitosamente!", "data": user_serialized}

    except Exception as e:
        print(f"[ERROR] Hubo un error al registrar el usuario: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")
