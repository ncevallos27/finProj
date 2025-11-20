# no cmake_minimum_required or project() here

add_executable(finProj_debug
        main.cpp
)

target_link_libraries(finProj_debug
        PRIVATE
        finproj_core
)

target_include_directories(finProj_debug
        PRIVATE
        ${Python3_INCLUDE_DIRS}
)