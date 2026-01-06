class Function_Stmt(StmtBase, ScopingRegionMixin):  # R1224
    """
    ::

        <function-stmt> = [ <prefix> ] FUNCTION <function-name>
                          ( [ <dummy-arg-name-list> ] ) [ <suffix> ]

    C1242 (R1227) A prefix shall not specify ELEMENTAL if
    proc-language-binding-spec appears in the function-stmt or
    subroutine-stmt. The spec associates this constraint with R1227
    but it needs to be checked here.

    """

    subclass_names = []
    use_names = ["Prefix", "Function_Name", "Dummy_Arg_Name_List", "Suffix"]

    @staticmethod
    def match(string):
        line, repmap = string_replace_map(string)
        m = pattern.function.search(line)
        if m is None:
            return
        prefix = line[: m.start()].rstrip() or None
        if prefix is not None:
            prefix = Prefix(repmap(prefix))
        line = line[m.end() :].lstrip()
        m = pattern.name.match(line)
        if m is None:
            return
        name = Function_Name(m.group())
        line = line[m.end() :].lstrip()
        if not line.startswith("("):
            return
        i = line.find(")")
        if i == -1:
            return
        dummy_args = line[1:i].strip() or None
        if dummy_args is not None:
            dummy_args = Dummy_Arg_List(repmap(dummy_args))
        line = line[i + 1 :].lstrip()
        suffix = None
        if line:
            suffix = Suffix(repmap(line))
        if suffix:
            # A suffix may or may not contain a binding spec.
            binding_spec = walk(suffix, Language_Binding_Spec)
            # Check that we conform to C1242.
            if not c1242_valid(prefix, binding_spec):
                return None
        return prefix, name, dummy_args, suffix

    def tostr(self):
        prefix, name, dummy_args, suffix = self.items
        if prefix is not None:
            s = "%s FUNCTION %s" % (prefix, name)
        else:
            s = "FUNCTION %s" % (name)
        if dummy_args is not None:
            s += "(%s)" % (dummy_args)
        else:
            s += "()"
        if suffix is not None:
            s += " %s" % (suffix)
        return s

    def get_name(self):
        """
        :returns: the function name.
        :rtype: :py:class:`Name`
        """
        return self.items[1]
