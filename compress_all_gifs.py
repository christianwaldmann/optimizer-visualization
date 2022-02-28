import os
import glob


filepaths = glob.glob("animations/*.gif")


for filepath in filepaths:
    cmd = f'gifsicle -i "{filepath}" -O3 --colors 256 -o "{filepath}"'
    os.system(cmd)


print("Compressing all gifs finished")
