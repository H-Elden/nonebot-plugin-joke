<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>
<div align="center">
  
# nonebot-plugin-joke

</div>

## 📖 介绍

笑一笑，十年少~ 看个笑话吧~

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-joke

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

**pip**

    pip install nonebot-plugin-joke

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_joke"]

</details>

## ⚙️ 配置

嘿嘿，没什么好配置的

## 🎉 使用

### 关键词触发

#### 中文笑话

关键词集合：`{"讲个笑话", "说个笑话"}`

#### 英文笑话

关键词集合：`{"讲个英文笑话", "讲个英语笑话", "说个英文笑话", "说个英语笑话"}`

## 示例图

<div align="center">
  <img src="readme_images/示例图.jpg" height="600" alt="示例图">
</div>

## 🙏鸣谢

> 使用 [夏柔API](https://api.aa1.cn/) 获取中文笑话

> 使用 [JokeAPI](https://sv443.net/jokeapi/v2/) 获取英文笑话

