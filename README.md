# aktools
### create docker network
```shell
# 172.21.0.1 到 172.21.0.254
sudo docker network create --subnet=172.21.0.0/24 ak
docker network ls
```

### run akapi
```shell
docker pull jei888/akapi:latest --platform linux/amd64
docker run --restart='always' -d --platform linux/amd64  --net ak --ip 172.21.0.2 -p 8055:80 jei888/akapi:latest 
# verify
curl '127.0.0.1:8055/rest?cmd=akshare.stock_zh_a_spot_em()'
curl '172.21.0.2/rest?cmd=akshare.stock_zh_a_spot_em()'
```

### run aktools
```shell
docker pull jei888/aktools:latest --platform linux/amd64
docker run -p 8066:80 jei888/aktools:latest 
# another cmd
docker run --platform linux/amd64 -p 8066:80 jei888/aktools:latest 
```