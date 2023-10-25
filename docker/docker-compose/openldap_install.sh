docker run -itd --name openldap --hostname openldap --env LDAP_TLS=false --env LDAP_DOMAIN="rrcc.cn"  --env LDAP_ADMIN_PASSWORD="123456"  osixia/openldap
docker run -d --privileged -p 60081:80 --name ldapadmin --link openldap:ldap-host --env LDAP_HOST=ldap-host --env LDAP_DOMAIN=dc=rrcc,dc=cn  docfactory/phpldapadmin

ldapsearch -x -H ldap://localhost -b dc=rrcc,dc=cn -D "cn=admin,dc=rrcc,dc=cn" -w 123456