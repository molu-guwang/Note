#!/bin/bash
#for centos init docker
sysctl net.ipv4.ip_forward=1
echo 'net.ipv4.ip_forward = 1' >> /etc/sysctl.conf
sysctl -p
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
yum install -y yum-utils   device-mapper-persistent-data   lvm2
yum-config-manager     --add-repo     http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io
systemctl start docker
echo '{

    "registry-mirrors":["https://almtd3fa.mirror.aliyuncs.com"],
    "insecure-registries": ["121.36.168.105:10443"]

}' >> /etc/docker/daemon.json
systemctl stop docker
mkdir -p  /home/data/docker
mkdir -p /etc/systemd/system/docker.service.d/
echo " [Service]
ExecStart=
ExecStart=/usr/bin/dockerd  --graph=/home/data/docker/lib/docker " >> /etc/systemd/system/docker.service.d/devicemapper.conf
systemctl daemon-reload
systemctl restart docker
systemctl enable docker
