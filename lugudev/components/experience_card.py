from datetime import date
import reflex as rx


def experience_card(
    company: str,
    time: str,
    align: str,
    # width: str = "100%",
    *args,
) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(
                company,
                size="5",
            ),
            rx.heading(
                rx.hstack(
                    rx.icon(
                        "calendar",
                        size=20,
                    ),
                    rx.text(
                        rx.text.em(
                            time,
                        ),
                    ),
                    align="center",
                ),
                size="2",
            ),
            rx.divider(),
            args,
        ),
        # width=f"{817/2+36}px",
        # width=width,
        align_self=align,
    )
