# render.py 固定点阵版本：赛博长安 7行画布
CELL_SIZE = 12
GAP = 2
BG = "#0f101a"
ON = "#ffcc22"

# 点阵蓝图：7行，每一行是一列开关，1点亮，0暗。你在这里画像素画
# 7行（y:0~6 周日到周六），横向x是列
grid = [
    [0,0,1,1,1,0,0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,0,0,1,1,1,1,0,0,1,0],
    [0,0,1,0,0,0,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
]

def build_svg():
    rows = len(grid)
    cols = len(grid[0])
    w = cols*(CELL_SIZE+GAP)
    h = rows*(CELL_SIZE+GAP)
    rects = []
    for y,row in enumerate(grid):
        for x,val in enumerate(row):
            fill = ON if val else BG
            rx = x*(CELL_SIZE+GAP)
            ry = y*(CELL_SIZE+GAP)
            rects.append(f'<rect x="{rx}" y="{ry}" width="{CELL_SIZE}" height="{CELL_SIZE}" fill="{fill}"/>')
    svg = f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
{"".join(rects)}
</svg>'''
    return svg

if __name__ == "__main__":
    svg_text = build_svg()
    with open("art.svg","w",encoding="utf-8") as f:
        f.write(svg_text)
