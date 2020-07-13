# CEPCSW_Pandora
This is Pandora client for CEPC experiment https://github.com/wenxingfang/CEPCSW/tree/lcg97
### Some Notices
* If you want to use it for other experiment, please take care the calo cell id decode part in CaloHitCreator.cpp .
* Configuration of pandora algorithm is set by pandoralg in tut_detsim_pandora.py. The default values are for CEPC experiment, please change it as you want.
* Function to get showershape of a cluster is still from Marlin (it dependents GSL 1.14).
* Currently vertices informations are not used.
