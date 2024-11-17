import reflex as rx


def bullet(
    text: str,
) -> rx.Component:
    return rx.hstack(
        rx.icon(
            "chevrons-right",
            size=20,
            width="20%",
        ),
        rx.text(text),
        align="center",
    )
