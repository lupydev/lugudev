import reflex as rx


def external(
    img_light: str,
    img_dark: str,
    href: str = "",
    width: str = "70px",
    heigh: str = "78px",
) -> rx.Component:
    return rx.link(
        rx.card(
            rx.center(
                rx.color_mode_cond(
                    light=rx.image(
                        src=f"/{img_dark}",
                        height="100%",
                        width=width,
                    ),
                    dark=rx.image(
                        src=f"/{img_light}",
                        height="100%",
                        width=width,
                    ),
                ),
                align="center",
                justify="center",
            ),
            width=width,
            height=heigh,
            padding="12px",
        ),
        href=href,
        is_external=True,
    )


def external_icon(
    icon: str = "external-link",
    href: str = "",
) -> rx.Component:
    return rx.link(
        rx.card(
            rx.center(
                rx.icon(icon),
                align="center",
                justify="center",
            ),
            padding="12px",
        ),
        href=href,
        is_external=True,
        color_scheme="gray",
        high_contrast=True,
    )
