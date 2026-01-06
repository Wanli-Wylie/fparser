from fparser.two.utils import (
    Base,
)

class Interface_Body(Base):  # R1205
    """
    ::

        <interface-body> = <function-body> | <subroutine-body>

    See also :py:class:`fparser.two.Fortran2003.Function_Body` and
    :py:class:`fparser.two.Fortran2003.Subroutine_Body`

    """

    subclass_names = ["Function_Body", "Subroutine_Body"]
    use_names = []
