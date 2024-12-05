import reflex as rx


def project_card_right(
    title: str,
    text: str,
    img: str,
    *args: rx.Component,
) -> rx.Component:
    return rx.card(
        rx.grid(
            rx.image(
                src=img,
                width="100%",
                height="300px",
                padding="1em",
                border_bottom=f"1px solid {rx.color("gray", 6)}",
                object_fit="contain",
            ),
            rx.vstack(
                rx.heading(title),
                rx.divider(),
                rx.text(
                    text,
                    height="100%",
                ),
                rx.divider(),
                rx.hstack(
                    args,
                    align_self="end",
                ),
                padding="16px",
                border_left=f"1px solid {rx.color("gray", 6)}",
            ),
            grid_template_columns=[
                "1fr",  # 1 column for mobile
                "repeat(2, 1fr)",  # 2 columns for tablet and up
            ],
            wrap="wrap",
        ),
        width="100%",
        padding="0",
    )


def project_card_left(
    title: str,
    text: str,
    img: str,
    *args: rx.Component,
) -> rx.Component:
    return rx.card(
        rx.grid(
            rx.vstack(
                rx.heading(title),
                rx.divider(),
                rx.text(
                    text,
                    height="100%",
                ),
                rx.divider(),
                rx.hstack(
                    args,
                    align_self="end",
                ),
                padding="16px",
                border_right=f"1px solid {rx.color("gray", 6)}",
            ),
            rx.image(
                src=img,
                width="100%",
                height="300px",
                padding="1em",
                object_fit="contain",
            ),
            grid_template_columns=[
                "1fr",  # 1 column for mobile
                "repeat(2, 1fr)",  # 2 columns for tablet and up
            ],
            wrap="wrap",
        ),
        width="100%",
        padding="0",
    )
