+++
title = "Installing DonkeyCar on your Host PC"
menuTitle = "DonkeyCar: Host PC"
draft = false
weight=12

+++

# Donkey installation

Let's install the Donkey software on your host pc. The only part where this differs between the three platforms, Mac OS X, Linux and Windows, is in the Miniconda software installation, so we'll get that out of the way first:

- If you're on a Mac: [download Miniconda here](https://docs.conda.io/en/latest/miniconda.html#macosx-installers), [git here](https://www.atlassian.com/git/tutorials/install-git) and install them

- If you're on Windows: [download Miniconda here](https://docs.conda.io/en/latest/miniconda.html#windows-installers), [git here](https://git-scm.com/download/win) and install them

- If you're on Linux: [download Miniconda here](https://docs.conda.io/en/latest/miniconda.html#linux-installers) and install it

- If you're on Mac/Linux open up a terminal and follow the rest of the tutorial

- If you're on Windows, open an Anaconda Prompt via Start Menu and follow the rest of the tutorial:

- Go to a place where you want the stuff we'll be working on to be.

- Make a folder for your projects:

    ```bash
    mkdir projects
    cd projects
    ```

- Clone the Donkey repo:

    ```bash
    git clone https://github.com/autorope/donkeycar
    cd donkeycar
    git checkout master
    ```

- Create the Python anaconda env:

    ```bash
    conda env create -f install\envs\windows.yml
    conda activate donkey
    pip install -e .[pc]
    ```

- If you're using a GPU and not using a Mac (sorry, no GPU support for you folks):

- Install Tensorflow GPU:

  - Check the [Software requirements](https://www.tensorflow.org/install/gpu#software_requirements) for Nvidia GPUs

  - Which basically means:

    - Download and install [NVIDIA drivers](https://www.nvidia.com/drivers), obviously

    - Download and install [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

    - Download and install [cuDNN](https://developer.nvidia.com/rdp/cudnn-download) ([you should just copy the bin, lib and include folders from the zip to your cuda installation folder](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#install-windows))

    - Download and install [TensorRT 5.0](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html) to improve latency and throughput for inference on some models ([same as the above](https://docs.nvidia.com/deeplearning/sdk/tensorrt-archived/tensorrt-515/tensorrt-install-guide/index.html))

      - Which means installing PyCUDA (make sure nvcc is in your PATH):

        ```bash
        pip install 'pycuda>=2017.1.1'
        ```

        If you're getting errors, [check the requirements here](https://wiki.tiker.net/PyCuda/Installation).
        If you're on Windows, you probably need the [VS C++ 14](https://www.scivision.dev/python-windows-visual-c-14-required/), just download it through the [VS Build Tools](https://aka.ms/vs/16/release/vs_buildtools.exe)
      
      - Downloading and installing [TensorRT 5.0](https://developer.nvidia.com/nvidia-tensorrt-5x-download)

Then you can finally:

```bash
conda install tensorflow-gpu==1.13.1
```