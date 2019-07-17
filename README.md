# iOS-System-Framework-Inheritance-Relation-Brain-Map
iOS 系统框架继承关系脑图

IOS 系统Frameworks  路径位置

/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/IPhoneSimulator.sdk/System/Library/Frameworks/

目录说明

Frameworks：

1:来自IOS 系统Frameworks复制

Output：

1:使用脚本遍历系统的Frameworks生成对应库中类的继承关系

Tools：

1:iOS_system_framework_sqllitte.py : 基于某一个库生成继承关系的sqllite数据库

2:iOS_framework_to_output_file.py :工具遍历系统Frameworks，生成每个库对应的目录结构

3:start_generate_db.sh：工具开始执行批量生成所以库对应继承关系DB

4:move_db.sh：归档工具，把所以的子文件夹中的DB迁移到统一的DB目录中，方面查看

DB：

创建DB的SQL语句
```
"CREATE TABLE sys_framework(\

ID  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\

name  TEXT UNIQUE  NOT NULL,\

super_name  TEXT  NOT NULL,\

type  TEXT ,\

dome  TEXT ,\

protol  TEXT);"
```

Doc：生成图片脑图（待完成）

Brain：脑图工具做脑图（待完成）

