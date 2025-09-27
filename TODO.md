# TO-DO: Endpoints de Zentora Backend

## 1. Auth (Autenticación)

Endpoints relacionados con la autenticación de usuarios y recuperación de acceso.

- [✅] **POST /auth/register**  
  Crear un nuevo usuario con email y contraseña.

- [ ] **POST /auth/resend-verification**  
  Reenviar correo de verificación de cuenta.

- [ ] **POST /auth/login**  
  Iniciar sesión con email y contraseña.

- [ ] **POST /auth/logout**  
  Cerrar sesión del usuario actual.

- [ ] **POST /auth/forgot-password**  
  Iniciar proceso de recuperación de contraseña (envío de link de restablecimiento).

- [ ] **POST /auth/social-login/{provider}**  
  Iniciar sesión mediante proveedor social (ej. GitHub, Google, etc.).

---

## 2. Profile (Perfil de usuario)

Endpoints relacionados con la gestión del perfil y seguridad de la cuenta del usuario autenticado.

- [ ] **GET /profile/me**  
  Obtener información de la sesión y datos del usuario actual.

- [ ] **POST /profile/reset-password**  
  Restablecer la contraseña mediante un link recibido por correo (solo usuarios con email/contraseña).

- [ ] **PATCH /profile/change-password**  
  Cambiar contraseña desde la sesión activa.

- [ ] **DELETE /profile/delete-account**  
  Eliminar la cuenta del usuario.

- [ ] **POST /profile/revoke-sessions**  
  Revocar todas las sesiones activas del usuario.

- [ ] **POST /profile/reactivate-account**  
  Reactivar una cuenta previamente eliminada.

- [ ] **PATCH /profile/update**  
  Actualizar información del usuario (nombre, foto, preferencias, etc.).

---

## 3. Admin / Management

Endpoints exclusivos para administradores y gestión avanzada de usuarios. **No accesibles por usuarios normales ni de pago.**

- [ ] **GET /admin/users**  
  Listar todos los usuarios registrados.

- [ ] **GET /admin/users/{user_id}**  
  Obtener información detallada de un usuario específico.

- [ ] **PATCH /admin/users/{user_id}**  
  Actualizar información de un usuario (roles, estado, privilegios, etc.).

- [ ] **DELETE /admin/users/{user_id}**  
  Eliminar un usuario (borrado lógico o físico según estrategia).

- [ ] **POST /admin/users/{user_id}/revoke-sessions**  
  Revocar todas las sesiones activas de un usuario.

- [ ] **POST /admin/users/{user_id}/reactivate**  
  Reactivar un usuario eliminado.

- [ ] **GET /admin/sessions**  
  Listar todas las sesiones activas del sistema (audit/monitoring).

- [ ] **DELETE /admin/sessions/{session_id}**  
  Revocar sesión específica (para incidentes de seguridad o auditoría).

---

## Notas generales

- Todos los endpoints de **Auth** deben interactuar con **Supabase Auth** para la creación, login, logout y recuperación de usuarios.  
- Endpoints de **Profile** deben verificar la sesión activa antes de permitir cualquier acción.  
- Endpoints de **Admin** deben usar roles o claims de Supabase para garantizar que solo el equipo tenga acceso.  
- Usar **serialización de usuarios** (`serialize_user`) para respuestas consistentes en todos los endpoints.
