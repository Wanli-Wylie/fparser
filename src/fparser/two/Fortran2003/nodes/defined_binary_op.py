from fparser.two.utils import (
    Base,
)

class Defined_Binary_Op(Base):  # pylint: disable=invalid-name
    """
    Fortran 2003 rule R723::

        defined-binary-op is . letter [ letter ]... .

    C704 (R723) A defined-binary-op shall not contain more than 63
    letters and shall not be the same as any intrinsic-operator or
    logical-literal-constant.

    Implemented in Defined_Op class.

    """

    subclass_names = ["Defined_Op"]
