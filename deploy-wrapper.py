#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VitePress 部署包装器脚本
用于 CI/CD 流水线中调用部署功能
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def setup_environment():
    """设置部署环境变量"""
    # 获取当前脚本目录
    current_dir = Path(__file__).parent
    deploy_dir = current_dir.parent / "vitepress-deploy-py"
    
    # 检查部署脚本目录是否存在
    if not deploy_dir.exists():
        print(f"错误: 部署脚本目录不存在: {deploy_dir}")
        sys.exit(1)
    
    # 切换到部署脚本目录
    os.chdir(deploy_dir)
    
    # 设置Python路径
    if str(deploy_dir) not in sys.path:
        sys.path.insert(0, str(deploy_dir))
    
    return deploy_dir

def validate_environment():
    """验证部署环境"""
    required_vars = [
        'SSH_HOSTNAME',
        'SSH_USERNAME', 
        'REMOTE_WEB_DIR'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"错误: 缺少必需的环境变量: {', '.join(missing_vars)}")
        print("请检查 CI/CD 系统的环境变量配置")
        return False
    
    return True

def run_deployment(args):
    """执行部署"""
    deploy_dir = setup_environment()
    
    # 验证环境变量
    if not validate_environment():
        sys.exit(1)
    
    # 构建部署命令
    cmd = ['python', 'deploy_new.py']
    
    # 添加命令行参数
    if args.validate_only:
        cmd.append('--validate-only')
    if args.no_clean:
        cmd.append('--no-clean')
    if args.no_backup:
        cmd.append('--no-backup')
    if args.force_clean:
        cmd.append('--force-clean')
    if args.skip_nginx:
        cmd.append('--skip-nginx')
    if args.dry_run:
        cmd.append('--dry-run')
    
    print(f"执行部署命令: {' '.join(cmd)}")
    print(f"工作目录: {deploy_dir}")
    
    try:
        # 执行部署脚本
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("部署成功!")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"部署失败: {e}")
        print(f"错误输出: {e.stderr}")
        return False
    except Exception as e:
        print(f"执行部署时发生错误: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='VitePress 部署包装器')
    parser.add_argument('--validate-only', action='store_true', help='仅验证配置，不执行部署')
    parser.add_argument('--no-clean', action='store_true', help='不清理远程文件')
    parser.add_argument('--no-backup', action='store_true', help='不创建备份')
    parser.add_argument('--force-clean', action='store_true', help='强制清理')
    parser.add_argument('--skip-nginx', action='store_true', help='跳过Nginx配置')
    parser.add_argument('--dry-run', action='store_true', help='模拟运行，不实际执行')
    
    args = parser.parse_args()
    
    # 打印环境信息
    print("=" * 50)
    print("VitePress 部署包装器")
    print("=" * 50)
    print(f"Python版本: {sys.version}")
    print(f"当前目录: {os.getcwd()}")
    print(f"SSH主机: {os.getenv('SSH_HOSTNAME', '未设置')}")
    print(f"SSH用户: {os.getenv('SSH_USERNAME', '未设置')}")
    print(f"远程目录: {os.getenv('REMOTE_WEB_DIR', '未设置')}")
    print("=" * 50)
    
    # 执行部署
    success = run_deployment(args)
    
    if success:
        print("\n✅ 部署完成")
        sys.exit(0)
    else:
        print("\n❌ 部署失败")
        sys.exit(1)

if __name__ == '__main__':
    main()