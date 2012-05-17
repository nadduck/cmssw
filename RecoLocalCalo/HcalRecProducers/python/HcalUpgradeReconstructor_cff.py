import FWCore.ParameterSet.Config as cms

hcalupgradereco = cms.EDProducer("HcalSimpleReconstructor",
    correctionPhaseNS = cms.double(25.0), 
    digiLabel = cms.InputTag("hcalDigis"),
    Subdetector = cms.string('upgrade'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    dropZSmarkedPassed = cms.bool(True),
    firstSample = cms.int32(4),
    samplesToAdd = cms.int32(4),
    tsFromDB = cms.bool(True)
)

