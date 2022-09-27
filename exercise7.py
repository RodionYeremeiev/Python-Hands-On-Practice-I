import sched
import time
import winsound


def set_alarm(alarm_time, sound_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, winsound.PlaySound, argument=(sound_file, winsound.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    s.run()
