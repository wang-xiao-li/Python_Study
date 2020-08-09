# 分享项目 Share To Github

VCS -> Import -> Share

# 拉取项目 

也可以首页GET

VCS -> Get From -> Repository
VCS -> Get From -> Github

# Git操作
## 提交操作 commit/push

完整的两步操作
右键 -> Git -> commit 
右键 -> Git -> push

如果想一部完成
右键 -> Git -> commit/push 

## 更新操作 pull

右键 -> git -> repo -> pull 

## 更新冲突操作 merge

原理是
王玉超 A --> A --> A1 --->A1
王晓丽 A --> A ---------> A2 ---> Merge A1+A2 解决冲突，就是合并自己和云端最新代码 ---> A3

A3 就是最新的，此时 A1 王玉超再次 pull 就是最新的A3了（因为之前A2已经解决过一次冲突了，因此没必要重复解决）



