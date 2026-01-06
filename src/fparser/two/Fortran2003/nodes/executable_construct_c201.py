from executable_construct import Executable_Construct

class Executable_Construct_C201(Base):
    subclass_names = Executable_Construct.subclass_names[:]
    subclass_names[subclass_names.index("Action_Stmt")] = "Action_Stmt_C201"
