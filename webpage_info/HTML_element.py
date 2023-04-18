class AbsHTMLElement:
    def __init__(self, alias, type_e, tag_type, tag_value) -> None:
        self.alias = alias
        self.type_e = type_e
        self.tag_type = tag_type
        self.tag_value = tag_value

    def __repr__(self) -> str:
        return f"HTMLElement(alias={self.alias}, type_e={self.type_e}, \
tag_type={self.tag_type}, tag_value={self.tag_value})"


class UserConfigHTMLElement(AbsHTMLElement):
    def __init__(self, alias, type_e, tag_type, tag_value) -> None:
        super().__init__(alias, type_e, tag_type, tag_value)


class HTMLElementFullInfo(AbsHTMLElement):
    def __init__(self, alias, type_e, tag_type, tag_value, element_value) -> None:
        super().__init__(alias, type_e, tag_type, tag_value)
        self.element_value = element_value
    
