import reflex as rx

from lugudev.views import experience, footer, hero, mobile_view, projects_view
from lugudev.components import navbar_icons


def index() -> rx.Component:
    return rx.vstack(
        navbar_icons(),
        rx.container(
            rx.color_mode.button(
                position="top-right",
                top="16px",
                right="16px",
                width="24px",
                height="24px",
                padding="0",
            ),
            rx.vstack(
                hero(),
                experience(),
                mobile_view(),
                projects_view(),
                gap="80px",
                justify="center",
                align="center",
                min_height="85vh",
                id="tuku",
            ),
            footer(),
            padding="124px 16px 0",
        ),
        align="center",
    )


app = rx.App()
app.add_page(index)
