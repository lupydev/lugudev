import reflex as rx

from lugudev.components import external


def project_card_right(
    title: str,
    text: str,
    img: str,
    width_external: str | None = None,
    height_external: str | None = None,
) -> rx.Component:
    return rx.card(
        rx.grid(
            rx.image(
                src=img,
                width="100%",
                height="300px",
                border="1px solid #2f3135",
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
                    external(
                        "github_light.svg",
                        "github_dark.svg",
                        "https://github.com/lupydev",
                        width_external,
                        height_external,
                    ),
                    external(
                        "github_light.svg",
                        "github_dark.svg",
                        "https://github.com/lupydev",
                        width_external,
                        height_external,
                    ),
                    align_self="end",
                ),
                padding="16px",
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
    width_external: str | None = None,
    height_external: str | None = None,
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
                    external(
                        "github_light.svg",
                        "github_dark.svg",
                        "https://github.com/lupydev",
                        width_external,
                        height_external,
                    ),
                    external(
                        "github_light.svg",
                        "github_dark.svg",
                        "https://github.com/lupydev",
                        width_external,
                        height_external,
                    ),
                    align_self="end",
                ),
                padding="16px",
            ),
            rx.image(
                src=img,
                width="100%",
                height="300px",
                border="1px solid #2f3135",
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
