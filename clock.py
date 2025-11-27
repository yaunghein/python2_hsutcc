import sys
import time
from datetime import datetime
from functools import wraps


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished: {func.__name__}")
        return result
    return wrapper


class Timer:
    def get_current_time() -> str:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second
        milliseconds = now.microsecond // 10000
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}"

    def countdown(seconds: int) -> None:
        end_time = time.time() + seconds

        while time.time() < end_time:
            remaining = end_time - time.time()

            mins, secs = divmod(int(remaining), 60)
            hours = mins // 60
            milliseconds = int((remaining - int(remaining)) * 100)

            formatted_time = f"{hours:02d}:{mins:02d}:{secs:02d}:{milliseconds:02d}"
            print(f" {formatted_time}", end="\r")
            time.sleep(0.01)


class Watch(Timer):
    def start(self) -> None:
        while True:
            try:
                current_time = Timer.get_current_time()
                print(f" {current_time}", end="\r")
                time.sleep(0.01)
            except KeyboardInterrupt:
                print("\nReturning to menu...\n")
                break


class WorkBreakTimer(Timer):
    def run_pattern(self, pattern: tuple[int, ...]) -> None:
        work_count = sum(1 for i in range(len(pattern)) if i % 2 == 0)
        break_count = len(pattern) - work_count

        for i, seconds in enumerate(pattern):
            if i % 2 == 0:
                session = i // 2 + 1
                print(
                    f"\n\nWORK Session {session}/{work_count} - {seconds} seconds\n")
            else:
                session = i // 2 + 1
                print(
                    f"\n\nBREAK Session {session}/{break_count} - {seconds} seconds\n")

            Timer.countdown(seconds)

        print("\nAll work-break sessions completed!\n")


class TimerApp:
    def __init__(self):
        self.watch = Watch()
        self.timer = Timer()
        self.work_timer = WorkBreakTimer()

    def show_main_menu(self):
        print("=" * 48)
        print("CHOOSE YOUR MODE\n")
        print("1. Normal Watch (Current Time)")
        print("2. Timer (Countdown Timer)")
        print("3. ASCII Clock Display")
        print("4. Exit Program\n")
        print("Warning: Whoever enters invalid input is GAY 🥺!")
        print("=" * 48)

    def show_timer_menu(self):
        print("\n")
        print("=" * 48)
        print("TIMER MODES\n")
        print("1. (5,3,5,3,5,3)")
        print("2. (10,5,10)")
        print("3. Normal Timer")
        print("4. Back to Main Menu\n")
        print("Warning: Invalid input = GAY 🥺!")
        print("=" * 48)

    @log_action
    def normal_timer(self):
        seconds_input = input("\nEnter seconds to countdown: ").strip()

        if not seconds_input.isdigit():
            print("You are gay 🫵 - that's not a valid number!")
            return

        seconds = int(seconds_input)
        print(f"\nStarting countdown from {seconds} seconds...\n")
        time.sleep(1)
        self.timer.countdown(seconds)

    @log_action
    def timer_menu_router(self):
        while True:
            self.show_timer_menu()
            choice = input("\nSelect timer mode (1-4): ").strip()

            if choice == "1":
                self.work_timer.run_pattern((5, 3, 5, 3, 5, 3))

            elif choice == "2":
                self.work_timer.run_pattern((10, 5, 10))

            elif choice == "3":
                self.normal_timer()

            elif choice == "4":
                print("\nReturning to main menu...\n")
                break

            else:
                print("\nYou are gay 🫵 - Invalid timer mode!\n")
                time.sleep(1)

    def run(self):
        while True:
            try:
                self.show_main_menu()
                mode = input("\nSelect mode (1-4): ").strip()

                if mode == "1":
                    self.watch.start()

                elif mode == "2":
                    self.timer_menu_router()

                elif mode == "3":
                    print("\nASCII Clock - COMING SOON!\n")
                    time.sleep(1)

                elif mode == "4":
                    print("\n👋 Adios!\n")
                    break

                else:
                    print("\nYou are gay 🫵 - Invalid choice!\n")
                    time.sleep(2)

            except KeyboardInterrupt:
                print("\n\nAdios.\n")
                sys.exit(0)


TimerApp().run()
