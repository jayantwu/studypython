cmake_minimum_required(VERSION 3.10)

project(test)

set(CMAKE_CXX_STANDARD 11)

include_directories(CMAKE_CURRENT_SOURCE_DIR/c_api)

set(LIBRARY_OUTPUT_PATH ./lib)

aux_source_directory(c_api/ SRC_FILE)
add_library(capi SHARED ${SRC_FILE})

add_custom_target(gen_ctypes ALL 
    COMMAND ctypesgen 
    --output-language=py32
    -I ${CMAKE_CURRENT_SOURCE_DIR}/c_api/
    -L ${LIBRARY_OUTPUT_PATH} -llibcapi.so
    ${CMAKE_CURRENT_SOURCE_DIR}/c_api/api.h -o ${LIBRARY_OUTPUT_PATH}/api.py
)
add_dependencies(gen_ctypes capi)

add_custom_target(cp_to_lib ALL
    COMMAND  cp ${CMAKE_CURRENT_SOURCE_DIR}/py/*.py ${CMAKE_CURRENT_SOURCE_DIR}/build/lib/
)
add_dependencies(cp_to_lib gen_ctypes)