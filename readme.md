## Best Proxy Rules

这里是一系列好用的翻墙规则，针对 [Shadowrocket](https://liguangming.com/Shadowrocket) 开发，支持广告过滤，使用 Python 按照一定的规则和模板定期自动生成，并且使用开源的力量，集众人之力逐渐完善。

本规则有以下特点：

- 仅对 `被墙` 且 `世界前 500` 的网站视为需要代理，所有被墙的网站太多，大多为黄赌毒，并没有必要加入此规则。
- 自动转换 `EasyList, Eaylist China, 乘风规则` 为 SR 规则，全面去除广告且保持最新。
- 也包括自定义的广告过滤规则，针对 iOS 端的网页广告、App 广告和视频广告。
- 提供多个规则文件让大家自由选择或者自由切换使用。


### 目录

- [黑名单过滤 + 广告](#黑名单过滤--广告)
- [白名单过滤 + 广告](#白名单过滤--广告)
- [黑名单过滤](#黑名单过滤)
- [白名单过滤](#白名单过滤)
- [手工规则](#手工规则)
- ~神奇~分隔符~
- [常见问题](#常见问题)
- [相关推荐](#相关推荐)
- [问题反馈](#问题反馈)
- [捐助](#捐助)


## 黑名单过滤 + 广告

黑名单中包含了境外网站中无法访问的那些，对不确定的网站则尽可能地直连。

- 代理：top500 网站中不可直连的境外网站
- 直连：境外其余网站、中国网站
- 包含广告过滤

规则地址：<https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist_ad.conf>

![](https://user-images.githubusercontent.com/12909077/27505548-db67b776-58d4-11e7-8775-ff038c8c11bf.png)

## 白名单过滤 + 广告

白名单中包含了境外网站中可以访问的那些，对不确定的网站则尽可能地代理。

- 直连：top500 网站中可直连的境外网站、中国网站
- 代理：其余的所有境外网站
- 包含广告过滤

规则地址：<https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf>

![](https://user-images.githubusercontent.com/12909077/27505553-ef1b86c6-58d4-11e7-9fb1-eafbd0c5dc81.png)

## 白名单过滤 

现在很多浏览器都自带了广告过滤功能，如果你不需要过滤 App 内置广告和视频广告，可以选择这个不带广告过滤的版本。

规则地址：<https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist.conf>

![](https://user-images.githubusercontent.com/12909077/27505552-ef108226-58d4-11e7-82eb-8558289d3953.png)

## 黑名单过滤 

现在很多浏览器都自带了广告过滤功能，如果你不需要过滤 App 内置广告和视频广告，可以选择这个不带广告过滤的版本。

规则地址：<https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist.conf>

![](https://user-images.githubusercontent.com/12909077/27505547-db64d97a-58d4-11e7-8311-538115b6faf3.png)

## 手工规则

这个规则和上面的 `黑名单 + 广告规则` 类似，但区别在于这是一个手工编写的规则，已经维护了一年多。而自动生成脚本是 2017-06 新开发的，或许还不够成熟，所以目前而言仍然强烈推荐选用此规则。

- 只对 `被墙` 且 `世界前 500` 的网站进行代理。
- 国内网站及剩余的境外网站使用直连。
- 广告过滤，包括网页广告、App 广告和视频广告。

规则地址：<https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_adb.conf>

![](https://user-images.githubusercontent.com/12909077/27505546-db64a162-58d4-11e7-8447-09148abae9aa.png)


## 常见问题

- **上千行的代理规则，会对上网速度产生影响吗？**

> 不会的。
>
> 我之前也认为这是一个每次网络数据包经过都会执行一次的规则文件，逐行匹配规则，所以需要尽可能精简。但后来和 SR 作者交流后发现这是一个误区，SR 在每次加载规则时都会生成一棵搜索树，可以理解为对主机名从后往前的有限状态机 DFA，并不是逐行匹配，并且对每次的匹配结果还有个哈希缓存。
>
> 换句话说，2000 行的规则和 50 行的规则在 SR 中均为同一量级的时间复杂度 O(1)。


## 相关推荐

[**AppleDNS**](https://github.com/gongjianhui/AppleDNS)

Hosts 生成工具，生成 `在当前所在网络环境下` Apple 服务器的 DNS 最优解析结果，加快访问速度。

电脑需支持 Python，按照 Readme 运行后，将生成的 hosts 粘贴到 `Shadowrocket->Settings->DNS->Hosts` 即可。

**<http://ip111.cn/>**

这是一个很棒的 IP 查询网站，支持同时查询你的境内境外 IP，以及谷歌 IP。

[**CloudGateRules_SR**](https://github.com/CloudGateRules/Shadowrocket)

这同样是由开源社区维护的另一款 SR 规则，大家也可以试试。


## 问题反馈

任何问题欢迎在 [Issues](https://github.com/h2y/Shadowrocket-ADBlock-Rules/issues) 中反馈，如果没有账号可以去 [我的网站](https://hzy.pw/p/2096#comments) 中留言。


## 捐助

本项目不接受任何形式的捐助，因为自由地上网本来就是大家的权利，没有必要为此付出更多的代价。

但是，作为一个翻墙规则，不可避免的会对网站有所遗漏，需要大家来共同完善，当发现不好用的地方时，请打开 SR 的日志功能，检查一下是哪一个被墙的域名走了直连，或者是哪一个可以直连的域名走了代理。

将需要修改的信息反馈给我，大家的努力会让这个规则越来越完善！
