cmake_minimum_required(VERSION 3.10)
project(helloworld)
add_executable(helloworld helloworld.cpp)

project(usespthread)
SET(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-pthread")
add_executable(usespthread usespthread.cpp)

SET(LIB_SRC myengine/myengine.cpp)	
include_directories(include)
ADD_LIBRARY(MyEngineDynamic SHARED ${LIB_SRC})
ADD_LIBRARY(MyEngineStatic STATIC ${LIB_SRC})

install(TARGETS MyEngineDynamic MyEngineStatic DESTINATION /usr/local/lib/)
INSTALL(FILES myengine/myengine.hpp DESTINATION /usr/local/include)
