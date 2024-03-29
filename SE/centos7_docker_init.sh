#!/bin/bash
#for centos init docker
sysctl net.ipv4.ip_forward=1
echo 'net.ipv4.ip_forward = 1' >> /etc/sysctl.conf
sysctl -p
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
curl  https://get.docker.com | bash -s docker --mirror Aliyun
yum install -y yum-utils   device-mapper-persistent-data   lvm2
yum-config-manager     --add-repo     http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io -y
systemctl start docker
echo '{

    "registry-mirrors":["https://almtd3fa.mirror.aliyuncs.com"],
    "data-root":"/home/data/docker/"


}' >> /etc/docker/daemon.json
systemctl stop docker
mkdir -p  /home/data/docker/mount
systemctl daemon-reload
systemctl restart docker
systemctl enable docker
