from setuptools import setup, find_packages

setup(
    name='liveportrait',
    version='0.1.0',
    author='Jason Stone',
    author_email='custom@livepeerservice.world',
    description='Efficient Portrait Animation with Stitching and Retargeting Control',
    packages=find_packages(),
    install_requires=[
        'tyro==0.8.5',
        'torch',
        'torchvision==0.18.0',
        'torchaudio==2.3.0',
        'numpy==1.26.4',
        'pyyaml==6.0.1',
        'opencv-python==4.10.0.84',
        'scipy==1.13.1',
        'imageio==2.34.2',
        'lmdb==1.4.1',
        'tqdm==4.66.4',
        'rich==13.7.1',
        'ffmpeg==1.4',
        'onnxruntime==1.18.0',
        'onnx==1.16.1',
        'scikit-image==0.24.0',
        'albumentations==1.4.10',
        'matplotlib==3.9.0',
        'imageio-ffmpeg==0.5.1',
        'gradio==4.37.1',
        'gdown',
    ],
    entry_points={
        'console_scripts': [
            'liveportrait=inference:main',
        ],
    },
)
