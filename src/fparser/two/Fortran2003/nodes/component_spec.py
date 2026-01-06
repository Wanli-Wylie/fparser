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
