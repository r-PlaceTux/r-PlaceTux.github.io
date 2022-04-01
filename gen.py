#!/bin/env python3
import matplotlib.pyplot as plt

p = plt.imread("tux.png")

topleft = (20, 679)

scale = 10

generated = ""

for row in range(len(p)):
    generated += f"<div class='row' style='top: {row * scale}px;'>"
    for square in range(len(p[row])):
        color = f"rgba({p[row][square][0]*255},{p[row][square][1]*255},{p[row][square][2]*255},{p[row][square][3]})"
        generated += f"<a style='background-color: {color};left: {square * scale}px;' class='square' href='https://new.reddit.com/r/place/?cx={topleft[0] + square}&cy={topleft[1] + row}&px=20'></a>"
    generated += "</div>"

template = f"""
<!DOCTYPE html>
<html lang="en">
<style>
* {{
    width: {scale}px;
    height: {scale}px;
    top: 0;
    left: 0;
    padding: 0;
    margin: 0;
}}
.row {{
    position: absolute;
    width: {scale * len(p[0])}px;
}}
.square {{
    position: absolute;
}}
.square:hover {{
    border-style: solid;
    border-radius: 0;
    border-thickness: 2px;
    border-color: gray;
}}
</style>
<body>
{generated}
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(template)
