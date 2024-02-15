
from PIL import Image
import cv2
import pygame

BLACK_COLOR = (17, 10, 14)
WHITE_COLOR = (242, 228, 220)
GRID_COLOR = (3, 7, 40)
BOARD_COLOR = (232, 165, 68)
width = 800
height = 800
TILE_SIZE = 20
GRID_WIDTH = (width // TILE_SIZE)
GRID_HEIGHT = (height // TILE_SIZE)
video_path = r"C:\Users\Nora\OneDrive\Bureau\bad_apple.mp4"

pygame.init()
pygame.display.set_caption('GO GAME')
colors = [BLACK_COLOR, WHITE_COLOR]

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def draw_board(image, colors):
    resized_image = resize(image)
    pixels = resized_image.getdata()

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, GRID_COLOR, (0, row * TILE_SIZE), (width, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, GRID_COLOR, (col * TILE_SIZE, 0), (col * TILE_SIZE, height))

    i = 0
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if row != 0 and col != 0:
                pygame.draw.circle(screen, colors[0], (col * TILE_SIZE, row * TILE_SIZE),TILE_SIZE // 2)
                pygame.draw.circle(screen, colors[pixels[i] // 150], (col * TILE_SIZE, row * TILE_SIZE),TILE_SIZE // 2-1)
                i += 1


def resize(image, width=GRID_WIDTH, height=GRID_HEIGHT):
    resized_image = image.resize((width-1, height-1)).convert('L')
    resized_image.save('test.jpg')

    return resized_image




def main():
    cam = cv2.VideoCapture(video_path)
    running = True
    pygame.init()

    while running:
        clock.tick(30)
        ret, frame = cam.read()

        if not ret:
            break

        cv2.imshow("frame", frame)
        draw_board(Image.fromarray(frame), colors)
        cv2.waitKey(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        screen.fill(BOARD_COLOR)

    cam.release()
    cv2.destroyAllWindows()
    pygame.quit()


if __name__ == "__main__":
    main()