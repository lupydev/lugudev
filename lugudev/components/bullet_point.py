import reflex as rx


def bullet(
    text: str,
) -> rx.Component:
    return rx.hstack(
        rx.icon(
            "chevrons-right",
            color=rx.color("iris", 9),
            size=20,
            width="31px",
        ),
        rx.text(
            text,
            width="100%",
        ),
        align="center",
    )
