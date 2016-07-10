#!/bin/bash
fileStr='--input file:/afs/cern.ch/work/g/ginnocen/HF2016TriggerDevelop_New/CMSSW_8_0_14/src/examplefile/test.root'
hltGetConfiguration /dev/CMSSW_8_0_0/GRun --full --offline --mc --unprescale --process TEST --globaltag auto:run2_mc_GRun --l1-emulator 'Full' --output none --max-events 500 $fileStr> hlt_stage2_MC.py

echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("TEST")
process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","TEST" )
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("openHLT.root"))' >> hlt_stage2_MC.py
