class Do_Term_Action_Stmt(StmtBase):  # R838
    """
    ::

        <do-term-action-stmt> = <action-stmt>

    Notes::

        C824 - <do-term-action-stmt> shall not be <continue-stmt>, <goto-stmt>,
              <return-stmt>, <stop-stmt>, <exit-stmt>, <cycle-stmt>,
              <end-function-stmt>, <end-subroutine-stmt>, <end-program-stmt>,
              <arithmetic-if-stmt>

    """

    subclass_names = ["Action_Stmt_C824"]
