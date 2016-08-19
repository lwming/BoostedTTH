import FWCore.ParameterSet.Config as cms
from BoostedTTH.BoostedAnalyzer.Selection_cff import *
from BoostedTTH.BoostedAnalyzer.Inputs_cff import *
from BoostedTTH.BoostedAnalyzer.Weights_cff import *

BoostedAnalyzer = cms.EDAnalyzer(
    'BoostedAnalyzer',
    Inputs_tth_sl, # defined in Inputs_cff
    LeptonSelectionMC, # defined in Selection_cff
    DiLeptonSelectionMC, # defined in Selection_cff
    DiLeptonJetTagSelection, # defined in Selection_cff
    DiLeptonMETSelection, # defined in Selection_cff
    checkBasicMCTriggers, # defined in Selection_cff

   # weight of one event: calculated as
    # cross section * lumi / (number of generated events with positive weight  -  number of generated events with negative weight )
    # so that the sum of weights corresponds to the number of events for the given lumi
    eventWeight = cms.double(1.),
    isData = cms.bool(False),
    datasetFlag=cms.int32(0),

    # b-tag SF, defined in Weights_cff
    bTagSFs = cms.PSet(BTagSFs80X),

    # PU weights, defined in Weights_cff
    nominalPUWeight = cms.PSet(NominalPUWeight),
    additionalPUWeights = cms.VPSet(AdditionalPUWeights),

    systematics = cms.vstring(""),
    doJERsystematic = cms.bool(False),

    generatorName = cms.string("notSpecified"),

    isreHLT = cms.bool(False),

    useFatJets = cms.bool(False),
    useForwardJets = cms.bool(False),
    useGenHadronMatch = cms.bool(True),

    dumpSyncExe = cms.bool(False),
    dumpSyncExe2 = cms.bool(False),

    doBoostedMEM = cms.bool(False),

    minJetsForMEM = cms.int32(4),
    minTagsForMEM = cms.int32(3),

    selectionNames = cms.vstring("VertexSelection","DiLeptonSelection","DiLeptonJetTagSelection","MinDiLeptonMassSelection","ZVetoSelection","DiLeptonMETSelection"),
    processorNames = cms.vstring("WeightProcessor","MCMatchVarProcessor","BasicVarProcessor","TriggerVarProcessor","SpinCorrelationProcessor","AdditionalJetProcessor"),

    outfileName = cms.string("BoostedTTH"),
)
