#!/bin/bash
#backup wecode_prod_db to wecode_pre_db

#clear old backup
mkdir -p /root/pro_mysql/data/backup/
mkdir -p /root/pre_mysql/data/backup/
rm  -rf /root/pro_mysql/data/backup/*
rm -rf /root/pre_mysql/data/backup/*

#backup wecode_prod_db
for backup_db in `mysql -h 172.17.12.129 -uroot -pWdMysql3306 -e "show databases;" | grep wecode_cloud_[0-9]| grep -v _00 `
do
mysqldump -h 172.17.12.129 -uroot -pWdMysql3306 --databases  $backup_db > /root/pro_mysql/data/backup/"$backup_db".sql;
done


mysqldump -h 172.17.12.129 -uroot -pWdMysql3306 --databases  wecode_operate_v2 > /root/pro_mysql/data/backup/wecode_operate_v2.sql
#mysqldump -h 172.17.12.129 -uroot -pWdMysql3306 --databases  wecode_operate > /root/pro_mysql/data/backup/wecode_operate.sql
mysqldump -h 172.17.12.129 -uroot -pWdMysql3306 --databases  wecode_cloud_base_v2  > /root/pro_mysql/data/backup/wecode_cloud_base_v2.sql
#mysqldump -h 172.17.12.129 -uroot -pWdMysql3306 --databases  wecode_cloud_base  > /root/pro_mysql/data/backup/wecode_cloud_base.sql
mysqldump -h 172.17.12.129 -uroot -pWdMysql3306 --databases  wecode_channel_v2  > /root/pro_mysql/data/backup/wecode_channel_v2.sql

#backup wecode_pre_db
for backup_db in `mysql -h 124.71.200.204 -uroot -pWdMysql3306 -e "show databases;" | grep wecode_cloud_[0-9]`
do
mysqldump -h 124.71.200.204 -uroot -pWdMysql3306 --databases  $backup_db > /root/pre_mysql/data/backup/"$backup_db".sql;
done

mysqldump -h 124.71.200.204 -uroot -pWdMysql3306 --databases  wecode_operate_v2 > /root/pre_mysql/data/backup/wecode_operate_v2.sql
#mysqldump -h 124.71.200.204 -uroot -pWdMysql3306 --databases  wecode_operate > /root/pre_mysql/data/backup/wecode_operate.sql
mysqldump -h 124.71.200.204 -uroot -pWdMysql3306 --databases  wecode_cloud_base_v2  > /root/pre_mysql/data/backup/wecode_cloud_base_v2.sql
#mysqldump -h 124.71.200.204 -uroot -pWdMysql3306 --databases  wecode_cloud_base  > /root/pre_mysql/data/backup/wecode_cloud_base.sql
mysqldump -h 124.71.200.204 -uroot -pWdMysql3306 --databases  wecode_channel_v2  > /root/pre_mysql/data/backup/wecode_channel_v2.sql


# get prod_db name
for backup_db in `mysql -h 172.17.12.129 -uroot -pWdMysql3306 -e "show databases;" | grep wecode_cloud_[0-9] | grep -v _00 `
	do
		echo $backup_db  >> backup_db_list.txt
	done

# get pre_db name
for sync_db in `mysql -h 124.71.200.204 -uroot -pWdMysql3306 -e "show databases;" | grep wecode_cloud_[0-9]`
	do
		echo  $sync_db  >> sync_db_list.txt
	done

#create db which diff prod_db from pre_db on pre_db
for diff_db in `diff sync_db_list.txt backup_db_list.txt | grep  \> | cut -d ' ' -f 2`
        do
		mysql -h 124.71.200.204 -uroot -pWdMysql3306 -e "CREATE DATABASE $diff_db CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';"
	done


#import data
for	import_db in `ls /root/pro_mysql/data/backup/ | grep -v  _00 | cut -d . -f 1`
	do
		mysql -h 124.71.200.204 -uroot -pWdMysql3306 $import_db <  /root/pro_mysql/data/backup/"$import_db".sql --default-character-set=utf8
	done

#clear file
rm -rf ./backup_db_list.txt
rm -rf ./sync_db_list.txt