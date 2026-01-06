from .directive import Directive
from .comment import Comment
from .include_stmt import Include_Stmt

def match_comment_or_include(reader):
    """Creates a comment, directive, or include object from the current line.

    :param reader: the fortran file reader containing the line
                   of code that we are trying to match
    :type reader: :py:class:`fparser.common.readfortran.FortranFileReader`
                   or
                   :py:class:`fparser.common.readfortran.FortranStringReader`

    :return: a comment, directive, or include object if found, otherwise
             `None`.
    :rtype: :py:class:`fparser.two.Fortran2003.Comment` or
            :py:class:`fparser.two.Fortran2003.Include_Stmt`
            or :py:class:`fparser.two.Fortran2003.Directive`

    """
    obj = None
    # Whether or not to specialise Directives is a run-time option.
    if reader.process_directives:
        obj = Directive(reader)
    obj = Comment(reader) if not obj else obj
    obj = Include_Stmt(reader) if not obj else obj
    return obj
