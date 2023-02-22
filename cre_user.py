import os

# 读取用户名和密码信息
with open('user_info.txt') as f:
    for line in f:
        username, password = line.strip().split(':')
        
        # 新建用户
        os.system(f'useradd {username}')
        
        # 设置密码
        os.system(f'echo "{password}" | passwd {username} --stdin')
