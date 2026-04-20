# Consistent Hashing
+ 分布式计算中，数据需要分布在N台服务器上
### 简单Hash
+ server = hash(key) % N # N = 节点数
+ 大量数据迁移导致性能问题和系统不稳定

### Consistent Hashing 运作
+ 目的是 服务器发生改变的时候，只需要搬运部分数据
  
1. Hash Ring
   + node和数据都映射到一个环中
   + 数据顺时针存储

2. 新节点加入
   + 新节点仅存储和上一个节点之间的数据

3. 节点删除
   + 原本数据转移到下一个节点处

### 虚拟节点
+ 问题
  + 数据分布不均匀
  + 节点性能不一致
+ 优点
  + 平均分布
  + 按照硬件能力
  + 弹性扩展

### 面试重点
+ 节点可能会变动，要做sharding/routing，最少数据搬动
+ 适用场景
  + Sharding for Distributed Cache （分布式缓存分片）
  + Storage sharding/routing （数据路由）
  + Sticky connections for users （用户连接粘性）
  + API Gateway / Sticky Sessions （网关会话粘性/会话保持）
  + Rate Limiting （限流）
  + Metrics / Aggregation （指标统计/数据聚合）
  + CDN/Edge Routing （CDN/边缘路由）