from fparser.two.symbol_table import SYMBOL_TABLES
from fparser.two.utils import (
    BlockBase,
)

from end_program_stmt import End_Program_Stmt
from execution_part import Execution_Part
from internal_subprogram_part import Internal_Subprogram_Part
from specification_part import Specification_Part

class Main_Program0(BlockBase):
    """
    Rule 1101 specifies that the opening 'program-stmt' is optional. This
    class handles the special case when it is not supplied and thus
    matches on::

        <main-program> =
                         [ <specification-part> ]
                         [ <execution-part> ]
                         [ <internal-subprogram-part> ]
                         <end-program-stmt>

    C1102 The program-name may be included in the end-program-stmt
    only if the optional program-stmt is used and, if included, shall
    be identical to the program-name specified in the
    program-stmt.

    In this class an end program name is not allowed due to C1102.

    """

    subclass_names = []
    use_names = [
        "Program_Stmt",
        "Specification_Part",
        "Execution_Part",
        "Internal_Subprogram_Part",
        "End_Program_Stmt",
    ]

    @staticmethod
    def match(reader):
        """
        Attempts to match the content in the reader with a program that is
        missing the optional opening program-stmt (R1101). If the match
        is successful, a symbol table named "fparser2:main_program" is
        also created.

        :param reader: Content to check for match
        :type reader: str or instance of :py:class:`FortranReaderBase`

        :return: 2-tuple of (list of matched classes,  None) or None \
                 if no match is found.
        :rtype: (list of matched classes, None) or NoneType

        """
        # For this special case we have to supply a name for the top-level
        # symbol table. We include a ':' so that it is not a valid Fortran
        # name and therefore cannot clash with any routine names.
        table_name = "fparser2:main_program"
        SYMBOL_TABLES.enter_scope(table_name)

        result = BlockBase.match(
            None,
            [Specification_Part, Execution_Part, Internal_Subprogram_Part],
            End_Program_Stmt,
            reader,
        )

        SYMBOL_TABLES.exit_scope()
        if not result:
            # The match failed so remove the associated symbol table
            SYMBOL_TABLES.remove(table_name)

        return result
