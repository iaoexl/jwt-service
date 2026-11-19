# JWT令牌服务(JwtService)

> 在某能耗系统对接测试过程中，有用到`JWT令牌` ，原 [JwtService.java](jwt.java/JwtService.java) 脚本需要部署Java环境，且挺复杂的。如果要运行原版脚本需要加载 [java-jwt-3.4.0.jar](jwt.java/java-jwt-3.4.0.jar) 库。
> 
> [main.py](jwt.python/main.py)  脚本在Windows环境中运行、测试，适配 [python-3.10](https://www.python.org/ftp/python/3.10.0/python-3.10.0rc2-amd64.exe) 程序。运行时需要将 `config.example.ini` 重命名为 `config.example.ini`

```cmd
# 复制一份
	copy config.example.ini config.ini
# 重命名
	ren config.example.ini config.ini
```

## 需要安装PyJWT库
``` bash
pip install PyJwt
```

## notepad++ 运行python脚本
```bash
cmd /k cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & echo. & pause & exit
```

## 代码推送与镜像同步说明

本项目的代码推送流程如下：

```text
本地代码 → AtomGit → 自动镜像同步 → 腾讯云 CNB / GitHub / Gitee
```

## 你可以在这些地方找到我 (Find Me Here)

<p align="center">
  <a href="https://gitcode.com/techtest/JwtService.git" target="_blank" rel="noopener">
    <img src="images/favicon_gitcode.ico" width="18" height="18" alt="GitCode">&nbsp;GitCode
  </a>
  <span style="color: #999;">&nbsp;/&nbsp;</span>
  <a href="https://atomgit.com/techtest/JwtService.git" target="_blank" rel="noopener">&nbsp;AtomGit
  </a>
  &nbsp;&nbsp;
  <a href="https://cnb.cool/iaoexl/techtest/JwtService.git" target="_blank" rel="noopener">
    <img src="images/favicon_cnb.ico" width="18" height="18" alt="腾讯云 CNB">&nbsp;腾讯云 CNB
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/iaoexl/JwtService.git" target="_blank" rel="noopener">
    <img src="images/favicon_github.png" width="18" height="18" alt="GitHub">&nbsp;GitHub
  </a>
  &nbsp;&nbsp;
  <a href="https://gitee.com/techtest/JwtService.git" target="_blank" rel="noopener">
    <img src="images/favicon_gitee.ico" width="18" height="18" alt="Gitee">&nbsp;Gitee
  </a>
</p>

<!--
## 支持这个项目（Support This Project）

> 如果这个项目为你节省了时间，欢迎支持它的持续维护：
> 
>（If this project saves you time, consider supporting its ongoing maintenance:）

|     微信赞赏码     |       支付宝        |       支付宝红包        |
| :----------------: | :-----------------: | :-----------------: |
| <img src="images/wx.jpg" alt="赞赏码" width="200"> | <img src="images/zfb.jpg" alt="支付宝" width="200">| <img src="images/zfb_hb.jpg" alt="支付宝红包" width="200">|
-->