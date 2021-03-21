"""
GPU info helper methods.
"""

from tensorflow.python.client import device_lib


def instance_gpu() -> str:
    """
    Returns the GPU for the Colab instance.

    :return: The GPU model
    """
    devices = device_lib.list_local_devices()
    gpu = [x.physical_device_desc for x in devices if x.device_type == "GPU"][0]
    return gpu.split(",")[1].split(":")[1].strip()
