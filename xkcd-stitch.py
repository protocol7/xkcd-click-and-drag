import subprocess
import os.path

for n in range(-19, 14):
    if n < 0:
        nc = "%ss" % -n
    elif n > 0:
        nc = "%sn" % n
    else:
        continue

    target = "/tmp/xkcd/stitched/%s.png" % nc

    tiles = []

    for e in range(-33, 49):
        name = nc

        if e < 0:
            name = name + "%sw" % -e
        elif e > 0:
            name = name + "%se" % e
        else:
            continue

        name = name + ".png"
        path = "/tmp/xkcd/scaled/" + name
        if not os.path.exists(path):
            print(path)
            if n > 0:
                path = "/tmp/xkcd/scaled/2n1w.png"
            else:
                path = "/tmp/xkcd/scaled/11s11e.png"

        tiles.append(path)

        #if not os.path.exists(target):
        #    # first image
        #    print("cp %s %s" % (path, target))
        #    subprocess.call(["cp", path, target])
        #else:
    cmd = ["convert"]
    cmd.extend(tiles)
    cmd.append("+append")
    cmd.append(target)
    subprocess.call(cmd)
