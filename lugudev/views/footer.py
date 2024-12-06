import reflex as rx

from lugudev.components import external_icon


def footer() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading("hi@lugu.dev"),
            rx.divider(),
        ),
        rx.hstack(
            external_icon(
                "github",
                "https://github.com/lupydev",
            ),
            external_icon(
                "linkedin",
                "https://www.linkedin.com/in/lugudev/",
            ),
            justify="center",
            align="center",
        ),
        # wrap="wrap",
        rx.text("Hecho con ❤️ por LuGuDev"),
        # width="100%",
        padding="5em 0 2em",
        align="center",
        spacing="4",
    )
