#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pip install PyJwt
"""
import os, sys
import jwt
import configparser
from datetime import datetime, timedelta, timezone

class JwtService:
    def __init__(self):
        self.config = configparser.ConfigParser()
        
        # 获取可执行文件所在目录（兼容打包环境）
        current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        config_path = os.path.join(current_dir, 'config.ini')
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config.read_file(f)
        self.algorithm = None
        self.verification = None
        self.jwt_verifier = None

    def init_and_refresh(self):
        self.algorithm = self.config.get('JWT', 'algorithm')
        self.verification = {
            'iss': self.config.get('TEST', 'dwmc')
        }

    def create_token(self, dwdm, dwmc):
        payload = {
            'sub': dwdm,
            'iss': dwmc,
            'exp': datetime.now(timezone.utc) + timedelta(days=1)
        }
        secret = dwmc
        try:
            token = jwt.encode(payload, secret, algorithm=self.algorithm)
            return token
        except jwt.PyJWTError as e:
            print(f"生成 JWT 令牌时出错: {e}")
            return None

    def decode_token(self, token, dwmc):
        try:
            decoded = jwt.decode(token, dwmc, algorithms=[self.algorithm], issuer=dwmc)
            return decoded
        except jwt.ExpiredSignatureError:
            print("令牌已过期")
            return None
        except jwt.InvalidIssuerError:
            print("发行人无效")
            return None
        except jwt.InvalidTokenError:
            print("无效的令牌")
            return None


if __name__ == "__main__":
    jwt_service = JwtService()
    try:
        # 从配置文件读取测试参数
        try:
            jwt_service.init_and_refresh()
            env_dwmc = jwt_service.config.get('TEST', 'dwmc')
            env_dwdm = jwt_service.config.get('TEST', 'dwdm')
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"配置读取错误: {e}")
            exit(1)
        token = jwt_service.create_token(env_dwdm, env_dwmc)
        if token:
            print("生成的令牌:\n", token)
            decoded = jwt_service.decode_token(token, env_dwmc)
            if decoded:
                print("解码结果:\n", decoded)
    except Exception as e:
        print(f"运行时出错: {e}")
    finally:
        input("按回车键退出...")