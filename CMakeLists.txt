cmake_minimum_required(VERSION 3.15)
project(finProj LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Put built .so in the build dir root (cmake-build-debug)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

# Use the Python from the active conda env, if any
if(DEFINED ENV{CONDA_PREFIX})
    set(Python_EXECUTABLE "/opt/anaconda3/envs/finProj/bin/python" CACHE FILEPATH "Python executable" FORCE)
endif()

# Tell pybind11 to use CMake's Python3 finder
set(PYBIND11_FINDPYTHON ON)

# Your headers
include_directories(cpp/include)
include_directories(cpp/src)

# pybind11 is a git submodule at extern/pybind11
add_subdirectory(extern/pybind11)

# All core C++ sources (except bindings.cpp)
file(GLOB FINPROJ_SOURCES "cpp/src/*.cpp")

# 1) Build core library with your C++ logic (Payoff, Pricer, etc.)
add_library(finproj_core STATIC ${FINPROJ_SOURCES})

# 2) Build the Python extension module named "finProj" from cpp/bindings.cpp
pybind11_add_module(finProj cpp/bindings.cpp)

# 3) Link the core C++ library into the Python module
target_link_libraries(finProj PRIVATE finproj_core)

# Optional: install the built module into the current directory
install(TARGETS finProj DESTINATION .)