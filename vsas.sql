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


-- python3 manage.py inspectdb > vsasApp/models.py
-- python3 manage.py inspectdb
-- python3 manage.py makemigrations
-- python3 manage.py migrate



