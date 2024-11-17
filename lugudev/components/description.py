import reflex as rx


def description() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(
                "Backend Developer",
                size="9",
            ),
            rx.heading(
                "Luis Guzmán",
                size="8",
            ),
            padding="12px",
        )
    )
