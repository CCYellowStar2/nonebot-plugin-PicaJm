<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-PicaJm

_✨ 在bot上查询和发送jm和哔咔本子 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/nonebot-plugin-PicaJm.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-PicaJm">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-PicaJm.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>


## 📖 介绍

可以让你在bot上查询jm和哔咔并打包压缩包下载，其中哔咔功能由于api本身很不稳定，所以有时候要重试好多遍才能用，可以只用jm功能

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-PicaJm

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-PicaJm
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-PicaJm
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-PicaJm
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-PicaJm
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_PicaJm"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| pica_account | 是 | 无 | 哔咔账号 |
| pica_password | 是 | 无 | 哔咔密码 |
| SYSTEM_PROXY | 是 | 无 | 本地代理 |
| zip_ispwd | 否 | True | 是否开启压缩包密码 |
| zip_password | 否 | 1919810 | 压缩包密码 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| jmxxxxxx(jm号) + 章节数(可选) | 群员 | 否 | 群聊 | 识别禁漫号发送本子 |
| 搜jm + 关键字 | 群员 | 否 | 群聊 | 返回符合的jm本子信息列表 |
| 搜pica + 关键字 | 群员 | 否 | 群聊 | 返回符合的哔咔本子信息列表 |
| 分区搜 + 分区 + 关键字 | 群员 | 否 | 群聊 | 返回指定分区下的哔咔本子信息列表 |
| 随机本子 | 群员 | 否 | 群聊 | 返回哔咔随机本子信息并发送 |
| 我的收藏 + 页数(默认第一页) | 群员 | 否 | 群聊 | 返回我的哔咔收藏下的本子信息 |
| 哔咔收藏 + 漫画id | 群员 | 否 | 群聊 | 收藏这个id的本子，反之取消 |
| 哔咔排行 + 排序模式(H24, D7, D30)(默认H24也就是日榜) | 群员 | 否 | 群聊 | 返回哔咔排行榜下的本子信息 |
| 清理哔咔缓存 | 主人 | 否 | 群聊 | 清理哔咔缓存的所有文件 |
| 检查哔咔 | 主人 | 否 | 群聊 | 检查哔咔并重新登录 |
### 效果图
![image](https://github.com/user-attachments/assets/39ff4383-cf90-44dd-b0a8-39f76eb98b69)  
![image](https://github.com/user-attachments/assets/f7976497-94c5-44cb-83ed-545797ced439)


