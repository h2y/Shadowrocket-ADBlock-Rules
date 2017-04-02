## Other Rules

我一开始直接使用的是 SR 自带的规则，不过发现了以下几个问题：

1.  根本不带过滤广告功能，没发挥出代理网络的全部优势。
2.  全局默认直连，对特定黑名单网站走代理。但规则同时又设定了白名单是几个意思，这可是移动设备，对每个数据包都要进行一次判断，影响性能而且耗电，强迫症表示不能忍。

然后在网上找到了不少其他人写的规则，但我又发现了以下几个问题：

1.  规则大都是 Surge Rules，和 Shadowrocket 有一些些格式上的差异，并不完全兼容。
2.  暂时没有找到对 SR 写的拥有广告过滤的规则。\*

\* 除了 [UPlus](https://github.com/BurpSuite/UPlus-Shadowrocket) 是针对 SR 写的带广告过滤的规则，但是。。。3700+ 行的规则，这太臃肿了，耗电量会很可怕的。实际上该规则里面有超过一半是对一些黄色、赌博网站走代理的规则，而这些网站嘛，还是就让她们被墙着好了 -。-

**所以说，我还是亲自来写一个规则吧！**

## My Rule

-   默认只对 `被墙` 且 `世界前 500` 的网站进行代理。
-   在 SR 中如果将 `全局路由` 设置为 `代理`，则变为代理所有非大陆网站。\*
-   广告过滤，包括网页广告、App 广告和视频广告。
-   严格控制规则的体积，毕竟这是每次数据请求都会被运行一次的东西。
-   使用开源的力量，逐渐成为 SR 上最好用的规则！

\* 本规则默认模式应为 `配置`，如果只是需要长期地代理所有非大陆网站，本规则并不是最佳方案。

**规则地址：**<https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_adb.conf>

![扫码下载](https://cloud.githubusercontent.com/assets/12909077/17640759/d7347da8-6139-11e6-8cfb-bd8d1800343c.png)

## Related

[**gongjianhui/AppleDNS**](https://github.com/gongjianhui/AppleDNS)

Hosts 生成工具，生成 `在当前所在网络环境下` Apple 服务器的 DNS 最优解析结果，明显加快访问速度。

电脑需支持 Python，按照 Readme 运行后，将生成的 hosts 粘贴到 `Shadowrocket->Settings->DNS->Hosts` 即可。

**问题反馈**

任何问题欢迎在 [Issues](https://github.com/h2y/Shadowrocket-ADBlock-Rules/issues) 中反馈，如果没有账号可以去 [我的网站](https://hzy.pw/p/2096#comments) 中留言。


## 捐助

本项目不接受任何形式的捐助，因为自由地上网本来就是大家的权利，没有必要为此付出更多的代价。

但是，作为一个翻墙规则，不可避免的会对网站有所遗漏，需要大家来共同完善，当发现不好用的地方时，请打开 SR 的日志功能，检查一下是哪一个被墙的域名走了直连，或者是哪一个可以直连的域名走了代理。

将需要修改的信息反馈给我，大家的努力会让这个规则越来越完善！
