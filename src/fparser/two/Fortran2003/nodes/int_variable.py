class Int_Variable(Base):  # R608
    """
    ::

        <int-variable> = <variable>

    """

    subclass_names = ["Variable"]


class Scalar_Int_Variable(Base):
    subclass_names = ["Int_Variable"]
