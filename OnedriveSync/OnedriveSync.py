# Author: ZhaoZh02
# Date: 2023.05.19

import os
import re
import sys
import time
import hashlib

# 读取配置文件
def variable_reader(config_path):
    cache_path = ""
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
                    cache_path = value
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
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config_path = os.path.dirname(sys.argv[0])
    cache_path, folder_paths = variable_reader(config_path)
    hash_hex = hash_file(folder_paths)
    cache_hex = ""
    # 打开格式为OnedriveSync和14位数字的文件
    pattern = re.compile(r"^OnedriveSync\d{14}$")
    for file in os.listdir(cache_path):
        if pattern.match(file):
            cache_file_path = os.path.join(cache_path, file)
            with open(cache_file_path, "r", encoding = "UTF-8") as f:
                cache_hex = f.read()
            # 如果哈希值不匹配，则删除文件
            if cache_hex != hash_hex:
                os.remove(cache_file_path)
    if cache_hex != hash_hex:
        # 创建格式为OnedriveSync和14位数字的文件
        cache_file_path = os.path.join(cache_path, f"OnedriveSync{timestamp}")
        with open(cache_file_path, "w", encoding = "UTF-8") as f:
            f.write(hash_hex)
    return

if __name__ == "__main__":
    while True:
        time_start = time.time()
        main()
        time_end = time.time()
        time.sleep(60 - (time_end - time_start))
