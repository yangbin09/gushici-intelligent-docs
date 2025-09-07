#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
部署环境验证脚本
用于快速检查部署配置是否正确
"""

import os
import sys
import subprocess
from pathlib import Path
import json

def print_header(title):
    """打印标题"""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def print_status(item, status, details=""):
    """打印状态信息"""
    status_icon = "✅" if status else "❌"
    print(f"{status_icon} {item:<30} {details}")
    return status

def check_file_exists(file_path, description):
    """检查文件是否存在"""
    path = Path(file_path)
    exists = path.exists()
    details = str(path.absolute()) if exists else "文件不存在"
    return print_status(description, exists, details)

def check_directory_structure():
    """检查目录结构"""
    print_header("目录结构检查")
    
    checks = [
        ("docs", "VitePress 文档目录"),
        ("docs/.vitepress", "VitePress 配置目录"),
        ("docs/.vitepress/config.js", "VitePress 配置文件"),
        ("docs/package.json", "前端依赖配置"),
        ("../vitepress-deploy-py", "部署脚本目录"),
        ("../vitepress-deploy-py/deploy_new.py", "主部署脚本"),
        ("../vitepress-deploy-py/requirements.txt", "Python 依赖文件"),
        ("../vitepress-deploy-py/.env", "部署环境配置"),
        ("deploy-wrapper.py", "部署包装器脚本"),
        (".env.example", "环境变量示例文件")
    ]
    
    all_passed = True
    for file_path, description in checks:
        if not check_file_exists(file_path, description):
            all_passed = False
    
    return all_passed

def check_python_environment():
    """检查 Python 环境"""
    print_header("Python 环境检查")
    
    # Python 版本
    python_version = sys.version.split()[0]
    version_ok = sys.version_info >= (3, 8)
    print_status("Python 版本", version_ok, f"v{python_version} (需要 >= 3.8)")
    
    # 检查必需的 Python 包
    required_packages = [
        "pathlib",
        "subprocess", 
        "os",
        "sys"
    ]
    
    packages_ok = True
    for package in required_packages:
        try:
            __import__(package)
            print_status(f"Python 包: {package}", True, "已安装")
        except ImportError:
            print_status(f"Python 包: {package}", False, "未安装")
            packages_ok = False
    
    return version_ok and packages_ok

def check_node_environment():
    """检查 Node.js 环境"""
    print_header("Node.js 环境检查")
    
    try:
        # 检查 Node.js
        node_result = subprocess.run(["node", "--version"], 
                                   capture_output=True, text=True)
        if node_result.returncode == 0:
            node_version = node_result.stdout.strip()
            print_status("Node.js", True, node_version)
        else:
            print_status("Node.js", False, "未安装或不可用")
            return False
    except FileNotFoundError:
        print_status("Node.js", False, "未安装")
        return False
    
    try:
        # 检查 pnpm
        pnpm_result = subprocess.run(["pnpm", "--version"], 
                                   capture_output=True, text=True)
        if pnpm_result.returncode == 0:
            pnpm_version = pnpm_result.stdout.strip()
            print_status("pnpm", True, f"v{pnpm_version}")
        else:
            print_status("pnpm", False, "未安装")
            return False
    except FileNotFoundError:
        print_status("pnpm", False, "未安装")
        return False
    
    return True

def check_environment_variables():
    """检查环境变量"""
    print_header("环境变量检查")
    
    # 读取 .env.example 获取所需变量
    env_example_path = Path(".env.example")
    required_vars = []
    
    if env_example_path.exists():
        with open(env_example_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    var_name = line.split('=')[0]
                    required_vars.append(var_name)
    
    # 检查关键环境变量
    critical_vars = [
        "SSH_HOSTNAME",
        "SSH_USERNAME", 
        "REMOTE_WEB_DIR"
    ]
    
    all_passed = True
    for var in critical_vars:
        value = os.getenv(var)
        if value:
            # 隐藏敏感信息
            display_value = "***" if "PASSWORD" in var else value
            print_status(f"环境变量: {var}", True, display_value)
        else:
            print_status(f"环境变量: {var}", False, "未设置")
            all_passed = False
    
    return all_passed

def check_deployment_config():
    """检查部署配置"""
    print_header("部署配置检查")
    
    deploy_env_path = Path("../vitepress-deploy-py/.env")
    if not deploy_env_path.exists():
        print_status("部署配置文件", False, "../vitepress-deploy-py/.env 不存在")
        return False
    
    print_status("部署配置文件", True, str(deploy_env_path.absolute()))
    
    # 尝试验证部署脚本
    try:
        result = subprocess.run([
            "python", "deploy-wrapper.py", "--validate-only"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print_status("部署脚本验证", True, "配置有效")
            return True
        else:
            print_status("部署脚本验证", False, f"验证失败: {result.stderr[:100]}")
            return False
    except subprocess.TimeoutExpired:
        print_status("部署脚本验证", False, "验证超时")
        return False
    except Exception as e:
        print_status("部署脚本验证", False, f"验证错误: {str(e)[:100]}")
        return False

def check_build_capability():
    """检查构建能力"""
    print_header("构建能力检查")
    
    # 检查是否可以安装依赖
    try:
        os.chdir("docs")
        result = subprocess.run([
            "pnpm", "install", "--dry-run"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print_status("依赖安装测试", True, "可以安装依赖")
        else:
            print_status("依赖安装测试", False, "依赖安装失败")
            return False
    except Exception as e:
        print_status("依赖安装测试", False, f"测试失败: {str(e)[:100]}")
        return False
    finally:
        os.chdir("..")
    
    return True

def generate_report(results):
    """生成验证报告"""
    print_header("验证报告")
    
    total_checks = len(results)
    passed_checks = sum(results.values())
    
    print(f"总检查项: {total_checks}")
    print(f"通过检查: {passed_checks}")
    print(f"失败检查: {total_checks - passed_checks}")
    print(f"通过率: {passed_checks/total_checks*100:.1f}%")
    
    if passed_checks == total_checks:
        print("\n🎉 所有检查都通过！部署环境配置正确。")
        return True
    else:
        print("\n⚠️  部分检查失败，请根据上述信息修复问题。")
        return False

def main():
    """主函数"""
    print("VitePress 部署环境验证工具")
    print(f"Python 版本: {sys.version}")
    print(f"工作目录: {os.getcwd()}")
    
    # 执行各项检查
    results = {
        "目录结构": check_directory_structure(),
        "Python环境": check_python_environment(),
        "Node.js环境": check_node_environment(),
        "环境变量": check_environment_variables(),
        "部署配置": check_deployment_config(),
        "构建能力": check_build_capability()
    }
    
    # 生成报告
    success = generate_report(results)
    
    # 提供建议
    if not success:
        print("\n📋 修复建议:")
        if not results["目录结构"]:
            print("- 确保项目目录结构完整")
        if not results["Python环境"]:
            print("- 安装 Python 3.8+ 版本")
        if not results["Node.js环境"]:
            print("- 安装 Node.js 和 pnpm")
        if not results["环境变量"]:
            print("- 配置必需的环境变量")
        if not results["部署配置"]:
            print("- 检查部署脚本配置")
        if not results["构建能力"]:
            print("- 检查前端依赖配置")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()