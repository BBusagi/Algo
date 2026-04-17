# API Design
+ Rest 资源导向 一次APIcall对应一个资源
+ GraphQL 查找导向 一次查找多个资源
+ gRTC 方法导向 直接调用函数或服务
+ RESRT/GraphQL适合外部API，gRTC适合内部服务间通讯

## REST
+ **一种基于HTTP的主流的架构风格**
+ 将服务器上的resource通过URI表达，并用HTTP等方法操作
### 常用操作语法
+ GET 获取 idempotent
+ POST 创建 非idempotent
+ PUT 更新 idempotent
+ PATCH 局部更新 不定
+ DELETE 删除 idempotent

### 数据传递
+ Path Parameter URL路径中标识唯一资源
+ Query Parameter 查找条件
+ Request Body 发送数据结构JSON
> JavaScript Object Notation
> 轻量级数据交换格式
> 简单、跨语言、可读性强、web高度契合

### Response回传设计
+ HTTP状态码
  + 2xx 成功
  + 3xx 重定向
  + 4xx 客户端出错
  + 5xx 服务器出错
+ Response Body 业务信息
+ Meta 协议层 L7

### 优缺点
+ 优点
  + 简单直接
  + 跨平台
  + 缓存机制完善
  + 分层架构友好
+ 缺点
  + 取太多数据
  + 取太少数据
  + 复杂操作难表达
  + 版本控制问题
  
### 面试
+ REST是API设计中的默认选型
+ 尤其适合缓存和泛用性的场景

## GraphQL
+ 客户端需要什么，服务器只回应什么
### 特征
+ 单一端点
+ 精确查找
+ 强类型
+ 单一请求跨资源

### 操作语法
+ Query 读取数据
+ Mutation 修改数据
+ Subscription 即时数据发送

### 回传格式 - JSON

### 优缺点
+ 优点
  + 客户端控制所需数据 - 避免请求过量或者不足
  + Schema强类型 - 文档与类型检测自动化
  + 一次请求多个资源 - 减少APIcall
+ 缺点
  + 服务器端实现复杂
  + Query过于灵活，导致性能瓶颈
  + Cache机制不如REST

### 面试重点
+ GraphQL 适合前端需要灵活查找，以及一次请求多种类型的场景

## gRTC
+ 隐藏网络细节，让远程方法调用近似本地调用
### 特征
+ 方法导向
+ 跨语言支持
+ 高效串行化格式
+ 双向串流

### 流程
+ 定义接口IDL
+ 产生C/S stub
+ 调用方法

### 优缺点
+ 优点
  + 调用直观
  + 高性能
  + 强类型
  + 支持串流
+ 缺点
  + 耦合性高
  + 不如REST通用
  + debug较差
  + 对外开放性较差

### 面试重点
+ 适用场景，微服务内部通讯，高性能、低延迟场景
+ 对外公开API
+ 对内服务通讯
> [ChipStack](https://www.chirpstack.io/) - gRTC通讯练习