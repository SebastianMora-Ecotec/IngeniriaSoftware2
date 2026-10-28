from notificaciones.factory import NotificacionFactory

def ejecutar_demo():
    canales = ["email", "sms", "push"]
    mensaje = "Tu pedido #1042 ha sido procesado con exito."
    usuario = "l.arrieta@est.ecotec.edu.ec"

    print("--- Demostracion del Patron Factory ---")
    for canal in canales:
        notificador = NotificacionFactory.crear_notificacion(canal)
        notificador.enviar(mensaje, usuario)

if __name__ == "__main__":
    ejecutar_demo()