## Quick start
```
$ source /cvmfs/cepcsw.ihep.ac.cn/prototype/releases/externals/97.0.2/setup.sh
$ git clone https://github.com/key4hep/Pandora.git
$ cd Pandora
$ mkdir build && cd build
$ cmake .. -DHOST_BINARY_TAG=${BINARY_TAG}
$ make
$ ./run gaudirun.py ../Examples/options/tut_pandora.py
```
### Some Notices
* Gaudi framework is used for running
* The event data model is Edm4hep
* If you want to use it for other experiment, please take care the calo cell id decode part in CaloHitCreator.cpp .
* Configuration of pandora algorithm is set by pandoralg in tut_detsim_pandora.py. The default values are for CEPC experiment, please change it as you want.
* Function to get ClusterShapes (in PfoCreator.cpp) of a cluster is still from Marlin.
