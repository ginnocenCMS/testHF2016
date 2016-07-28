# /users/ginnocen/Dmeson2016pPb/DHFtrigger/V3 (CMSSW_8_0_12)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )
process.load("setup_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/ginnocen/Dmeson2016pPb/DHFtrigger/V3')
)

process.HLTPSetTobTecStepTrajectoryBuilder = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  useSameTrajFilter = cms.bool( False ),
  minNrOfHitsForRebuild = cms.int32( 4 ),
  alwaysUseInvalidHits = cms.bool( False ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepTrajectoryFilterBase" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepInOutTrajectoryFilterBase" ) ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
)
process.HLTPSetTobTecStepTrajectoryFilterBase = cms.PSet( 
  maxLostHits = cms.int32( 0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  seedPairPenalty = cms.int32( 1 ),
  minPt = cms.double( 0.1 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  strictSeedExtension = cms.bool( False ),
  seedExtension = cms.int32( 0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetTobTecStepInOutTrajectoryFilterBase = cms.PSet( 
  maxLostHits = cms.int32( 0 ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 1 ),
  minPt = cms.double( 0.1 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  strictSeedExtension = cms.bool( False ),
  seedExtension = cms.int32( 0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetLowPtStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 4 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetInitialStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPInitialStepChi2ChargeMeasurementEstimator30" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetDetachedStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 2 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  seedPairPenalty = cms.int32( 0 ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetDetachedStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetPixelPairStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 2 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  seedPairPenalty = cms.int32( 0 ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetPixelPairStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetMixedStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForMixedStep" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 2 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialForMixedStepOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetPixelLessStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 2 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 4 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTSiStripClusterChargeCutNone = cms.PSet(  value = cms.double( -1.0 ) )
process.HLTSiStripClusterChargeCutLoose = cms.PSet(  value = cms.double( 1620.0 ) )
process.HLTSiStripClusterChargeCutTight = cms.PSet(  value = cms.double( 1945.0 ) )
process.HLTPSetDetachedStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CompositeTrajectoryFilter" ),
  filters = cms.VPSet( 
    cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilterBase" )    )
  )
)
process.HLTPSetInitialStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CompositeTrajectoryFilter" ),
  filters = cms.VPSet( 
    cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilterBase" )    )
  )
)
process.HLTPSetPixelPairStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CompositeTrajectoryFilter" ),
  filters = cms.VPSet( 
    cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilterBase" )    )
  )
)
process.HLTPSetInitialStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.2 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 2 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetLowPtStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 1 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetMixedStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.4 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetPixelLessStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetJetCoreStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  pixelSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
)
process.HLTPSetJetCoreStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetJetCoreStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetJetCoreStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 50 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)

process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPPixelLessStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.11 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTobTecStepFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 30.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTobTecStepRKFitter" ),
  MinNumberOfHits = cms.int32( 7 ),
  Smoother = cms.string( "hltESPTobTecStepRKSmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPTobTecStepFitterSmoother" ),
  RejectTracks = cms.bool( True )
)
process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 30.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTobTecStepRKFitterForLoopers" ),
  MinNumberOfHits = cms.int32( 7 ),
  Smoother = cms.string( "hltESPTobTecStepRKSmootherForLoopers" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPTobTecStepFitterSmootherForLoopers" ),
  RejectTracks = cms.bool( True )
)
process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPLowPtStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.16 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKSmoother" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKSmootherForLoopers" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPDetachedStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.13 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKFitterForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer( "FlexibleKFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPTobTecStepFlexibleKFFittingSmoother" ),
  appendToDataLabel = cms.string( "" ),
  standardFitter = cms.string( "hltESPTobTecStepFitterSmoother" ),
  looperFitter = cms.string( "hltESPTobTecStepFitterSmootherForLoopers" )
)
process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTobTecStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.09 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 0.5 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MaxDisplacement = cms.double( 0.5 ),
  MaxSagitta = cms.double( 2.0 ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  MaxChi2 = cms.double( 16.0 )
)
process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 0.5 ),
  clusterChargeCut = cms.PSet(  value = cms.double( 800.0 ) ),
  MaxDisplacement = cms.double( 0.5 ),
  MaxSagitta = cms.double( 2.0 ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPInitialStepChi2ChargeMeasurementEstimator30" ),
  MaxChi2 = cms.double( 30.0 )
)
process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPTobTecStepClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPPixelLessStepClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPMixedStepClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForMixedStepOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( 0.1 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.PropagatorWithMaterialForMixedStep = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForMixedStep" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( 0.1 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltCaloStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::CaloSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1360, 1366 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltGmtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GMTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1402 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    Verbosity = cms.untracked.int32( 0 ),
    EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sL1ZeroBias = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPrePADmesonPPTrackingGlobalDpt8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( False ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    CablingMapLabel = cms.string( "" ),
    UserErrorList = cms.vint32(  )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltSiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClusters" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2 ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeNconst = cms.double( 28.5 ),
      ampErrorCalculation = cms.bool( False ),
      kPoorRecoFlagEB = cms.bool( True ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      useLumiInfoRunHeader = cms.bool( False ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      prefitMaxChiSqEB = cms.double( 15.0 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      timealgo = cms.string( "None" ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      EEtimeNconst = cms.double( 31.8 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      doPrefitEE = cms.bool( True ),
      doPrefitEB = cms.bool( True )
    )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet( 
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    ExpectedOrbitMessageTime = cms.untracked.int32( -1 ),
    FilterDataQuality = cms.bool( True ),
    silent = cms.untracked.bool( True ),
    HcalFirstFED = cms.untracked.int32( 700 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    ElectronicsMap = cms.string( "" ),
    UnpackCalib = cms.untracked.bool( True ),
    FEDs = cms.untracked.vint32(  ),
    UnpackerMode = cms.untracked.int32( 0 ),
    UnpackTTP = cms.untracked.bool( False ),
    lastSample = cms.int32( 9 ),
    UnpackZDC = cms.untracked.bool( True ),
    firstSample = cms.int32( 0 )
)
process.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
    pedestalUpperLimit = cms.double( 2.7 ),
    timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
    pedestalSubtractionType = cms.int32( 1 ),
    respCorrM3 = cms.double( 0.95 ),
    timeSlewParsType = cms.int32( 3 ),
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 3 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( True ),
    Subdetector = cms.string( "HBHE" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    pulseShapeParameters = cms.PSet( 
      MinimumChargeThreshold = cms.double( 20.0 ),
      TS4TS5ChargeThreshold = cms.double( 70.0 ),
      TrianglePeakTS = cms.uint32( 0 ),
      LinearThreshold = cms.vdouble(  ),
      LinearCut = cms.vdouble(  ),
      LeftSlopeThreshold = cms.vdouble(  ),
      LeftSlopeCut = cms.vdouble(  ),
      RightSlopeCut = cms.vdouble(  ),
      RightSlopeSmallThreshold = cms.vdouble(  ),
      RightSlopeSmallCut = cms.vdouble(  ),
      MinimumTS4TS5Threshold = cms.double( 100.0 ),
      TS4TS5UpperThreshold = cms.vdouble( 70.0, 90.0, 100.0, 400.0 ),
      TS4TS5UpperCut = cms.vdouble( 1.0, 0.8, 0.75, 0.72 ),
      TS4TS5LowerThreshold = cms.vdouble( 100.0, 120.0, 160.0, 200.0, 300.0, 500.0 ),
      TS4TS5LowerCut = cms.vdouble( -1.0, -0.7, -0.5, -0.4, -0.3, 0.1 ),
      UseDualFit = cms.bool( False ),
      TriangleIgnoreSlow = cms.bool( False ),
      TS3TS4ChargeThreshold = cms.double( 70.0 ),
      TS3TS4UpperChargeThreshold = cms.double( 20.0 ),
      TS5TS6ChargeThreshold = cms.double( 70.0 ),
      TS5TS6UpperChargeThreshold = cms.double( 20.0 ),
      R45PlusOneRange = cms.double( 0.2 ),
      R45MinusOneRange = cms.double( 0.2 ),
      RMS8MaxThreshold = cms.vdouble(  ),
      RMS8MaxCut = cms.vdouble(  ),
      RightSlopeThreshold = cms.vdouble(  )
    ),
    timingshapedcutsParameters = cms.PSet( 
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
    ),
    ts4Min = cms.double( 5.0 ),
    ts3chi2 = cms.double( 5.0 ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet( 
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      )
    ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet( 
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    )
)
process.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
    pedestalUpperLimit = cms.double( 2.7 ),
    timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
    pedestalSubtractionType = cms.int32( 1 ),
    respCorrM3 = cms.double( 0.95 ),
    timeSlewParsType = cms.int32( 3 ),
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 2 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet( 
      hflongEthresh = cms.double( 40.0 ),
      hflongMinWindowTime = cms.vdouble( -10.0 ),
      hfshortEthresh = cms.double( 40.0 ),
      hflongMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMinWindowTime = cms.vdouble( -12.0 )
    ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 1 ),
    digistat = cms.PSet( 
      HFdigiflagFirstSample = cms.int32( 1 ),
      HFdigiflagMinEthreshold = cms.double( 40.0 ),
      HFdigiflagSamplesToAdd = cms.int32( 3 ),
      HFdigiflagExpectedPeak = cms.int32( 2 ),
      HFdigiflagCoef = cms.vdouble( 0.93, -0.012667, -0.38275 )
    ),
    hfTimingTrustParameters = cms.PSet( 
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    PETstat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_R_29 = cms.vdouble( 0.8 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble( 0.8 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_R = cms.vdouble( 0.98 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    correctForPhaseContainment = cms.bool( False ),
    correctForTimeslew = cms.bool( False ),
    setNoiseFlags = cms.bool( True ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HF" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 2 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    pulseShapeParameters = cms.PSet(  ),
    timingshapedcutsParameters = cms.PSet(  ),
    ts4Min = cms.double( 5.0 ),
    ts3chi2 = cms.double( 5.0 ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(  ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(  )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    pedestalUpperLimit = cms.double( 2.7 ),
    timeSlewPars = cms.vdouble( 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0, 12.2999, -2.19142, 0.0 ),
    pedestalSubtractionType = cms.int32( 1 ),
    respCorrM3 = cms.double( 0.95 ),
    timeSlewParsType = cms.int32( 3 ),
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HO" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    pulseShapeParameters = cms.PSet(  ),
    timingshapedcutsParameters = cms.PSet(  ),
    ts4Min = cms.double( 5.0 ),
    ts3chi2 = cms.double( 5.0 ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(  ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HcalPhase = cms.int32( 0 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    UseRejectedHitsOnly = cms.bool( False ),
    EBThreshold = cms.double( 0.07 ),
    HEDGrid = cms.vdouble(  ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltAK4CaloJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( 0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.4 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    useMassDropTagger = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    subtractorName = cms.string( "" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    useTrimming = cms.bool( False ),
    muMax = cms.double( -1.0 ),
    yMin = cms.double( -1.0 ),
    useFiltering = cms.bool( False ),
    rFilt = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    dRMin = cms.double( -1.0 ),
    nFilt = cms.int32( -1 ),
    usePruning = cms.bool( False ),
    maxDepth = cms.int32( -1 ),
    yCut = cms.double( -1.0 ),
    DzTrVtxMax = cms.double( 0.0 ),
    UseOnlyOnePV = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    trimPtFracMin = cms.double( -1.0 ),
    dRMax = cms.double( -1.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False )
)
process.hltAK4CaloJetsIDPassed = cms.EDProducer( "HLTCaloJetIDProducer",
    min_N90 = cms.int32( -2 ),
    min_N90hits = cms.int32( 2 ),
    min_EMF = cms.double( 1.0E-6 ),
    jetsInput = cms.InputTag( "hltAK4CaloJets" ),
    JetIDParams = cms.PSet( 
      useRecHits = cms.bool( True ),
      hbheRecHitsColl = cms.InputTag( "hltHbhereco" ),
      hoRecHitsColl = cms.InputTag( "hltHoreco" ),
      hfRecHitsColl = cms.InputTag( "hltHfreco" ),
      ebRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      eeRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
    ),
    max_EMF = cms.double( 999.0 )
)
process.hltFixedGridRhoFastjetAllCalo = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltAK4CaloFastJetCorrector = cms.EDProducer( "L1FastjetCorrectorProducer",
    srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L1FastJet" )
)
process.hltAK4CaloRelativeCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L2Relative" )
)
process.hltAK4CaloAbsoluteCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L3Absolute" )
)
process.hltAK4CaloResidualCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L2L3Residual" )
)
process.hltAK4CaloCorrector = cms.EDProducer( "ChainedJetCorrectorProducer",
    correctors = cms.VInputTag( 'hltAK4CaloFastJetCorrector','hltAK4CaloRelativeCorrector','hltAK4CaloAbsoluteCorrector','hltAK4CaloResidualCorrector' )
)
process.hltAK4CaloJetsCorrected = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltAK4CaloJets" ),
    correctors = cms.VInputTag( 'hltAK4CaloCorrector' )
)
process.hltAK4CaloJetsCorrectedIDPassed = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltAK4CaloJetsIDPassed" ),
    correctors = cms.VInputTag( 'hltAK4CaloCorrector' )
)
process.hltPAJetsForCoreTracking = cms.EDFilter( "CandPtrSelector",
    src = cms.InputTag( "hltAK4CaloJetsCorrectedIDPassed" ),
    cut = cms.string( "pt > 100 && abs(eta) < 2.5" )
)
process.hltSiPixelClustersAfterSplitting = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltSiPixelClustersCacheAfterSplitting = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHitsAfterSplitting = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltPixelLayerTripletsAfterSplitting = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      PedestalSubtractionFedMode = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      useCMMeanMap = cms.bool( False )
    ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    onDemand = cms.bool( True )
)
process.hltSiStripClustersAfterSplitting = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
    pixelClusterProducer = cms.string( "hltSiPixelClustersAfterSplitting" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" )
)
process.hltPAIter0PixelTripletsSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.02 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        ptMin = cms.double( 0.6 ),
        nSigmaZ = cms.double( 4.0 ),
        useMultipleScattering = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTripletsAfterSplitting" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRZtolerance = cms.double( 0.037 ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
        ),
        maxElement = cms.uint32( 1000000 )
      ),
      maxElement = cms.uint32( 1000000 )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 )
    )
)
process.hltPAIter0CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter0PixelTripletsSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersAfterSplitting" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter0CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter0CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersAfterSplitting" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "initialStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter0PrimaryVertices = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxNormalizedChi2 = cms.double( 20.0 ),
      minPt = cms.double( 0.0 ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 5.0 ),
      trackQuality = cms.string( "any" ),
      minPixelLayersWithHits = cms.int32( 2 ),
      minSiliconLayersWithHits = cms.int32( 5 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltPAIter0CtfWithMaterialTracks" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        vertexSize = cms.double( 0.01 ),
        d0CutOff = cms.double( 3.0 ),
        Tmin = cms.double( 4.0 ),
        dzCutOff = cms.double( 4.0 ),
        coolingFactor = cms.double( 0.6 )
      ),
      algorithm = cms.string( "DA_vect" )
    )
)
process.hltPAIter0TrackClassifier1 = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter0CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter0_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.9, -0.8, 0.7 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter0TrackClassifier2 = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltPAIter0CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter3_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.5, 0.0, 0.5 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter0TrackClassifier3 = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter0CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter1_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.6, -0.3, -0.1 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter0TrackSelection = cms.EDProducer( "ClassifierMerger",
    inputClassifiers = cms.vstring( 'hltPAIter0TrackClassifier1',
      'hltPAIter0TrackClassifier2',
      'hltPAIter0TrackClassifier3' )
)
process.hltPAIter1ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( 'hltPAIter0TrackSelection','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltPAIter0CtfWithMaterialTracks" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltPAIter1MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltPAIter1ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersAfterSplitting" )
)
process.hltPAIter1DetachedTripletLayers = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter1ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter1ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltPAIter1DetachedTripletSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 1.5 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        ptMin = cms.double( 0.3 ),
        useMultipleScattering = cms.bool( False ),
        originHalfLength = cms.double( 15.0 )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      FilterStripHits = cms.bool( False ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
    ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter1DetachedTripletLayers" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 1000000 ),
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        ComponentName = cms.string( "PixelTripletLargeTipGenerator" ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRZtolerance = cms.double( 0.037 )
      )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 )
    )
)
process.hltPAIter1CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter1DetachedTripletSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPDetachedStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter1MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter1CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter1CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter1MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "detachedTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter1TrackClassifier1 = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltPAIter1CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter3_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.5, 0.0, 0.5 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter1TrackClassifier2 = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter1CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter0_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.2, 0.0, 0.4 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter1TrackSelection = cms.EDProducer( "ClassifierMerger",
    inputClassifiers = cms.vstring( 'hltPAIter1TrackClassifier1',
      'hltPAIter1TrackClassifier2' )
)
process.hltPAIter2ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( 'hltPAIter1TrackSelection','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltPAIter1CtfWithMaterialTracks" ),
    oldClusterRemovalInfo = cms.InputTag( "hltPAIter1ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltPAIter2MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltPAIter2ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersAfterSplitting" )
)
process.hltPAIter2LowPtTripletLayers = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter2ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter2ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltPAIter2LowPtTripletSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.02 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        ptMin = cms.double( 0.2 ),
        useMultipleScattering = cms.bool( False ),
        nSigmaZ = cms.double( 4.0 )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter2LowPtTripletLayers" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 1000000 ),
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRZtolerance = cms.double( 0.037 ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
        )
      )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 )
    )
)
process.hltPAIter2CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter2LowPtTripletSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPLowPtStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter2MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter2CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter2CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter2MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "lowPtTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter2TrackSelection = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter2CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter1_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.6, -0.3, -0.1 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter3ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( 'hltPAIter2TrackSelection','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltPAIter2CtfWithMaterialTracks" ),
    oldClusterRemovalInfo = cms.InputTag( "hltPAIter2ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltPAIter3MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltPAIter3ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersAfterSplitting" )
)
process.hltPAIter3PixelPairLayers = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter3ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter3ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltPAIter3PixelPairSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        ptMin = cms.double( 0.6 ),
        useFixedError = cms.bool( True ),
        originRadius = cms.double( 0.015 ),
        sigmaZVertex = cms.double( 3.0 ),
        fixedError = cms.double( 0.03 ),
        VertexCollection = cms.InputTag( "hltPAIter0PrimaryVertices" ),
        useFoundVertices = cms.bool( True ),
        useFakeVertices = cms.bool( False ),
        nSigmaZ = cms.double( 4.0 ),
        useMultipleScattering = cms.bool( True )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      FilterStripHits = cms.bool( False ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
    ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter3PixelPairLayers" )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 )
    )
)
process.hltPAIter3CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter3PixelPairSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter3MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter3CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter3CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter3MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "pixelPairStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter3TrackSelection = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter3CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter2_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.2, 0.0, 0.3 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter4ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( 'hltPAIter3TrackSelection','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltPAIter3CtfWithMaterialTracks" ),
    oldClusterRemovalInfo = cms.InputTag( "hltPAIter3ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltPAIter4MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltPAIter4ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersAfterSplitting" )
)
process.hltPAIter4MixedTripletLayersA = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      maxRing = cms.int32( 1 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      skipClusters = cms.InputTag( "hltPAIter4ClustersRefRemoval" ),
      minRing = cms.int32( 1 )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter4ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter4ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltPAIter4MixedTripletSeedsA = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 1.5 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        originHalfLength = cms.double( 15.0 ),
        ptMin = cms.double( 0.4 ),
        useMultipleScattering = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      FilterStripHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "hltESPMixedStepClusterShapeHitFilter" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
    ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter4MixedTripletLayersA" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 100000 ),
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        ComponentName = cms.string( "PixelTripletLargeTipGenerator" ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        useMultScattering = cms.bool( True ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRZtolerance = cms.double( 0.0 )
      )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 )
    )
)
process.hltPAIter4MixedTripletLayersB = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix2+BPix3+TIB1' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" ),
      skipClusters = cms.InputTag( "hltPAIter4ClustersRefRemoval" )
    ),
    TIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      skipClusters = cms.InputTag( "hltPAIter4ClustersRefRemoval" )
    )
)
process.hltPAIter4MixedTripletSeedsB = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 1.5 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        originHalfLength = cms.double( 10.0 ),
        ptMin = cms.double( 0.6 ),
        useMultipleScattering = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( False ),
      FilterPixelHits = cms.bool( True ),
      FilterStripHits = cms.bool( True ),
      ClusterShapeHitFilterName = cms.string( "hltESPMixedStepClusterShapeHitFilter" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
    ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter4MixedTripletLayersB" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 100000 ),
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        ComponentName = cms.string( "PixelTripletLargeTipGenerator" ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        useMultScattering = cms.bool( True ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRZtolerance = cms.double( 0.0 )
      )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterial" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      maxseeds = cms.int32( 10000 )
    )
)
process.hltPAIter4MixedSeeds = cms.EDProducer( "SeedCombiner",
    seedCollections = cms.VInputTag( 'hltPAIter4MixedTripletSeedsA','hltPAIter4MixedTripletSeedsB' )
)
process.hltPAIter4CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter4MixedSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPMixedStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter4MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter4CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter4CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter4MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "mixedTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter4TrackClassifier1 = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltPAIter4CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter4_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.5, 0.0, 0.5 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter4TrackClassifier2 = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter4CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter0_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.2, -0.2, -0.2 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter4TrackSelection = cms.EDProducer( "ClassifierMerger",
    inputClassifiers = cms.vstring( 'hltPAIter4TrackClassifier1',
      'hltPAIter4TrackClassifier2' )
)
process.hltPAIter5ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( 'hltPAIter4TrackSelection','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltPAIter4CtfWithMaterialTracks" ),
    oldClusterRemovalInfo = cms.InputTag( "hltPAIter4ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltPAIter5MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltPAIter5ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersAfterSplitting" )
)
process.hltPAIter5PixelLessLayers = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'TIB1+TIB2+MTIB3',
      'TIB1+TIB2+MTIB4',
      'TIB1+TIB2+MTID1_pos',
      'TIB1+TIB2+MTID1_neg',
      'TID1_pos+TID2_pos+TID3_pos',
      'TID1_neg+TID2_neg+TID3_neg',
      'TID1_pos+TID2_pos+MTID3_pos',
      'TID1_neg+TID2_neg+MTID3_neg',
      'TID1_pos+TID2_pos+MTEC1_pos',
      'TID1_neg+TID2_neg+MTEC1_neg',
      'TID2_pos+TID3_pos+TEC1_pos',
      'TID2_neg+TID3_neg+TEC1_neg',
      'TID2_pos+TID3_pos+MTEC1_pos',
      'TID2_neg+TID3_neg+MTEC1_neg',
      'TEC1_pos+TEC2_pos+TEC3_pos',
      'TEC1_neg+TEC2_neg+TEC3_neg',
      'TEC1_pos+TEC2_pos+MTEC3_pos',
      'TEC1_neg+TEC2_neg+MTEC3_neg',
      'TEC1_pos+TEC2_pos+TEC4_pos',
      'TEC1_neg+TEC2_neg+TEC4_neg',
      'TEC1_pos+TEC2_pos+MTEC4_pos',
      'TEC1_neg+TEC2_neg+MTEC4_neg',
      'TEC2_pos+TEC3_pos+TEC4_pos',
      'TEC2_neg+TEC3_neg+TEC4_neg',
      'TEC2_pos+TEC3_pos+MTEC4_pos',
      'TEC2_neg+TEC3_neg+MTEC4_neg',
      'TEC2_pos+TEC3_pos+TEC5_pos',
      'TEC2_neg+TEC3_neg+TEC5_neg',
      'TEC2_pos+TEC3_pos+TEC6_pos',
      'TEC2_neg+TEC3_neg+TEC6_neg',
      'TEC3_pos+TEC4_pos+TEC5_pos',
      'TEC3_neg+TEC4_neg+TEC5_neg',
      'TEC3_pos+TEC4_pos+MTEC5_pos',
      'TEC3_neg+TEC4_neg+MTEC5_neg',
      'TEC3_pos+TEC5_pos+TEC6_pos',
      'TEC3_neg+TEC5_neg+TEC6_neg',
      'TEC4_pos+TEC5_pos+TEC6_pos',
      'TEC4_neg+TEC5_neg+TEC6_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      maxRing = cms.int32( 2 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      skipClusters = cms.InputTag( "hltPAIter5ClustersRefRemoval" ),
      minRing = cms.int32( 1 )
    ),
    MTID = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter5ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      minRing = cms.int32( 3 ),
      maxRing = cms.int32( 3 ),
      useRingSlector = cms.bool( True )
    ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter5ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      minRing = cms.int32( 3 ),
      maxRing = cms.int32( 3 ),
      useRingSlector = cms.bool( True )
    ),
    MTIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter5ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    ),
    TID = cms.PSet( 
      skipClusters = cms.InputTag( "hltPAIter5ClustersRefRemoval" ),
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      minRing = cms.int32( 1 ),
      maxRing = cms.int32( 2 )
    ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(  ),
    TIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      skipClusters = cms.InputTag( "hltPAIter5ClustersRefRemoval" )
    )
)
process.hltPAIter5PixelLessSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 1.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        originHalfLength = cms.double( 12.0 ),
        ptMin = cms.double( 0.4 ),
        useMultipleScattering = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "CombinedSeedComparitor" ),
      mode = cms.string( "and" ),
      comparitors = cms.VPSet( 
        cms.PSet(  ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
          FilterAtHelixStage = cms.bool( True ),
          FilterPixelHits = cms.bool( False ),
          FilterStripHits = cms.bool( True ),
          ClusterShapeHitFilterName = cms.string( "hltESPPixelLessStepClusterShapeHitFilter" ),
          ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
        ),
        cms.PSet(  ComponentName = cms.string( "StripSubClusterShapeSeedFilter" ),
          FilterAtHelixStage = cms.bool( False ),
          maxNSat = cms.uint32( 3 ),
          trimMaxADC = cms.double( 30.0 ),
          trimMaxFracTotal = cms.double( 0.15 ),
          trimMaxFracNeigh = cms.double( 0.25 ),
          maxTrimmedSizeDiffPos = cms.double( 0.7 ),
          maxTrimmedSizeDiffNeg = cms.double( 1.0 ),
          subclusterWindow = cms.double( 0.7 ),
          seedCutMIPs = cms.double( 0.35 ),
          seedCutSN = cms.double( 7.0 ),
          subclusterCutMIPs = cms.double( 0.45 ),
          subclusterCutSN = cms.double( 12.0 )
        )
      )
    ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardMultiHitGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter5PixelLessLayers" ),
      GeneratorPSet = cms.PSet( 
        ComponentName = cms.string( "MultiHitGeneratorFromChi2" ),
        maxElement = cms.uint32( 1000000 ),
        useFixedPreFiltering = cms.bool( False ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        extraHitRZtolerance = cms.double( 0.0 ),
        extraZKDBox = cms.double( 0.2 ),
        extraRKDBox = cms.double( 0.2 ),
        extraPhiKDBox = cms.double( 0.005 ),
        fnSigmaRZ = cms.double( 2.0 ),
        refitHits = cms.bool( True ),
        ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        maxChi2 = cms.double( 5.0 ),
        chi2VsPtCut = cms.bool( True ),
        pt_interv = cms.vdouble( 0.4, 0.7, 1.0, 2.0 ),
        chi2_cuts = cms.vdouble( 3.0, 4.0, 5.0, 5.0 ),
        detIdsToDebug = cms.vint32( 0, 0, 0 )
      )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterial" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 2.0 ),
      maxseeds = cms.int32( 1000000 )
    )
)
process.hltPAIter5CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter5PixelLessSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPPixelLessStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter5MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter5CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter5CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter5MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "pixelLessStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter5TrackClassifier1 = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter5CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter5_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.4, 0.0, 0.4 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter5TrackClassifier2 = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter5CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter0_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( 0.0, 0.0, 0.0 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter5TrackSelection = cms.EDProducer( "ClassifierMerger",
    inputClassifiers = cms.vstring( 'hltPAIter5TrackClassifier1',
      'hltPAIter5TrackClassifier2' )
)
process.hltPAIter6ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( 'hltPAIter5TrackSelection','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltPAIter5CtfWithMaterialTracks" ),
    oldClusterRemovalInfo = cms.InputTag( "hltPAIter5ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltPAIter6MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltPAIter6ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClustersAfterSplitting" )
)
process.hltPAIter6TobTecLayersTripl = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'TOB1+TOB2+MTOB3',
      'TOB1+TOB2+MTOB4',
      'TOB1+TOB2+MTEC1_pos',
      'TOB1+TOB2+MTEC1_neg' ),
    MTOB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter6ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter6ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      minRing = cms.int32( 6 ),
      maxRing = cms.int32( 7 ),
      useRingSlector = cms.bool( True )
    ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter6ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    ),
    BPix = cms.PSet(  ),
    TIB = cms.PSet(  )
)
process.hltPAIter6TobTecSeedsTripl = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 3.5 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        originHalfLength = cms.double( 20.0 ),
        ptMin = cms.double( 0.55 ),
        useMultipleScattering = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "CombinedSeedComparitor" ),
      mode = cms.string( "and" ),
      comparitors = cms.VPSet( 
        cms.PSet(  ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
          FilterPixelHits = cms.bool( False ),
          FilterStripHits = cms.bool( True ),
          ClusterShapeHitFilterName = cms.string( "hltESPTobTecStepClusterShapeHitFilter" ),
          ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" ),
          FilterAtHelixStage = cms.bool( True )
        ),
        cms.PSet(  ComponentName = cms.string( "StripSubClusterShapeSeedFilter" ),
          FilterAtHelixStage = cms.bool( False ),
          maxNSat = cms.uint32( 3 ),
          trimMaxADC = cms.double( 30.0 ),
          trimMaxFracTotal = cms.double( 0.15 ),
          trimMaxFracNeigh = cms.double( 0.25 ),
          maxTrimmedSizeDiffPos = cms.double( 0.7 ),
          maxTrimmedSizeDiffNeg = cms.double( 1.0 ),
          subclusterWindow = cms.double( 0.7 ),
          seedCutMIPs = cms.double( 0.35 ),
          seedCutSN = cms.double( 7.0 ),
          subclusterCutMIPs = cms.double( 0.45 ),
          subclusterCutSN = cms.double( 12.0 )
        )
      )
    ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardMultiHitGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter6TobTecLayersTripl" ),
      GeneratorPSet = cms.PSet( 
        ComponentName = cms.string( "MultiHitGeneratorFromChi2" ),
        maxElement = cms.uint32( 1000000 ),
        useFixedPreFiltering = cms.bool( False ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        extraHitRZtolerance = cms.double( 0.0 ),
        extraZKDBox = cms.double( 0.2 ),
        extraRKDBox = cms.double( 0.2 ),
        extraPhiKDBox = cms.double( 0.01 ),
        fnSigmaRZ = cms.double( 2.0 ),
        refitHits = cms.bool( True ),
        ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
        TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        maxChi2 = cms.double( 5.0 ),
        chi2VsPtCut = cms.bool( True ),
        pt_interv = cms.vdouble( 0.4, 0.7, 1.0, 2.0 ),
        chi2_cuts = cms.vdouble( 3.0, 4.0, 5.0, 5.0 ),
        detIdsToDebug = cms.vint32( 0, 0, 0 )
      )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterial" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      maxseeds = cms.int32( 1000000 )
    )
)
process.hltPAIter6TobTecLayersPair = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'TOB1+TEC1_pos',
      'TOB1+TEC1_neg',
      'TEC1_pos+TEC2_pos',
      'TEC1_neg+TEC2_neg',
      'TEC2_pos+TEC3_pos',
      'TEC2_neg+TEC3_neg',
      'TEC3_pos+TEC4_pos',
      'TEC3_neg+TEC4_neg',
      'TEC4_pos+TEC5_pos',
      'TEC4_neg+TEC5_neg',
      'TEC5_pos+TEC6_pos',
      'TEC5_neg+TEC6_neg',
      'TEC6_pos+TEC7_pos',
      'TEC6_neg+TEC7_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter6ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
      useRingSlector = cms.bool( True ),
      minRing = cms.int32( 5 ),
      maxRing = cms.int32( 5 )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(  ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      skipClusters = cms.InputTag( "hltPAIter6ClustersRefRemoval" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) )
    ),
    BPix = cms.PSet(  ),
    TIB = cms.PSet(  )
)
process.hltPAIter6TobTecSeedsPair = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 6.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        originHalfLength = cms.double( 30.0 ),
        ptMin = cms.double( 0.6 ),
        useMultipleScattering = cms.bool( False )
      )
    ),
    SeedComparitorPSet = cms.PSet( 
      ComponentName = cms.string( "CombinedSeedComparitor" ),
      mode = cms.string( "and" ),
      comparitors = cms.VPSet( 
        cms.PSet(  ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
          FilterAtHelixStage = cms.bool( True ),
          FilterPixelHits = cms.bool( False ),
          FilterStripHits = cms.bool( True ),
          ClusterShapeHitFilterName = cms.string( "hltESPTobTecStepClusterShapeHitFilter" ),
          ClusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCacheAfterSplitting" )
        ),
        cms.PSet(  ComponentName = cms.string( "StripSubClusterShapeSeedFilter" ),
          FilterAtHelixStage = cms.bool( False ),
          maxNSat = cms.uint32( 3 ),
          trimMaxADC = cms.double( 30.0 ),
          trimMaxFracTotal = cms.double( 0.15 ),
          trimMaxFracNeigh = cms.double( 0.25 ),
          maxTrimmedSizeDiffPos = cms.double( 0.7 ),
          maxTrimmedSizeDiffNeg = cms.double( 1.0 ),
          subclusterWindow = cms.double( 0.7 ),
          seedCutMIPs = cms.double( 0.35 ),
          seedCutSN = cms.double( 7.0 ),
          subclusterCutMIPs = cms.double( 0.45 ),
          subclusterCutSN = cms.double( 12.0 )
        )
      )
    ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter6TobTecLayersPair" )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterial" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      maxseeds = cms.int32( 1000000 )
    )
)
process.hltPAIter6TobTecSeeds = cms.EDProducer( "SeedCombiner",
    seedCollections = cms.VInputTag( 'hltPAIter6TobTecSeedsTripl','hltPAIter6TobTecSeedsPair' )
)
process.hltPAIter6CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter6TobTecSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTobTecStepTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter6MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter6CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter6CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltPAIter6MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPTobTecStepFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "tobTecStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter6TrackClassifier1 = cms.EDProducer( "TrackMVAClassifierDetached",
    src = cms.InputTag( "hltPAIter6CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter6_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.6, -0.45, -0.3 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter6TrackClassifier2 = cms.EDProducer( "TrackMVAClassifierPrompt",
    src = cms.InputTag( "hltPAIter6CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "MVASelectorIter0_13TeV" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    qualityCuts = cms.vdouble( 0.0, 0.0, 0.0 ),
    mva = cms.PSet(  ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIter6TrackSelection = cms.EDProducer( "ClassifierMerger",
    inputClassifiers = cms.vstring( 'hltPAIter6TrackClassifier1',
      'hltPAIter6TrackClassifier2' )
)
process.hltPAIter7GoodPrimaryVertices = cms.EDFilter( "PrimaryVertexObjectFilter",
    src = cms.InputTag( "hltPAIter0PrimaryVertices" ),
    filterParams = cms.PSet( 
      maxZ = cms.double( 15.0 ),
      minNdof = cms.double( 25.0 ),
      maxRho = cms.double( 2.0 )
    )
)
process.hltPAIter7JetCoreLayers = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'BPix3+TIB1',
      'BPix3+TIB2' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      hitErrorRZ = cms.double( 0.0036 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      hitErrorRZ = cms.double( 0.006 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltSiPixelRecHitsAfterSplitting" )
    ),
    TIB = cms.PSet( 
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    )
)
process.hltPAIter7JetCoreSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        ptMin = cms.double( 10.0 ),
        originRadius = cms.double( 0.2 ),
        originHalfLength = cms.double( 0.2 ),
        deltaPhiRegion = cms.double( 0.2 ),
        measurementTrackerName = cms.string( "" ),
        deltaEtaRegion = cms.double( 0.2 ),
        JetSrc = cms.InputTag( "hltPAJetsForCoreTracking" ),
        vertexSrc = cms.InputTag( "hltPAIter7GoodPrimaryVertices" ),
        howToUseMeasurementTracker = cms.string( "Never" )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      MaxNumberOfPixelClusters = cms.uint32( 40000 ),
      cut = cms.string( "strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)" ),
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClustersAfterSplitting" ),
      MaxNumberOfCosmicClusters = cms.uint32( 400000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClustersAfterSplitting" )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 1000000 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.InputTag( "hltPAIter7JetCoreLayers" )
    ),
    SeedCreatorPSet = cms.PSet( 
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( True ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      maxseeds = cms.int32( 10000 )
    )
)
process.hltPAIter7CkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltPAIter7JetCoreSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 10000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersAfterSplitting" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetJetCoreStepTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltPAIter7CtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltPAIter7CkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClustersAfterSplitting" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "jetCoreRegionalStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltPAIter7TrackSelection = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltPAIter7CtfWithMaterialTracks" ),
    GBRForestLabel = cms.string( "" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltPAIter7GoodPrimaryVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet( 
      dr_par = cms.PSet( 
        dr_par1 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
        drWPVerr_par = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 ),
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_exp = cms.vint32( 2147483647, 2147483647, 2147483647 )
      ),
      minLayers = cms.vint32( 3, 5, 5 ),
      dz_par = cms.PSet( 
        dz_exp = cms.vint32( 2147483647, 2147483647, 2147483647 ),
        dz_par1 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
        dzWPVerr_par = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 )
      ),
      maxChi2 = cms.vdouble( 9999.0, 9999.0, 9999.0 ),
      maxChi2n = cms.vdouble( 1.6, 1.0, 0.7 ),
      maxLostLayers = cms.vint32( 4, 3, 2 ),
      maxDz = cms.vdouble( 0.5, 0.35, 0.2 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      maxDr = cms.vdouble( 0.3, 0.2, 0.1 ),
      minNdof = cms.vdouble( -1.0, -1.0, -1.0 ),
      min3DLayers = cms.vint32( 1, 2, 3 ),
      minPixelHits = cms.vint32( 1, 1, 1 ),
      minNVtxTrk = cms.int32( 2 )
    ),
    GBRForestFileName = cms.string( "" )
)
process.hltPAIterativeTrackingMerged = cms.EDProducer( "TrackCollectionMerger",
    shareFrac = cms.double( 0.19 ),
    inputClassifiers = cms.vstring( 'hltPAIter0TrackSelection',
      'hltPAIter7TrackSelection',
      'hltPAIter1TrackSelection',
      'hltPAIter2TrackSelection',
      'hltPAIter3TrackSelection',
      'hltPAIter4TrackSelection',
      'hltPAIter5TrackSelection',
      'hltPAIter6TrackSelection' ),
    minQuality = cms.string( "loose" ),
    minShareHits = cms.uint32( 2 ),
    allowFirstHitShare = cms.bool( True ),
    foundHitBonus = cms.double( 10.0 ),
    trackProducers = cms.VInputTag( 'hltPAIter0CtfWithMaterialTracks','hltPAIter7CtfWithMaterialTracks','hltPAIter1CtfWithMaterialTracks','hltPAIter2CtfWithMaterialTracks','hltPAIter3CtfWithMaterialTracks','hltPAIter4CtfWithMaterialTracks','hltPAIter5CtfWithMaterialTracks','hltPAIter6CtfWithMaterialTracks' ),
    lostHitPenalty = cms.double( 5.0 )
)
process.hltPAOnlinePrimaryVertices = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "" )
      ),
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( True ),
        minNdof = cms.double( 2.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "WithBS" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxNormalizedChi2 = cms.double( 20.0 ),
      minPt = cms.double( 0.0 ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 5.0 ),
      trackQuality = cms.string( "any" ),
      minPixelLayersWithHits = cms.int32( 2 ),
      minSiliconLayersWithHits = cms.int32( 5 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltPAIterativeTrackingMerged" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        vertexSize = cms.double( 0.01 ),
        d0CutOff = cms.double( 3.0 ),
        Tmin = cms.double( 4.0 ),
        dzCutOff = cms.double( 4.0 ),
        coolingFactor = cms.double( 0.6 )
      ),
      algorithm = cms.string( "DA_vect" )
    )
)
process.hltPAFullCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltPAIterativeTrackingMerged" ),
    particleType = cms.string( "pi+" )
)
process.hltPAFullTrackFilterForDmeson = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    saveTags = cms.bool( True ),
    MinTrks = cms.int32( 0 ),
    MinPt = cms.double( 0.0 ),
    MaxVz = cms.double( 9999.0 ),
    MaxEta = cms.double( 9999.0 ),
    trackCollection = cms.InputTag( "hltPAFullCands" ),
    vertexCollection = cms.InputTag( "hltPAOnlinePrimaryVertices" ),
    MaxPt = cms.double( 10000.0 ),
    MinSep = cms.double( 999.0 )
)
process.hltPAtktkVtxForDmesonDpt8 = cms.EDProducer( "HLTDisplacedtktkVtxProducer",
    Src = cms.InputTag( "hltPAFullCands" ),
    massParticle1 = cms.double( 0.1396 ),
    PreviousCandTag = cms.InputTag( "hltPAFullTrackFilterForDmeson" ),
    massParticle2 = cms.double( 0.4937 ),
    ChargeOpt = cms.int32( -1 ),
    MaxEta = cms.double( 2.5 ),
    MaxInvMass = cms.double( 2.27 ),
    MinPtPair = cms.double( 8.0 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinInvMass = cms.double( 1.47 ),
    MinPt = cms.double( 0.0 )
)
process.hltPAtktkFilterForDmesonDpt8 = cms.EDFilter( "HLTDisplacedtktkFilter",
    saveTags = cms.bool( True ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinVtxProbability = cms.double( 0.0 ),
    MaxLxySignificance = cms.double( 0.0 ),
    TrackTag = cms.InputTag( "hltPAFullCands" ),
    DisplacedVertexTag = cms.InputTag( "hltPAtktkVtxForDmesonDpt8" ),
    MaxNormalisedChi2 = cms.double( 999.0 ),
    FastAccept = cms.bool( False ),
    MinCosinePointingAngle = cms.double( 0.8 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinLxySignificance = cms.double( 1.0 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPrePADmesonPPTrackingGlobalDpt15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPAtktkVtxForDmesonDpt15 = cms.EDProducer( "HLTDisplacedtktkVtxProducer",
    Src = cms.InputTag( "hltPAFullCands" ),
    massParticle1 = cms.double( 0.1396 ),
    PreviousCandTag = cms.InputTag( "hltPAFullTrackFilterForDmeson" ),
    massParticle2 = cms.double( 0.4937 ),
    ChargeOpt = cms.int32( -1 ),
    MaxEta = cms.double( 2.5 ),
    MaxInvMass = cms.double( 2.27 ),
    MinPtPair = cms.double( 15.0 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinInvMass = cms.double( 1.47 ),
    MinPt = cms.double( 0.0 )
)
process.hltPAtktkFilterForDmesonDpt15 = cms.EDFilter( "HLTDisplacedtktkFilter",
    saveTags = cms.bool( True ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinVtxProbability = cms.double( 0.0 ),
    MaxLxySignificance = cms.double( 0.0 ),
    TrackTag = cms.InputTag( "hltPAFullCands" ),
    DisplacedVertexTag = cms.InputTag( "hltPAtktkVtxForDmesonDpt15" ),
    MaxNormalisedChi2 = cms.double( 999.0 ),
    FastAccept = cms.bool( False ),
    MinCosinePointingAngle = cms.double( 0.8 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinLxySignificance = cms.double( 1.0 )
)
process.hltPrePADmesonPPTrackingGlobalDpt30 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPAtktkVtxForDmesonDpt30 = cms.EDProducer( "HLTDisplacedtktkVtxProducer",
    Src = cms.InputTag( "hltPAFullCands" ),
    massParticle1 = cms.double( 0.1396 ),
    PreviousCandTag = cms.InputTag( "hltPAFullTrackFilterForDmeson" ),
    massParticle2 = cms.double( 0.4937 ),
    ChargeOpt = cms.int32( -1 ),
    MaxEta = cms.double( 2.5 ),
    MaxInvMass = cms.double( 2.27 ),
    MinPtPair = cms.double( 30.0 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinInvMass = cms.double( 1.47 ),
    MinPt = cms.double( 0.0 )
)
process.hltPAtktkFilterForDmesonDpt30 = cms.EDFilter( "HLTDisplacedtktkFilter",
    saveTags = cms.bool( True ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinVtxProbability = cms.double( 0.0 ),
    MaxLxySignificance = cms.double( 0.0 ),
    TrackTag = cms.InputTag( "hltPAFullCands" ),
    DisplacedVertexTag = cms.InputTag( "hltPAtktkVtxForDmesonDpt30" ),
    MaxNormalisedChi2 = cms.double( 999.0 ),
    FastAccept = cms.bool( False ),
    MinCosinePointingAngle = cms.double( 0.8 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinLxySignificance = cms.double( 1.0 )
)
process.hltPrePADmesonPPTrackingGlobalDpt50 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPAtktkVtxForDmesonDpt50 = cms.EDProducer( "HLTDisplacedtktkVtxProducer",
    Src = cms.InputTag( "hltPAFullCands" ),
    massParticle1 = cms.double( 0.1396 ),
    PreviousCandTag = cms.InputTag( "hltPAFullTrackFilterForDmeson" ),
    massParticle2 = cms.double( 0.4937 ),
    ChargeOpt = cms.int32( -1 ),
    MaxEta = cms.double( 2.5 ),
    MaxInvMass = cms.double( 2.27 ),
    MinPtPair = cms.double( 50.0 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinInvMass = cms.double( 1.47 ),
    MinPt = cms.double( 0.0 )
)
process.hltPAtktkFilterForDmesonDpt50 = cms.EDFilter( "HLTDisplacedtktkFilter",
    saveTags = cms.bool( True ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinVtxProbability = cms.double( 0.0 ),
    MaxLxySignificance = cms.double( 0.0 ),
    TrackTag = cms.InputTag( "hltPAFullCands" ),
    DisplacedVertexTag = cms.InputTag( "hltPAtktkVtxForDmesonDpt50" ),
    MaxNormalisedChi2 = cms.double( 999.0 ),
    FastAccept = cms.bool( False ),
    MinCosinePointingAngle = cms.double( 0.8 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinLxySignificance = cms.double( 1.0 )
)
process.hltPrePADmesonPPTrackingGlobalDpt5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPAtktkVtxForDmesonDpt5 = cms.EDProducer( "HLTDisplacedtktkVtxProducer",
    Src = cms.InputTag( "hltPAFullCands" ),
    massParticle1 = cms.double( 0.1396 ),
    PreviousCandTag = cms.InputTag( "hltPAFullTrackFilterForDmeson" ),
    massParticle2 = cms.double( 0.4937 ),
    ChargeOpt = cms.int32( -1 ),
    MaxEta = cms.double( 2.5 ),
    MaxInvMass = cms.double( 2.27 ),
    MinPtPair = cms.double( 5.0 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinInvMass = cms.double( 1.47 ),
    MinPt = cms.double( 0.0 )
)
process.hltPAtktkFilterForDmesonDpt5 = cms.EDFilter( "HLTDisplacedtktkFilter",
    saveTags = cms.bool( True ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinVtxProbability = cms.double( 0.0 ),
    MaxLxySignificance = cms.double( 0.0 ),
    TrackTag = cms.InputTag( "hltPAFullCands" ),
    DisplacedVertexTag = cms.InputTag( "hltPAtktkVtxForDmesonDpt5" ),
    MaxNormalisedChi2 = cms.double( 999.0 ),
    FastAccept = cms.bool( False ),
    MinCosinePointingAngle = cms.double( 0.8 ),
    triggerTypeDaughters = cms.int32( 91 ),
    MinLxySignificance = cms.double( 1.0 )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltCaloStage2Digis + process.hltGmtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelClustersCache + process.hltSiPixelRecHits )
process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTAK4CaloJetsReconstructionSequence = cms.Sequence( process.HLTDoCaloSequence + process.hltAK4CaloJets + process.hltAK4CaloJetsIDPassed )
process.HLTAK4CaloCorrectorProducersSequence = cms.Sequence( process.hltAK4CaloFastJetCorrector + process.hltAK4CaloRelativeCorrector + process.hltAK4CaloAbsoluteCorrector + process.hltAK4CaloResidualCorrector + process.hltAK4CaloCorrector )
process.HLTAK4CaloJetsCorrectionSequence = cms.Sequence( process.hltFixedGridRhoFastjetAllCalo + process.HLTAK4CaloCorrectorProducersSequence + process.hltAK4CaloJetsCorrected + process.hltAK4CaloJetsCorrectedIDPassed )
process.HLTAK4CaloJetsSequence = cms.Sequence( process.HLTAK4CaloJetsReconstructionSequence + process.HLTAK4CaloJetsCorrectionSequence )
process.HLTDoLocalPixelSequenceAfterSplitting = cms.Sequence( process.hltSiPixelClustersAfterSplitting + process.hltSiPixelClustersCacheAfterSplitting + process.hltSiPixelRecHitsAfterSplitting )
process.HLTPAPixelClusterSplitting = cms.Sequence( process.HLTAK4CaloJetsSequence + process.hltPAJetsForCoreTracking + process.HLTDoLocalPixelSequenceAfterSplitting + process.hltPixelLayerTripletsAfterSplitting )
process.HLTDoLocalStripSequenceAfterSplitting = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacility + process.hltSiStripClustersAfterSplitting )
process.HLTPAIterativeTrackingIteration0 = cms.Sequence( process.hltPAIter0PixelTripletsSeeds + process.hltPAIter0CkfTrackCandidates + process.hltPAIter0CtfWithMaterialTracks + process.hltPAIter0PrimaryVertices + process.hltPAIter0TrackClassifier1 + process.hltPAIter0TrackClassifier2 + process.hltPAIter0TrackClassifier3 + process.hltPAIter0TrackSelection )
process.HLTPAIterativeTrackingIteration1 = cms.Sequence( process.hltPAIter1ClustersRefRemoval + process.hltPAIter1MaskedMeasurementTrackerEvent + process.hltPAIter1DetachedTripletLayers + process.hltPAIter1DetachedTripletSeeds + process.hltPAIter1CkfTrackCandidates + process.hltPAIter1CtfWithMaterialTracks + process.hltPAIter1TrackClassifier1 + process.hltPAIter1TrackClassifier2 + process.hltPAIter1TrackSelection )
process.HLTPAIterativeTrackingIteration2 = cms.Sequence( process.hltPAIter2ClustersRefRemoval + process.hltPAIter2MaskedMeasurementTrackerEvent + process.hltPAIter2LowPtTripletLayers + process.hltPAIter2LowPtTripletSeeds + process.hltPAIter2CkfTrackCandidates + process.hltPAIter2CtfWithMaterialTracks + process.hltPAIter2TrackSelection )
process.HLTPAIterativeTrackingIteration3 = cms.Sequence( process.hltPAIter3ClustersRefRemoval + process.hltPAIter3MaskedMeasurementTrackerEvent + process.hltPAIter3PixelPairLayers + process.hltPAIter3PixelPairSeeds + process.hltPAIter3CkfTrackCandidates + process.hltPAIter3CtfWithMaterialTracks + process.hltPAIter3TrackSelection )
process.HLTPAIterativeTrackingIteration4 = cms.Sequence( process.hltPAIter4ClustersRefRemoval + process.hltPAIter4MaskedMeasurementTrackerEvent + process.hltPAIter4MixedTripletLayersA + process.hltPAIter4MixedTripletSeedsA + process.hltPAIter4MixedTripletLayersB + process.hltPAIter4MixedTripletSeedsB + process.hltPAIter4MixedSeeds + process.hltPAIter4CkfTrackCandidates + process.hltPAIter4CtfWithMaterialTracks + process.hltPAIter4TrackClassifier1 + process.hltPAIter4TrackClassifier2 + process.hltPAIter4TrackSelection )
process.HLTPAIterativeTrackingIteration5 = cms.Sequence( process.hltPAIter5ClustersRefRemoval + process.hltPAIter5MaskedMeasurementTrackerEvent + process.hltPAIter5PixelLessLayers + process.hltPAIter5PixelLessSeeds + process.hltPAIter5CkfTrackCandidates + process.hltPAIter5CtfWithMaterialTracks + process.hltPAIter5TrackClassifier1 + process.hltPAIter5TrackClassifier2 + process.hltPAIter5TrackSelection )
process.HLTPAIterativeTrackingIteration6 = cms.Sequence( process.hltPAIter6ClustersRefRemoval + process.hltPAIter6MaskedMeasurementTrackerEvent + process.hltPAIter6TobTecLayersTripl + process.hltPAIter6TobTecSeedsTripl + process.hltPAIter6TobTecLayersPair + process.hltPAIter6TobTecSeedsPair + process.hltPAIter6TobTecSeeds + process.hltPAIter6CkfTrackCandidates + process.hltPAIter6CtfWithMaterialTracks + process.hltPAIter6TrackClassifier1 + process.hltPAIter6TrackClassifier2 + process.hltPAIter6TrackSelection )
process.HLTPAIterativeTrackingIteration7 = cms.Sequence( process.hltPAIter7GoodPrimaryVertices + process.hltPAIter7JetCoreLayers + process.hltPAIter7JetCoreSeeds + process.hltPAIter7CkfTrackCandidates + process.hltPAIter7CtfWithMaterialTracks + process.hltPAIter7TrackSelection )
process.HLTPAIterativeTracking = cms.Sequence( process.HLTPAIterativeTrackingIteration0 + process.HLTPAIterativeTrackingIteration1 + process.HLTPAIterativeTrackingIteration2 + process.HLTPAIterativeTrackingIteration3 + process.HLTPAIterativeTrackingIteration4 + process.HLTPAIterativeTrackingIteration5 + process.HLTPAIterativeTrackingIteration6 + process.HLTPAIterativeTrackingIteration7 + process.hltPAIterativeTrackingMerged )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLT_PADmesonPPTrackingGlobal_Dpt8_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPrePADmesonPPTrackingGlobalDpt8 + process.HLTDoLocalPixelSequence + process.HLTPAPixelClusterSplitting + process.HLTDoLocalStripSequenceAfterSplitting + process.HLTPAIterativeTracking + process.hltPAOnlinePrimaryVertices + process.hltPAFullCands + process.hltPAFullTrackFilterForDmeson + process.hltPAtktkVtxForDmesonDpt8 + process.hltPAtktkFilterForDmesonDpt8 + process.HLTEndSequence )
process.HLT_PADmesonPPTrackingGlobal_Dpt15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPrePADmesonPPTrackingGlobalDpt15 + process.HLTDoLocalPixelSequence + process.HLTPAPixelClusterSplitting + process.HLTDoLocalStripSequenceAfterSplitting + process.HLTPAIterativeTracking + process.hltPAOnlinePrimaryVertices + process.hltPAFullCands + process.hltPAFullTrackFilterForDmeson + process.hltPAtktkVtxForDmesonDpt15 + process.hltPAtktkFilterForDmesonDpt15 + process.HLTEndSequence )
process.HLT_PADmesonPPTrackingGlobal_Dpt30_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPrePADmesonPPTrackingGlobalDpt30 + process.HLTDoLocalPixelSequence + process.HLTPAPixelClusterSplitting + process.HLTDoLocalStripSequenceAfterSplitting + process.HLTPAIterativeTracking + process.hltPAOnlinePrimaryVertices + process.hltPAFullCands + process.hltPAFullTrackFilterForDmeson + process.hltPAtktkVtxForDmesonDpt30 + process.hltPAtktkFilterForDmesonDpt30 + process.HLTEndSequence )
process.HLT_PADmesonPPTrackingGlobal_Dpt50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPrePADmesonPPTrackingGlobalDpt50 + process.HLTDoLocalPixelSequence + process.HLTPAPixelClusterSplitting + process.HLTDoLocalStripSequenceAfterSplitting + process.HLTPAIterativeTracking + process.hltPAOnlinePrimaryVertices + process.hltPAFullCands + process.hltPAFullTrackFilterForDmeson + process.hltPAtktkVtxForDmesonDpt50 + process.hltPAtktkFilterForDmesonDpt50 + process.HLTEndSequence )
process.HLT_PADmesonPPTrackingGlobal_Dpt5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPrePADmesonPPTrackingGlobalDpt5 + process.HLTDoLocalPixelSequence + process.HLTPAPixelClusterSplitting + process.HLTDoLocalStripSequenceAfterSplitting + process.HLTPAIterativeTracking + process.hltPAOnlinePrimaryVertices + process.hltPAFullCands + process.hltPAFullTrackFilterForDmeson + process.hltPAtktkVtxForDmesonDpt5 + process.hltPAtktkFilterForDmesonDpt5 + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtStage2Digis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )


process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_PADmesonPPTrackingGlobal_Dpt8_v1, process.HLT_PADmesonPPTrackingGlobal_Dpt15_v1, process.HLT_PADmesonPPTrackingGlobal_Dpt30_v1, process.HLT_PADmesonPPTrackingGlobal_Dpt50_v1, process.HLT_PADmesonPPTrackingGlobal_Dpt5_v1, process.HLTriggerFinalPath ))


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/data/twang/MC_samples/Pythia8_prompt_D0pt0p0_Pthat50_TuneCUETP8M1_8160GeV_evtgen130_GEN_SIM_PU_20160725/FEVTDEBUG_step3/step3_RAW2DIGI_L1Reco_RECO.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# override the GlobalTag's L1T menu from an Xml file
from HLTrigger.Configuration.CustomConfigs import L1XML
process = L1XML(process,"L1Menu_Collisions2016_v3_ugt_1board_modified_pPb_Spectra.xml")

# run the Full L1T emulator, then repack the data into a new RAW collection, to be used by the HLT
from HLTrigger.Configuration.CustomConfigs import L1REPACK
process = L1REPACK(process,"Full")

# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.hltResults = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.hltResults        = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.hltResults  = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'TEST' )
    process.hltDQMHLTScalers.processname                      = 'TEST'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'TEST'

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 500 )
)

# enable TrigReport, TimeReport and MultiThreading
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 ),
    sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'auto:run2_mc_GRun')
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('L1TGlobalSummary')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

# load the DQMStore and DQMRootOutputModule
process.load( "DQMServices.Core.DQMStore_cfi" )
process.DQMStore.enableMultiThread = True

process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
    fileName = cms.untracked.string("DQMIO.root")
)

process.DQMOutput = cms.EndPath( process.dqmOutput )

# add specific customizations
_customInfo = {}
_customInfo['menuType'  ]= "GRun"
_customInfo['globalTags']= {}
_customInfo['globalTags'][True ] = "auto:run2_hlt_GRun"
_customInfo['globalTags'][False] = "auto:run2_mc_GRun"
_customInfo['inputFiles']={}
_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
_customInfo['maxEvents' ]=  500
_customInfo['globalTag' ]= "auto:run2_mc_GRun"
_customInfo['inputFile' ]=  ['file:/data/twang/MC_samples/Pythia8_prompt_D0pt0p0_Pthat50_TuneCUETP8M1_8160GeV_evtgen130_GEN_SIM_PU_20160725/FEVTDEBUG_step3/step3_RAW2DIGI_L1Reco_RECO.root']
_customInfo['realData'  ]=  False
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")

process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("TEST")
process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("openHLT.root"))

AddCaloMuon = False
runOnMC = True
HIFormat = False
UseGenPlusSim = False
VtxLabel = "offlinePrimaryVerticesWithBS"
TrkLabel = "generalTracks"
### finder building block
from Bfinder.finderMaker.OnlyTrack_finderMaker_75X_cff import OnlyTrack_finderMaker_75X
OnlyTrack_finderMaker_75X(process, AddCaloMuon, runOnMC, HIFormat, UseGenPlusSim, VtxLabel, TrkLabel)
process.Dfinder.tkPtCut = cms.double(1.0)#before fit
process.Dfinder.dPtCut = cms.vdouble(4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5)#before fit
process.Dfinder.dCutSeparating_PtVal = cms.vdouble(8., 8., 8., 8., 8., 8., 8., 8., 8., 8., 8., 8.)
process.Dfinder.tktkRes_svpvDistanceCut_lowptD = cms.vdouble(0., 0., 0., 0., 0., 0., 0., 0., 3.0, 3.0, 3.0, 3.0 )
process.Dfinder.tktkRes_svpvDistanceCut_highptD = cms.vdouble(0., 0., 0., 0., 0., 0., 0., 0., 1.5, 1.5, 1.5, 1.5)
process.Dfinder.svpvDistanceCut_lowptD = cms.vdouble(2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0., 0., 0., 0.)
process.Dfinder.svpvDistanceCut_highptD = cms.vdouble(2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0., 0., 0., 0.)
process.Dfinder.Dchannel = cms.vint32(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
process.p = cms.Path(process.DfinderSequence)

