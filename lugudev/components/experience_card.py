import reflex as rx


def experience_card(
    company: str,
    time: str,
    align: str,
    *args: rx.Component,
) -> rx.Component:
    return (
        rx.card(
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
            width="70%",
            padding="16px",
            align_self=align,
        ),
    )


def experience_card_mobile(
    company: str,
    time: str,
    align: str,
    *args: rx.Component,
) -> rx.Component:
    return (
        rx.mobile_only(
            rx.card(
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
                width="100%",
                align_self=align,
            ),
        ),
    )
