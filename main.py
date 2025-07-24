from update_checker import is_update_available
from notifier import show_update_popup

def main():
    print("Checking for updates...")
    if is_update_available():
        show_update_popup()
    else:
        print("Your app is up to date.")

if __name__ == "__main__":
    main()

