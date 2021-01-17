## Quick start
```
$ source /cvmfs/cepcsw.ihep.ac.cn/prototype/releases/externals/98.0.0/setup-98.0.0.sh
$ git clone https://github.com/key4hep/k4Pandora.git
$ cd k4Pandora
$ mkdir build && cd build
$ cmake .. 
$ make
$ ./run gaudirun.py ../Examples/options/tut_pandora.py
```
### Some Notices
* k4Pandora is a pandora app for the Key4HEP software framework. It uses Gaudi_v35 framework for running and Edm4hep for the event data model.  
* If you want to use it for other experiment, please take care the calo cell id decode part in CaloHitCreator.cpp .
* Configuration of pandora algorithm is set by pandoralg in tut_detsim_pandora.py. The default values are for CEPC experiment, please change it as you want.
* Function to get ClusterShapes (in PfoCreator.cpp) of a cluster is still from Marlin.
