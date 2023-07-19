import json
import os
import matplotlib.pyplot as plt
import oapackage
import numpy as np

parentDir = "graphs/pareto"

def graphPareto(obj1, obj2, name1, name2, pOpt):
    lpipsFlag = False
    if name1 == "LPIPS":
        lpipsFlag = True

    obj1 = np.array(obj1)
    if lpipsFlag:
        obj1 = 1/obj1
    obj2 = 1 / np.array(obj2)

    ratio = obj1 + obj2

    filename = name1+"-"+name2

    plt.scatter(obj1, obj2, c=ratio)
    if lpipsFlag:
        plt.xlabel("1/"+name1)
    else:
        plt.xlabel(name1)
    plt.ylabel("1/"+name2)
    # plt.legend()
    plt.savefig(os.path.join(parentDir, filename), dpi=1080)
    plt.clf()

    pareto = oapackage.ParetoDoubleLong()

    for i in range(0, len(obj1)):
        w = oapackage.doubleVector((obj1[i], obj2[i]))
        pareto.addvalue(w, i)

    pareto.show(verbose=1)

    lst = np.array(pareto.allindices())

    pOpt[filename] = [data[i] for i in lst]

    filename = name1 + "-" + name2 + "_PARETO"

    plt.plot(obj1, obj2, '.b', label='Non Pareto-optimal', markersize=10)
    plt.plot(obj1[lst], obj2[lst], '.r', label='Pareto optimal', markersize=10)
    if lpipsFlag:
        plt.xlabel("1/"+name1)
    else:
        plt.xlabel(name1)
    plt.ylabel("1/"+name2)
    plt.legend(loc=3, numpoints=1)
    plt.savefig(os.path.join(parentDir, filename), dpi=1080)
    plt.clf()

    return pOpt

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

    time = []
    memory = []
    psnr = []
    ssim = []
    lpips = []

    for val in data[0:25]:
        time.append(val["results"]["time"] / 60)
        memory.append(val["results"]["memory"] * (10 ** -6))
        psnr.append(val["results"]["psnr"])
        ssim.append(val["results"]["ssim"])
        lpips.append(val["results"]["lpips"])

    paretoOptimal = {}

    paretoOptimal = graphPareto(psnr[0:24], time[0:24], "PSNR", "time (mins)", paretoOptimal)
    paretoOptimal = graphPareto(lpips[0:24], time[0:24], "LPIPS", "time (mins)", paretoOptimal)
    paretoOptimal = graphPareto(ssim[0:24], time[0:24], "SSIM", "time (mins)", paretoOptimal)
    paretoOptimal = graphPareto(psnr, memory, "PSNR", "memory (mb)", paretoOptimal)
    paretoOptimal = graphPareto(lpips, memory, "LPIPS", "memory (mb)", paretoOptimal)
    paretoOptimal = graphPareto(ssim, memory, "SSIM", "memory (mb)", paretoOptimal)

    print(paretoOptimal)

    with open("graphs/pareto/resultsPareto.json", 'w') as f:
        json.dump(paretoOptimal, f, indent=2)
