CMAKE_MINIMUM_REQUIRED(VERSION 3.15)

project(k4Pandora)

find_package(ROOT COMPONENTS RIO Tree)

find_package(Gaudi)

include(GNUInstallDirs)
include(CTest)

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/InstallArea/ CACHE PATH
    "Install path prefix, prepended onto install directories." FORCE )
endif()


# Set up C++ Standard
# ``-DCMAKE_CXX_STANDARD=<standard>`` when invoking CMake
set(CMAKE_CXX_STANDARD 17 CACHE STRING "")

if(NOT CMAKE_CXX_STANDARD MATCHES "14|17")
  message(FATAL_ERROR "Unsupported C++ standard: ${CMAKE_CXX_STANDARD}")
endif()

include(cmake/k4PandoraDependencies.cmake)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${PandoraSDK_LIBRARY_DIRS}/cmake")


##############################################################################
# Source Code
##############################################################################

add_subdirectory(Pandora)
add_subdirectory(Service)

##############################################################################
# INSTALL
##############################################################################

install(EXPORT ${PROJECT_NAME}Targets
  NAMESPACE ${PROJECT_NAME}::
  FILE "${PROJECT_NAME}Targets.cmake"
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}/"
  )

gaudi_install(CMAKE cmake/${PROJECT_NAME}Config.cmake)

