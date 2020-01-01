+++
title = "DonkeyCar installation: Host PC"
menuTitle = "DonkeyCar: Host PC"
draft = false
weight=12

+++

Let's install the Donkey software on your host PC. The only part where this differs between the three platforms, Mac OS X, Linux and Windows, is in the Miniconda software installation, so we'll get that out of the way first.

#### Mac OS X

- Download and install: 
  - [Miniconda here](https://docs.conda.io/en/latest/miniconda.html#macosx-installers), 
  - [git here](https://www.atlassian.com/git/tutorials/install-git)
- Open up a terminal and follow the rest of the tutorial

#### Windows

- Download and install: 
  - [Miniconda here](https://docs.conda.io/en/latest/miniconda.html#windows-installers), 
  - [git here](https://git-scm.com/download/win)
- Open an Anaconda Prompt via Start Menu and follow the rest of the tutorial

#### Linux

- [Download Miniconda here](https://docs.conda.io/en/latest/miniconda.html#linux-installers) and install it
- Open up a terminal and follow the rest of the tutorial

#### The rest of the tutorial:

- Go to a place where you want the stuff we'll be working on to be.

    ```bash
    # e.g. on Linux or Mac
    cd ~
    
    # e.g. on Windows
    cd c:\\Users\\yourUsername
    ```

- Make a folder for your projects and `cd` to it:

    ```bash
    mkdir projects
    cd projects
    ```

- Clone the Donkey repository using git:

    ```bash
    git clone https://github.com/autorope/donkeycar
    cd donkeycar
    git checkout master
    ```

- Create the Python Anaconda environment using the yml file from the repository:

    ```bash
    # Windows
    conda env create -f install\envs\windows.yml
    # Mac
    conda env create -f install\envs\mac.yml
    # Linux/Ubuntu
    conda env create -f install\envs\ubuntu.yml
    # All three OS's
    conda activate donkey
    pip install -e .[pc]
    ```

##### If you're not using a host PC with a GPU, you're done!

#### If you're using a NVidia GPU and not using a Mac (sorry, no TensorFlow GPU support for you folks):

- Install the [TensorFlow software requirements](https://www.tensorflow.org/install/gpu#software_requirements) for Nvidia GPUs, which basically means:

  - Download and install [NVIDIA drivers](https://www.nvidia.com/drivers)

  - Download and install the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

  - Download and install [cuDNN](https://developer.nvidia.com/rdp/cudnn-download) ([you should just copy the bin, lib and include folders from the zip to your cuda installation folder](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#install-windows))

  - Download and install [TensorRT 5.0](https://docs.nvidia.com/deeplearning/sdk/tensorrt-install-guide/index.html) to improve latency and throughput for inference on some models ([same as the above](https://docs.nvidia.com/deeplearning/sdk/tensorrt-archived/tensorrt-515/tensorrt-install-guide/index.html))

    - Which means installing PyCUDA (make sure nvcc is in your PATH):

      ```bash
      pip install 'pycuda>=2017.1.1'
      ```

      - If you're getting errors, [check the requirements here](https://wiki.tiker.net/PyCuda/Installation).
      - If you're on Windows, you probably need the [VS C++ 14](https://www.scivision.dev/python-windows-visual-c-14-required/), just download it through the [VS Build Tools](https://aka.ms/vs/16/release/vs_buildtools.exe)
    
    - Downloading and installing [TensorRT 5.0](https://developer.nvidia.com/nvidia-tensorrt-5x-download)


- Then you can finally:

  ```bash
  conda install tensorflow-gpu==1.13.1
  ```

  