class Name(StringBase):  # R304
    """
    Fortran 2003 rule R304::

        name is letter [ alphanumeric_character ]...

    """

    # There are no other classes. This is a simple string match.
    subclass_names = []

    @staticmethod
    def match(string):
        """Match the string with the regular expression abs_name in the
        pattern_tools file.

        :param str string: the string to match with the pattern rule.
        :return: a tuple of size 1 containing a string with the \
        matched name if there is a match, or None if there is not.
        :rtype: (str) or None

        """
        return StringBase.match(pattern.abs_name, string.strip())


class Arg_Name(Base):
    subclass_names = ["Name"]


class Array_Name(Base):
    subclass_names = ["Name"]


class Associate_Construct_Name(Base):
    subclass_names = ["Name"]


class Associate_Name(Base):
    subclass_names = ["Name"]


class Binding_Name(Base):
    subclass_names = ["Name"]


class Block_Data_Name(Base):
    subclass_names = ["Name"]


class Case_Construct_Name(Base):
    subclass_names = ["Name"]


class Common_Block_Name(Base):
    subclass_names = ["Name"]


class Component_Name(Base):
    subclass_names = ["Name"]


class Cray_Pointee_Name(Base):
    subclass_names = ["Name"]


class Cray_Pointer_Name(Base):
    subclass_names = ["Name"]


class Data_Pointer_Component_Name(Base):
    subclass_names = ["Name"]


class Do_Construct_Name(Base):
    subclass_names = ["Name"]


class Entity_Name(Base):
    subclass_names = ["Name"]


class Entry_Name(Base):
    subclass_names = ["Name"]


class Forall_Construct_Name(Base):
    subclass_names = ["Name"]


class Function_Name(Base):
    subclass_names = ["Name"]


class Generic_Name(Base):
    subclass_names = ["Name"]


class If_Construct_Name(Base):
    subclass_names = ["Name"]


class Index_Name(Base):
    subclass_names = ["Name"]


class Local_Name(Base):
    subclass_names = ["Name"]


class Module_Name(Base):
    subclass_names = ["Name"]


class Namelist_Group_Name(Base):
    subclass_names = ["Name"]


class Parent_Type_Name(Base):
    subclass_names = ["Name"]


class Part_Name(Base):
    subclass_names = ["Name"]


class Proc_Entity_Name(Base):
    subclass_names = ["Name"]


class Procedure_Component_Name(Base):
    subclass_names = ["Name"]


class Procedure_Entity_Name(Base):
    subclass_names = ["Name"]


class Procedure_Name(Base):
    subclass_names = ["Name"]


class Program_Name(Base):
    subclass_names = ["Name"]


class Result_Name(Base):
    subclass_names = ["Name"]


class Scalar_Variable_Name(Base):
    subclass_names = ["Name"]


class Select_Construct_Name(Base):
    subclass_names = ["Name"]


class Subroutine_Name(Base):
    subclass_names = ["Name"]


class Type_Param_Name(Base):
    subclass_names = ["Name"]


class Use_Name(Base):
    subclass_names = ["Name"]


class Where_Construct_Name(Base):
    subclass_names = ["Name"]


class Binding_Name_List(SequenceBase):
    subclass_names = ["Binding_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Binding_Name, string)

    def __iter__(self):
        return iter(self.items)


class Entity_Name_List(SequenceBase):
    subclass_names = ["Entity_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Entity_Name, string)

    def __iter__(self):
        return iter(self.items)


class External_Name_List(SequenceBase):
    subclass_names = ["External_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", External_Name, string)

    def __iter__(self):
        return iter(self.items)


class Final_Subroutine_Name_List(SequenceBase):
    subclass_names = ["Final_Subroutine_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Final_Subroutine_Name, string)

    def __iter__(self):
        return iter(self.items)


class Import_Name_List(SequenceBase):
    subclass_names = ["Import_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Import_Name, string)

    def __iter__(self):
        return iter(self.items)


class Intrinsic_Procedure_Name_List(SequenceBase):
    subclass_names = ["Intrinsic_Procedure_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Intrinsic_Procedure_Name, string)

    def __iter__(self):
        return iter(self.items)


class Procedure_Name_List(SequenceBase):
    subclass_names = ["Procedure_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Procedure_Name, string)

    def __iter__(self):
        return iter(self.items)


class Type_Param_Name_List(SequenceBase):
    subclass_names = ["Type_Param_Name"]
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r",", Type_Param_Name, string)

    def __iter__(self):
        return iter(self.items)
