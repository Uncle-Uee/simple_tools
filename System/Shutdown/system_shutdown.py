"""
Created By: Ubaidullah Effendi-Emjedi

Icon By: "https://icons8.com"
"""
import os

ONE_MINUTE = 60
HOUR_IN_SECONDS = 3600


def shutdown(hours: float = 0):
    """
    Shutdown Computer
    :param hours:
    :return:
    """
    if hours <= 0.0:
        os.system(f"shutdown /s /t {ONE_MINUTE}")
        print("60 Seconds Before Shutdown!!!\n")
    else:
        time_in_seconds = int(hours * HOUR_IN_SECONDS)
        os.system(f"shutdown /s /t {time_in_seconds}")
        print("Shutdown Scheduled!\n")


def abort_shutdown():
    """
    Abort Shutdown
    :return:
    """
    os.system("shutdown /a")
    print("Operation Aborted!\n")


def runtime():
    print("""
    You are required to enter a number of hours. 
    For example, inputting 1.5 hours is equivalent to 1 and a half hours.
    To get minutes you can use fractions.
    For example, inputting 0.5 hours is equivalent to half an hour. Exactly 30minutes.
    If you input 0 hours, the PC will Shutdown in 60 seconds!
    If you enter -1 hours, a Previous Shutdown Schedule will be aborted and/or the program will end!
        """)
    try:
        hours = float(input("Enter a number of hours: "))
        if hours >= 0:
            shutdown(hours)
        else:
            abort_shutdown()
    except ValueError as error:
        print(error)
        print("Try Again!")
        runtime()

    os.system("pause")


if __name__ == "__main__":
    runtime()
