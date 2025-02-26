import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from datetime import datetime

# 定义要监控的文件和脚本
TARGET_FILE = 'asteroids.txt'
SCRIPT_TO_RUN = 'asteroid_convert.py'
MONITOR_DIR = r'C:\Users\用户名\AppData\Roaming\SharpCap\AnnotationCatalogs'

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # 检查是否是目标文件发生了变动
        if event.src_path.endswith(TARGET_FILE):
            self.run_script()

    def on_created(self, event):
        # 检查是否是目标文件被创建
        if event.src_path.endswith(TARGET_FILE):
            self.run_script()

    def run_script(self):
        # 打印当前日期时间
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{current_time}] {TARGET_FILE} has been changed. Running {SCRIPT_TO_RUN}...")
        
        # 运行脚本
        subprocess.run(['python', SCRIPT_TO_RUN], cwd=MONITOR_DIR)
        
        # 打印完成信息
        print(f"[{current_time}] {SCRIPT_TO_RUN} executed successfully.")

if __name__ == "__main__":
    # 设置监控的文件夹路径
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, MONITOR_DIR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()