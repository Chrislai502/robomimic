from setuptools import setup, find_packages
from os import path, getenv

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    lines = f.readlines()

# Remove images from README
lines = [x for x in lines if (('.png' not in x) and ('.gif' not in x))]
long_description = ''.join(lines)

# Pin torch version if specified in the environment variable
pytorch_version = getenv("PYTORCH_VERSION", "")
pytorch_dep = f"torch=={pytorch_version}" if pytorch_version else "torch"

setup(
    name="robomimic",
    packages=[
        package for package in find_packages() if package.startswith("robomimic")
    ],
    install_requires=[
        "numpy>=1.13.3",
        "h5py>=0.0.0",
        "psutil>=0.0.0",
        "tqdm>=0.0.0",
        "termcolor>=0.0.0",
        "tensorboard>=0.0.0",
        "tensorboardX>=0.0.0",
        "imageio>=0.0.0",
        "imageio-ffmpeg>=0.0.0",
        "matplotlib>=0.0.0",
        "egl_probe>=0.0.1",
        pytorch_dep,
        "torchvision==0.18.1",
        "diffusers==0.11.1",
        "tianshou==0.4.10",
        "transformers",
    ],
    eager_resources=['*'],
    include_package_data=True,
    python_requires='>=3',
    description="robomimic: A Modular Framework for Robot Learning from Demonstration",
    author="Ajay Mandlekar, Danfei Xu, Josiah Wong, Soroush Nasiriany, Chen Wang",
    url="https://github.com/ARISE-Initiative/robomimic",
    author_email="amandlek@cs.stanford.edu",
    version="0.3.0",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
