class Saved_Entity(BracketBase):  # R544
    """
    ::

        <saved-entity> = <object-name>
                         | <proc-pointer-name>
                         | / <common-block-name> /

    """

    subclass_names = ["Object_Name", "Proc_Pointer_Name"]
    use_names = ["Common_Block_Name"]

    @staticmethod
    def match(string):
        return BracketBase.match("//", Common_Block_Name, string)
