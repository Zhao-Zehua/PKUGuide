# Author: ZhaoZh02
# Date: 2023.05.18

import os
import sys
import time
import hashlib

# 读取配置文件
def variable_reader(config_path):
    cache_path = r"\OnedriveSync"
    folder_paths = []
    with open(f"{config_path}/OnedriveSync.ini", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                try:
                    key, value = map(str.strip, line.split(":", 1))
                except ValueError:
                    key, value = map(str.strip, line.split("：", 1))
                value = value.strip("\"")
                value = value.strip("\'")
                if key == "cache_path":
                    cache_path = value + cache_path
                elif key == "folder_path":
                    folder_paths.append(value)
    return cache_path, folder_paths

# 遍历所有文件名和修改时间，生成哈希值
def hash_file(folder_paths):
    hash_str = ""
    for folder_path in folder_paths:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_time = str(os.path.getmtime(file_path))
                hash_str += file_path
                hash_str += file_time
    hash_hex = hashlib.md5(hash_str.encode("UTF-8")).hexdigest()
    return hash_hex

# 主函数
def main():
    config_path = os.path.dirname(sys.argv[0])
    cache_path, folder_paths = variable_reader(config_path)
    hash_hex = hash_file(folder_paths)
    try:
        with open(cache_path, "r", encoding = "UTF-8") as f:
            cache_hex = f.read()
    except Exception as e:
        cache_hex = ""
    if hash_hex != cache_hex:
        with open(cache_path, "w", encoding = "UTF-8") as f:
            f.write(hash_hex)
    return

if __name__ == "__main__":
    while True:
        time_start = time.time()
        main()
        time_end = time.time()
        time.sleep(60 - (time_end - time_start))
