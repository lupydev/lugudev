import reflex as rx


def cv(width: str = "391px") -> rx.Component:
    return rx.link(
        rx.card(
            rx.hstack(
                rx.icon("download"),
                rx.heading(
                    "Curriculum Vitae",
                    size="6",
                ),
                justify="center",
                align="center",
                padding="12px",
                width="100%",
            ),
            width="100%",
        ),
        width=width,
        href="https://drive.google.com/file/d/1BueF_Df6MV__ZqOKctc1U2igPF9B72HY/view?usp=sharing",
        is_external=True,
        color=rx.color_mode_cond(light="black", dark="white"),
        color_scheme="gray",
    )
