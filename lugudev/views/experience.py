from datetime import date
import reflex as rx
import locale
from lugudev.components import title, experience_card, bullet

# Establecer el idioma en español
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")


def experience() -> rx.Component:

    short_month_name = date.today().strftime("%b")

    return rx.tablet_and_desktop(
        rx.vstack(
            title("Experiencia"),
            experience_card(
                "Klio Data",
                f"Feb 2024 - {short_month_name.capitalize()} {date.today().year}",
                "flex-start",
                bullet(
                    r"Desarrollé una plataforma de encuestas transformando un producto manual a 100% digital, mejorando la eficiencia operativa y ampliando el alcance a usuarios a nivel global."
                ),
                bullet(
                    "Implementé Docker para crear entornos de desarrollo consistentes y desplegables, facilitando la escalabilidad y el mantenimiento del software."
                ),
                bullet(
                    r"Optimicé el rendimiento del ERP interno, reduciendo en más de un 30% el llamado a APIs mejorando la velocidad de respuesta del sistema."
                ),
                bullet(
                    r"Fortalecí la infraestructura de código en diversos proyectos, optimizando la escalabilidad y facilitando el crecimiento sostenible de las aplicaciones."
                ),
                bullet(
                    r"Gestioné y automaticé flujos de trabajo complejos utilizando Apache Airflow, mejorando la eficiencia y monitoreo de procesos en entorno de datos."
                ),
                bullet(
                    r"Desarrollé y mejoré scripts utilizando Python para automatizar procesos repetitivos, aumentando en un 20% la eficiencia y reduciendo un 25% el tiempo de ejecución de tareas manuales."
                ),
                bullet(
                    r"Colaboré en equipos de desarrollo bajo metodologías ágiles (Scrum/Kanban), facilitando entregas incrementales y mejorando la adaptación a cambios de requerimientos."
                ),
            ),
            experience_card(
                "NoCountry",
                f"Oct 2024 - Mar 2024",
                "flex-end",
                bullet(
                    "Colaboré en el desarrollo de un MVP desde cero, asegurando una base sólida para la evolución del producto."
                ),
                bullet(
                    "Diseñé e implementé una RESTful API eficiente, facilitando la comunicación entre servicios y mejorando la experiencia de usuario."
                ),
                bullet(
                    "Contribuí en la creación del modelo entidad-relación para definir la estructura de las tablas, optimizando la organización de datos."
                ),
                bullet(
                    "Trabajé bajo la metodología Scrum, cumpliendo con entregas puntuales y adaptándome rápidamente a cambios de requerimientos."
                ),
            ),
            width="100%",
            spacing="8",
        )
    )
