#!/bin/bash
# 自动化构建和测试脚本
echo "Building project..."
gcc -o my_program main.c util.c

if [ $? -ne 0 ]; then
  echo "Build failed"
  exit 1
fi

echo "Running tests..."
./my_program

if [ $? -ne 0 ]; then
  echo "Tests failed"
  exit 1
fi

echo "Build and tests succeeded"
