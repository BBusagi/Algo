# Database Transactions
+ 将相关联的数据操作做为一个整体来保证运行

### ACID 
+ Atomicity 原子性
  + 要么成功 要么失败，不存在中间状态
  + 中途失败，全部回滚，WAL实现
+ Consistency 一致性
  + 数据库只能从一个合法状态转移到另一个合法状态
  + 商业逻辑上的一致性
+ Isolation 隔离性
  + 多个Transaction相互不应该干涉
+ Durability
  + 一旦commit之后就应该永久保留