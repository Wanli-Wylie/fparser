#!/usr/bin/env python

# Modified work Copyright (c) 2017-2025 Science and Technology
# Facilities Council.
# Original work Copyright (c) 1999-2008 Pearu Peterson

# All rights reserved.

# Modifications made as part of the fparser project are distributed
# under the following license:

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:

# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# --------------------------------------------------------------------

# The original software (in the f2py project) was distributed under
# the following license:

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#   a. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   b. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#   c. Neither the name of the F2PY project nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.

"""Fortran 2003 Syntax Rules."""
# Original author: Pearu Peterson <pearu@cens.ioc.ee>
# First version created: Oct 2006

import inspect
import re
import sys

from pathlib import Path
from typing import Union

from fparser.common.splitline import string_replace_map
from fparser.two import pattern_tools as pattern
from fparser.common.readfortran import FortranReaderBase
from fparser.two.symbol_table import SYMBOL_TABLES
from fparser.two.utils import (
    Base,
    BlockBase,
    StringBase,
    WORDClsBase,
    NumberBase,
    STRINGBase,
    BracketBase,
    StmtBase,
    EndStmtBase,
    BinaryOpBase,
    Type_Declaration_StmtBase,
    CALLBase,
    CallBase,
    KeywordValueBase,
    ScopingRegionMixin,
    SeparatorBase,
    SequenceBase,
    UnaryOpBase,
    walk,
    DynamicImport,
)
from fparser.two.utils import (
    EXTENSIONS,
    NoMatchError,
    FortranSyntaxError,
    InternalSyntaxError,
    InternalError,
    show_result,
)

#
# SECTION  1
#

# R101: <xyz-list> = <xyz> [ , <xyz> ]...
# R102: <xyz-name> = <name>
# R103: <scalar-xyz> = <xyz>


#
# SECTION  2
#




def match_comment_or_include(reader):
    """Creates a comment, directive, or include object from the current line.

    :param reader: the fortran file reader containing the line
                   of code that we are trying to match
    :type reader: :py:class:`fparser.common.readfortran.FortranFileReader`
                   or
                   :py:class:`fparser.common.readfortran.FortranStringReader`

    :return: a comment, directive, or include object if found, otherwise
             `None`.
    :rtype: :py:class:`fparser.two.Fortran2003.Comment` or
            :py:class:`fparser.two.Fortran2003.Include_Stmt`
            or :py:class:`fparser.two.Fortran2003.Directive`

    """
    obj = None
    # Whether or not to specialise Directives is a run-time option.
    if reader.process_directives:
        obj = Directive(reader)
    obj = Comment(reader) if not obj else obj
    obj = Include_Stmt(reader) if not obj else obj
    return obj


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
    from fparser.two.C99Preprocessor import match_cpp_directive

    obj = match_comment_or_include(reader)
    obj = match_cpp_directive(reader) if not obj else obj
    while obj:
        content.append(obj)
        obj = match_comment_or_include(reader)
        obj = match_cpp_directive(reader) if not obj else obj






































    # subclass_names.remove('End_Program_Stmt')








#
# SECTION  3
#

# R301: <character> = <alphanumeric-character> | <special-character>
# R302: <alphanumeric-character> = <letter> | <digit> | <underscore>
# R303: <underscore> = _














# R310: <intrinsic-operator> = <power-op> | <mult-op> | <add-op> |
# <concat-op> | <rel-op> | <not-op> | <and-op> | <or-op> | <equiv-op>
# Rule 310 is defined in pattern_tools.py. As it is only used by Rule
# 312 it does not need to be defined explicitly as a class. Note, it
# could be created as a class if it were useful for code
# manipulation. We could additionally create each of the operators
# themselves as classes.








#
# SECTION  4
#
















# R407: <kind-param> = <digit-string> | <scalar-int-constant-name>
# R408: <signed-digit-string> = [ <sign> ] <digit-string>
# R409: <digit-string> = <digit> [ <digit> ]...
# R410: <sign> = + | -










# R415: <hex-digit> = <digit> | A | B | C | D | E | F






# R418: <significand> = <digit-string> . [ <digit-string> ]  | . <digit-string>
# R419: <exponent-letter> = E | D
# R420: <exponent> = <signed-digit-string>






































































































# R467: <left-square-bracket> = [
# R468: <right-square-bracket> = ]










#
# SECTION  5
#






































































































































#
# SECTION  6
#












































































#
# SECTION  7
#







    # exclude_op_pattern = pattern.non_defined_binary_op)














# R707: power-op is **
# R708: mult-op is * or /
# R709: add-op is + or -




# R711: <concat-op> = //




# R713: <rel-op> = .EQ. | .NE. | .LT. | .LE. | .GT. | .GE. |
# == | /= | < | <= | > | >=










# R718: <not-op> = .NOT.
# R719: <and-op> = .AND.
# R720: <or-op> = .OR.
# R721: <equiv-op> = .EQV. | .NEQV.














































































#
# SECTION  8
#
































































# pylint: disable=invalid-name










































#
# SECTION  9
#
































































#
# SECTION 10
#








def skip_digits(string):
    """Skips over any potential digits (including spaces) to the next
    non-digit character and return its index. If no such character is
    found or if the first character in the string is not a digit then
    specify that the skip has failed.

    :param str string: The string to search
    :returns: a 2-tuple with the first entry indicating if a valid \
    character has been found and the second entry indicating the index \
    of this character in the 'string' argument.
    :rtype: (bool, int)

    """
    found = False
    index = 0
    for index, char in enumerate(string):
        if not (char.isdigit() or char == " "):
            if index > 0:
                found = True
            break
    return found, index










































#
# SECTION 11
#








































#
# SECTION 12
#








































































def c1242_valid(prefix, binding_spec):
    """If prefix and binding-spec exist then check whether they conform to
    constraint C1242 - "A prefix shall not specify ELEMENTAL if
    proc-language-binding-spec appears in the function-stmt or
    subroutine-stmt."

    :param prefix: matching prefix instance if one exists.
    :type: :py:class:`fparser.two.Fortran2003.Prefix` or `NoneType`
    :param binding_spec: matching binding specification instance if \
        one exists.
    :type binding_spec: \
        :py:class:`fparser.two.Fortran2003.Language_Binding_Spec` or
        `NoneType`
    :returns: False if prefix and binding-spec break constraint C1242, \
        otherwise True.
    :rtype: bool

    """
    if binding_spec and prefix:
        # Prefix(es) may or may not be of type ELEMENTAL
        elemental = any(
            "ELEMENTAL" in str(child) for child in walk(prefix.items, Prefix_Spec)
        )
        if elemental:
            # Constraint C1242. A prefix shall not specify ELEMENTAL if
            # proc-language-binding-spec appears in the function-stmt or
            # subroutine-stmt.
            return False
    return True
















#
# GENERATE Scalar_, _List, _Name CLASSES
#



# pylint: disable=eval-used
# pylint: disable=exec-used
# Load class definitions from split files.

_MODULE_DIR = Path(__file__).parent
_CLASS_FILES = [
    'nodes/directive.py',
    'nodes/comment.py',
    'nodes/program.py',
    'nodes/include_filename.py',
    'nodes/include_stmt.py',
    'nodes/program_unit.py',
    'nodes/external_subprogram.py',
    'nodes/specification_part.py',
    'nodes/implicit_part.py',
    'nodes/implicit_part_stmt.py',
    'nodes/declaration_construct.py',
    'nodes/execution_part.py',
    'nodes/execution_part_construct.py',
    'nodes/execution_part_construct_c201.py',
    'nodes/internal_subprogram_part.py',
    'nodes/internal_subprogram.py',
    'nodes/specification_stmt.py',
    'nodes/executable_construct.py',
    'nodes/executable_construct_c201.py',
    'nodes/action_stmt.py',
    'nodes/action_stmt_c201.py',
    'nodes/action_stmt_c802.py',
    'nodes/action_stmt_c824.py',
    'nodes/keyword.py',
    'nodes/name.py',
    'nodes/constant.py',
    'nodes/literal_constant.py',
    'nodes/named_constant.py',
    'nodes/int_constant.py',
    'nodes/char_constant.py',
    'nodes/defined_operator.py',
    'nodes/extended_intrinsic_op.py',
    'nodes/label.py',
    'nodes/type_spec.py',
    'nodes/type_param_value.py',
    'nodes/intrinsic_type_spec.py',
    'nodes/kind_selector.py',
    'nodes/signed_int_literal_constant.py',
    'nodes/int_literal_constant.py',
    'nodes/digit_string.py',
    'nodes/boz_literal_constant.py',
    'nodes/binary_constant.py',
    'nodes/octal_constant.py',
    'nodes/hex_constant.py',
    'nodes/signed_real_literal_constant.py',
    'nodes/real_literal_constant.py',
    'nodes/complex_literal_constant.py',
    'nodes/real_part.py',
    'nodes/imag_part.py',
    'nodes/char_selector.py',
    'nodes/length_selector.py',
    'nodes/char_length.py',
    'nodes/char_literal_constant.py',
    'nodes/logical_literal_constant.py',
    'nodes/derived_type_def.py',
    'nodes/derived_type_stmt.py',
    'nodes/type_name.py',
    'nodes/type_attr_spec.py',
    'nodes/private_or_sequence.py',
    'nodes/end_type_stmt.py',
    'nodes/sequence_stmt.py',
    'nodes/type_param_def_stmt.py',
    'nodes/type_param_decl.py',
    'nodes/type_param_attr_spec.py',
    'nodes/component_part.py',
    'nodes/component_def_stmt.py',
    'nodes/data_component_def_stmt.py',
    'nodes/dimension_component_attr_spec.py',
    'nodes/component_attr_spec.py',
    'nodes/component_decl.py',
    'nodes/component_array_spec.py',
    'nodes/component_initialization.py',
    'nodes/proc_component_def_stmt.py',
    'nodes/proc_component_pass_arg_name.py',
    'nodes/proc_component_attr_spec.py',
    'nodes/private_components_stmt.py',
    'nodes/type_bound_procedure_part.py',
    'nodes/binding_private_stmt.py',
    'nodes/proc_binding_stmt.py',
    'nodes/specific_binding.py',
    'nodes/binding_pass_arg_name.py',
    'nodes/generic_binding.py',
    'nodes/binding_attr.py',
    'nodes/final_binding.py',
    'nodes/derived_type_spec.py',
    'nodes/type_param_spec.py',
    'nodes/structure_constructor.py',
    'nodes/component_spec.py',
    'nodes/component_data_source.py',
    'nodes/enum_def.py',
    'nodes/enum_def_stmt.py',
    'nodes/enumerator_def_stmt.py',
    'nodes/enumerator.py',
    'nodes/end_enum_stmt.py',
    'nodes/array_constructor.py',
    'nodes/ac_spec.py',
    'nodes/ac_value.py',
    'nodes/ac_implied_do.py',
    'nodes/ac_implied_do_control.py',
    'nodes/ac_do_variable.py',
    'nodes/type_declaration_stmt.py',
    'nodes/declaration_type_spec.py',
    'nodes/dimension_attr_spec.py',
    'nodes/intent_attr_spec.py',
    'nodes/attr_spec.py',
    'nodes/entity_decl.py',
    'nodes/object_name.py',
    'nodes/initialization.py',
    'nodes/null_init.py',
    'nodes/access_spec.py',
    'nodes/language_binding_spec.py',
    'nodes/array_spec.py',
    'nodes/explicit_shape_spec.py',
    'nodes/lower_bound.py',
    'nodes/upper_bound.py',
    'nodes/assumed_shape_spec.py',
    'nodes/deferred_shape_spec.py',
    'nodes/assumed_size_spec.py',
    'nodes/intent_spec.py',
    'nodes/access_stmt.py',
    'nodes/access_id.py',
    'nodes/object_name_deferred_shape_spec_list_item.py',
    'nodes/allocatable_stmt.py',
    'nodes/asynchronous_stmt.py',
    'nodes/bind_stmt.py',
    'nodes/bind_entity.py',
    'nodes/data_stmt.py',
    'nodes/data_stmt_set.py',
    'nodes/data_stmt_object.py',
    'nodes/data_implied_do.py',
    'nodes/data_i_do_object.py',
    'nodes/data_i_do_variable.py',
    'nodes/data_stmt_value.py',
    'nodes/data_stmt_repeat.py',
    'nodes/data_stmt_constant.py',
    'nodes/int_constant_subobject.py',
    'nodes/constant_subobject.py',
    'nodes/dimension_stmt.py',
    'nodes/intent_stmt.py',
    'nodes/optional_stmt.py',
    'nodes/parameter_stmt.py',
    'nodes/named_constant_def.py',
    'nodes/cray_pointer_stmt.py',
    'nodes/cray_pointer_decl.py',
    'nodes/cray_pointee_decl.py',
    'nodes/cray_pointee_array_spec.py',
    'nodes/pointer_stmt.py',
    'nodes/pointer_decl.py',
    'nodes/protected_stmt.py',
    'nodes/save_stmt.py',
    'nodes/saved_entity.py',
    'nodes/proc_pointer_name.py',
    'nodes/target_entity_decl.py',
    'nodes/target_stmt.py',
    'nodes/value_stmt.py',
    'nodes/volatile_stmt.py',
    'nodes/implicit_stmt.py',
    'nodes/implicit_spec.py',
    'nodes/letter_spec.py',
    'nodes/namelist_stmt.py',
    'nodes/namelist_group_object.py',
    'nodes/equivalence_stmt.py',
    'nodes/equivalence_set.py',
    'nodes/equivalence_object.py',
    'nodes/common_stmt.py',
    'nodes/common_block_object.py',
    'nodes/variable.py',
    'nodes/variable_name.py',
    'nodes/designator.py',
    'nodes/logical_variable.py',
    'nodes/default_logical_variable.py',
    'nodes/char_variable.py',
    'nodes/default_char_variable.py',
    'nodes/int_variable.py',
    'nodes/substring.py',
    'nodes/parent_string.py',
    'nodes/substring_range.py',
    'nodes/data_ref.py',
    'nodes/part_ref.py',
    'nodes/structure_component.py',
    'nodes/type_param_inquiry.py',
    'nodes/array_element.py',
    'nodes/array_section.py',
    'nodes/subscript.py',
    'nodes/section_subscript.py',
    'nodes/subscript_triplet.py',
    'nodes/stride.py',
    'nodes/vector_subscript.py',
    'nodes/allocate_stmt.py',
    'nodes/stat_variable.py',
    'nodes/errmsg_variable.py',
    'nodes/source_expr.py',
    'nodes/alloc_opt.py',
    'nodes/allocation.py',
    'nodes/allocate_object.py',
    'nodes/allocate_shape_spec.py',
    'nodes/lower_bound_expr.py',
    'nodes/upper_bound_expr.py',
    'nodes/nullify_stmt.py',
    'nodes/pointer_object.py',
    'nodes/deallocate_stmt.py',
    'nodes/dealloc_opt.py',
    'nodes/scalar_char_initialization_expr.py',
    'nodes/primary.py',
    'nodes/parenthesis.py',
    'nodes/level_1_expr.py',
    'nodes/defined_unary_op.py',
    'nodes/defined_op.py',
    'nodes/mult_operand.py',
    'nodes/add_operand.py',
    'nodes/level_2_expr.py',
    'nodes/level_2_unary_expr.py',
    'nodes/level_3_expr.py',
    'nodes/level_4_expr.py',
    'nodes/and_operand.py',
    'nodes/or_operand.py',
    'nodes/equiv_operand.py',
    'nodes/level_5_expr.py',
    'nodes/expr.py',
    'nodes/defined_binary_op.py',
    'nodes/logical_expr.py',
    'nodes/char_expr.py',
    'nodes/default_char_expr.py',
    'nodes/int_expr.py',
    'nodes/numeric_expr.py',
    'nodes/specification_expr.py',
    'nodes/initialization_expr.py',
    'nodes/char_initialization_expr.py',
    'nodes/int_initialization_expr.py',
    'nodes/logical_initialization_expr.py',
    'nodes/assignment_stmt.py',
    'nodes/pointer_assignment_stmt.py',
    'nodes/data_pointer_object.py',
    'nodes/bounds_spec.py',
    'nodes/bounds_remapping.py',
    'nodes/data_target.py',
    'nodes/proc_pointer_object.py',
    'nodes/proc_component_ref.py',
    'nodes/proc_target.py',
    'nodes/where_stmt.py',
    'nodes/where_construct.py',
    'nodes/where_construct_stmt.py',
    'nodes/where_body_construct.py',
    'nodes/where_assignment_stmt.py',
    'nodes/mask_expr.py',
    'nodes/masked_elsewhere_stmt.py',
    'nodes/elsewhere_stmt.py',
    'nodes/end_where_stmt.py',
    'nodes/forall_construct.py',
    'nodes/forall_construct_stmt.py',
    'nodes/forall_header.py',
    'nodes/forall_triplet_spec.py',
    'nodes/forall_body_construct.py',
    'nodes/forall_assignment_stmt.py',
    'nodes/end_forall_stmt.py',
    'nodes/forall_stmt.py',
    'nodes/block.py',
    'nodes/if_construct.py',
    'nodes/if_then_stmt.py',
    'nodes/else_if_stmt.py',
    'nodes/else_stmt.py',
    'nodes/end_if_stmt.py',
    'nodes/if_stmt.py',
    'nodes/case_construct.py',
    'nodes/select_case_stmt.py',
    'nodes/case_stmt.py',
    'nodes/end_select_stmt.py',
    'nodes/case_expr.py',
    'nodes/case_selector.py',
    'nodes/case_value_range.py',
    'nodes/case_value.py',
    'nodes/associate_construct.py',
    'nodes/associate_stmt.py',
    'nodes/association.py',
    'nodes/selector.py',
    'nodes/end_associate_stmt.py',
    'nodes/select_type_construct.py',
    'nodes/select_type_stmt.py',
    'nodes/type_guard_stmt.py',
    'nodes/end_select_type_stmt.py',
    'nodes/do_construct.py',
    'nodes/block_do_construct.py',
    'nodes/block_label_do_construct.py',
    'nodes/block_nonlabel_do_construct.py',
    'nodes/do_stmt.py',
    'nodes/label_do_stmt.py',
    'nodes/nonlabel_do_stmt.py',
    'nodes/loop_control.py',
    'nodes/do_variable.py',
    'nodes/do_block.py',
    'nodes/end_do.py',
    'nodes/end_do_stmt.py',
    'nodes/nonblock_do_construct.py',
    'nodes/action_term_do_construct.py',
    'nodes/do_body.py',
    'nodes/do_term_action_stmt.py',
    'nodes/outer_shared_do_construct.py',
    'nodes/shared_term_do_construct.py',
    'nodes/inner_shared_do_construct.py',
    'nodes/do_term_shared_stmt.py',
    'nodes/cycle_stmt.py',
    'nodes/exit_stmt.py',
    'nodes/goto_stmt.py',
    'nodes/computed_goto_stmt.py',
    'nodes/arithmetic_if_stmt.py',
    'nodes/continue_stmt.py',
    'nodes/stop_stmt.py',
    'nodes/stop_code.py',
    'nodes/io_unit.py',
    'nodes/file_unit_number.py',
    'nodes/internal_file_variable.py',
    'nodes/open_stmt.py',
    'nodes/connect_spec.py',
    'nodes/file_name_expr.py',
    'nodes/iomsg_variable.py',
    'nodes/close_stmt.py',
    'nodes/close_spec.py',
    'nodes/read_stmt.py',
    'nodes/write_stmt.py',
    'nodes/print_stmt.py',
    'nodes/io_control_spec_list.py',
    'nodes/io_control_spec.py',
    'nodes/format.py',
    'nodes/input_item.py',
    'nodes/output_item.py',
    'nodes/io_implied_do.py',
    'nodes/io_implied_do_object.py',
    'nodes/io_implied_do_control.py',
    'nodes/dtv_type_spec.py',
    'nodes/wait_stmt.py',
    'nodes/wait_spec.py',
    'nodes/backspace_stmt.py',
    'nodes/endfile_stmt.py',
    'nodes/rewind_stmt.py',
    'nodes/position_spec.py',
    'nodes/flush_stmt.py',
    'nodes/flush_spec.py',
    'nodes/inquire_stmt.py',
    'nodes/inquire_spec.py',
    'nodes/format_stmt.py',
    'nodes/format_item_list.py',
    'nodes/format_specification.py',
    'nodes/format_item_c1002.py',
    'nodes/hollerith_item.py',
    'nodes/format_item.py',
    'nodes/r.py',
    'nodes/data_edit_desc_c1002.py',
    'nodes/data_edit_desc.py',
    'nodes/w.py',
    'nodes/m.py',
    'nodes/d.py',
    'nodes/e.py',
    'nodes/v.py',
    'nodes/control_edit_desc.py',
    'nodes/k.py',
    'nodes/position_edit_desc.py',
    'nodes/n.py',
    'nodes/sign_edit_desc.py',
    'nodes/blank_interp_edit_desc.py',
    'nodes/round_edit_desc.py',
    'nodes/decimal_edit_desc.py',
    'nodes/char_string_edit_desc.py',
    'nodes/main_program.py',
    'nodes/main_program0.py',
    'nodes/program_stmt.py',
    'nodes/end_program_stmt.py',
    'nodes/module.py',
    'nodes/module_stmt.py',
    'nodes/end_module_stmt.py',
    'nodes/module_subprogram_part.py',
    'nodes/module_subprogram.py',
    'nodes/use_stmt.py',
    'nodes/module_nature.py',
    'nodes/rename.py',
    'nodes/only.py',
    'nodes/only_use_name.py',
    'nodes/local_defined_operator.py',
    'nodes/use_defined_operator.py',
    'nodes/block_data.py',
    'nodes/block_data_stmt.py',
    'nodes/end_block_data_stmt.py',
    'nodes/interface_block.py',
    'nodes/interface_specification.py',
    'nodes/interface_stmt.py',
    'nodes/end_interface_stmt.py',
    'nodes/function_body.py',
    'nodes/subroutine_body.py',
    'nodes/interface_body.py',
    'nodes/procedure_stmt.py',
    'nodes/generic_spec.py',
    'nodes/dtio_generic_spec.py',
    'nodes/import_stmt.py',
    'nodes/external_stmt.py',
    'nodes/procedure_declaration_stmt.py',
    'nodes/proc_interface.py',
    'nodes/proc_attr_spec.py',
    'nodes/proc_decl.py',
    'nodes/interface_name.py',
    'nodes/intrinsic_stmt.py',
    'nodes/function_reference.py',
    'nodes/intrinsic_name.py',
    'nodes/intrinsic_function_reference.py',
    'nodes/call_stmt.py',
    'nodes/procedure_designator.py',
    'nodes/actual_arg_spec.py',
    'nodes/actual_arg.py',
    'nodes/alt_return_spec.py',
    'nodes/function_subprogram.py',
    'nodes/function_stmt.py',
    'nodes/proc_language_binding_spec.py',
    'nodes/dummy_arg_name.py',
    'nodes/prefix.py',
    'nodes/prefix_spec.py',
    'nodes/suffix.py',
    'nodes/end_function_stmt.py',
    'nodes/subroutine_subprogram.py',
    'nodes/subroutine_stmt.py',
    'nodes/dummy_arg.py',
    'nodes/end_subroutine_stmt.py',
    'nodes/entry_stmt.py',
    'nodes/return_stmt.py',
    'nodes/contains_stmt.py',
    'nodes/stmt_function_stmt.py',
]

for _class_file in _CLASS_FILES:
    _path = _MODULE_DIR / _class_file
    exec(compile(_path.read_text(), str(_path), "exec"), globals())

class Ac_Value_List(SequenceBase):
    subclass_names = ['Ac_Value']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Ac_Value, string)

    def __iter__(self):
        return iter(self.items)


class Access_Id_List(SequenceBase):
    subclass_names = ['Access_Id']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Access_Id, string)

    def __iter__(self):
        return iter(self.items)


class Actual_Arg_Spec_List(SequenceBase):
    subclass_names = ['Actual_Arg_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Actual_Arg_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Alloc_Opt_List(SequenceBase):
    subclass_names = ['Alloc_Opt']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Alloc_Opt, string)

    def __iter__(self):
        return iter(self.items)


class Allocate_Object_List(SequenceBase):
    subclass_names = ['Allocate_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Allocate_Object, string)

    def __iter__(self):
        return iter(self.items)


class Allocate_Shape_Spec_List(SequenceBase):
    subclass_names = ['Allocate_Shape_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Allocate_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Allocation_List(SequenceBase):
    subclass_names = ['Allocation']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Allocation, string)

    def __iter__(self):
        return iter(self.items)


class Association_List(SequenceBase):
    subclass_names = ['Association']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Association, string)

    def __iter__(self):
        return iter(self.items)


class Assumed_Shape_Spec_List(SequenceBase):
    subclass_names = ['Assumed_Shape_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Assumed_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Attr_Spec_List(SequenceBase):
    subclass_names = ['Attr_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Bind_Entity_List(SequenceBase):
    subclass_names = ['Bind_Entity']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Bind_Entity, string)

    def __iter__(self):
        return iter(self.items)


class Binding_Attr_List(SequenceBase):
    subclass_names = ['Binding_Attr']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Binding_Attr, string)

    def __iter__(self):
        return iter(self.items)


class Binding_Name_List(SequenceBase):
    subclass_names = ['Binding_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Binding_Name, string)

    def __iter__(self):
        return iter(self.items)


class Bounds_Remapping_List(SequenceBase):
    subclass_names = ['Bounds_Remapping']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Bounds_Remapping, string)

    def __iter__(self):
        return iter(self.items)


class Bounds_Spec_List(SequenceBase):
    subclass_names = ['Bounds_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Bounds_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Case_Value_Range_List(SequenceBase):
    subclass_names = ['Case_Value_Range']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Case_Value_Range, string)

    def __iter__(self):
        return iter(self.items)


class Close_Spec_List(SequenceBase):
    subclass_names = ['Close_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Close_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Common_Block_Object_List(SequenceBase):
    subclass_names = ['Common_Block_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Common_Block_Object, string)

    def __iter__(self):
        return iter(self.items)


class Component_Attr_Spec_List(SequenceBase):
    subclass_names = ['Component_Attr_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Component_Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Component_Decl_List(SequenceBase):
    subclass_names = ['Component_Decl']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Component_Decl, string)

    def __iter__(self):
        return iter(self.items)


class Component_Spec_List(SequenceBase):
    subclass_names = ['Component_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Component_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Connect_Spec_List(SequenceBase):
    subclass_names = ['Connect_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Connect_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Cray_Pointer_Decl_List(SequenceBase):
    subclass_names = ['Cray_Pointer_Decl']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Cray_Pointer_Decl, string)

    def __iter__(self):
        return iter(self.items)


class Data_I_Do_Object_List(SequenceBase):
    subclass_names = ['Data_I_Do_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Data_I_Do_Object, string)

    def __iter__(self):
        return iter(self.items)


class Data_Stmt_Object_List(SequenceBase):
    subclass_names = ['Data_Stmt_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Data_Stmt_Object, string)

    def __iter__(self):
        return iter(self.items)


class Data_Stmt_Value_List(SequenceBase):
    subclass_names = ['Data_Stmt_Value']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Data_Stmt_Value, string)

    def __iter__(self):
        return iter(self.items)


class Dealloc_Opt_List(SequenceBase):
    subclass_names = ['Dealloc_Opt']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Dealloc_Opt, string)

    def __iter__(self):
        return iter(self.items)


class Deferred_Shape_Spec_List(SequenceBase):
    subclass_names = ['Deferred_Shape_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Deferred_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Dummy_Arg_List(SequenceBase):
    subclass_names = ['Dummy_Arg']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Dummy_Arg, string)

    def __iter__(self):
        return iter(self.items)


class Dummy_Arg_Name_List(SequenceBase):
    subclass_names = ['Dummy_Arg_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Dummy_Arg_Name, string)

    def __iter__(self):
        return iter(self.items)


class Entity_Decl_List(SequenceBase):
    subclass_names = ['Entity_Decl']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Entity_Decl, string)

    def __iter__(self):
        return iter(self.items)


class Entity_Name_List(SequenceBase):
    subclass_names = ['Entity_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Entity_Name, string)

    def __iter__(self):
        return iter(self.items)


class Enumerator_List(SequenceBase):
    subclass_names = ['Enumerator']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Enumerator, string)

    def __iter__(self):
        return iter(self.items)


class Equivalence_Object_List(SequenceBase):
    subclass_names = ['Equivalence_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Equivalence_Object, string)

    def __iter__(self):
        return iter(self.items)


class Equivalence_Set_List(SequenceBase):
    subclass_names = ['Equivalence_Set']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Equivalence_Set, string)

    def __iter__(self):
        return iter(self.items)


class Explicit_Shape_Spec_List(SequenceBase):
    subclass_names = ['Explicit_Shape_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Explicit_Shape_Spec, string)

    def __iter__(self):
        return iter(self.items)


class External_Name_List(SequenceBase):
    subclass_names = ['External_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', External_Name, string)

    def __iter__(self):
        return iter(self.items)


class Final_Subroutine_Name_List(SequenceBase):
    subclass_names = ['Final_Subroutine_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Final_Subroutine_Name, string)

    def __iter__(self):
        return iter(self.items)


class Forall_Triplet_Spec_List(SequenceBase):
    subclass_names = ['Forall_Triplet_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Forall_Triplet_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Implicit_Spec_List(SequenceBase):
    subclass_names = ['Implicit_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Implicit_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Import_Name_List(SequenceBase):
    subclass_names = ['Import_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Import_Name, string)

    def __iter__(self):
        return iter(self.items)


class Input_Item_List(SequenceBase):
    subclass_names = ['Input_Item']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Input_Item, string)

    def __iter__(self):
        return iter(self.items)


class Inquire_Spec_List(SequenceBase):
    subclass_names = ['Inquire_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Inquire_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Intrinsic_Procedure_Name_List(SequenceBase):
    subclass_names = ['Intrinsic_Procedure_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Intrinsic_Procedure_Name, string)

    def __iter__(self):
        return iter(self.items)


class Io_Implied_Do_Object_List(SequenceBase):
    subclass_names = ['Io_Implied_Do_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Io_Implied_Do_Object, string)

    def __iter__(self):
        return iter(self.items)


class Label_List(SequenceBase):
    subclass_names = ['Label']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Label, string)

    def __iter__(self):
        return iter(self.items)


class Letter_Spec_List(SequenceBase):
    subclass_names = ['Letter_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Letter_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Named_Constant_Def_List(SequenceBase):
    subclass_names = ['Named_Constant_Def']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Named_Constant_Def, string)

    def __iter__(self):
        return iter(self.items)


class Namelist_Group_Object_List(SequenceBase):
    subclass_names = ['Namelist_Group_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Namelist_Group_Object, string)

    def __iter__(self):
        return iter(self.items)


class Object_Name_Deferred_Shape_Spec_List_Item_List(SequenceBase):
    subclass_names = ['Object_Name_Deferred_Shape_Spec_List_Item']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Object_Name_Deferred_Shape_Spec_List_Item, string)

    def __iter__(self):
        return iter(self.items)


class Object_Name_List(SequenceBase):
    subclass_names = ['Object_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Object_Name, string)

    def __iter__(self):
        return iter(self.items)


class Only_List(SequenceBase):
    subclass_names = ['Only']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Only, string)

    def __iter__(self):
        return iter(self.items)


class Output_Item_List(SequenceBase):
    subclass_names = ['Output_Item']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Output_Item, string)

    def __iter__(self):
        return iter(self.items)


class Pointer_Decl_List(SequenceBase):
    subclass_names = ['Pointer_Decl']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Pointer_Decl, string)

    def __iter__(self):
        return iter(self.items)


class Pointer_Object_List(SequenceBase):
    subclass_names = ['Pointer_Object']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Pointer_Object, string)

    def __iter__(self):
        return iter(self.items)


class Position_Spec_List(SequenceBase):
    subclass_names = ['Position_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Position_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Proc_Attr_Spec_List(SequenceBase):
    subclass_names = ['Proc_Attr_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Proc_Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Proc_Component_Attr_Spec_List(SequenceBase):
    subclass_names = ['Proc_Component_Attr_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Proc_Component_Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Proc_Decl_List(SequenceBase):
    subclass_names = ['Proc_Decl']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Proc_Decl, string)

    def __iter__(self):
        return iter(self.items)


class Procedure_Name_List(SequenceBase):
    subclass_names = ['Procedure_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Procedure_Name, string)

    def __iter__(self):
        return iter(self.items)


class Rename_List(SequenceBase):
    subclass_names = ['Rename']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Rename, string)

    def __iter__(self):
        return iter(self.items)


class Saved_Entity_List(SequenceBase):
    subclass_names = ['Saved_Entity']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Saved_Entity, string)

    def __iter__(self):
        return iter(self.items)


class Section_Subscript_List(SequenceBase):
    subclass_names = ['Section_Subscript']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Section_Subscript, string)

    def __iter__(self):
        return iter(self.items)


class Target_Entity_Decl_List(SequenceBase):
    subclass_names = ['Target_Entity_Decl']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Target_Entity_Decl, string)

    def __iter__(self):
        return iter(self.items)


class Type_Attr_Spec_List(SequenceBase):
    subclass_names = ['Type_Attr_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Type_Attr_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Type_Param_Decl_List(SequenceBase):
    subclass_names = ['Type_Param_Decl']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Type_Param_Decl, string)

    def __iter__(self):
        return iter(self.items)


class Type_Param_Name_List(SequenceBase):
    subclass_names = ['Type_Param_Name']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Type_Param_Name, string)

    def __iter__(self):
        return iter(self.items)


class Type_Param_Spec_List(SequenceBase):
    subclass_names = ['Type_Param_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Type_Param_Spec, string)

    def __iter__(self):
        return iter(self.items)


class V_List(SequenceBase):
    subclass_names = ['V']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', V, string)

    def __iter__(self):
        return iter(self.items)


class Wait_Spec_List(SequenceBase):
    subclass_names = ['Wait_Spec']
    use_names = []

    @staticmethod
    def match(string):
        return SequenceBase.match(r',', Wait_Spec, string)

    def __iter__(self):
        return iter(self.items)


class Arg_Name(Base):
    subclass_names = ['Name']


class Array_Name(Base):
    subclass_names = ['Name']


class Associate_Construct_Name(Base):
    subclass_names = ['Name']


class Associate_Name(Base):
    subclass_names = ['Name']


class Binding_Name(Base):
    subclass_names = ['Name']


class Block_Data_Name(Base):
    subclass_names = ['Name']


class Case_Construct_Name(Base):
    subclass_names = ['Name']


class Common_Block_Name(Base):
    subclass_names = ['Name']


class Component_Name(Base):
    subclass_names = ['Name']


class Cray_Pointee_Name(Base):
    subclass_names = ['Name']


class Cray_Pointer_Name(Base):
    subclass_names = ['Name']


class Data_Pointer_Component_Name(Base):
    subclass_names = ['Name']


class Do_Construct_Name(Base):
    subclass_names = ['Name']


class Entity_Name(Base):
    subclass_names = ['Name']


class Entry_Name(Base):
    subclass_names = ['Name']


class Forall_Construct_Name(Base):
    subclass_names = ['Name']


class Function_Name(Base):
    subclass_names = ['Name']


class Generic_Name(Base):
    subclass_names = ['Name']


class If_Construct_Name(Base):
    subclass_names = ['Name']


class Index_Name(Base):
    subclass_names = ['Name']


class Local_Name(Base):
    subclass_names = ['Name']


class Module_Name(Base):
    subclass_names = ['Name']


class Namelist_Group_Name(Base):
    subclass_names = ['Name']


class Parent_Type_Name(Base):
    subclass_names = ['Name']


class Part_Name(Base):
    subclass_names = ['Name']


class Proc_Entity_Name(Base):
    subclass_names = ['Name']


class Procedure_Component_Name(Base):
    subclass_names = ['Name']


class Procedure_Entity_Name(Base):
    subclass_names = ['Name']


class Procedure_Name(Base):
    subclass_names = ['Name']


class Program_Name(Base):
    subclass_names = ['Name']


class Result_Name(Base):
    subclass_names = ['Name']


class Scalar_Variable_Name(Base):
    subclass_names = ['Name']


class Select_Construct_Name(Base):
    subclass_names = ['Name']


class Subroutine_Name(Base):
    subclass_names = ['Name']


class Type_Param_Name(Base):
    subclass_names = ['Name']


class Use_Name(Base):
    subclass_names = ['Name']


class Where_Construct_Name(Base):
    subclass_names = ['Name']


class Scalar_Char_Constant(Base):
    subclass_names = ['Char_Constant']


class Scalar_Char_Expr(Base):
    subclass_names = ['Char_Expr']


class Scalar_Constant(Base):
    subclass_names = ['Constant']


class Scalar_Constant_Subobject(Base):
    subclass_names = ['Constant_Subobject']


class Scalar_Default_Char_Expr(Base):
    subclass_names = ['Default_Char_Expr']


class Scalar_Default_Char_Variable(Base):
    subclass_names = ['Default_Char_Variable']


class Scalar_Default_Logical_Variable(Base):
    subclass_names = ['Default_Logical_Variable']


class Scalar_Expr(Base):
    subclass_names = ['Expr']


class Scalar_Int_Constant(Base):
    subclass_names = ['Int_Constant']


class Scalar_Int_Constant_Subobject(Base):
    subclass_names = ['Int_Constant_Subobject']


class Scalar_Int_Expr(Base):
    subclass_names = ['Int_Expr']


class Scalar_Int_Initialization_Expr(Base):
    subclass_names = ['Int_Initialization_Expr']


class Scalar_Int_Literal_Constant(Base):
    subclass_names = ['Int_Literal_Constant']


class Scalar_Int_Variable(Base):
    subclass_names = ['Int_Variable']


class Scalar_Logical_Expr(Base):
    subclass_names = ['Logical_Expr']


class Scalar_Logical_Initialization_Expr(Base):
    subclass_names = ['Logical_Initialization_Expr']


class Scalar_Mask_Expr(Base):
    subclass_names = ['Mask_Expr']


class Scalar_Numeric_Expr(Base):
    subclass_names = ['Numeric_Expr']


class Scalar_Structure_Component(Base):
    subclass_names = ['Structure_Component']


DynamicImport().import_now()


# Inspect the contents of this module and list all of the classes in __all__
# for automatic documentation generation with AutoDoc.

classes = inspect.getmembers(
    sys.modules[__name__],
    lambda member: inspect.isclass(member) and member.__module__ == __name__,
)

__all__ = [name[0] for name in classes]
