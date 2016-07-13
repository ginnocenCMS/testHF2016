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
config.General.requestName = 'DHFtrigger_V3_withfinder_18July_5pm_v3'
config.General.workArea = 'DHFtrigger_V3_withfinder_18July_5pm'
config.Data.inputDataset = '/ReggeGribovPartonMCpPb_MinBias_8016GeV_EposLHC/gsfs-EPOS_MinBias_pPb_RECO_17072016-2dbfb02bdba22ee6fbd5c4414ef7b888/USER'
config.Data.totalUnits =-1
config.Data.outLFNDirBase = '/store/group/phys_heavyions/ginnocen/Dmeson_pPbHLT/DHFtrigger_V3_withfinder_18July_5pm_v3'
config.Data.outputDatasetTag = 'DHFtrigger_V3_withfinder_18July_5pm_v3'
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

