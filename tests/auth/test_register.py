from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app


def test_register_success():
    """
    Este test verifica que el endpoint /api/v1/auth/register funcione correctamente cuando el registro es exitoso, simulando la respuesta de Supabase y comprobando que la API responde como se espera, sin depender de servicios externos.
    """
    test_email = "testuser@example.com"
    test_password = "testpassword123"

    mock_user = MagicMock()
    mock_user.email = test_email
    mock_result = MagicMock()
    mock_result.user = mock_user

    with patch(
        "app.api.v1.endpoints.auth.supabase.auth.sign_up", return_value=mock_result
    ):
        with TestClient(app) as client:
            response = client.post(
                "/api/v1/auth/register",
                json={"email": test_email, "password": test_password},
            )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["message"] == "Usuario registrado exitosamente!"
    assert data["data"]["email"] == test_email
