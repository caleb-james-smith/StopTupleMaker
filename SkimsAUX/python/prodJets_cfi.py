
import FWCore.ParameterSet.Config as cms

prodJets = cms.EDFilter(
  "prodJets",
  jetSrc = cms.InputTag('slimmedJets'),
  jetOtherSrc = cms.InputTag('patJetsAK4PFCHS'),
  jetType = cms.string('AK4PFchs'),
  qgTaggerKey = cms.string('QGTagger'),
  vtxSrc = cms.InputTag('offlineSlimmedPrimaryVertices'),#goodVertices'),
#  metSrc = cms.InputTag('slimmedMETs'),
  bTagKeyString = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
  W_emuVec = cms.InputTag("prodGenInfo:WemuVec"),
  W_tauVec = cms.InputTag("prodGenInfo:WtauVec"),
  W_tau_emuVec = cms.InputTag("prodGenInfo:WtauemuVec"),
  W_tau_prongsVec = cms.InputTag("prodGenInfo:WtauprongsVec"),
  W_tau_nuVec = cms.InputTag("prodGenInfo:WtaunuVec"),
  genDecayLVec = cms.InputTag("prodGenInfo:genDecayLVec"),
  genDecayMomRefVec = cms.InputTag("prodGenInfo:genDecayMomRefVec"),
  eleLVec = cms.InputTag("prodElectronsNoIso:elesLVec"), 
  muLVec = cms.InputTag("prodMuonsNoIso:muonsLVec"), 
  trksForIsoVetoLVec = cms.InputTag("prodIsoTrks:trksForIsoVetoLVec"),
  looseisoTrksLVec = cms.InputTag("prodIsoTrks:looseisoTrksLVec"),
  #puppiJetsSrc = cms.InputTag("slimmedJetsPuppi"),
  puppiJetsSrc = cms.InputTag("selectedPatJetsAK8PFPuppi"),
  puppiSubJetsSrc = cms.InputTag("selectedPatJetsAK8PFPuppiSoftDropPacked"),
  ak8JetsSrc = cms.InputTag("slimmedJetsAK8"),
  #ak8SubJetsSrc = cms.InputTag("slimmedJetsAK8PFCHSSoftDropPacked"),
  ak8SubJetsSrc = cms.InputTag("slimmedJetsAK8PFPuppiSoftDropPacked","SubJets"),
  debug  = cms.bool(False),
  NjettinessAK8Puppi_label = cms.string('NjettinessAK8Puppi'),
  ak8PFJetsPuppi_label = cms.string('ak8PFJetsPuppi'),
 deepCSVBJetTags = cms.string('pfDeepCSVJetTags'),#'deepFlavourJetTags:probb'),#'deepFlavourJetTags'),
  deepFlavorBJetTags = cms.string('pfDeepFlavourJetTags'),
  deepCSVNegBJetTags = cms.string('negativeDeepFlavourJetTags'),#pfNegativeDeepCSVJetTags'),
  deepCSVPosBJetTags = cms.string('positiveDeepFlavourJetTags'),
  combinedSVBJetTags = cms.string('pfCombinedSecondaryVertexV2BJetTags'),
  combinedSVPosBJetTags = cms.string('pfPositiveCombinedSecondaryVertexV2BJetTags'),
  combinedSVNegBJetTags = cms.string('pfNegativeCombinedSecondaryVertexV2BJetTags'),
  combinedIVFSVBJetTags = cms.string('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
  combinedIVFSVPosBJetTags = cms.string('pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags'),
  combinedIVFSVNegBJetTags = cms.string('pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags'),
  simpleSVHighEffBJetTags = cms.string('pfSimpleSecondaryVertexHighEffBJetTags'),
  simpleSVNegHighEffBJetTags = cms.string('pfNegativeSimpleSecondaryVertexHighEffBJetTags'),
  simpleSVHighPurBJetTags = cms.string('pfSimpleSecondaryVertexHighPurBJetTags'),
  simpleSVNegHighPurBJetTags = cms.string('pfNegativeSimpleSecondaryVertexHighPurBJetTags'),
  softPFMuonBJetTags = cms.string('softPFMuonBJetTags'),
  softPFMuonNegBJetTags = cms.string('negativeSoftPFMuonBJetTags'),
  softPFMuonPosBJetTags = cms.string('positiveSoftPFMuonBJetTags'),
  softPFElectronBJetTags = cms.string('softPFElectronBJetTags'),
  softPFElectronNegBJetTags = cms.string('negativeSoftPFElectronBJetTags'),
  softPFElectronPosBJetTags = cms.string('positiveSoftPFElectronBJetTags'),
  doubleSVBJetTags = cms.string('pfBoostedDoubleSecondaryVertexAK8BJetTags'),
  cMVABJetTags = cms.string('pfCombinedMVABJetTags'),
  cMVAv2BJetTags = cms.string('pfCombinedMVAV2BJetTags'),
  cMVAv2NegBJetTags = cms.string('pfNegativeCombinedMVAV2BJetTags'),
  cMVAv2PosBJetTags = cms.string('pfPositiveCombinedMVAV2BJetTags'),
  CvsBCJetTags = cms.string('pfCombinedCvsBJetTags'),
  CvsBNegCJetTags = cms.string('pfNegativeCombinedCvsBJetTags'),
  CvsBPosCJetTags = cms.string('pfPositiveCombinedCvsBJetTags'),
  CvsLCJetTags = cms.string('pfCombinedCvsLJetTags'),
  CvsLNegCJetTags = cms.string('pfNegativeCombinedCvsLJetTags'),
  CvsLPosCJetTags = cms.string('pfPositiveCombinedCvsLJetTags'),
  tagInfoName = cms.string('pfDeepCSV'),#'deepNN'),
  ipTagInfos = cms.string('pfImpactParameter'),
  svTagInfos = cms.string('pfInclusiveSecondaryVertexFinder'),
  ipTagInfosCTag = cms.string('pfImpactParameter'),
  svTagInfosCTag = cms.string('pfInclusiveSecondaryVertexFinderCvsL'),
  softPFMuonTagInfosCTag = cms.string('softPFMuons'),
  softPFElectronTagInfosCTag = cms.string('softPFElectrons'),
  jetPNegBJetTags= cms.string('pfNegativeOnlyJetBProbabilityBJetTags'),
  jetPBJetTags = cms.string('pfJetBProbabilityBJetTags'),
  jetPPosBJetTags= cms.string('pfPositiveOnlyJetBProbabilityBJetTags'),
  jetBPBJetTags= cms.string('jetBPBJetTags'),
  jetBPNegBJetTags= cms.string('jetBPNegBJetTags'),
  jetBPPosBJetTags= cms.string('jetBPPosBJetTags'),
  bDiscriminatorCSV = cms.vstring('pfCombinedInclusiveSecondaryVertexV2BJetTags'
                            ,'deepFlavourJetTags:probudsg'
                            ,'deepFlavourJetTags:probb'
                            ,'deepFlavourJetTags:probc'
                            ,'deepFlavourJetTags:probbb'
                            ,'deepFlavourJetTags:probcc'
                            ,'pfDeepCSVJetTags:probb'
                            ,'pfDeepCSVJetTags:probc'
                            ,'pfDeepCSVJetTags:probudsg'
                            ,'pfDeepCSVJetTags:probbb'
                            ,'pfDeepCSVDiscriminatorsJetTags:BvsAll'
                            ,'pfDeepCSVDiscriminatorsJetTags:CvsB'
                            ,'pfDeepCSVDiscriminatorsJetTags:CvsL'
                            ),
  bDiscriminators = cms.vstring(),
  ak8JetSrc = cms.InputTag("selectedPatJetsAK8PFPuppi"),
  ak8ptCut = cms.double(170.0),
)
