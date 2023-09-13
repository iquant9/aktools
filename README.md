# aktools
### create docker network
```shell
# 172.21.0.1 到 172.21.0.254
sudo docker network create --subnet=172.21.0.0/24 ak
docker network ls
```

### run akapi
```shell
docker run --platform linux/amd64  --net ak --ip 172.21.0.1 -p 8055:80 jei888/akapi:latest 
```
