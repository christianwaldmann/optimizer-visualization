import imageio
import glob
import os


outfilename = "animations/out.gif"


images = []


def getKey(fp):
    filename = os.path.splitext(os.path.basename(fp))[0]
    intpart = filename.split()[0]
    return int(intpart)


# sort pictures and ignore last one because this might be corrupted
filenames = sorted(glob.glob("tmp/*png"), key=getKey)[:-1]


imageio.plugins.freeimage.download()


for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave(outfilename, images, format="GIF-FI", duration=0.001)


print(outfilename)
