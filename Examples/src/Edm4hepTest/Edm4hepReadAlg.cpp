#include "Edm4hepReadAlg.h"
#include "edm4hep/EventHeaderCollection.h"
#include "edm4hep/MCParticleCollection.h"
#include "edm4hep/SimCalorimeterHitCollection.h"
#include "edm4hep/CaloHitContributionCollection.h"

DECLARE_COMPONENT(Edm4hepReadAlg)

Edm4hepReadAlg::Edm4hepReadAlg(const std::string& name, ISvcLocator* svcLoc)
    : GaudiAlgorithm(name, svcLoc)
{
    declareProperty("HeaderCol", m_headerCol);
    declareProperty("Input_MC_Col", m_mcParCol, "MCParticle collection (input)");
    declareProperty("Input_EB_Col", m_calorimeterCol, "EcalBarrel calo hit collection (input)");
}

StatusCode Edm4hepReadAlg::initialize()
{
    debug() << "begin initialize Edm4hepReadAlg" << endmsg;
    return GaudiAlgorithm::initialize();
}

StatusCode Edm4hepReadAlg::execute()
{
    debug() << "begin execute Edm4hepReadAlg" << endmsg;

    auto mcCol = m_mcParCol.get();
    for ( auto p : *mcCol ) {
        info() << p.getObjectID().index << " : [";
        for ( auto it = p.daughters_begin(), end = p.daughters_end(); it != end; ++it ) {
            info() << " " << it->getObjectID().index;
        }
        info() << " ]; ";
    }
    info() << "}" << endmsg;

    auto caloCol = m_calorimeterCol.get();
    if(!caloCol){info() << "Error can't get m_calorimeterCol"  
               << endmsg; return StatusCode::SUCCESS;}

    info() << "total hit size " << caloCol->size() << endmsg;
    //for (auto calohit : *caloCol) {
    for (int i =0; i< caloCol->size(); i++) {
        edm4hep::CalorimeterHit calohit = caloCol->at(i);
        float en = calohit.getEnergy();
        info() << " hit en: " << en << endmsg;

    }

    return StatusCode::SUCCESS;
}

StatusCode Edm4hepReadAlg::finalize()
{
    debug() << "begin finalize Edm4hepReadAlg" << endmsg;
    return GaudiAlgorithm::finalize();
}
