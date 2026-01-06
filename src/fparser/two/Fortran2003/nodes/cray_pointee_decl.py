from cray_pointee_array_spec import Cray_Pointee_Array_Spec
from name import Cray_Pointee_Name

class Cray_Pointee_Decl(CallBase):  # pylint: disable=invalid-name
    """
    ::

        cray-pointee-decl is cray-pointee-name ( cray-pointee-array-spec )

    """

    subclass_names = []
    use_names = ["Cray_Pointee_Name", "Cray_Pointee_Array_Spec"]

    @staticmethod
    def match(string):
        """Implements the matching for a Cray-pointee declaration.

        :param str string: the string to match as a Cray-pointee \
        declaration.
        :return: None if there is no match, otherwise a tuple of size \
        2 containing the name of the pointee as the first argument and \
        a Cray-pointee array spec as the second argument.
        :rtype: None or (Name, Cray_Pointee_Array_Spec)

        """
        return CallBase.match(
            Cray_Pointee_Name, Cray_Pointee_Array_Spec, string, require_rhs=True
        )
