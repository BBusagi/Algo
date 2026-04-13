# Networking Essentials
## OSI模型 7层网络架构
+ 例 web请求
  + tcp三次握手 - 建立网络请求
  + Http get response
  + tcp四次挥手 - 拆除网络请求
+ 三个关键点
  + app开发，可以默认网络自身的可靠
  + 真实的网络请求过程会比较复杂，发生额外的延迟成本
  + 保持可连接的状态其实是消耗成本的

## 传输层
### UDP 快速而不可靠
  + 无连接 + 不可靠 + 无序 + 低延迟
  + 适合速度 > 可靠性的场景，客户可以自行处理丢包或乱序的情况
  + 自定义可靠UDP/QUIC/WebRTC

### TCP 可靠但有额外开销
  + 面向连接 + 可靠 + 有序 + 流式传输
  + 适用数据完整性的场景，即UDP之外的场景

### UDP vs TCP
  + 一般默认适用TCP，需要思考，这道题是否适用UDP
  + UDP适用场景
    + 需要低延迟
    + 允许丢包
    + 海量数据，可以接受偶尔丢包
    + 不需要web支持
  + 现代系统多为TCP+UDP
    + TCP → 控制通道（Control Plane）
    + UDP → 数据通道（Data Plane）

## 应用层
### HTTP 网络基础
  + 通常包括 请求方法，状态码，header，body
  + header一般设计为灵活，而非条件写死
  + 常用API
    + GET 请求资料 幂等
    + POST 发送资料
    + PUT 更新资料
    + PATCH 部分更新
    + DELETE 删除资料 幂等
    > 幂等 重复执行不会改变最终结果

### HTTPS Http加上安全层(TLS/SSL)
> HTTPS 传输过程安全，但是无法保证业务身份
> 需要进行认证和授权
> 认证（Authentication）是否是合法身份
> 授权（Authorization）是否是合法操作

### 常用网络API范式 
+ REST GraphQL gRPC

### REST 简单且灵活
  + 原则是讲客户端操作转化为resource资源的操作
  + 默认的API接口设计