from .component_base import OutputComponent


class SkillTemplate:
    def __init__(self):
        self.__version = "2.0"
        self.__components = []

    def set_add_component(self, component : OutputComponent):
        if(len(self.__components) > 3):
            raise ValueError("3개 이하만 가능 합니다")
        else:
            self.__components.append(component)

    def to_string(self) -> str:
        fields = {
            "version" : self.__version,
            "template": {
                "outputs":[]
            }
        }
        for c in self.__components:
            fields['template']['outputs'].append(c.to_string())

        return fields
