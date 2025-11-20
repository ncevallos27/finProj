from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

# Define the C++ extension module
ext_modules = [
    Pybind11Extension(
        "finProj",
        sources=sorted(glob("cpp/src/*.cpp") + glob("cpp/bindings.cpp")),
        include_dirs=["cpp/include"],
        cxx_std=17,  # matches your project
    ),
]

setup(
    name="finProj",
    version="0.1.0",
    author="Nicolas Cevallos",
    description="Option pricing library with pybind11 bindings",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)