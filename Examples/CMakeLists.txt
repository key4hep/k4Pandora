
# Modules
gaudi_add_module(k4PandoraExamples
                 SOURCES src/Edm4hepTest/Edm4hepReadAlg.cpp
                         src/Edm4hepTest/Edm4hepWriteAlg.cpp
                 LINK k4FWCore::k4FWCore 
                      Gaudi::GaudiAlgLib Gaudi::GaudiKernel
                      ${LCIO_LIBRARIES} 
                      EDM4HEP::edm4hep EDM4HEP::edm4hepDict
                      ${podio_LIBRARIES} podio::podioRootIO
)


install(TARGETS k4PandoraExamples
  EXPORT CEPCSWTargets
  RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}" COMPONENT bin
  LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}" COMPONENT shlib
  COMPONENT dev)
