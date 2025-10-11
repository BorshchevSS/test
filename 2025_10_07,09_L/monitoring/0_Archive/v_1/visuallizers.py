from PIL import Image, ImageDraw, ImageFont

class ConsoleVisuallizer:
    @staticmethod
    def draw_bar(percentage, label, width):
        filled_width = int(percentage / 100 * width)
        empty_fill = width - filled_width

        bar = "█" * filled_width + "░" * empty_fill
        print(f"{label} [{bar}] {percentage}%")