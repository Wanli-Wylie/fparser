class Bind_Entity(BracketBase):  # R523
    """
    ::

        <bind-entity> = <entity-name>
                        | / <common-block-name> /

    """

    subclass_names = ["Entity_Name"]
    use_names = ["Common_Block_Name"]

    @staticmethod
    def match(string):
        return BracketBase.match("//", Common_Block_Name, string)
