import json
import os
import matplotlib.pyplot as plt

parentDir = "graphs"

def plot_graphs(param, time, memory, psnr, ssim, lpips, name):
    path = os.path.join(parentDir, name)
    os.mkdir(path)

    filename = name+"-TIME"
    directory = os.path.join(path, filename)
    plt.plot(param, time, label="time (mins)")
    plt.scatter(param, time)
    plt.xlabel(name)
    plt.legend()
    plt.savefig(directory, dpi=1080)
    plt.clf()

    filename = name+"-MEMORY"
    directory = os.path.join(path, filename)
    plt.plot(param, memory, label="memory (mb)")
    plt.scatter(param, memory)
    plt.xlabel(name)
    plt.legend()
    plt.savefig(directory, dpi=1080)
    plt.clf()

    filename = name+"-PSNR"
    directory = os.path.join(path, filename)
    plt.plot(param, psnr, label="psnr")
    plt.scatter(param, psnr)
    plt.xlabel(name)
    plt.legend()
    plt.savefig(directory, dpi=1080)
    plt.clf()

    filename = name+"-SSIM"
    directory = os.path.join(path, filename)
    plt.plot(param, ssim, label="ssim")
    plt.scatter(param, ssim)
    plt.xlabel(name)
    plt.legend()
    plt.savefig(directory, dpi=1080)
    plt.clf()

    filename = name+"-LPIPS"
    directory = os.path.join(path, filename)
    plt.plot(param, lpips, label="lpips")
    plt.scatter(param, lpips)
    plt.xlabel(name)
    plt.legend()
    plt.savefig(directory, dpi=1080)
    plt.clf()


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

    for val in data[0:5]:
        param.append(val["config"]["coarse_train.n_iters"])
        time.append(val["results"]["time"]/60)
        memory.append(val["results"]["memory"] * (10**-6))
        psnr.append(val["results"]["psnr"])
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plot_graphs(param, time, memory, psnr, ssim, lpips, "coarse_train-n_iters")


    # coarse_train.n_rand

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[5:10]:
        param.append(val["config"]["coarse_train.n_rand"])
        time.append(val["results"]["time"]/60)
        memory.append(val["results"]["memory"] * (10**-6))
        psnr.append(val["results"]["psnr"])
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plot_graphs(param, time, memory, psnr, ssim, lpips, "coarse_train-n_rand")


    # fine_train.n_iters

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[10:15]:
        param.append(val["config"]["fine_train.n_iters"])
        time.append(val["results"]["time"]/60)
        memory.append(val["results"]["memory"] * (10**-6))
        psnr.append(val["results"]["psnr"])
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plot_graphs(param, time, memory, psnr, ssim, lpips, "fine_train-n_iters")


    # coarse_render.num_voxels

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[15:20]:
        param.append(val["config"]["coarse_render.num_voxels"])
        time.append(val["results"]["time"] / 60)
        memory.append(val["results"]["memory"] * (10 ** -6))
        psnr.append(val["results"]["psnr"])
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plot_graphs(param, time, memory, psnr, ssim, lpips, "coarse_render-num_voxels")


    # fine_render.num_voxels

    param = []
    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[20:25]:
        param.append(val["config"]["fine_render.num_voxels"])
        time.append(val["results"]["time"] / 60)
        memory.append(val["results"]["memory"] * (10 ** -6))
        psnr.append(val["results"]["psnr"])
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    plot_graphs(param, time, memory, psnr, ssim, lpips, "fine_render-num_voxels")


