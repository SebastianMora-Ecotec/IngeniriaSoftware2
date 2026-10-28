from notificaciones.servicios import NotificacionEmail, NotificacionSMS, NotificacionPush

class NotificacionFactory:
    @staticmethod
    def crear_notificacion(tipo: str):
        tipo = tipo.lower()
        if tipo == "email":
            return NotificacionEmail()
        elif tipo == "sms":
            return NotificacionSMS()
        elif tipo == "push":
            return NotificacionPush()
        else:
            raise ValueError(f"Canal de notificacion desconocido: {tipo}")