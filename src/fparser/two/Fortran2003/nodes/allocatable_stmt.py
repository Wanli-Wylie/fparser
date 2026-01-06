from object_name_deferred_shape_spec_list_item import Object_Name_Deferred_Shape_Spec_List_Item_List

class Allocatable_Stmt(StmtBase, WORDClsBase):  # R520
    """
    Fortran2003 Rule R520::

        <allocateble-stmt> = ALLOCATABLE [ :: ] <object-name> [
            ( <deferred-shape-spec-list> ) ] [ , <object-name>
            [ ( <deferred-shape-spec-list> ) ] ]...

    """

    subclass_names = []
    use_names = ["Object_Name_Deferred_Shape_Spec_List_Item_List"]

    @staticmethod
    def match(string):
        return WORDClsBase.match(
            "ALLOCATABLE",
            Object_Name_Deferred_Shape_Spec_List_Item_List,
            string,
            colons=True,
            require_cls=True,
        )
