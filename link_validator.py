#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档链接验证和修复工具
自动检测和修复Markdown文档中的链接引用问题
"""

import os
import re
import sys
import os
import argparse
from pathlib import Path
from urllib.parse import urlparse
import requests
from typing import List, Tuple, Dict

class LinkValidator:
    def __init__(self, target_file: str, dry_run: bool = False):
        self.target_file = Path(target_file)
        self.dry_run = dry_run
        self.base_dir = self.target_file.parent
        self.fixes_count = 0
        self.total_links = 0
        self.broken_links = 0
        self.url_links = 0
        
        # Markdown链接正则表达式
        self.link_patterns = [
            # [text](url) - 普通链接
            (r'\[([^\]]+)\]\(([^\)]+)\)', 'link'),
            # ![alt](url) - 图片链接
            (r'!\[([^\]]*)\]\(([^\)]+)\)', 'image'),
            # [text]: url - 参考链接
            (r'^\s*\[([^\]]+)\]:\s*(.+)$', 'reference')
        ]
    
    def is_url(self, link: str) -> bool:
        """检查是否为URL"""
        parsed = urlparse(link)
        return bool(parsed.scheme and parsed.netloc)
    
    def is_valid_url(self, url: str) -> bool:
        """验证URL是否可访问"""
        try:
            response = requests.head(url, timeout=5, allow_redirects=True)
            return response.status_code < 400
        except:
            return False
    
    def find_file_in_project(self, filename: str) -> List[Path]:
        """在项目中查找文件"""
        # 从当前文件目录开始向上查找项目根目录
        current_dir = self.target_file.parent
        project_root = current_dir
        
        # 向上查找，直到找到包含.git或package.json的目录，或到达根目录
        while project_root.parent != project_root:
            if (project_root / '.git').exists() or (project_root / 'package.json').exists():
                break
            project_root = project_root.parent
        
        matches = []
        for root, dirs, files in os.walk(project_root):
            if filename in files:
                matches.append(Path(root) / filename)
        
        return matches
    
    def get_relative_path(self, target_path: Path) -> str:
        """获取相对路径"""
        try:
            return os.path.relpath(target_path, self.base_dir).replace('\\', '/')
        except ValueError:
            return str(target_path).replace('\\', '/')
    
    def fix_local_link(self, link: str) -> str:
        """修复本地链接"""
        # 移除锚点
        clean_link = link.split('#')[0].strip()
        anchor = '#' + link.split('#')[1] if '#' in link else ''
        
        # 跳过空链接
        if not clean_link:
            return link
        
        # URL解码处理（如%20转换为空格）
        import urllib.parse
        clean_link = urllib.parse.unquote(clean_link)
        
        # 处理VitePress绝对路径（以/docs/开头）
        if clean_link.startswith('/docs/'):
            # 这是VitePress的路由路径，检查对应的文件系统路径
            vitepress_path = clean_link[1:]  # 移除开头的/
            docs_root = self.base_dir
            while docs_root.name != 'docs' and docs_root.parent != docs_root:
                docs_root = docs_root.parent
            if docs_root.name == 'docs':
                target_path = docs_root / vitepress_path[5:]  # 移除'docs/'
            else:
                target_path = self.base_dir / vitepress_path
            
            # 检查目录或index.md文件
            if target_path.is_dir():
                index_file = target_path / 'index.md'
                if index_file.exists():
                    return link  # VitePress路径正确
            elif target_path.with_suffix('.md').exists():
                return link  # VitePress路径正确
            
            # 如果VitePress路径不存在，尝试查找正确的路径
            filename = Path(clean_link).name
            if not filename:  # 目录路径
                dirname = Path(clean_link).parts[-1] if Path(clean_link).parts else ''
                if dirname:
                    # 查找匹配的目录
                    for root, dirs, files in os.walk(docs_root if docs_root.name == 'docs' else self.base_dir):
                        if dirname in dirs:
                            found_dir = Path(root) / dirname
                            if (found_dir / 'index.md').exists():
                                rel_path = found_dir.relative_to(docs_root if docs_root.name == 'docs' else self.base_dir)
                                new_link = f"/docs/{rel_path.as_posix()}/"
                                print(f"VitePress路径修复: {link} -> {new_link}")
                                return new_link + anchor
        
        # 处理其他绝对路径（以/开头但不是/docs/）
        elif clean_link.startswith('/'):
            # 转换为相对于docs目录的路径
            docs_root = self.base_dir
            while docs_root.name != 'docs' and docs_root.parent != docs_root:
                docs_root = docs_root.parent
            if docs_root.name == 'docs':
                clean_link = clean_link[1:]  # 移除开头的/
                target_path = docs_root / clean_link
            else:
                target_path = self.base_dir / clean_link[1:]
        else:
            # 处理相对路径
            if clean_link.startswith('./'):
                clean_link = clean_link[2:]
            target_path = self.base_dir / clean_link
        
        # 如果文件存在，返回修正后的链接
        if target_path.exists():
            # 重新计算相对路径
            new_path = self.get_relative_path(target_path)
            if not new_path.startswith('./'):
                new_path = './' + new_path
            if new_path != link.split('#')[0]:
                print(f"路径标准化: {link.split('#')[0]} -> {new_path}")
                return new_path + anchor
            return link
        
        # 文件不存在，尝试查找正确的路径
        filename = Path(clean_link).name
        if filename:
            matches = self.find_file_in_project(filename)
            if matches:
                # 选择最近的匹配（路径最短的）
                try:
                    best_match = min(matches, key=lambda p: len(str(p.relative_to(self.base_dir.parent))))
                except ValueError:
                    best_match = matches[0]
                new_path = self.get_relative_path(best_match)
                # 确保使用相对路径格式
                if not new_path.startswith('./'):
                    new_path = './' + new_path
                print(f"找到文件匹配: {clean_link} -> {new_path}")
                return new_path + anchor
        
        # 如果找不到文件，标记为问题链接
        self.broken_links += 1
        print(f"警告: 找不到文件 {clean_link}")
        return link
    
    def process_links(self, content: str) -> str:
        """处理文档中的所有链接"""
        modified_content = content
        
        for pattern, link_type in self.link_patterns:
            def replace_link(match):
                text = match.group(1)
                link = match.group(2)
                self.total_links += 1
                
                # 跳过URL
                if self.is_url(link):
                    self.url_links += 1
                    return match.group(0)
                
                # 修复本地链接
                fixed_link = self.fix_local_link(link)
                if fixed_link != link:
                    self.fixes_count += 1
                    print(f"修复链接: {link} -> {fixed_link}")
                
                # 重构链接
                if link_type == 'image':
                    return f"![{text}]({fixed_link})"
                elif link_type == 'reference':
                    return f"[{text}]: {fixed_link}"
                else:  # link_type == 'link'
                    return f"[{text}]({fixed_link})"
            
            modified_content = re.sub(pattern, replace_link, modified_content, flags=re.MULTILINE)
        
        return modified_content
    
    def validate_and_fix(self):
        """验证和修复链接"""
        if not self.target_file.exists():
            print(f"错误: 文件不存在 {self.target_file}")
            return False
        
        print(f"处理文件: {self.target_file}")
        
        # 读取文件内容
        try:
            with open(self.target_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"错误: 无法读取文件 {e}")
            return False
        
        # 处理链接
        modified_content = self.process_links(content)
        
        # 保存修改
        if not self.dry_run and modified_content != content:
            try:
                with open(self.target_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"文件已更新: {self.target_file}")
            except Exception as e:
                print(f"错误: 无法写入文件 {e}")
                return False
        
        print(f"\n=== 链接验证统计 ===")
        print(f"总链接数: {self.total_links}")
        print(f"URL链接: {self.url_links}")
        print(f"本地链接: {self.total_links - self.url_links}")
        print(f"损坏链接: {self.broken_links}")
        print(f"修复链接: {self.fixes_count}")
        
        if self.broken_links > 0:
            print(f"\n警告: 发现 {self.broken_links} 个损坏的链接需要手动处理!")
        
        return True

def main():
    parser = argparse.ArgumentParser(description='文档链接验证和修复工具')
    parser.add_argument('file', help='要处理的Markdown文件路径')
    parser.add_argument('--dry-run', action='store_true', help='只检查不修改文件')
    
    args = parser.parse_args()
    
    validator = LinkValidator(args.file, args.dry_run)
    success = validator.validate_and_fix()
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()