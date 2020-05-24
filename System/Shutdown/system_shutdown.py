"""
Created By: Ubaidullah Effendi-Emjedi
Contributors: Hishaam Ryklief

Icon By: "https://icons8.com"
"""
import os
import re

TEN_SECONDS = 10
SIXTY_SECONDS = 60
HOUR_IN_SECONDS = 3600

HOURS_SYMBOL = 'h'
MINUTES_SYMBOL = 'm'
SECONDS_SYMBOL = 's'

ABORT_ACTION = "-a"

SPLIT_BY_SYMBOL = ':'
EMPTY_STRING = ""


def shutdown(seconds: int = 0, instruction: str = "/s"):
    os.system(f"shutdown {instruction} /t {seconds if seconds > TEN_SECONDS else SIXTY_SECONDS}")
    __seconds_to_time_string(seconds)


def abort_shutdown():
    os.system("shutdown /a")
    print("Operation Aborted!\n")


def get_shutdown_command(time_string=""):
    return time_string[:-3], time_string[-2:]


def get_total_seconds(time_string=""):
    hours, minutes, seconds = __get_hms(time_string)
    return (hours * HOUR_IN_SECONDS) + (minutes * SIXTY_SECONDS) + seconds


def validate_string(time_string=""):
    pattern = r'(\d+?(:\d|h|m|s))?((\d+?(:\d|h|m|s))|([:](\d+?(:\d|h|m|s)))*)?(\s[/]s|\s[/]r)'
    return bool(re.fullmatch(pattern=pattern, string=time_string)) or not (time_string is not EMPTY_STRING)


def __seconds_to_time_string(seconds):
    hours = int(seconds / HOUR_IN_SECONDS)
    minutes = int((seconds - (hours * HOUR_IN_SECONDS)) / SIXTY_SECONDS)
    seconds = seconds - ((hours * HOUR_IN_SECONDS) + minutes * SIXTY_SECONDS)
    time_string = f"{hours}h:{minutes}m:{seconds}s"
    print(f"Shutdown Scheduled in: {time_string}")


def __get_hms(time_string=""):
    hours = 0
    minutes = 0
    seconds = 0
    if __can_split_time_string(time_string):
        hms = __split_time_string(time_string)
        for i in range(len(hms)):
            hours += __get_hours(hms[i])
            minutes += __get_minutes(hms[i])
            seconds += __get_seconds(hms[i])
    else:
        hours += __get_hours(time_string)
        minutes += __get_minutes(time_string)
        seconds += __get_seconds(time_string)
    return hours, minutes, seconds


def __can_split_time_string(time_string=""):
    return SPLIT_BY_SYMBOL in time_string


def __split_time_string(time_string=""):
    return time_string.split(SPLIT_BY_SYMBOL)


def __get_hours(hours=""):
    return int(hours[:-1]) if HOURS_SYMBOL in hours else 0


def __get_minutes(minutes=""):
    return int(minutes[:-1]) if MINUTES_SYMBOL in minutes else 0


def __get_seconds(seconds=""):
    return int(seconds[:-1]) if SECONDS_SYMBOL in seconds else 0


def __instructions():
    print("""
        You are required to enter a time string before your computer will shutdown or restart. 
        A valid time string is made up of the following: 
        xh, where x is a value in hours, or
        xm, where x is a value in minutes, or
        xs, where x is a value in seconds or
        You can enter either one or combination of each separated by a ':'.
        Your valid time string needs to end in a '/s' (shutdown) or a '/r' (restart)
        For example, the input '1h:1m:1s /s' the computer will shutdown in 1 hour 1 min and 1 sec, which is 3661 seconds.
        If you enter -a, a Previous Schedule will be aborted and/or the program will end!
            """)


def runtime():
    __instructions()
    try:
        time_string = input("Enter a Valid Time String: ")
        if validate_string(time_string):
            time_string, instruction = get_shutdown_command(time_string)
            total_seconds = get_total_seconds(time_string)
            shutdown(total_seconds, instruction)
        elif time_string == ABORT_ACTION:
            abort_shutdown()
        else:
            runtime()
    except ValueError as error:
        print(error)
        runtime()

    os.system("pause")


if __name__ == "__main__":
    runtime()
