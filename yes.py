import sdl2
import sdl2.ext
import random
import math

# Constants
WIDTH, HEIGHT = 640, 480
MAP_SIZE = 20
FOV = math.pi / 3  # 60 degrees field of view
HALF_FOV = FOV / 2
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = 8

# Simple maze generation
def generate_maze(size):
    maze = [[1 for _ in range(size)] for _ in range(size)]
    # Create a simple room with walls
    for i in range(1, size-1):
        for j in range(1, size-1):
            maze[i][j] = 0
    maze[size-2][size-2] = 2  # Exit point

    # Print the maze for debugging
    print("Generated Maze:")
    for row in maze:
        print(''.join(['#' if cell == 1 else 'E' if cell == 2 else ' ' for cell in row]))

    return maze

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0

    def move(self, dx, dy, maze):
        new_x = self.x + dx * math.cos(self.angle) - dy * math.sin(self.angle)
        new_y = self.y + dx * math.sin(self.angle) + dy * math.cos(self.angle)

        # Collision detection with walls
        if maze[int(new_y)][int(new_x)] == 0:  # Check if the new position is not a wall
            self.x, self.y = new_x, new_y

    def rotate(self, angle):
        self.angle += angle

# Raycasting function
def cast_rays(player, maze):
    rays = []
    start_angle = player.angle - HALF_FOV

    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            target_x = player.x - math.sin(start_angle) * depth
            target_y = player.y + math.cos(start_angle) * depth

            col = int(target_x)
            row = int(target_y)

            # Add bounds checking
            if row < 0 or row >= MAP_SIZE or col < 0 or col >= MAP_SIZE:
                rays.append((depth, ray, start_angle))
                break

            # Ray hit a wall
            if maze[row][col] == 1:
                rays.append((depth, ray, start_angle))
                break

        start_angle += STEP_ANGLE

    return rays

# Main game class
class Game:
    def __init__(self):
        print("Initializing game...")
        sdl2.ext.init()
        self.window = sdl2.ext.Window("The Maze", size=(WIDTH, HEIGHT))
        self.window.show()
        self.renderer = sdl2.ext.Renderer(self.window)
        self.maze = generate_maze(MAP_SIZE)
        self.player = Player(1.5, 1.5)  # Start player near the top-left corner

    def handle_events(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                return False
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    self.player.move(0.1, 0, self.maze)
                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    self.player.move(-0.1, 0, self.maze)
                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    self.player.rotate(-0.1)
                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    self.player.rotate(0.1)
        return True

    def update(self):
        # Check victory condition
        if self.check_victory():
            print("You Win!")
            sdl2.ext.quit()
            exit()

    def check_victory(self):
        exit_x, exit_y = MAP_SIZE - 2, MAP_SIZE - 2  # Example exit location
        if int(self.player.x) == exit_x and int(self.player.y) == exit_y:
            return True
        return False

    def render_minimap(self):
        for row in range(MAP_SIZE):
            for col in range(MAP_SIZE):
                color = sdl2.ext.Color(255, 255, 255) if self.maze[row][col] == 1 else sdl2.ext.Color(0, 0, 0)
                if self.maze[row][col] == 2:  # Exit
                    color = sdl2.ext.Color(0, 255, 0)
                self.renderer.fill((col * 5, row * 5, 5, 5), color)
        # Draw player on minimap
        self.renderer.fill((int(self.player.x * 5), int(self.player.y * 5), 5, 5), sdl2.ext.Color(255, 0, 0))

    def render(self):
        self.renderer.clear(sdl2.ext.Color(0, 0, 0))  # Clear with black
        
        # Raycasting for 3D view
        rays = cast_rays(self.player, self.maze)
        for ray in rays:
            depth, column, angle = ray
            wall_height = HEIGHT / (depth * math.cos(angle - self.player.angle) + 0.0001)
            color = max(255 - depth * 30, 0)
            self.renderer.fill((column * (WIDTH // CASTED_RAYS), (HEIGHT - wall_height) // 2, WIDTH // CASTED_RAYS + 1, wall_height), sdl2.ext.Color(color, color, color))
            # Minimap
                                                                                                    self.render_minimap()

                                                                                                            self.renderer.present()
                                                                                                                    sdl2.SDL_Delay(100)  # Add a small delay to slow down the loop

                                                                                                                        def run(self):
                                                                                                                                    running = True
                                                                                                                                            while running:
                                                                                                                                                            running = self.handle_events()
                                                                                                                                                                        self.update()
                                                                                                                                                                                    self.render()
                                                                                                                                                                                            sdl2.ext.quit()

                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                    game = Game()
                                                                                                                                                                                                        game.run()
