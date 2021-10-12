local_str = {
    "locale": "Using locale",
    "project name": "DaVinci Resolve checker",
    "you are running": "You are running",
    "script not tested on distro": "but this script was not tested on it.",
    "which DR package": "Installed DaVinci Resolve package:",
    "chassis": "Chassis type:",
    "laptop": "laptop",
    "desktop": "desktop",
    "openCL drivers": "Installed OpenCL drivers:",
    "presented gpus": "Presented GPUs:",
    "kernel driver": "kernel driver in use:",
    "opengl vendor": "OpenGL vendor string:",
    "missing opengl vendor": "Unable to detect the OpenGL vendor string. Probably you are trying to use AMD Pro OpenGL while your primary GPU is Intel. Also probably you are launching script via ssh.",
    "should uninstall opencl-mesa": "You should uninstall opencl-mesa. Otherwise DR (v17.1.1) behaves wrong: image is corrupted. But if you uncheck gpu checkbox in settings and relaunch DR, then even entire desktop session becomes corrupted and you only can reboot your pc. This is observed at least on amd gpu.",
    "several intel gpus": "You have several INTEL GPUs. I am confused. Are you using multi-cpu desktop motherboard? Or intel igpu + intel dgpu (which does not exist at the moment of writing)?",
    "several amd gpus": "You have several AMD GPUs. I am confused. Which one do you intend to use?",
    "several nvidia gpus": "You have several NVIDIA GPUs. I am confused. Which one do you intend to use?",
    "confused by nvidia and amd gpus": "You have AMD and NVIDIA GPUs. I am confused. Which one do you intend to use?",
    "amd gpu binded to vfio-pci": "Your amd gpu is binded to vfio-pci, dropping it from further checking.",
    "nvidia gpu binded to vfio-pci": "Your nvidia gpu is binded to vfio-pci, dropping it from further checking.",
    "only intel gpu, cannot run DR": "You have only Intel GPU. Currently DR cannot use intel GPUs for OpenCL. You cannot run DR. See https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=81579",
    "mixed intel and amd gpus": "I did not find a working configuration yet for laptops with Intel + AMD graphics. Did you?",
    "set primary display to PCIE": "Your primary gpu is Intel. Go to your uefi settings and set primary display to PCIE. Otherwise you could not use DaVinci Resolve (I did not tested it).",
    "switch from radeon driver to amdgpu": "You are currently using radeon driver. Switch to amdgpu as described here: https://wiki.archlinux.org/title/AMDGPU#Enable_Southern_Islands_(SI)_and_Sea_Islands_(CIK)_support. Otherwise you could not run DaVinci Resolve.",
    "no support for amd driver, cannot run DR": "Your gpu only supports radeon driver. DaVinci Resolve requires amdgpu progl, which can only work with amdgpu driver. You cannot run DaVinci Resolve.",
    "not running amdgpu driver, cannot run DR": "For some reason, you are not running amdgpu driver. You cannot run DaVinci Resolve.",
    "not using Pro OpenGL": "You are not using Pro OpenGL implementation. Install amdgpu-pro-libgl and run DaVinci Resolve with progl prefix. Otherwise it will crash.",
    "missing opencl driver": "You do not have opencl-driver for AMD GPU. Install it, otherwise you could not use DaVinci Resolve.",
    "good to run DR": "All seems good. You should be able to run DaVinci Resolve successfully.",
    "missing opencl-nvidia package": "You do not have opencl-nvidia package (or alternative package which provides opencl-nvidia). Install it, otherwise you could not use DR. Even if you are planning to use cuda, opencl-nvidia is its required dependency.",
    "missing nvidia as kernel driver": "You are not using nvidia as kernel driver. Use proprietary nvidia driver, otherwise you could not use DaVinci Resolve.",
    "not running nvidia rendered": "You are not running NVIDIA renderer. Try to run the script with prime-run or other method for optimus, otherwise you could not use DaVinci Resolve.",
}
