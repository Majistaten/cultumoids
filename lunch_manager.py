from pathlib import Path
import image_downloader
import lunch_extractor
import image_processor
import datetime
import os

PATH = "./images"
day_menu = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": []}


def load_menu() -> None:
    print("Loading menu...")
    if not os.path.exists("menu.txt"):
        update_menu()
    with open("menu.txt", "r", encoding="utf-8") as file:
        if _get_current_week() != file.readline().strip():
            update_menu()
        file.readline()
        for day in day_menu:
            day_menu[day] = []
            while True:
                line = file.readline().strip()
                if line.startswith(tuple(day_menu.keys())):
                    continue
                if not line:
                    break
                day_menu[day].append(line)


def update_menu() -> None:
    print("Updating menu...")
    remove_images()
    image_name = image_downloader.download_image("https://restaurangcultum.se", PATH)
    image_processor.prepare_daily_images(image_name, PATH)
    for day in day_menu:
        day_menu[day] = lunch_extractor.extract_menu(f"{PATH}/{day}.png")

    with open("menu.txt", "w") as file:
        file.write(f"{_get_current_week()}\n\n")
        for day, menu in day_menu.items():
            file.write(f"{day}\n")
            for item in menu:
                file.write(f"{item}\n")
            file.write("\n")


def remove_images() -> None:
    for image in Path(PATH).glob("*.png"):
        image.unlink()


def get_menu(day: str) -> str:
    return "\n".join(day_menu[day]).replace(day, "").strip()


def _get_weekday() -> str:
    return datetime.datetime.today().strftime("%A").lower()


def get_todays_menu() -> str:
    if _get_weekday() == "saturday" or _get_weekday() == "sunday":
        return "Det är helg, ingen lunch idag!"
    return get_menu(_get_weekday())


def _get_current_week() -> str:
    return datetime.datetime.today().strftime("%W")


def get_full_menu() -> str:
    return "\n".join([get_menu(day) + "\n" for day in day_menu])
