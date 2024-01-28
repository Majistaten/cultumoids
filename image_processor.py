import cv2

def prepare_daily_images(image_path:str, path:str) -> None:
    img = cv2.imread(f'{path}/{image_path}')

    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    day_width = 780
    day_height = 512

    day_coordinates = {
        'monday': (44, 920),
        'tuesday': (850, 920),
        'wednesday': (1655, 920),
        'thursday': (427, 1470),
        'friday': (1233, 1470)
    }

    for day, coordinates in day_coordinates.items():
        x, y = coordinates
        cropped = threshold[y : y + day_height, x : x + day_width]
        cv2.imwrite(f'./{path}/{day}.png', cropped)

if __name__ == '__main__':
    prepare_daily_images('./images/Dagens%20lunch%20v.4%20-%20Restaurang%20Cultum.png')
