import requests
import json

GH_USER = "hutao-oo"
TOKEN = ""
GRAPHQL_API = "https://api.github.com/graphql"

def fetch_calendar():
    headers = {"Authorization": f"bearer {TOKEN}"}
    query = """
    query ($user: String!) {
      user(login: $user) {
        contributionsCollection {
          contributionCalendar {
            weeks { contributionDays { contributionCount } }
          }
        }
      }
    }
    """
    resp = requests.post(GRAPHQL_API, json={"query": query, "variables": {"user": GH_USER}}, headers=headers)
    cal = resp.json()["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    grid = []
    for week in cal["weeks"]:
        days = [d["contributionCount"] for d in week["contributionDays"]]
        grid.append(days)
    return grid

def draw_svg(grid):
    cell_size = 12
    w = 53
    h = 7
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    svg = f'<svg width="{w*cell_size}" height="{h*cell_size}" xmlns="http://www.w3.org/2000/svg">'
    for x in range(w):
        for y in range(h):
            try:
                val = grid[x][y]
            except IndexError:
                val = 0
            fill = colors[min(val,4)]
            svg += f'<rect x="{x*cell_size}" y="{y*cell_size}" width="{cell_size-1}" height="{cell_size-1}" fill="{fill}"/>'
    svg += "</svg>"
    with open("art.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    data = fetch_calendar()
    draw_svg(data)
