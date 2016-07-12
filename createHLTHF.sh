#!/bin/bash
fileStr='--input file:/afs/cern.ch/work/g/ginnocen/HF2016TriggerDevelop_New/CMSSW_8_0_14/src/examplefile/test.root'
#hltGetConfiguration /dev/CMSSW_8_0_0/GRun --full --offline --mc --unprescale --process TEST --globaltag auto:run2_mc_GRun --l1-emulator 'Full' --output none --max-events 500 $fileStr> hlt_stage2_MC.py
hltGetConfiguration /users/ginnocen/Dmeson2016pPb/DHFtrigger/V1 --full --offline --mc --unprescale --process TEST --globaltag 80X_mcRun2_asymptotic_v12 --l1-emulator 'Full' --max-events 500 $fileStr> hlt_stage2_MC.py
hltConfigFromDB --cff --configName /dev/CMSSW_8_0_0/GRun --nopaths --services -PrescaleService,-EvFDaqDirector,-FastMonitoringService > setup_cff.py
sed -i '/process = cms.Process( "TEST" )/a process.load("setup_cff")' hlt_stage2_MC.py

echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("TEST")
process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("openHLT.root"))' >> hlt_stage2_MC.py
