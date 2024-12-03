import reflex as rx
from lugudev.components import cv, external


def hero() -> rx.Component:
    return rx.grid(
        rx.card(
            rx.image("https://i.postimg.cc/VkHYXNX7/profile.png"),
            padding="0",
        ),
        rx.vstack(
            rx.card(
                rx.vstack(
                    rx.heading(
                        "Backend Developer",
                        size="9",
                    ),
                    rx.heading(
                        "Luis Guzmán",
                        size="8",
                    ),
                ),
                width="100%",
                padding="31px 24px",
            ),
            rx.grid(
                cv(),
                rx.hstack(
                    external(
                        "github_light.svg",
                        "github_dark.svg",
                        "https://github.com/lupydev",
                    ),
                    external(
                        "linkedin_light.svg",
                        "linkedin_dark.svg",
                        "https://www.linkedin.com/in/lugudev/",
                    ),
                    width="100%",
                ),
                width="100%",
                grid_template_columns=[
                    "1fr",
                    f"73% 25%",
                ],
                spacing="3",
            ),
        ),
        grid_template_columns=[
            "1fr",  # 1 column for mobile
            "1fr",
            f"30% 68.6%",  # 2 columns for tablet and up
        ],
        spacing="3",
    )
