#!/usr/bin/env python

import os
import sys

from Gaudi.Configuration import *


##############################################################################
# Event Data Svc
##############################################################################
from Configurables import K4DataSvc
dsvc = K4DataSvc("EventDataSvc", input="you_input.root")
##############################################################################
from Configurables import PodioInput ## set the input collection data
podioinput = PodioInput("PodioReader", collections=[ 
    "MCParticle",
    "ECALBarrel"
    ])
##############################################################################
from Configurables import GearSvc
gearSvc  = GearSvc("GearSvc")
gearSvc.GearXMLFile = "../Pandora/FullDetGear.xml"
##############################################################################
from Configurables import PandoraPFAlg

pandoralg = PandoraPFAlg("PandoraPFAlg")
## KEEP same with lcioinput name for the ReadXXX ###########
pandoralg.ReadMCParticle                       = "MCParticle"                   
pandoralg.ReadECALBarrel                       = "ECALBarrel"                   
pandoralg.ReadECALEndcap                       = "ECALEndcap"                   
pandoralg.ReadECALOther                        = "ECALOther"                    
pandoralg.ReadHCALBarrel                       = "HCALBarrel"                   
pandoralg.ReadHCALEndcap                       = "HCALEndcap"                   
pandoralg.ReadHCALOther                        = "HCALOther"                    
pandoralg.ReadMUON                             = "MUON"                         
pandoralg.ReadLCAL                             = "LCAL"                         
pandoralg.ReadLHCAL                            = "LHCAL"                        
pandoralg.ReadBCAL                             = "BCAL"                         
pandoralg.ReadKinkVertices                     = "KinkVertices"                 
pandoralg.ReadProngVertices                    = "ProngVertices"                
pandoralg.ReadSplitVertices                    = "SplitVertices"                
pandoralg.ReadV0Vertices                       = "V0Vertices"                   
pandoralg.ReadTracks                           = "MarlinTrkTracks"                       
pandoralg.MCRecoCaloAssociation                = "RecoCaloAssociation_ECALBarrel"                       
pandoralg.WriteClusterCollection               = "PandoraClusters"              
pandoralg.WriteReconstructedParticleCollection = "PandoraPFOs" 
pandoralg.WriteVertexCollection                = "PandoraPFANewStartVertices"               
pandoralg.AnaOutput = "Ana.root"

pandoralg.PandoraSettingsDefault_xml = "../Pandora/PandoraSettingsDefault.xml"
#### Do not chage the collection name, only add or remove ###############
pandoralg.TrackCollections      =  ["MarlinTrkTracks"]
pandoralg.ECalCaloHitCollections=  ["ECALBarrel", "ECALEndcap", "ECALOther"]
pandoralg.HCalCaloHitCollections=  ["HCALBarrel", "HCALEndcap", "HCALOther"]
pandoralg.LCalCaloHitCollections=  ["LCAL"]
pandoralg.LHCalCaloHitCollections= ["LHCAL"]
pandoralg.MuonCaloHitCollections=  ["MUON"]
pandoralg.MCParticleCollections =  ["MCParticle"]
pandoralg.RelCaloHitCollections =  ["RecoCaloAssociation_ECALBarrel", "RecoCaloAssociation_ECALEndcap", "RecoCaloAssociation_ECALOther", "RecoCaloAssociation_HCALBarrel", "RecoCaloAssociation_HCALEndcap", "RecoCaloAssociation_HCALOther", "RecoCaloAssociation_LCAL", "RecoCaloAssociation_LHCAL", "RecoCaloAssociation_MUON"]
pandoralg.RelTrackCollections   =  ["MarlinTrkTracksMCTruthLink"]
pandoralg.KinkVertexCollections =  ["KinkVertices"]
pandoralg.ProngVertexCollections=  ["ProngVertices"]
pandoralg.SplitVertexCollections=  ["SplitVertices"]
pandoralg.V0VertexCollections   =  ["V0Vertices"]
pandoralg.ECalToMipCalibration  = 160.0 
pandoralg.HCalToMipCalibration  = 34.8 
pandoralg.ECalMipThreshold      = 0.5 
pandoralg.HCalMipThreshold      = 0.3 
pandoralg.ECalToEMGeVCalibration= 0.9 #for G2CD Digi, 1.007 for NewLDCaloDigi 
pandoralg.HCalToEMGeVCalibration= 1.007 
pandoralg.ECalToHadGeVCalibrationBarrel= 1.12 #very small effect 
pandoralg.ECalToHadGeVCalibrationEndCap= 1.12 
pandoralg.HCalToHadGeVCalibration= 1.07
pandoralg.MuonToMipCalibration= 10.0 
pandoralg.DigitalMuonHits= 0 
pandoralg.MaxHCalHitHadronicEnergy   = 1.0 
pandoralg.UseOldTrackStateCalculation= 0 
pandoralg.AbsorberRadLengthECal= 0.2854 #= 1/3.504 mm 
pandoralg.AbsorberIntLengthECal= 0.0101 #= 1/99.46 mm 
pandoralg.AbsorberRadLengthHCal= 0.0569 
pandoralg.AbsorberIntLengthHCal= 0.006  
pandoralg.AbsorberRadLengthOther= 0.0569
pandoralg.AbsorberIntLengthOther= 0.006 

##############################################################################

# write PODIO file
from Configurables import PodioOutput
write = PodioOutput("write")
write.filename = "test.root"
write.outputCommands = ["keep *"]

# ApplicationMgr
from Configurables import ApplicationMgr
ApplicationMgr(
        TopAlg = [podioinput,pandoralg],
        EvtSel = 'NONE',
        EvtMax = 10,
        ExtSvc = [dsvc, gearSvc],
        OutputLevel=INFO
)
