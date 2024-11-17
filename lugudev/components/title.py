import reflex as rx


def title(title: str) -> rx.Component:
    return rx.card(
        rx.heading(
            title,
            size="8",
        ),
        justify="center",
        # width="817px",
        width="100%",
        padding="24px",
        text_align="center",
        box_shadow="-8px 8px 12px #2d2f33",
    )