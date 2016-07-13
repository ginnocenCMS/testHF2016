#!/bin/bash
fileStr='--input root://cms-xrd-global.cern.ch//store/user/gsfs/HIJINGpPb_MinBias816/HIJING_MinBias_pPb_RAWDEBUG_20160514/160514_124027/0000/step2_MinBias_pPb_DIGI_L1_DIGI2RAW_HLT_1.root'
fileStrSec='--input root://cms-xrd-global.cern.ch//store/user/gsfs/HIJINGpPb_MinBias816/HIJING_MinBias_pPb_RECODEBUG_20160514/160514_215359/0000/step3_MinBias_pPb_RAW2DIGI_L1Reco_RECO_1.root'
#hltGetConfiguration /dev/CMSSW_8_0_0/GRun --full --offline --mc --unprescale --process TEST --globaltag auto:run2_mc_GRun --l1-emulator 'Full' --output none --max-events 500 $fileStr> hlt_stage2_MC.py
hltGetConfiguration /users/ginnocen/Dmeson2016pPb/DHFtrigger/V3 --full --offline --mc --unprescale --process TEST --globaltag auto:run2_mc_GRun --l1-emulator 'Full' --max-events 500 $fileStr> hlt_stage2_MC.py
hltConfigFromDB --cff --configName /dev/CMSSW_8_0_0/GRun --nopaths --services -PrescaleService,-EvFDaqDirector,-FastMonitoringService > setup_cff.py
sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_stage2_MC.py

echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("TEST")
process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("openHLT.root"))' >> hlt_stage2_MC.py

echo '
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
process.Dfinder.Dchannel = cms.vint32(1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1)
process.p = cms.Path(process.DfinderSequence)
'>> hlt_stage2_MC.py