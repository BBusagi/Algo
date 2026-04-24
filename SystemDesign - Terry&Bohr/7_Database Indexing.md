# Database Indexing
+ 索引即目录
+ 无索引的时候，会Full Table Scan
+ 优点
  + 加快索引
  + 减少搜索成本
  + 提升排序与搜索效率，WHERE JOIN ORDERBY LIKE
+ 缺点
  + 占用额外空间
  + 写入会变慢
  + 索引太多会导致性能下降
+ 常见索引种类
  + B-Tree
  + LSM
  + Hash
  + Geospatial
  + Inverted

## B-Tree Index 平衡树索引
+ 特点
  + 平很
  + 多叉树
  + 磁盘友好
+ 数据库的主键索引、唯一索引、普通索引
  + 等值查找、范围查找、排序、前缀搜索
+ 结构包含 多个Key，子节点指针
+ 特点
  + 搜索快
  + 范围查找支持
  + 排序支持
  + 动态更新

### 缺点
+ 每次写入会造成随机磁盘IO
+ 对随机写比顺序写慢得多
+ 高并发，大量写入时，BTree效率不佳

### **B+Tree**
+ B-Tree 每个节点
+ B+Tree 仅叶节点

### 使用场景
+ B-Tree
  + PostgreDB
  + DynamoDB
+ B+Tree
  + MongoDB
  + MySQL InnoDB

## LSM Tree
+ Log-Structured Merge-tree ⽇志结构合并树
+ 通过将disk写入变为sequential writes，提示写入性能
### 流程
+ 写入先进内存→磁盘
1. MemTable
2. WAL 预写日志（Write-Ahead Log）
3. SSTable 磁盘文件（Sorted String Table）
4. Compaction 多个SSTable
5. 查找时依次查找MemTable、 Immutable MemTable、各级SSTable
   + SSTable有bloom filter、index block、block cache等加快查找

### 优缺点
+ 优点
  + 写入性能高
  + 磁盘友好
  + 支持大规模数据
+ 缺点
  + 读取开销高
  + 合并压缩开销高
  + 写放大

### 使用场景
+ 写多读少
+ 分布式KV-Store
+ 嵌入式保存引擎
+ 区块链保存层

## Hash Index
+ 适用等值查找，不适合范围查找
+ 包括Hash，Hash Table, Collision Hash
+ 计算Hash值 → 目标Bucket查找 → 回传

### 优缺点
+ 优点
  + 查找快
  + 空间利用率高
  + 插入快，直接放入bucket
+ 缺点
  + 不支持范围查找
  + 碰撞
  + 扩容成本高，bucket满时需要重新rehash

## Geospatial Index 空间索引
+ 针对二维甚至多维信息
+ 一维存储下的经纬交集索引存在性能问题 
  > 扫描数据过多 + 索引利用不充分 → 查询变慢
### Gaohash 
+ 将经纬转化为一维字符串和整数
+ 不断细分，相近的地方有相同前缀
+ 结合B-Tree 前缀和
+ Redis, MonoDB

### QuadTree
+ 递归式空间切分
+ 动态精度，只有当整个区域数据太多的时候才会继续切分
+ 需要专门的树状结构

### R-Tree (Rectangle Tree)
+ 非固定切分，弹性、可重叠矩形
+ 同一结构中处理点与大型形状
+ 空间索引的标准选择

## 各个结构比较
+ B-Tree 读取为主，范围查找(MySQL InnoDB)
+ LSM Tree 写入为主
+ Hash 精确查找(MySQL Memory, Redis, Sharding)