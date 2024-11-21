import reflex as rx


class DrawerState(rx.State):
    is_open: bool = False

    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
        ),
        href=url,
    )


def navbar_icons() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                navbar_icons_item("Home", "home", "/#"),
                navbar_icons_item("Experiencia", "badge-check", "/#"),
                navbar_icons_item("Proyectos", "briefcase-business", "/#"),
                justify="center",
                align_items="center",
                spacing="6",
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
                                rx.box(rx.button("Close")), align_self="end"
                            ),
                            rx.divider(),
                            rx.drawer.close(
                                navbar_icons_item("Home", "home", "/#"),
                            ),
                            navbar_icons_item("Experiencia", "badge-check", "/#"),
                            navbar_icons_item("Proyectos", "briefcase-business", "/#"),
                            align_items="start",
                            direction="column",
                            width="100%",
                            gap="12px",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="2em",
                        background_color="#191c1d",
                        # background_color=rx.color("green", 3)
                    )
                ),
                direction="left",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        # top="0px",
        z_index="5",
        width="100%",
    )
