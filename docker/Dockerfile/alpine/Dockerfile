FROM alpine
MAINTAINER moeru
WORKDIR /home/
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
&& apk update \
&& apk add -U tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& apk add bash build-base pcre pcre-dev openssl openssl-dev python2 python3 \
zlib zlib-dev git wget nodejs npm  openjdk8 \
&& npm config set sass-binary-site http://npm.taobao.org/mirrors/node-sass \
&& npm config set registry https://registry.npm.taobao.org/ \
&& npm config get \
&& npm install -g n &&n 15.5.0 \
&& npm install -g pm2 && npm install \
&& npm install -g yarn \
&& rm -rf /usr/bin/node && ln -s /usr/local/bin/node /usr/bin/ \
&& mkdir -p /root/letsy/web
WORKDIR /root/letsy/web
RUN yarn && yarn add cross-env \
&& wget http://nginx.org/download/nginx-1.16.1.tar.gz && tar zxvf nginx-1.16.1.tar.gz \
&& cd nginx-1.16.1 && ./configure --prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx \
--modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf \
--error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log \
--http-client-body-temp-path=/var/lib/nginx/tmp/client_body --with-ld-opt="-L /usr/local/lib" \
--http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi \
--http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi \
--pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx \
--user=nginx --group=nginx  --with-ipv6 --with-http_ssl_module \
--with-http_v2_module --with-http_realip_module --with-stream_ssl_preread_module \
--with-http_addition_module  \
--with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module \
--with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module \
--with-http_secure_link_module --with-http_degradation_module --with-http_slice_module \
--with-http_stub_status_module  --with-http_auth_request_module \
--with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic \
--with-stream_ssl_module   && make && make install
