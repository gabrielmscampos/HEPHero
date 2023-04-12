import os


def get_samples( basedir, period, APV ):

    list_basedir = os.listdir(basedir)
    yearTag = period + "_files"
    if APV:
        apvIn = "APV"
        apvNotIn = "FakeNameX"
    else:
        apvIn = "_"
        apvNotIn = "APV"
        
    samples = {
        'Signal_400_100':           [i for i in list_basedir if 'Signal_400_100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_400_200':           [i for i in list_basedir if 'Signal_400_200' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_500_100':           [i for i in list_basedir if 'Signal_500_100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_500_200':           [i for i in list_basedir if 'Signal_500_200' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_500_300':           [i for i in list_basedir if 'Signal_500_300' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_600_100':           [i for i in list_basedir if 'Signal_600_100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_600_200':           [i for i in list_basedir if 'Signal_600_200' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_600_300':           [i for i in list_basedir if 'Signal_600_300' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_600_400':           [i for i in list_basedir if 'Signal_600_400' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_800_100':           [i for i in list_basedir if 'Signal_800_100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_800_200':           [i for i in list_basedir if 'Signal_800_200' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_800_300':           [i for i in list_basedir if 'Signal_800_300' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_800_400':           [i for i in list_basedir if 'Signal_800_400' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_800_600':           [i for i in list_basedir if 'Signal_800_600' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_1000_100':          [i for i in list_basedir if 'Signal_1000_100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_1000_200':          [i for i in list_basedir if 'Signal_1000_200' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_1000_300':          [i for i in list_basedir if 'Signal_1000_300' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_1000_400':          [i for i in list_basedir if 'Signal_1000_400' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_1000_600':          [i for i in list_basedir if 'Signal_1000_600' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Signal_1000_800':          [i for i in list_basedir if 'Signal_1000_800' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_PtZ-0To50':     [i for i in list_basedir if 'DYJetsToLL_PtZ-0To50' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_PtZ-3To50':     [i for i in list_basedir if 'DYJetsToLL_PtZ-3To50' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_PtZ-50To100':   [i for i in list_basedir if 'DYJetsToLL_PtZ-50To100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_PtZ-100To250':  [i for i in list_basedir if 'DYJetsToLL_PtZ-100To250' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_PtZ-250To400':  [i for i in list_basedir if 'DYJetsToLL_PtZ-250To400' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_PtZ-400To650':  [i for i in list_basedir if 'DYJetsToLL_PtZ-400To650' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_PtZ-650ToInf':  [i for i in list_basedir if 'DYJetsToLL_PtZ-650ToInf' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_Pt-0To3':       [i for i in list_basedir if 'DYJetsToLL_Pt-0To3' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_Pt-Inclusive':  [i for i in list_basedir if 'DYJetsToLL_Pt-Inclusive' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_Pt-50To100':    [i for i in list_basedir if 'DYJetsToLL_Pt-50To100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_Pt-100To250':   [i for i in list_basedir if 'DYJetsToLL_Pt-100To250' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_Pt-250To400':   [i for i in list_basedir if 'DYJetsToLL_Pt-250To400' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_Pt-400To650':   [i for i in list_basedir if 'DYJetsToLL_Pt-400To650' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_Pt-650ToInf':   [i for i in list_basedir if 'DYJetsToLL_Pt-650ToInf' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_M-10to50':      [i for i in list_basedir if 'DYJetsToLL_M-10to50' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-Inclusive':  [i for i in list_basedir if 'DYJetsToLL_HT-Inclusive' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-70to100':    [i for i in list_basedir if 'DYJetsToLL_HT-70to100' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-100to200':   [i for i in list_basedir if 'DYJetsToLL_HT-100to200' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-200to400':   [i for i in list_basedir if 'DYJetsToLL_HT-200to400' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-400to600':   [i for i in list_basedir if 'DYJetsToLL_HT-400to600' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-600to800':   [i for i in list_basedir if 'DYJetsToLL_HT-600to800' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-800to1200':  [i for i in list_basedir if 'DYJetsToLL_HT-800to1200' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-1200to2500': [i for i in list_basedir if 'DYJetsToLL_HT-1200to2500' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'DYJetsToLL_HT-2500toInf':  [i for i in list_basedir if 'DYJetsToLL_HT-2500toInf' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTTo2L2Nu':                [i for i in list_basedir if 'TTTo2L2Nu' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTToSemiLeptonic':         [i for i in list_basedir if 'TTToSemiLeptonic' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ST_tW_top':                [i for i in list_basedir if 'ST_tW_top' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ST_tW_antitop':            [i for i in list_basedir if 'ST_tW_antitop' in i and apvIn in i and apvNotIn not in i and yearTag in i], 
        'ST_t-channel_top':         [i for i in list_basedir if 'ST_t-channel_top' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ST_t-channel_antitop':     [i for i in list_basedir if 'ST_t-channel_antitop' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ST_s-channel':             [i for i in list_basedir if 'ST_s-channel' in i and apvIn in i and apvNotIn not in i and yearTag in i], 
        'ZZ_Inclusive':             [i for i in list_basedir if 'ZZ_Inclusive' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ZZ_Others':                [i for i in list_basedir if 'ZZ_Others' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ZZTo2L2Nu':                [i for i in list_basedir if 'ZZTo2L2Nu' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ZZTo4L':                   [i for i in list_basedir if 'ZZTo4L' == i.split("_")[0] and apvIn in i and apvNotIn not in i and yearTag in i],
        'ZZTo2Q2L':                 [i for i in list_basedir if 'ZZTo2Q2L' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WZ_Inclusive':             [i for i in list_basedir if 'WZ_Inclusive' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WZ_Others':                [i for i in list_basedir if 'WZ_Others' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WZTo3LNu':                 [i for i in list_basedir if 'WZTo3LNu' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WZTo2Q2L':                 [i for i in list_basedir if 'WZTo2Q2L' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WW':                       [i for i in list_basedir if 'WW' == i.split("_")[0] and apvIn in i and apvNotIn not in i and yearTag in i],
        'WWTo2L2Nu':                [i for i in list_basedir if 'WWTo2L2Nu' == i.split("_")[0] and apvIn in i and apvNotIn not in i and yearTag in i],
        'WZZ':                      [i for i in list_basedir if 'WZZ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WWZ':                      [i for i in list_basedir if 'WWZ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ZZZ':                      [i for i in list_basedir if 'ZZZ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WWW':                      [i for i in list_basedir if 'WWW' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTWW':                     [i for i in list_basedir if 'TTWW' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTWZ':                     [i for i in list_basedir if 'TTWZ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTZZ':                     [i for i in list_basedir if 'TTZZ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TWZToLL_thad_Wlept':       [i for i in list_basedir if 'TWZToLL_thad_Wlept' in i and apvIn in i and apvNotIn not in i and yearTag in i], 
        'TWZToLL_tlept_Whad':       [i for i in list_basedir if 'TWZToLL_tlept_Whad' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TWZToLL_tlept_Wlept':      [i for i in list_basedir if 'TWZToLL_tlept_Wlept' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTWJetsToLNu':             [i for i in list_basedir if 'TTWJetsToLNu' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTWJetsToQQ':              [i for i in list_basedir if 'TTWJetsToQQ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTZToQQ':                  [i for i in list_basedir if 'TTZToQQ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTZToLL':                  [i for i in list_basedir if 'TTZToLL' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'TTZToNuNu':                [i for i in list_basedir if 'TTZToNuNu' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'tZq_ll':                   [i for i in list_basedir if 'tZq_ll' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ttH_HToZZ':                [i for i in list_basedir if 'ttH_HToZZ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ttHTobb':                  [i for i in list_basedir if 'ttHTobb' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ttHToTauTau':              [i for i in list_basedir if 'ttHToTauTau' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'GluGluHToWWTo2L2Nu':       [i for i in list_basedir if 'GluGluHToWWTo2L2Nu' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'GluGluHToZZTo2L2Q':        [i for i in list_basedir if 'GluGluHToZZTo2L2Q' in i and apvIn in i and apvNotIn not in i and yearTag in i], 
        'GluGluHToZZTo4L':          [i for i in list_basedir if 'GluGluHToZZTo4L' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WplusH_HToZZTo2L2X':       [i for i in list_basedir if 'WplusH_HToZZTo2L2X' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WplusH_HToZZTo4L':         [i for i in list_basedir if 'WplusH_HToZZTo4L' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WminusH_HToZZTo2L2X':      [i for i in list_basedir if 'WminusH_HToZZTo2L2X' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WminusH_HToZZTo4L':        [i for i in list_basedir if 'WminusH_HToZZTo4L' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ZH_HToBB_ZToLL':           [i for i in list_basedir if 'ZH_HToBB_ZToLL' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'ZH_HToZZ':                 [i for i in list_basedir if 'ZH_HToZZ' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-15To20':            [i for i in list_basedir if 'QCD_Pt-15To20' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-20To30':            [i for i in list_basedir if 'QCD_Pt-20To30' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-30To50':            [i for i in list_basedir if 'QCD_Pt-30To50' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-50To80':            [i for i in list_basedir if 'QCD_Pt-50To80' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-80To120':           [i for i in list_basedir if 'QCD_Pt-80To120' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-120To170':          [i for i in list_basedir if 'QCD_Pt-120To170' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-170To300':          [i for i in list_basedir if 'QCD_Pt-170To300' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-300To470':          [i for i in list_basedir if 'QCD_Pt-300To470' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-470To600':          [i for i in list_basedir if 'QCD_Pt-470To600' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-600To800':          [i for i in list_basedir if 'QCD_Pt-600To800' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-800To1000':         [i for i in list_basedir if 'QCD_Pt-800To1000' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'QCD_Pt-1000ToInf':         [i for i in list_basedir if 'QCD_Pt-1000ToInf' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'WJetsToLNu':               [i for i in list_basedir if 'WJetsToLNu' == i.split("_")[0] and apvIn in i and apvNotIn not in i and yearTag in i],
        'WGToLNuG':                 [i for i in list_basedir if 'WGToLNuG' in i and apvIn in i and apvNotIn not in i and yearTag in i],
        'Data_A':                   [i for i in list_basedir if 'Data' in i and '_A_' in i and yearTag in i],
        'Data_B':                   [i for i in list_basedir if 'Data' in i and '_B_' in i and yearTag in i],
        'Data_C':                   [i for i in list_basedir if 'Data' in i and '_C_' in i and yearTag in i],
        'Data_D':                   [i for i in list_basedir if 'Data' in i and '_D_' in i and yearTag in i],
        'Data_E':                   [i for i in list_basedir if 'Data' in i and '_E_' in i and yearTag in i],
        'Data_HIPM_F':              [i for i in list_basedir if 'Data' in i and '_F_' in i and 'HIPM' in i and yearTag in i],
        'Data_F':                   [i for i in list_basedir if 'Data' in i and '_F_' in i and 'HIPM' not in i and yearTag in i],
        'Data_G':                   [i for i in list_basedir if 'Data' in i and '_G_' in i and yearTag in i],
        'Data_H':                   [i for i in list_basedir if 'Data' in i and '_H_' in i and yearTag in i],
    }
    
    empty_samples = []
    for sample in samples:
        if len(samples[sample]) == 0:
            empty_samples.append(sample)

    for sample in empty_samples:
        del samples[sample]

    return samples


