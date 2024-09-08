counter=0
#初始化计数器

#循环脚本直至出错
while true;do
	((counter++))
	./run.sh >> output.log 2>> error.log

	if [[ $? -ne 0  ]]; then
		echo "failed after $counter runs."
		echo "Standard Output:"
		cat output.log
		echo
		echo "Standard Error:"
		cat error.log
		break
	fi
done
