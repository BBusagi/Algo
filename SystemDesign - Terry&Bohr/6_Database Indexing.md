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
