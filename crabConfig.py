from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")

config.section_("JobType")
config.JobType.pluginName = 'Analysis'

config.section_("Data")
config.Data.useParent = True
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.JobType.psetName = 'hlt_stage2_MC.py'
config.JobType.maxMemoryMB = 4000
config.General.requestName = 'DHFtrigger_V3_withfinderonPP8TeV_pthat15_28July_130pm_v1'
config.General.workArea = 'DHFtrigger_V3_withfinderonPP8TeV_pthat15_28July_130pm_v1'
config.Data.inputDataset = '/Pythia8_prompt_D0pt0p0_Pthat15_TuneCUETP8M1_8160GeV_evtgen130_GEN_SIM_PU_20160725/twang-crab_Pythia8_prompt_D0pt0p0_Pthat15_TuneCUETP8M1_8160GeV_evtgen130_step3-079c1f4d470d781fe433b5c041f933e9/USER'
config.Data.totalUnits =-1
config.Data.outLFNDirBase = '/store/group/phys_heavyions/ginnocen/Dmeson_pPbHLT/DHFtrigger_V3_withfinderonPP8TeV_pthat15_28July_130pm_v1'
config.Data.outputDatasetTag = 'DHFtrigger_V3_withfinderonPP8TeV_pthat15_28July_130pm_v1'
config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    #config.General.workArea = 'ppHM_HLT_Run2015D_TOTEM_L1MBHF2'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    submit(config)

