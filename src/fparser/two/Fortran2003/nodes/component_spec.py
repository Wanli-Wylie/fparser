from component_data_source import Component_Data_Source
from keyword import Keyword

class Component_Spec(KeywordValueBase):  # R458
    """
    ::

        <component-spec> = [ <keyword> = ] <component-data-source>

    """

    subclass_names = ["Component_Data_Source"]
    use_names = ["Keyword"]

    @staticmethod
    def match(string):
        return KeywordValueBase.match(Keyword, Component_Data_Source, string)


class Component_Spec_List(SequenceBase):
    subclass_names = ["Component_Spec"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Component_Spec, string)

    def __iter__(self):
        return iter(self.items)
