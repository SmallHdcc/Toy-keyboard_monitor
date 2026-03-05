from pynput import keyboard
import time
from threading import Thread


class KeyMonitor:
    def __init__(self):
        self.keys = {}
        self.running = True

    def on_press(self, key):
        if key in self.keys:
            self.keys[key] += 1
        else:
            self.keys[key] = 1

    def record(self):
        while self.running:
            time.sleep(10)
            for k, v in self.keys.items():
                print(f"键:{k},次数:{v}")

    def start(self):
        Thread(target=self.record, daemon=True).start()
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    print("键盘监控启动...")
    monitor = KeyMonitor()
    monitor.start()
