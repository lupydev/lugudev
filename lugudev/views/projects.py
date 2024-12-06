import reflex as rx
from lugudev.components import (
    external,
    external_icon,
    project_card_right,
    project_card_left,
    title,
)


def projects_view() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
            title("Proyectos"),
            project_card_right(
                "HiDx",
                "Plataforma de RRHH para evaluar personas, equipos y sistemas a través de diagnósticos.",
                "/hidx_logo.png",
                external_icon(href="https://hidx.company/"),
            ),
            #! el siguiente proyecto debe usar el componente project_card_left
            spacing="8",
            id="projects",
        ),
    )
