CELL_SIZE = 12
GAP = 2
color_map = {
    0: "#0f101a",
    1: "#00d4ff",
    2: "#ffcc22",
    3: "#ff3388"
}
grid = [
    [0,0,2,2,2,0,0],
    [0,2,2,2,2,2,0],
    [2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2],
    [0,2,2,0,0,2,0],
    [0,0,2,0,0,2,0],
    [0,0,0,0,0,0,0],
]

def build_svg():
    rows = len(grid)
    cols = len(grid[0])
    w = cols * CELL_SIZE + (cols - 1) * GAP
    h = rows * CELL_SIZE + (rows - 1) * GAP
    rects = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            fill = color_map[val]
            rx = x * (CELL_SIZE + GAP)
            ry = y * (CELL_SIZE + GAP)
            rects.append(f'<rect x="{rx}" y="{ry}" width="{CELL_SIZE}" height="{CELL_SIZE}" fill="{fill}"/>')
    svg = f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
<defs>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="2" result="blur"/>
    <feComposite in="SourceGraphic" in2="blur" operator="over"/>
  </filter>
</defs>
{"".join(rects)}
</svg>'''
    return svg

if __name__ == "__main__":
    svg_text = build_svg()
    with open("art.svg", "w", encoding="utf-8") as f:
        f.write(svg_text)
