import attr


@attr.s
class CustomItem:
    one_field = attr.ib()
    another_field = attr.ib()
