# 🐉Kalecgos

符合[OneBot](https://github.com/howmanybots/onebot)标准的Yet Another机器人框架。

Kalecgos（卡雷苟斯）是WOW的一条战五渣蓝龙。唯一一条被矮人一枪击落的守护巨龙。

**这啥？**
------

这是个**玩具**工程，目的是用最接近WOW插件的语法来完成一个带插件功能的`OneBot`机器人框架。

**再说详细点？**
------

写过WOW插件的都知道WOW插件是**事件驱动**的，插件主要就是[注册事件](https://wow.gamepedia.com/API_Frame_RegisterEvent)，然后监听事件并[调用API](https://wow.gamepedia.com/World_of_Warcraft_API)完成功能。

**所以？**
------

所以这个机器人框架的处理流程就是：

* 收到消息，根据消息类型触发事件，例如私聊信息触发事件 `CHAT_MSG_PRIVATE` ，写过WOW插件的话是不是敲熟悉的😂
* 插件通过 `Kalecgos.api.RegisterEvent` 来注册事件🤣
* 插件会接收到一个 `Event` 结构体，解包之后会有事件名称和聊天内容信息🤯
* 插件处理信息后，如果需要回复，通过 `Kalecgos.api.SendChatMessage` 发出去👌
* 不仅如此，插件还可以给自己设置作者信息，格式竟然和WOW插件的 `.toc` 差不多🤑

看一眼 `Kalecgos/plugins/test` 里面的内容就知道有多搞笑了。

**怎么用？**
------

`Kalecgos` 目前依赖以下包，装一下就好：

`pip install quart pypubsub requests`

未来会需要更多包，但现在这些就够了。

直接 `python run.py` 就搞定了，会启动在 `8888` 端口，由于是 `Quart` 框架，所以用 `hypercorn` 启动就是生产环境。

**进度：**
------
- [X] 挖坑
- [ ] 收发信息功能
- [ ] 各类事件
- [ ] 建立网页版设置项，因为做UI什么的都比不上做网页跨平台
- [ ] 撰写插件标准文档