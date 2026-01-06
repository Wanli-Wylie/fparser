#!/usr/bin/env python
"""
系统性对比 Fortran2003 模块的旧版本（.bak文件）和新版本（重构后的目录结构）

对比内容包括：
1. 导出的类和函数
2. 类的定义（签名、方法、属性等）
3. 类的继承关系
4. 模块级别的变量和常量
5. 导入的依赖
6. 类的数量统计
7. 类的差异（新增、删除、修改）
"""

import sys
import os
import inspect
import importlib.util
import importlib
from pathlib import Path
from typing import Dict, Set, List, Tuple, Any
from collections import defaultdict
import difflib


class ModuleComparator:
    """对比两个版本的 Fortran2003 模块"""
    
    def __init__(self, old_module_path: str, new_module_path: str):
        """
        初始化对比器
        
        Args:
            old_module_path: 旧版本模块路径（.bak文件，去掉.bak）
            new_module_path: 新版本模块路径（目录）
        """
        self.old_module_path = Path(old_module_path)
        self.new_module_path = Path(new_module_path)
        self.old_module = None
        self.new_module = None
        self.old_classes = {}
        self.new_classes = {}
        self.old_functions = {}
        self.new_functions = {}
        self.old_constants = {}
        self.new_constants = {}
        self.old_imports = set()
        self.new_imports = set()
        
    def load_old_module(self):
        """加载旧版本模块（从.bak文件）"""
        print("=" * 80)
        print("加载旧版本模块...")
        print("=" * 80)
        
        # 创建临时文件（去掉.bak）
        temp_path = self.old_module_path.parent / "Fortran2003_old_temp.py"
        try:
            # 读取.bak文件内容
            with open(self.old_module_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 修改内容以避免循环导入：注释掉 DynamicImport().import_now()
            # 这个调用会尝试导入新版本的模块
            modified_content = content.replace(
                'DynamicImport().import_now()',
                '# DynamicImport().import_now()  # 已注释以避免循环导入'
            )
            
            # 写入临时文件
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            # 动态导入模块
            spec = importlib.util.spec_from_file_location(
                "fparser.two.Fortran2003_old", temp_path
            )
            if spec is None or spec.loader is None:
                raise ImportError(f"无法加载模块: {temp_path}")
            
            # 添加到sys.path以便导入依赖
            old_sys_path = sys.path[:]
            module_dir = str(self.old_module_path.parent.parent.parent)
            if module_dir not in sys.path:
                sys.path.insert(0, module_dir)
            
            # 临时修改 sys.modules 以避免循环导入
            old_fortran2003 = sys.modules.get('fparser.two.Fortran2003')
            if 'fparser.two.Fortran2003' in sys.modules:
                del sys.modules['fparser.two.Fortran2003']
            
            try:
                self.old_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(self.old_module)
                print(f"✓ 成功加载旧版本模块: {temp_path}")
            finally:
                # 恢复 sys.modules
                if old_fortran2003 is not None:
                    sys.modules['fparser.two.Fortran2003'] = old_fortran2003
                sys.path[:] = old_sys_path
            
        except Exception as e:
            print(f"✗ 加载旧版本模块失败: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            # 清理临时文件
            if temp_path.exists():
                try:
                    temp_path.unlink()
                except:
                    pass
        
        return True
    
    def load_new_module(self):
        """加载新版本模块（从目录）"""
        print("=" * 80)
        print("加载新版本模块...")
        print("=" * 80)
        
        try:
            # 添加到sys.path
            module_dir = str(self.new_module_path.parent.parent.parent)
            if module_dir not in sys.path:
                sys.path.insert(0, module_dir)
            
            # 导入模块
            module_name = "fparser.two.Fortran2003"
            self.new_module = importlib.import_module(module_name)
            print(f"✓ 成功加载新版本模块: {module_name}")
            return True
            
        except Exception as e:
            print(f"✗ 加载新版本模块失败: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def extract_module_info(self, module, is_old: bool):
        """提取模块信息（类、函数、常量、导入等）"""
        if module is None:
            return
        
        print(f"\n提取{'旧' if is_old else '新'}版本模块信息...")
        
        # 获取所有成员
        members = inspect.getmembers(module)
        
        # 提取类
        classes = {}
        for name, obj in members:
            if inspect.isclass(obj) and obj.__module__ == module.__name__:
                classes[name] = obj
        
        # 提取函数
        functions = {}
        for name, obj in members:
            if inspect.isfunction(obj) and obj.__module__ == module.__name__:
                functions[name] = obj
        
        # 提取常量（大写字母开头的变量）
        constants = {}
        for name, obj in members:
            if not inspect.isclass(obj) and not inspect.isfunction(obj):
                if name.isupper() or name.startswith('_'):
                    constants[name] = obj
        
        # 提取导入
        imports = set()
        if hasattr(module, '__file__') and module.__file__:
            try:
                with open(module.__file__, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 简单的导入提取（可以改进）
                    import re
                    import_lines = re.findall(r'^(?:from\s+[\w.]+\s+)?import\s+([^\n]+)', content, re.MULTILINE)
                    for line in import_lines:
                        imports.update([imp.strip().split(' as ')[0].split('.')[0] 
                                       for imp in line.split(',')])
            except Exception as e:
                print(f"  警告: 无法提取导入信息: {e}")
        
        if is_old:
            self.old_classes = classes
            self.old_functions = functions
            self.old_constants = constants
            self.old_imports = imports
        else:
            self.new_classes = classes
            self.new_functions = functions
            self.new_constants = constants
            self.new_imports = imports
        
        print(f"  类数量: {len(classes)}")
        print(f"  函数数量: {len(functions)}")
        print(f"  常量数量: {len(constants)}")
        print(f"  导入数量: {len(imports)}")
    
    def compare_classes(self):
        """对比类"""
        print("\n" + "=" * 80)
        print("对比类定义")
        print("=" * 80)
        
        old_class_names = set(self.old_classes.keys())
        new_class_names = set(self.new_classes.keys())
        
        # 统计
        added_classes = new_class_names - old_class_names
        removed_classes = old_class_names - new_class_names
        common_classes = old_class_names & new_class_names
        
        print(f"\n类统计:")
        print(f"  旧版本类数量: {len(old_class_names)}")
        print(f"  新版本类数量: {len(new_class_names)}")
        print(f"  共同类数量: {len(common_classes)}")
        print(f"  新增类数量: {len(added_classes)}")
        print(f"  删除类数量: {len(removed_classes)}")
        
        # 详细对比共同类
        modified_classes = []
        unchanged_classes = []
        
        print(f"\n对比共同类 ({len(common_classes)} 个)...")
        for class_name in sorted(common_classes):
            old_cls = self.old_classes[class_name]
            new_cls = self.new_classes[class_name]
            
            # 对比类的基本信息
            old_mro = old_cls.__mro__
            new_mro = new_cls.__mro__
            
            old_methods = {name for name, _ in inspect.getmembers(old_cls, inspect.isfunction)}
            new_methods = {name for name, _ in inspect.getmembers(new_cls, inspect.isfunction)}
            
            old_attrs = {name for name, _ in inspect.getmembers(old_cls, lambda x: not inspect.isfunction(x) and not inspect.isclass(x))}
            new_attrs = {name for name, _ in inspect.getmembers(new_cls, lambda x: not inspect.isfunction(x) and not inspect.isclass(x))}
            
            # 检查是否有变化
            mro_changed = old_mro != new_mro
            methods_changed = old_methods != new_methods
            attrs_changed = old_attrs != new_attrs
            
            if mro_changed or methods_changed or attrs_changed:
                modified_classes.append({
                    'name': class_name,
                    'mro_changed': mro_changed,
                    'old_mro': old_mro,
                    'new_mro': new_mro,
                    'methods_changed': methods_changed,
                    'old_methods': old_methods,
                    'new_methods': new_methods,
                    'attrs_changed': attrs_changed,
                    'old_attrs': old_attrs,
                    'new_attrs': new_attrs,
                })
            else:
                unchanged_classes.append(class_name)
        
        # 输出结果
        if added_classes:
            print(f"\n新增类 ({len(added_classes)} 个):")
            for name in sorted(added_classes):
                print(f"  + {name}")
        
        if removed_classes:
            print(f"\n删除类 ({len(removed_classes)} 个):")
            for name in sorted(removed_classes):
                print(f"  - {name}")
        
        if modified_classes:
            print(f"\n修改的类 ({len(modified_classes)} 个):")
            for info in modified_classes[:10]:  # 只显示前10个
                print(f"\n  {info['name']}:")
                if info['mro_changed']:
                    print(f"    继承关系变化:")
                    print(f"      旧: {[c.__name__ for c in info['old_mro']]}")
                    print(f"      新: {[c.__name__ for c in info['new_mro']]}")
                if info['methods_changed']:
                    added_methods = info['new_methods'] - info['old_methods']
                    removed_methods = info['old_methods'] - info['new_methods']
                    if added_methods:
                        print(f"    新增方法: {sorted(added_methods)}")
                    if removed_methods:
                        print(f"    删除方法: {sorted(removed_methods)}")
                if info['attrs_changed']:
                    added_attrs = info['new_attrs'] - info['old_attrs']
                    removed_attrs = info['old_attrs'] - info['new_attrs']
                    if added_attrs:
                        print(f"    新增属性: {sorted(added_attrs)}")
                    if removed_attrs:
                        print(f"    删除属性: {sorted(removed_attrs)}")
            if len(modified_classes) > 10:
                print(f"  ... 还有 {len(modified_classes) - 10} 个修改的类未显示")
        
        print(f"\n未变化的类: {len(unchanged_classes)} 个")
        
        return {
            'added': added_classes,
            'removed': removed_classes,
            'modified': modified_classes,
            'unchanged': unchanged_classes,
        }
    
    def compare_functions(self):
        """对比函数"""
        print("\n" + "=" * 80)
        print("对比函数定义")
        print("=" * 80)
        
        old_func_names = set(self.old_functions.keys())
        new_func_names = set(self.new_functions.keys())
        
        added_funcs = new_func_names - old_func_names
        removed_funcs = old_func_names - new_func_names
        common_funcs = old_func_names & new_func_names
        
        print(f"\n函数统计:")
        print(f"  旧版本函数数量: {len(old_func_names)}")
        print(f"  新版本函数数量: {len(new_func_names)}")
        print(f"  共同函数数量: {len(common_funcs)}")
        print(f"  新增函数数量: {len(added_funcs)}")
        print(f"  删除函数数量: {len(removed_funcs)}")
        
        if added_funcs:
            print(f"\n新增函数:")
            for name in sorted(added_funcs):
                print(f"  + {name}")
        
        if removed_funcs:
            print(f"\n删除函数:")
            for name in sorted(removed_funcs):
                print(f"  - {name}")
        
        return {
            'added': added_funcs,
            'removed': removed_funcs,
            'common': common_funcs,
        }
    
    def compare_constants(self):
        """对比常量"""
        print("\n" + "=" * 80)
        print("对比常量")
        print("=" * 80)
        
        old_const_names = set(self.old_constants.keys())
        new_const_names = set(self.new_constants.keys())
        
        added_consts = new_const_names - old_const_names
        removed_consts = old_const_names - new_const_names
        common_consts = old_const_names & new_const_names
        
        print(f"\n常量统计:")
        print(f"  旧版本常量数量: {len(old_const_names)}")
        print(f"  新版本常量数量: {len(new_const_names)}")
        print(f"  共同常量数量: {len(common_consts)}")
        print(f"  新增常量数量: {len(added_consts)}")
        print(f"  删除常量数量: {len(removed_consts)}")
        
        # 对比共同常量的值
        changed_consts = []
        for name in common_consts:
            if self.old_constants[name] != self.new_constants[name]:
                changed_consts.append(name)
        
        if added_consts:
            print(f"\n新增常量:")
            for name in sorted(added_consts):
                print(f"  + {name} = {self.new_constants[name]}")
        
        if removed_consts:
            print(f"\n删除常量:")
            for name in sorted(removed_consts):
                print(f"  - {name} = {self.old_constants[name]}")
        
        if changed_consts:
            print(f"\n值变化的常量:")
            for name in sorted(changed_consts):
                print(f"  {name}:")
                print(f"    旧: {self.old_constants[name]}")
                print(f"    新: {self.new_constants[name]}")
        
        return {
            'added': added_consts,
            'removed': removed_consts,
            'changed': changed_consts,
            'common': common_consts,
        }
    
    def compare_imports(self):
        """对比导入"""
        print("\n" + "=" * 80)
        print("对比导入依赖")
        print("=" * 80)
        
        added_imports = self.new_imports - self.old_imports
        removed_imports = self.old_imports - self.new_imports
        common_imports = self.old_imports & self.new_imports
        
        print(f"\n导入统计:")
        print(f"  旧版本导入数量: {len(self.old_imports)}")
        print(f"  新版本导入数量: {len(self.new_imports)}")
        print(f"  共同导入数量: {len(common_imports)}")
        print(f"  新增导入数量: {len(added_imports)}")
        print(f"  删除导入数量: {len(removed_imports)}")
        
        if added_imports:
            print(f"\n新增导入:")
            for name in sorted(added_imports):
                print(f"  + {name}")
        
        if removed_imports:
            print(f"\n删除导入:")
            for name in sorted(removed_imports):
                print(f"  - {name}")
        
        return {
            'added': added_imports,
            'removed': removed_imports,
            'common': common_imports,
        }
    
    def compare_module_structure(self):
        """对比模块结构（文件组织）"""
        print("\n" + "=" * 80)
        print("对比模块结构")
        print("=" * 80)
        
        print(f"\n旧版本:")
        print(f"  文件: {self.old_module_path}")
        if self.old_module_path.exists():
            size = self.old_module_path.stat().st_size
            print(f"  大小: {size:,} 字节")
            with open(self.old_module_path, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())
            print(f"  行数: {lines:,}")
        
        print(f"\n新版本:")
        print(f"  目录: {self.new_module_path}")
        if self.new_module_path.exists():
            # 统计新版本的文件
            py_files = list(self.new_module_path.rglob("*.py"))
            total_size = sum(f.stat().st_size for f in py_files)
            total_lines = 0
            for f in py_files:
                try:
                    with open(f, 'r', encoding='utf-8') as file:
                        total_lines += len(file.readlines())
                except:
                    pass
            
            print(f"  Python文件数量: {len(py_files)}")
            print(f"  总大小: {total_size:,} 字节")
            print(f"  总行数: {total_lines:,}")
            
            # 列出主要文件
            print(f"\n  主要文件:")
            for f in sorted(py_files)[:20]:
                rel_path = f.relative_to(self.new_module_path.parent.parent.parent)
                print(f"    - {rel_path}")
            if len(py_files) > 20:
                print(f"    ... 还有 {len(py_files) - 20} 个文件")
    
    def generate_report(self, output_file: str = "fortran2003_comparison_report.txt"):
        """生成完整的对比报告"""
        print("\n" + "=" * 80)
        print("生成对比报告")
        print("=" * 80)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("Fortran2003 模块对比报告\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"旧版本: {self.old_module_path}\n")
            f.write(f"新版本: {self.new_module_path}\n\n")
            
            # 类对比
            class_result = self.compare_classes()
            f.write("\n" + "=" * 80 + "\n")
            f.write("类对比结果\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"旧版本类数量: {len(self.old_classes)}\n")
            f.write(f"新版本类数量: {len(self.new_classes)}\n")
            f.write(f"新增类: {len(class_result['added'])}\n")
            f.write(f"删除类: {len(class_result['removed'])}\n")
            f.write(f"修改类: {len(class_result['modified'])}\n")
            f.write(f"未变化类: {len(class_result['unchanged'])}\n\n")
            
            if class_result['added']:
                f.write("新增类列表:\n")
                for name in sorted(class_result['added']):
                    f.write(f"  + {name}\n")
                f.write("\n")
            
            if class_result['removed']:
                f.write("删除类列表:\n")
                for name in sorted(class_result['removed']):
                    f.write(f"  - {name}\n")
                f.write("\n")
            
            # 函数对比
            func_result = self.compare_functions()
            f.write("\n" + "=" * 80 + "\n")
            f.write("函数对比结果\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"旧版本函数数量: {len(self.old_functions)}\n")
            f.write(f"新版本函数数量: {len(self.new_functions)}\n")
            f.write(f"新增函数: {len(func_result['added'])}\n")
            f.write(f"删除函数: {len(func_result['removed'])}\n\n")
            
            # 常量对比
            const_result = self.compare_constants()
            f.write("\n" + "=" * 80 + "\n")
            f.write("常量对比结果\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"旧版本常量数量: {len(self.old_constants)}\n")
            f.write(f"新版本常量数量: {len(self.new_constants)}\n")
            f.write(f"新增常量: {len(const_result['added'])}\n")
            f.write(f"删除常量: {len(const_result['removed'])}\n")
            f.write(f"值变化常量: {len(const_result['changed'])}\n\n")
            
            # 导入对比
            import_result = self.compare_imports()
            f.write("\n" + "=" * 80 + "\n")
            f.write("导入对比结果\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"旧版本导入数量: {len(self.old_imports)}\n")
            f.write(f"新版本导入数量: {len(self.new_imports)}\n")
            f.write(f"新增导入: {len(import_result['added'])}\n")
            f.write(f"删除导入: {len(import_result['removed'])}\n\n")
        
        print(f"✓ 报告已保存到: {output_file}")
    
    def run_comparison(self):
        """运行完整的对比流程"""
        print("=" * 80)
        print("Fortran2003 模块对比工具")
        print("=" * 80)
        
        # 加载模块
        if not self.load_old_module():
            print("无法加载旧版本模块，退出")
            return False
        
        if not self.load_new_module():
            print("无法加载新版本模块，退出")
            return False
        
        # 提取信息
        self.extract_module_info(self.old_module, is_old=True)
        self.extract_module_info(self.new_module, is_old=False)
        
        # 对比
        self.compare_module_structure()
        class_result = self.compare_classes()
        func_result = self.compare_functions()
        const_result = self.compare_constants()
        import_result = self.compare_imports()
        
        # 生成报告
        self.generate_report()
        
        print("\n" + "=" * 80)
        print("对比完成！")
        print("=" * 80)
        
        return True


def main():
    """主函数"""
    # 设置路径
    script_dir = Path(__file__).parent
    old_module_path = script_dir / "src" / "fparser" / "two" / "Fortran2003.py.bak"
    new_module_path = script_dir / "src" / "fparser" / "two" / "Fortran2003"
    
    if not old_module_path.exists():
        print(f"错误: 找不到旧版本文件: {old_module_path}")
        return 1
    
    if not new_module_path.exists():
        print(f"错误: 找不到新版本目录: {new_module_path}")
        return 1
    
    # 创建对比器并运行
    comparator = ModuleComparator(old_module_path, new_module_path)
    success = comparator.run_comparison()
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

