环境准备
安装环境	Ubuntu 20.04.4 LTS
软件版本:	xl2tpd-1.3.12
注：此服务必须以root用户安装启动

服务端安装步骤
安装xl2tp、ppp

apt-get update
apt-get install ppp xl2tpd

修改xl2tpd配置文件

cp /etc/xl2tpd/xl2tpd.conf /etc/xl2tpd/xl2tpd.conf.bak

vim /etc/xl2tpd/xl2tpd.conf

;
; Sample l2tpd configuration file
;
; This example file should give you some idea of how the options for l2tpd
; should work.  The best place to look for a list of all options is in
; the source code itself, until I have the time to write better documentation :)
; Specifically, the file "file.c" contains a list of commands at the end.
;
; You most definitely don't have to spell out everything as it is done here
;
[global]
listen-addr = 0.0.0.0
port = 1701
access control = no
;auth file = /etc/xl2tpd/l2tp-secrets
;max retries = 5   #最多尝试重连次数，默认5次

debug avp = yes
debug network = yes
debug packet = yes
debug state = yes
debug tunnel = yes

; ipsec saref = no
; saref refinfo = 30

[lns default]
;;;
exclusive = no
ip range = 172.19.3.2 - 172.19.3.10  #ip地址范围
assign ip = yes
; (no) lac =
; hidden bit =
local ip = 172.19.3.1  #本机ip
; local ip range =
; length bit =
require chap = yes
require pap = no
require authentication = no
unix authentication = no
hostname = Your Hostname
ppp debug = yes
pass peer = yes
pppoptfile = /etc/ppp/options.l2tpd.lns #指定ppp配置文件
; call rws =
; tunnel rws =
; flow bits =
challenge = no
; rx bps =
; tx bps =


修改PPP配置文件

vim  /etc/ppp/options.l2tpd.lns (此文件为xl2tpd.conf指定，如果没有，vim会自动创建)

+mschap-v2
ipcp-accept-local
ipcp-accept-remote

# 分配给 LAC 的 DNS 地址
ms-dns 8.8.8.8
ms-dns 8.8.4.4

noccp
auth
mtu 1280
mru 1280
proxyarp
lcp-echo-failure 4
lcp-echo-interval 30
connect-delay 5000
name test  #这里和密钥文件的名字必须一样


添加ppp认证用户

vim /etc/ppp/chap-secrets

# Secrets for authentication using CHAP
# client	server	secret			IP addresses
test	test	test1234	*

启动服务

systemctl start xl2tpd.service

加入开机启动

/lib/systemd/systemd-sysv-install enable xl2tpd

验证服务端服务

服务日志在/var/log/syslog
tail  -200f  /var/log/syslog | grep -v  kubelet
