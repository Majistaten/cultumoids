import re


def get_text(image_path: str) -> any:
    import easyocr

    reader = easyocr.Reader(["sv"])
    return reader.readtext(image_path)


def extract_menu(url: str) -> any:
    day_pattern = r"\b(MÅNDAG|TISDAG|ONSDAG|TORSDAG|FREDAG)\b\s?"
    date_pattern = r"\b\d{1,2}/\d{1,2}\b"
    capital_split_pattern = r"(?<!^)(?=[A-ZÅÄÖ])"
    image_text = get_text(url)
    menu = []
    for text in image_text:
        menu.append(text[-2])

    menu = " ".join(menu)
    menu = re.split(day_pattern, menu)
    menu[2] = re.sub(date_pattern, "", menu[2]).strip()
    menu = [menu[1]] + re.split(capital_split_pattern, menu.pop(2))
    return menu
