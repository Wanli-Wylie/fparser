from int_initialization_expr import Scalar_Int_Initialization_Expr
from type_param_value import Type_Param_Value

class Char_Selector(Base):  # R424
    """
    ::

        <char-selector> = <length-selector>
                          | ( LEN = <type-param-value> ,
                             KIND = <scalar-int-initialization-expr> )
                          | ( <type-param-value> ,
                             [ KIND = ] <scalar-int-initialization-expr> )
                          | ( KIND = <scalar-int-initialization-expr>
                            [ , LEN = <type-param-value> ] )

    """

    subclass_names = ["Length_Selector"]
    use_names = ["Type_Param_Value", "Scalar_Int_Initialization_Expr"]

    @staticmethod
    def match(string: str):
        """
        Attempts to match the supplied text as a char-selector.

        :param string: the text to attempt to match.

        :returns: the matched Char_Selector object or None.
        :rtype: Union[None, Tuple[Optional[Type_Param_Value],
                                  Scalar_Int_Initialization_Expr]]

        """
        if string[0] + string[-1] != "()":
            return
        line, repmap = string_replace_map(string[1:-1].strip())
        if line[:3].upper() == "LEN" and line[3:].lstrip().startswith("="):
            line = line[3:].lstrip()
            line = line[1:].lstrip()
            i = line.find(",")
            if i == -1:
                return
            v = line[:i].rstrip()
            line = line[i + 1 :].lstrip()
            if line[:4].upper() != "KIND":
                return
            line = line[4:].lstrip()
            if not line.startswith("="):
                return
            line = line[1:].lstrip()
            v = repmap(v)
            line = repmap(line)
            return Type_Param_Value(v), Scalar_Int_Initialization_Expr(line)

        if line[:4].upper() == "KIND" and line[4:].lstrip().startswith("="):
            line = line[4:].lstrip()
            line = line[1:].lstrip()
            i = line.find(",")
            if i == -1:
                return None, Scalar_Int_Initialization_Expr(line)
            v = line[i + 1 :].lstrip()
            line = line[:i].rstrip()
            if v[:3].upper() != "LEN":
                return
            v = v[3:].lstrip()
            if not v.startswith("="):
                return
            v = v[1:].lstrip()
            return Type_Param_Value(v), Scalar_Int_Initialization_Expr(line)

        i = line.find(",")
        if i == -1:
            return
        v = line[:i].rstrip()
        line = line[i + 1 :].lstrip()
        if line[:4].upper() == "KIND" and line[4:].lstrip().startswith("="):
            line = line[4:].lstrip()
            line = line[1:].lstrip()
        return Type_Param_Value(v), Scalar_Int_Initialization_Expr(line)

    def tostr(self):
        if self.items[0] is None:
            return "(KIND = %s)" % (self.items[1])
        return "(LEN = %s, KIND = %s)" % (self.items[0], self.items[1])
