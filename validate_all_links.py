#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量链接验证工具
检查项目中所有Markdown文件的链接
"""

import os
import sys
from pathlib import Path
from link_validator import LinkValidator

def find_markdown_files(directory: Path) -> list:
    """查找目录中的所有Markdown文件"""
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        # 跳过隐藏目录和node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(Path(root) / file)
    
    return markdown_files

def main():
    # 获取项目根目录
    project_root = Path.cwd()
    if (project_root / 'docs').exists():
        docs_dir = project_root / 'docs'
    else:
        docs_dir = project_root
    
    print(f"扫描目录: {docs_dir}")
    
    # 查找所有Markdown文件
    markdown_files = find_markdown_files(docs_dir)
    print(f"找到 {len(markdown_files)} 个Markdown文件")
    
    total_files = 0
    total_links = 0
    total_broken = 0
    total_fixed = 0
    files_with_issues = []
    
    # 验证每个文件
    for md_file in markdown_files:
        print(f"\n{'='*60}")
        validator = LinkValidator(str(md_file), dry_run=True)
        validator.validate_and_fix()
        
        total_files += 1
        total_links += validator.total_links
        total_broken += validator.broken_links
        total_fixed += validator.fixes_count
        
        if validator.broken_links > 0:
            files_with_issues.append((md_file, validator.broken_links))
    
    # 总结报告
    print(f"\n{'='*60}")
    print(f"=== 批量验证总结 ===")
    print(f"检查文件数: {total_files}")
    print(f"总链接数: {total_links}")
    print(f"损坏链接数: {total_broken}")
    print(f"可修复链接数: {total_fixed}")
    
    if files_with_issues:
        print(f"\n有问题的文件:")
        for file_path, broken_count in files_with_issues:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}: {broken_count} 个损坏链接")
    else:
        print("\n✅ 所有链接都正常!")
    
    return 0 if total_broken == 0 else 1

if __name__ == '__main__':
    sys.exit(main())