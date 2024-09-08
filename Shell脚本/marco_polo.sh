#保存当前目录
marco(){
	export SAVED_DIR=$(pwd)
}

#回到保存的目录
polo(){
	if [ -z "$SAVED_DIR"];then
		echo "No directory saved."
	else
		cd "$SAVED_DIR"||echo"Failed to change direcyory to $SAVED_DIR"
	fi
}
