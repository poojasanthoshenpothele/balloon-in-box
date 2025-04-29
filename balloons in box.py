import tkinter as tk
import random
import math

# Box dimensions
BOX_WIDTH = 600
BOX_HEIGHT = 400
BALLOON_COUNT = 10

class Balloon:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = 5  # Start with a small radius
        self.color = f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"
        self.id = None  # Canvas object ID

    def inflate(self, balloons):
        """Inflate balloon until it touches another balloon or the box walls."""
        while True:
            # Check if it touches the box boundary
            if (self.x - self.radius <= 0 or self.x + self.radius >= BOX_WIDTH or
                self.y - self.radius <= 0 or self.y + self.radius >= BOX_HEIGHT):
                break
            
            # Check if it touches any other balloon
            for other in balloons:
                if other != self:
                    distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
                    if distance <= self.radius + other.radius:
                        return  # Stop inflation if touching another balloon

            # Increase radius
            self.radius += 2

    def draw(self):
        """Draw balloon on the canvas."""
        self.id = self.canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=self.color, outline="black"
        )

def generate_balloons(canvas):
    """Generate and display balloons in the box."""
    canvas.delete("all")  # Clear canvas
    balloons = []

    for _ in range(BALLOON_COUNT):
        x = random.randint(50, BOX_WIDTH - 50)
        y = random.randint(50, BOX_HEIGHT - 50)
        balloon = Balloon(canvas, x, y)
        balloon.inflate(balloons)
        balloon.draw()
        balloons.append(balloon)

# Create GUI Window
root = tk.Tk()
root.title("Balloons in a Box")
root.geometry(f"{BOX_WIDTH+20}x{BOX_HEIGHT+50}")

# Create Canvas for Drawing
canvas = tk.Canvas(root, width=BOX_WIDTH, height=BOX_HEIGHT, bg="white")
canvas.pack()

# Button to Start Simulation
button = tk.Button(root, text="Start Simulation", command=lambda: generate_balloons(canvas))
button.pack()

root.mainloop()
