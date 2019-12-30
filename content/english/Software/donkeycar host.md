+++
title = "Installing DonkeyCar on your Host PC"
menuTitle = "DonkeyCar: Host PC"
draft = false
weight=12

+++

# Donkey installation

- Install [miniconda Python 3.7](https://conda.io/miniconda.html)
- Install [git](https://git-scm.com/download)
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