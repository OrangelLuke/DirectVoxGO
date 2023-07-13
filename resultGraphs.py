import json
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ruta = "results.json"
    if os.path.exists(ruta):  # We check if the file exits
        with open(ruta) as archivo:
            contenido = json.load(archivo)  # Load JSON content into a variable
            if isinstance(contenido, list):  # Check if content is a list
                data = contenido
            else:
                print("The content is not a valid list.")
    else:
        print("JSON archive does not exist")


    # coarse_train.n_iters

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[0:3]:
        param.append(val["config"]["coarse_train.n_iters"])
        time.append(val["results"]["time"]/60)
        memory.append(val["results"]["memory"] * (10**-9))
        psnr.append(val["results"]["psnr"]-25)
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plt.plot(param, time, label = "time (mins)")
    plt.scatter(param, time)
    plt.plot(param, memory, label = "memory (gb)")
    plt.scatter(param, memory)
    plt.plot(param, psnr, label = "psnr (-25)")
    plt.scatter(param, psnr)
    plt.plot(param, ssim, label = "ssim")
    plt.scatter(param, ssim)
    plt.plot(param, lpips, label = "lpips")
    plt.scatter(param, lpips)
    plt.xlabel("coarse_train.n_iters")
    plt.legend()
    plt.savefig('coarse_train-n_iters.png', dpi = 1080)
    plt.show()


    # coarse_train.n_rand

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[3:6]:
        param.append(val["config"]["coarse_train.n_rand"])
        time.append(val["results"]["time"]/60)
        memory.append(val["results"]["memory"] * (10**-9))
        psnr.append(val["results"]["psnr"]-25)
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plt.plot(param, time, label = "time (mins)")
    plt.scatter(param, time)
    plt.plot(param, memory, label = "memory (gb)")
    plt.scatter(param, memory)
    plt.plot(param, psnr, label = "psnr (-25)")
    plt.scatter(param, psnr)
    plt.plot(param, ssim, label = "ssim")
    plt.scatter(param, ssim)
    plt.plot(param, lpips, label = "lpips")
    plt.scatter(param, lpips)
    plt.xlabel("coarse_train.n_rand")
    plt.legend()
    plt.savefig('coarse_train-n_rand.png', dpi = 1080)
    plt.show()


    # fine_train.n_iters

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[6:9]:
        param.append(val["config"]["fine_train.n_iters"])
        time.append(val["results"]["time"]/60)
        memory.append(val["results"]["memory"] * (10**-9))
        psnr.append(val["results"]["psnr"]-25)
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plt.plot(param, time, label = "time (mins)")
    plt.scatter(param, time)
    plt.plot(param, memory, label = "memory (gb)")
    plt.scatter(param, memory)
    plt.plot(param, psnr, label = "psnr (-25)")
    plt.scatter(param, psnr)
    plt.plot(param, ssim, label = "ssim")
    plt.scatter(param, ssim)
    plt.plot(param, lpips, label = "lpips")
    plt.scatter(param, lpips)
    plt.xlabel("fine_train.n_iters")
    plt.legend()
    plt.savefig('fine_train-n_iters.png', dpi = 1080)
    plt.show()


    # coarse_render.num_voxels

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[9:13]:
        param.append(val["config"]["coarse_render.num_voxels"])
        time.append(val["results"]["time"] / 60)
        memory.append(val["results"]["memory"] * (10 ** -9))
        psnr.append(val["results"]["psnr"] - 25)
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plt.plot(param, time, label="time (mins)")
    plt.scatter(param, time)
    plt.plot(param, memory, label="memory (gb)")
    plt.scatter(param, memory)
    plt.plot(param, psnr, label="psnr (-25)")
    plt.scatter(param, psnr)
    plt.plot(param, ssim, label="ssim")
    plt.scatter(param, ssim)
    plt.plot(param, lpips, label="lpips")
    plt.scatter(param, lpips)
    plt.xlabel("coarse_render.num_voxels")
    plt.legend()
    plt.savefig('coarse_render-num_voxels.png', dpi=1080)
    plt.show()


    # fine_render.num_voxels

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[13:17]:
        param.append(val["config"]["fine_render.num_voxels"])
        time.append(val["results"]["time"] / 60)
        memory.append(val["results"]["memory"] * (10 ** -9))
        psnr.append(val["results"]["psnr"] - 25)
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plt.plot(param, time, label="time (mins)")
    plt.scatter(param, time)
    plt.plot(param, memory, label="memory (gb)")
    plt.scatter(param, memory)
    plt.plot(param, psnr, label="psnr (-25)")
    plt.scatter(param, psnr)
    plt.plot(param, ssim, label="ssim")
    plt.scatter(param, ssim)
    plt.plot(param, lpips, label="lpips")
    plt.scatter(param, lpips)
    plt.xlabel("fine_render.num_voxels")
    plt.legend()
    plt.savefig('fine_render-num_voxels.png', dpi=1080)
    plt.show()



