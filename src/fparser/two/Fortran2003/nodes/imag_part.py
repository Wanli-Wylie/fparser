class Imag_Part(Base):  # R423
    """
    ::

        <imag-part> = <real-part>

    """

    subclass_names = [
        "Signed_Int_Literal_Constant",
        "Signed_Real_Literal_Constant",
        "Named_Constant",
    ]
