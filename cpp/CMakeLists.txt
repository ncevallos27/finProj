cmake_minimum_required(VERSION 3.29)
project(finProj)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


include_directories(.)
include_directories(include)
include_directories($ENV{CONDA_PREFIX}/envs/finProj/include)

add_executable(finProj
        include/binomialTree.h
        src/binomialTree.cpp
        include/option.h
        include/pricer.h
        src/pricer.cpp
        include/stock.h
        src/stock.cpp
        include/payoff.h
        src/payoff.cpp
        include/euroCall.h
        src/euroCall.cpp
        include/euroPut.h
        src/euroPut.cpp
        src/option.cpp
        main.cpp
        bindings.cpp
        include/bindings.h)

target_include_directories(finProj PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(finProj PRIVATE Python3::Python)