from fparser.two.C99Preprocessor import match_cpp_directive
from .match_comment_or_include import match_comment_or_include
def add_comments_includes_directives(content, reader):
    """Creates comment, include, and/or cpp directive objects and adds them to
    the content list. Comment, include, and/or directive objects are added
    until a line that is not a comment, include, or directive is found.

    :param content: a `list` of matched objects. Any matched comments, \
                    includes, or directives in this routine are added to \
                    this list.
    :type content: :obj:`list`
    :param reader: the fortran file reader containing the line(s) \
                   of code that we are trying to match
    :type reader: :py:class:`fparser.common.readfortran.FortranFileReader` \
                  or \
                  :py:class:`fparser.common.readfortran.FortranStringReader`

    """
    

    obj = match_comment_or_include(reader)
    obj = match_cpp_directive(reader) if not obj else obj
    while obj:
        content.append(obj)
        obj = match_comment_or_include(reader)
        obj = match_cpp_directive(reader) if not obj else obj
