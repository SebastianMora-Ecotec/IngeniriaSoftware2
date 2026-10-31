from notificaciones.factory import NotificacionFactory

def ejecutar_demo():
    canales = ["email", "sms", "push", "telegram"]
    mensaje = "Tu pedido #1042 ha sido procesado con exito."
    usuario = "K.hernandez@est.ecotec.edu.ec"

    print("--- Demostracion del Patron Factory ---")
    for canal in canales:
        notificador = NotificacionFactory.crear_notificacion(canal)
        notificador.enviar(mensaje, usuario)

    try:
        NotificacionFactory.crear_notificacion("fax")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar_demo()