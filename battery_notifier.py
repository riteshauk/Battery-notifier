import time
import psutil
from plyer import notification

def check_battery():
    last_notified = -1

    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        print(f"Battery: {percent}%, Plugged in: {plugged}")

        # Notify when battery is high and plugged in
        if percent in {80, 85, 90, 95, 100} and plugged:
            if percent != last_notified:
                notification.notify(
                    title="Battery Notification",
                    message=f"Battery is at {percent}%. You may unplug the charger.",
                    timeout=10
                )
                last_notified = percent

        # Notify when battery is low and NOT plugged in
        elif percent in {35, 40, 45, 50} and not plugged:
            if percent != last_notified:
                notification.notify(
                    title="Battery Warning",
                    message=f"Battery is low ({percent}%). Please plug in the charger.",
                    timeout=10
                )
                last_notified = percent

        time.sleep(10)

if __name__ == "__main__":
    notification.notify(
        title="Battery Notifier",
        message="ACTIVE: Battery Notifier is now running.",
        timeout=10
    )
    check_battery()
