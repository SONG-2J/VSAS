-- 创建 用户-项目表
create table user_project(
    id integer primary key ,
    pid integer not null ,
    username text not null ,
    project_name text
);

-- 插入一些数据
insert into user_project(pid,username,project_name) values
(1001,'admin','1818可视化'),
(1002,'admin','1818情感分析');

-- 创建 用户-表表
create table user_table(
    id integer primary key ,
    tid integer not null ,
    username text not null ,
    table_name text,
    table_path text
);

-- 插入数据
insert into user_table(tid,username,table_name,table_path) values
(1001,'admin','评论-1818-1','./data/comments/1818-1.csv'),
(1002,'admin','评论-1818-2','./data/comments/1818-2.csv'),
(1003,'admin','评论-1818-3','./data/comments/1818-3.csv'),
(1004,'admin','评论-1818-4','./data/comments/1818-4.csv'),
(1005,'admin','评论-1818-5','./data/comments/1818-5.csv'),
(1006,'admin','弹幕-1818-1-14','./data/barrages/1818黄金眼弹幕_1-14.csv');

-- python3 manage.py inspectdb > vsasApp/models.py
-- python3 manage.py inspectdb
-- python3 manage.py makemigrations
-- python3 manage.py migrate



