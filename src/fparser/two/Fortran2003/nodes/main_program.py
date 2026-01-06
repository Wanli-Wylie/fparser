from end_program_stmt import End_Program_Stmt
from execution_part import Execution_Part
from internal_subprogram_part import Internal_Subprogram_Part
from program_stmt import Program_Stmt
from specification_part import Specification_Part

class Main_Program(BlockBase):  # R1101 [C1101, C1102, C1103]
    """
    Fortran 2003 rule R1101::

        main-program is program-stmt
                        [ specification-part ]
                        [ execution-part ]
                        [ internal-subprogram-part ]
                        end-program-stmt

    This class does not cater for the case where there is no
    program-stmt. The separate Main_Program0() class matches this
    situation. See Class Program() method match() for how this is
    implemented.

    C1101 In a main-program, the execution-part shall not contain a
    RETURN statement or an ENTRY statement. This is currently not
    checked, see issue #140.

    C1102 The program-name may be included in the end-program-stmt
    only if the optional program-stmt is used and, if included, shall
    be identical to the program-name specified in the program-stmt.

    C1103 An automatic object shall not appear in the
    specification-part (R204) of a main program. This is currently not
    checked, see issue #140.

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
        """Implements the matching of a main program which has a Program
        statement. See class Main_Program0 for matching without a
        Program Statement. Matching uses `BlockBase` as it conforms to
        the start/end with optional content pattern. `match_names` is
        set to `True` so that different names e.g. `program x` and
        `end program y` will not match.

        :param reader: the Fortran reader containing the line(s) of \
                       code that we are trying to match
        :type reader: :py:class:`fparser.common.readfortran.FortranReaderBase`

        :returns: `None` if there is not match or, if there is a match, \
                  a `tuple` containing a single `list`, with minimum \
                  size 2 and maximum size 5, which contains instances \
                  of the classes that have matched. The first entry in \
                  the list will be a `Program_Stmt` and the last entry \
                  in the list will be an `End_Program_Stmt`. In-between \
                  these two instances will be an optional \
                  `Specification_Part` followed by an optional \
                  `Execution_Part` followed by an optional \
                  `Internal_Subprogram_Part`.
        :rtype: `NoneType` or \
                ([:py:class:`fparser.two.Fortran2003.Program_Stmt`, \
                optional \
                :py:class:`fparser.two.Fortran2003.Specification_Part`, \
                optional \
                :py:class:`fparser.two.Fortran2003.Execution_Part`, \
                optional \
                :py:class:`fparser.two.Fortran2003.Internal_Subprogram_Part`, \
                :py:class:`fparser.two.Fortran2003.End_Program_Stmt`])

        """
        return BlockBase.match(
            Program_Stmt,
            [Specification_Part, Execution_Part, Internal_Subprogram_Part],
            End_Program_Stmt,
            reader,
            match_names=True,
            strict_order=True,
        )
