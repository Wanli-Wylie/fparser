class Label_Do_Stmt(StmtBase):  # pylint: disable=invalid-name
    """
    R828::

        <label-do-stmt> = [ <do-construct-name> : ] DO <label> [ <loop-control> ]

    """

    subclass_names = []
    use_names = ["Do_Construct_Name", "Label", "Loop_Control"]

    @classmethod
    def match(cls, string):
        """
        :param string: (source of) Fortran string to parse
        :type string: str or :py:class:`FortranReaderBase`
        :return: 3-tuple containing strings and instances of the classes
                 determining labeled "DO" statement (optional statement name,
                 label and loop control expression if present)
        :rtype: 3-tuple of objects
        """
        # do-construct-name is determined by reader
        if string[:2].upper() != "DO":
            return
        line = string[2:].lstrip()
        mpat = pattern.label.match(line)
        if mpat is None:
            return
        label = mpat.group()
        line = line[mpat.end() :].lstrip()
        if line:
            return None, Label(label), cls.loop_control_cls()(line)
        return None, Label(label), None

    @staticmethod
    def loop_control_cls():
        """
        :returns: Fortran2003 Loop_Control class.
        :rtype: :py:class:`fparser.two.Fortran2003.Loop_Control`

        """
        return Loop_Control

    def tostr(self):
        """
        :return: string containing Fortran code for the parsed
                 labeled "DO" statement
        :rtype: string
        """
        # pylint: disable=unbalanced-tuple-unpacking
        name, label, loop_control = self.items
        if name is None:
            dostmt = "DO %s" % (label)
        else:
            dostmt = "%s: DO %s" % (label)
        if loop_control is not None:
            dostmt += " %s" % (loop_control)
        return dostmt

    def get_start_name(self):
        """
        :return: optional labeled "DO" statement name
        :rtype: string
        """
        return self.item.name

    def get_start_label(self):
        """
        :return: label of "DO" statement
        :rtype: string
        """
        return int(self.items[1])

    do_construct_name = property(lambda self: self.items[0])
    label = property(lambda self: self.items[1])
    loop_control = property(lambda self: self.items[2])
