# CEPCSW_Pandora
This is Pandora client for CEPC experiment https://github.com/wenxingfang/CEPCSW/tree/lcg97
## Quick start
```
$ source /cvmfs/cepcsw.ihep.ac.cn/prototype/releases/externals/97.0.2/setup.sh
$ git clone https://github.com/wenxingfang/CEPCSW_Pandora.git
$ cd CEPCSW_Pandora
$ mkdir build && cd build
$ cmake .. -DHOST_BINARY_TAG=${BINARY_TAG}
$ make
$ ./run gaudirun.py ../Examples/options/tut_detsim_pandora.py
```
### Some Notices
* If you want to use it for other experiment, please take care the calo cell id decode part in CaloHitCreator.cpp .
* Configuration of pandora algorithm is set by pandoralg in tut_detsim_pandora.py. The default values are for CEPC experiment, please change it as you want.
* Function to get showershape of a cluster is still from Marlin (it dependents GSL 1.14).
* Currently vertices informations are not used.
