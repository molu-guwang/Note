FROM centos:7
MAINTAINER letsbim
# ADD jdk1.8.0_242 /opt/jdk8
# ENV JAVA_HOME /opt/jdk8
# ENV PATH $JAVA_HOME/bin:$PATH
# Change timezone
RUN rm -rf /etc/localtime &&ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# Install necessary tools
RUN yum install -y pcre-devel wget net-tools gcc zlib zlib-devel make openssl-devel
WORKDIR /home
# Install jdk
RUN wget https://mirrors.tuna.tsinghua.edu.cn/centos/7/os/x86_64/Packages/java-1.8.0-openjdk-1.8.0.262.b10-1.el7.x86_64.rpm \
&& yum install java-1.8.0-openjdk-1.8.0.262.b10-1.el7.x86_64.rpm -y
# Install node
RUN curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo |  tee /etc/yum.repos.d/yarn.repo\
&& yum install yarn -y \
&& npm config set sass-binary-site http://npm.taobao.org/mirrors/node-sass \
&& npm config set registry https://registry.npm.taobao.org/ \
&& npm config get \
&& npm install -g n &&n 12.16.1 \
&& npm install -g pm2 \
&& npm install -g yarn \
&& rm -rf /usr/bin/node && ln -s /usr/local/bin/node /usr/bin/

# Install Nginx
RUN wget http://nginx.org/download/nginx-1.16.1.tar.gz && tar zxvf nginx-1.16.1.tar.gz
RUN cd nginx-1.16.1 && ./configure --prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx \
--modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf \
--error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log \
--http-client-body-temp-path=/var/lib/nginx/tmp/client_body --with-ld-opt="-L /usr/local/lib" \
--http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi \
--http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi \
--pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx \
--user=nginx --group=nginx --with-file-aio --with-ipv6 --with-http_ssl_module \
--with-http_v2_module --with-http_realip_module --with-stream_ssl_preread_module \
--with-http_addition_module  \
--with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module \
--with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module \
--with-http_secure_link_module --with-http_degradation_module --with-http_slice_module \
--with-http_stub_status_module  --with-http_auth_request_module \
--with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic \
--with-stream_ssl_module   && make && make install

# ADD Nginx.conf
#COPY nginx.conf /etc/nginx/
#RUN mkdir -p /var/lib/nginx/tmp/
# Install web
#RUN mkdir -p /root/letsbim/{backstage,cloud,cloud-admin,data}
# COPY ccr-web-tenantdemo.jar  /root/letsbim/backstage/
# COPY cloud.tar.gz /root/letsbim/cloud/
# COPY cloud-admin.tar.gz /root/letsbim/cloud-admin/
#COPY start.sh /root
# Run cloud
# WORKDIR /root/letsbim/cloud/
# RUN  pm2 start npm --watch --name cloud -- run start
# Run cloud-admin
# WORKDIR /root/letsbim/cloud-admin
# RUN  pm2 start npm --watch --name cloud-admin -- run start
# Run backstage
# WORKDIR /root/letsbim/backstage/
# RUN nohup java  -jar ccr-web-tenantdemo.jar > nohup.out 2>&1  & sleep 1

#ENTRYPOINT nginx -g "daemon off;"