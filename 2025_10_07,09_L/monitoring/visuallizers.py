from PIL import Image, ImageDraw, ImageFont

class ConsoleVisuallizer:

    @staticmethod
    def draw_bar(percentage, label, width=30):
        filled_width = int(percentage / 100 * width)
        empty_fill = width - filled_width

        bar = '█' * filled_width + '░' * empty_fill

        print(f'{label:<15} [{bar}] {percentage:6.2f}%')


class ImageVisuallizer:

    def create_report(self, metrics, filename='report.png'):

        width, height = 800, 600
        bg_color = (25, 25, 35)
        padding = 50
        bar_width = 80
        bar_spacing = 60

        colors = [(46, 204, 113), (52, 152,219), (155, 89, 182)]

        image = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(image)
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()

        title_text = 'System Resources Report'
        title_bbox = draw.textbbox((0, 0),
                                   title_text,
                                   font=title_font)
        title_w = title_bbox[2] - title_bbox[0]
        draw.text( ((width - title_w) / 2, padding),
                   title_text,
                   fill=(236, 240, 241),
                   font=title_font)

        chart_area_y = padding + 70
        max_height = height - chart_area_y - padding - 50
        percent_metrics = [m for m in metrics
                           if hasattr(m, 'current_usage')]
        for i, metric in enumerate(percent_metrics):
            x0 = padding + i*(bar_width+bar_spacing)+100
            y1 = chart_area_y + max_height
            bar_height = (metric.value/100) * max_height
            x1 = x0 + bar_width
            y0 = y1 - bar_height

            draw.rectangle([x0, y0,x1, y1],
                           fill=colors[i%len(colors)])

            label_text = f'{metric.name}'
            value_text = f'{metric.value:.2f}%'
            label_bbox = draw.textbbox((0, 0),
                                       label_text,
                                       font=label_font)
            label_w = label_bbox[2] - label_bbox[0]
            draw.text((x0, y0-25),
                      value_text,
                      fill=(255, 255, 255),
                      font=label_font)
            draw.text((x0 + (bar_width-label_w)/2, y1+10),
                      label_text,
                      fill=(200, 200, 200),
                      font=label_font
                      )
        image.save(filename)

        # len(metrics)=5   1 2 3 4 5
        # len(colors)=2    1 % 2
        #                  2 % 2
        #                  3 % 2