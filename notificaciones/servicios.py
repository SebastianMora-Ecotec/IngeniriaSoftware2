class NotificacionEmail:
    def enviar(self, mensaje: str, usuario: str):
        print(f"[EMAIL] Enviando correo a {usuario}: {mensaje}")

class NotificacionSMS:
    def enviar(self, mensaje: str, usuario: str):
        print(f"[SMS] Enviando mensaje de texto a {usuario}: {mensaje}")

class NotificacionPush:
    def enviar(self, mensaje: str, usuario: str):
        print(f"[PUSH] Enviando notificacion push a {usuario}: {mensaje}")