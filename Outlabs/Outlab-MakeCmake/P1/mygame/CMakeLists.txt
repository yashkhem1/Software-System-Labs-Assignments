cmake_minimum_required(VERSION 3.10)
project(mygame)
set ( PROJECT_LINK_LIBS libMyEngineDynamic.so )
add_executable(mygamedynamic mygame.cpp)
target_link_libraries(mygamedynamic ${PROJECT_LINK_LIBS} )
set ( PROJECT_LINK_LIBS libMyEngineStatic.a )
add_executable(mygamestatic mygame.cpp)
target_link_libraries(mygamestatic ${PROJECT_LINK_LIBS} )

