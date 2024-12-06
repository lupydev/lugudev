import reflex as rx


class DrawerState(rx.State):
    is_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open


def navbar_icons_item(
    text: str,
    icon: str,
    url: str,
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
        high_contrast=True,
    )


def navbar_icons() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.container(
                rx.hstack(
                    navbar_icons_item("Home", "home", "/#"),
                    navbar_icons_item(
                        "Experiencia",
                        "badge-check",
                        "/#experience",
                    ),
                    navbar_icons_item(
                        "Proyectos",
                        "briefcase-business",
                        "/#projects",
                    ),
                    justify="center",
                    align_items="center",
                    spacing="6",
                    bg=rx.color("gray", 3),
                    padding="1em",
                    border_bottom_left_radius="8px",
                    border_bottom_right_radius="8px",
                ),
                padding="0",
            ),
        ),
        rx.mobile_only(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("menu"),
                ),
                rx.drawer.overlay(z_index="15"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.flex(
                            rx.drawer.close(
                                rx.box(
                                    rx.icon("x"),
                                ),
                                align_self="end",
                            ),
                            rx.divider(),
                            rx.drawer.close(
                                navbar_icons_item(
                                    "Home",
                                    "home",
                                    "/#",
                                ),
                            ),
                            rx.drawer.close(
                                navbar_icons_item(
                                    "Experiencia",
                                    "badge-check",
                                    "/#experiencem",
                                ),
                            ),
                            rx.drawer.close(
                                navbar_icons_item(
                                    "Proyectos",
                                    "briefcase-business",
                                    "/#projectsm",
                                ),
                            ),
                            align_items="start",
                            direction="column",
                            width="100%",
                            gap="12px",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1em 2em",
                        bg=rx.color("gray", 3),
                    ),
                ),
                direction="left",
            ),
            bg=rx.color("gray", 3),
            padding="1em",
        ),
        position="fixed",
        z_index="5",
        width="100%",
    )
