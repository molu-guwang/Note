#!/bin/bash
#:Filename      :deployJar
#:Date          :2018-05-24
#:Author        :DengDefei
#:Description   :为部署Jar环境行方便, command:'curl -fsSL http://config.codelogger.org/shell/deployJar.sh | bash -s -- -t/home/bzwq/app.jar -p8080 -a-Xmx256m\ -Xms128m -l'

_TARGET=""
_DIRECTORY=""
_NAME=""
_DEBUG=""
_PORT=""
_LOG=
_LOG_FILE=""
_STOP=
_PID=
_COMMAND=
_ARGUMENTS=""
_LOG_DIR=


JAR_FILE='/home/wecode/cct/cct-web-202107.jar'
RUN_JAR_PARAMS='--spring.profiles.active=test -d64 -server'
LOG_FILE='/dev/null'

while getopts "a:d:t:p:x:s:l:f:h" opt; do
  case $opt in
  	a)
			_ARGUMENTS=" $OPTARG"
		;;
		d)
			_DEBUG=" $OPTARG"
		;;
  	t)
			_TARGET="$OPTARG"
			_DIRECTORY=$(dirname $OPTARG)"/"
			_NAME=$(echo $(basename $OPTARG) | cut -f 1 -d '.')
		;;
    p)
    	_PORT=$OPTARG
     	;;
    l)
			_LOG=true
		;;
		f)
			_LOG=true
			if [ "$OPTARG" != "" ]; then
				_LOG_FILE=$OPTARG
			fi
			;;
	s)
		_STOP=true
		;;

	h)
		_HELP_FORMAT="%-4s %-80s\n"
		printf "$_HELP_FORMAT" "参数" "描述"
		printf "$_HELP_FORMAT" "-t" "jar包绝对地址, 如: '-t/home/bzwq/test.jar'"
		printf "$_HELP_FORMAT" "-p" "jar包占用端口, 如: '-p7777'"
		printf "$_HELP_FORMAT" "-a" "自定义参数, 如: '-a-DenableSecurity=true\ -Dtoken=xxxx'"
		printf "$_HELP_FORMAT" "-l" "开启日志输出，不指定该参数则不输出日志. 日志默认输出到目标jar包相同目录下的同文件名.log"
		printf "$_HELP_FORMAT" "-f" "强制开启日志输出，指定参数为'-f/var/log/test.log',则输出到/var/log/test.log文件"
		printf "$_HELP_FORMAT" "-s" "强制关闭目标程序(不会启动目标文件)，默认按端口，次之按文件"
		exit
		;;
  esac
done


function getPidByPort {
	if [ -f "/usr/sbin/lsof" ]; then
		echo `/usr/sbin/lsof -i:"$1" | grep LISTEN | awk '{ print $2}'`
	else
		echo `/usr/bin/lsof -i:"$1" | grep LISTEN | awk '{ print $2}'`
	fi
}
function getPidByFile {
	echo `ps aux | grep \\\\-jar | grep $1 | awk '{ print $2}'`
}
function getPid {
	if [ "$_PORT" == "" ]; then
		if [ ! "$_NAME" == "" ]; then
			_PID=`getPidByFile "$_TARGET"`
		fi
	else
		_PID=`getPidByPort $_PORT`
	fi
}


getPid
if [[ $_PID =~ ^[0-9]+$ ]]; then
	echo "kill process $_PID"
	kill $_PID;
	echo "sleep 5 seconds"
	sleep 5
	getPid
	if [[ $_PID =~ ^[0-9]+$ ]]; then
		kill -9 $_PID
		sleep 1
	fi
fi

if [ $_STOP ]; then
	getPid
	if [[ $_PID =~ ^[0-9]+$ ]]; then
		echo "无法关闭进程:$_PORT"
	else
		echo "已经关闭指定程序进程"
	fi
	exit
fi

if [ "$_NAME" == "" ]; then
	echo "请指定需要启动的jar包的绝对地址，如: -t/home/test.jar"
	exit
fi

if [ $_LOG ]; then
	if [ "$_LOG_FILE" = "" ]; then
		_LOG_FILE="$_DIRECTORY$_NAME.log"
	else
		mkdir -p "$(dirname $_LOG_FILE)"
	fi
fi
echo "日志文件:$_LOG_FILE"

_DATE=$(date +%Y%m%d%H%M)
echo "DATE=$_DATE"

_JAR_FILE=${_TARGET##*/}
echo "_JAR_FILE=$_JAR_FILE"
_TMP_DIR="${_DIRECTORY}tmp/"
_JAR_BAK_DIR="${_DIRECTORY}bak/"
if [ ! -d "${_JAR_BAK_DIR}" ]; then
  mkdir -p "${_JAR_BAK_DIR}"
fi
echo "_TMP_DIR:$_TMP_DIR"
/bin/cp "$_TARGET" "${_JAR_BAK_DIR}${_JAR_FILE}.${_DATE}.bak"
/bin/cp "$_TMP_DIR$_JAR_FILE" "$_TARGET"

source /etc/profile
_COMMAND="nohup java -jar $_DEBUG $_TARGET $_ARGUMENTS > $_LOG_FILE 2>&1 &"
echo "正在执行:$_COMMAND"
eval $_COMMAND
echo "执行成功"



bash /home/wecode/deployJar.sh '-t/home/wecode/cct/cct-web-202107.jar' '-a--spring.profiles.active=test -d64 -server' '-f/dev/null'

"nohup java -jar  /home/wecode/cct/cct-web-202107.jar --spring.profiles.active=test -d64 -server > /dev/null 2>&1 &"