# Client-Server Architecture
+ C/S 是现代网络最基本的架构模式
  + Client 发送请求
  + Server 接受请求，处理逻辑，回传结果
  + 遵循Request-Response的基本通讯方式
+ 特点
  + 职责分离，C负责展示和交互，S负责商业逻辑和数据处理
  + 集中管理，数据和逻辑集中在S，C不需要关心数据
  + 多客户端支持
  + 扩展基础

## C/S
### 客户端 Client
  + 分类 浏览器、手机APP、桌面APP、其他服务（一个服务可能是另外一个服务的Client）
  + 职责 UI显示、收集输入、发送请求、接受并展示Server回应
### 服务端 Server
  + 分类 WebServer ApplicationServer Database
  + 职责 验证和授权、商业逻辑、数据库读写、结果回传
  + 通常server不是一台，而是多台服务器的集群
  
## 客户端选型
### Thin Client
+ 逻辑主要在server，client只负责显示
+ Server-Side Rendering
+ 优点 轻量、易维护、安全性⾼
+ 缺点 用户体验较慢
### Thick Client
+ C端较多逻辑，S端主要为数据
+ React/VUE等SPA
+ 优点 用户体验流程，server负担较少
+ 缺点 前端代码较复杂
+ 默认为ThickClient+RESTful API

## Peer-to-Peer (P2P)
+ 和C/S完全不同的架构
+ 节点直接通讯，去中心化
+ 优点 直接，低延迟
+ 只有在明确涉及视频/音频通话时，才会使用

## 画系统架构图的流程
1. 从Client开始 用户是什么接口使用系统
2. Server 处理请求的后端服务是什么
3. 定义API client和server之间的如何沟通
4. DataBase Server的数据存在哪儿？
5. 扩展 流量变大了怎么办