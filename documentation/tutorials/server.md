---
title: Server
---

# Setup

#TODO

# Running

1. Start [AWS](https://aws.amazon.com/) instance
2. Copy public URL
3. Open terminal and SSH into instance with key
   `ssh -i /path/to/private_key user@hostname`
   Currently user is Ubuntu, host name is the copied public URL of the instance
4. Start tmux
5. Start KGQA pipeline
	1. `cd Model Reporting/KGQA`
	2. `conda activate model-reporting-3.12`
	3. `python word_embedding/server.py 127.0.0.1 9600`
	4. Wait until ![[server#^ed6a25]]
	5. New tmux tab
	6. `cd Model Reporting/KGQA/src`
	7. `conda activate model-reporting-3.12`
	8. `python -m kgqan.server`
	9. Wait until ![[server#^3e8c81]]
	10. New tmux tab
6. Start RDF endpoint
	1. `cd Model Reporting/Local ORKG Endpoint`
	2. `./start-14.02.2023.sh`
	3. Output should look like ![[server#^d93ad6]]
7. Start Flask app if not running, elif running but not working properly restart

---
```
Done loading
testing word-embedding functionality
0.0003914930000560302
listening on ('0.0.0.0', 9600)
```
^ed6a25

```
logger.py - log_info - line 39 - INFO - Server started http://0.0.0.0:8898
```
^3e8c81

```
12:23:48 INFO  Server          :: Running in read-only mode for /orkg-14.02.2023
12:23:48 INFO  Server          :: Apache Jena Fuseki 5.0.0
12:23:49 INFO  Config          :: FUSEKI_HOME=/opt/apache-jena-fuseki-5.0.0
12:23:49 INFO  Config          :: FUSEKI_BASE=/home/ubuntu/Model Reporting/Local ORKG Endpoint/run
12:23:49 INFO  Config          :: Shiro file: file:///home/ubuntu/Model Reporting/Local ORKG Endpoint/run/shiro.ini
12:23:49 INFO  Config          :: Template file: templates/config-tdb2-dir-readonly
12:23:50 INFO  Server          :: Database: TDB2 dataset: location=data-14.02.2023
12:23:50 INFO  Server          :: Path = /orkg-14.02.2023
12:23:50 INFO  Server          ::   Memory: 4.0 GiB
12:23:50 INFO  Server          ::   Java:   17.0.12
12:23:50 INFO  Server          ::   OS:     Linux 6.5.0-1023-aws amd64
12:23:50 INFO  Server          ::   PID:    2513
12:23:50 INFO  Server          :: Started 2024/12/11 12:23:50 UTC on port 3030
```

^d93ad6
