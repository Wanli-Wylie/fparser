from fparser.two.utils import (
    Base,
)

class Ac_Do_Variable(Base):
    """
    Fortran2003 rule R472.
    Specifies the permitted form of an implicit do-loop variable within an
    array constructor::

        ac-do-variable is scalar-int-variable
        ac-do-variable shall be a named variable

    Subject to the following constraint::

        C493 (R472) ac-do-variable shall be a named variable.

    C493 is currently not checked - issue #257.

    """

    subclass_names = ["Scalar_Int_Variable"]
