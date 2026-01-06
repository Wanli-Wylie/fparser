class Real_Part(Base):  # R422
    """
    ::

        <real-part> = <signed-int-literal-constant>
                      | <signed-real-literal-constant>
                      | <named-constant>
    """

    subclass_names = [
        "Signed_Int_Literal_Constant",
        "Signed_Real_Literal_Constant",
        "Named_Constant",
    ]
