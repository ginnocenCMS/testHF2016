#include <TH1.h>
#include <TH2.h>
#include <TTree.h>
#include <TLegend.h>
#include <TLegendEntry.h>
#include <TCut.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TGraphAsymmErrors.h>

const int nBin = 35;
Float_t bins[nBin+1]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,26,28,30,32,34,36,38,40,45,50,55,60,70,80};

// Take a tree, a variable and calculate the efficiency
TGraphAsymmErrors* getEfficiency(TTree *t, TString variable, TCut preselection, TCut cut, int nBin, Float_t *bins, Double_t PreScale, Double_t HLTPS)
{
	static int count = 0;
	count++;
	TH1D *hPass = new TH1D (Form("hPass%d",count),"",nBin,bins);
	TH1D *hAll = new TH1D (Form("hAll%d",count),"",nBin,bins);
	t->Draw(Form("%s>>hAll%d",variable.Data(),count),preselection);
	t->Draw(Form("%s>>hPass%d",variable.Data(),count),preselection&&cut);

	hPass->Scale(HLTPS/PreScale);	   
	hAll->Draw();
	cout<<"ici"<<endl;

	TGraphAsymmErrors *g = new TGraphAsymmErrors;
	g->BayesDivide(hPass,hAll);
	return g;
}

void plotTrigger_expressreco_Dpt50()
{
	gStyle->SetOptStat(0);

	bool sideband = false;
	bool cent = false;   
	TString outf,infname;

	outf = "result_Run285530";
	infname = "~jisun/jisun/public/HFTrig_2016/Dntuple_285530.root";  

	// ============== Open file and basic settings ===============   
	// Open Dntuple file

	// L1 trigger thresholds
	TCut l1CutMBSeed1 = "20";	// L1_MinimumBiasHF0_OR_BptxAND for Dpt5, Dpt8
	TCut l1CutMBSeed2 = "1";	// L1_SingleJet8_BptxAND for Dpt15
	TCut l1CutMBSeed3 = "14";	// L1_SingleJet12_BptxAND for Dpt30
	TCut l1CutMBSeed4 = "1";	// L1_SingleJet24_BptxAND for Dpt50

	Double_t l1CutMBSeed1v = 20;	// L1_MinimumBiasHF0_OR_BptxAND for Dpt5, Dpt8
	Double_t l1CutMBSeed2v = 1;	// L1_SingleJet8_BptxAND for Dpt15
	Double_t l1CutMBSeed3v = 14;	// L1_SingleJet12_BptxAND for Dpt30
	Double_t l1CutMBSeed4v = 1;	// L1_SingleJet24_BptxAND for Dpt50


	TFile *inf = new TFile(infname.Data());
	TTree* ntDkpi = (TTree*)inf->Get("ntDkpi");
	TTree* ntHlt = (TTree*)inf->Get("ntHlt");

	ntDkpi->AddFriend(ntHlt);

	TFile *infMB = new TFile(infname.Data());
	TTree* ntDkpiMB = (TTree*)infMB->Get("ntDkpi");
	TTree* ntHltMB= (TTree*)infMB->Get("ntHlt");

	ntDkpiMB->SetName("ntDkpiMB");
	ntHltMB->SetName("ntHltMB");
	ntDkpiMB->AddFriend(ntHltMB);

	// Define bin size and bin width for trigger turnon curve histograms

	// Templates for plotting  
	TH1D *hTmp = new TH1D ("hTmp","",nBin,bins);
	TH1D *hTmp2 = new TH1D ("hTmp2","",nBin,bins);

	// D meson selection
	TCut DmassCut             = "(abs(Dmass-1.8696)<0.1)";
	TCut DmesonCut            = "(DsvpvDistance/DsvpvDisErr)>2.5&&Dchi2cl>0.10&&Dalpha<0.12";
	//TCut DmesonDaughterTrkCut="Dtrk1highPurity&&Dtrk1Pt>1&&abs(Dtrk1Eta)<2.0&&Dtrk2highPurity&&Dtrk2Pt>1&&abs(Dtrk2Eta)<2.0";
	TCut DmesonDaughterTrkCut="Dtrk1highPurity&&Dtrk1Pt>1&&abs(Dtrk1Eta)<2.0&&Dtrk2highPurity&&Dtrk2Pt>1&&abs(Dtrk2Eta)<2.0&&Dtrk1PtErr/Dtrk1Pt<0.3&&Dtrk2PtErr/Dtrk2Pt<0.3&&(Dtrk1PixelHit+Dtrk1StripHit)>=11&&(Dtrk2PixelHit+Dtrk2StripHit)>=11&&(Dtrk1Chi2ndf/(Dtrk1nStripLayer+Dtrk1nPixelLayer)<0.25)&&(Dtrk2Chi2ndf/(Dtrk2nStripLayer+Dtrk2nPixelLayer)<0.25)";
	if (sideband) DmassCut = "(abs(Dmass-1.8696)>0.06 && abs(Dmass-1.8696)>0.12)";

	TCut MBCut = "LumiNo>79";
	// Final selection for D candidates for trigger turnon studies
	TCut DAnaCut = DmassCut && DmesonCut && DmesonDaughterTrkCut && MBCut;

	TCut HLTCut5 = "HLT_PADmesonPPTrackingGlobal_Dpt5_v2";
	TCut HLTCut8 = "HLT_PADmesonPPTrackingGlobal_Dpt8_v2";
	TCut HLTCut15 = "HLT_PADmesonPPTrackingGlobal_Dpt15_v3";
	TCut HLTCut30 = "HLT_PADmesonPPTrackingGlobal_Dpt30_v2";
	TCut HLTCut50 = "HLT_PADmesonPPTrackingGlobal_Dpt50_v2";

	TCut HLTCutET8 = "HLT_PADmesonPPTrackingGlobal_Dpt8_EvtTagging_v2";
	TCut HLTCutET15 = "HLT_PADmesonPPTrackingGlobal_Dpt15_EvtTagging_v3";

	Double_t HLTCut5PS = 80;	// L1_MinimumBiasHF0_OR_BptxAND for Dpt5, Dpt8
	Double_t HLTCut8PS = 20;	// L1_SingleJet8_BptxAND for Dpt15
	Double_t HLTCut15PS = 14;	// L1_SingleJet12_BptxAND for Dpt30
	Double_t HLTCut30PS = 14;	// L1_SingleJet24_BptxAND for Dpt50
	Double_t HLTCut50PS = 1;	// L1_SingleJet24_BptxAND for Dpt50

	// ============== L1 trigger efficiency study ===============
	cout<<"step3"<<endl;

	TCanvas *c = new TCanvas("c","",600,600);

	TGraphAsymmErrors* g5;
	TGraphAsymmErrors* g8;
	TGraphAsymmErrors* g15;
	TGraphAsymmErrors* g30;
	TGraphAsymmErrors* g50;

	TGraphAsymmErrors* g8ET;
	TGraphAsymmErrors* g15ET;

	cout << " DAnaCut.GetTitle(): " << DAnaCut.GetTitle() << endl;

	//g50  = getEfficiency(ntDkpiMB,"Dpt", TCut(DAnaCut), HLTCut50, nBin, bins, 1.0, 1.0);
	//g8ET  = getEfficiency(ntDkpiMB,"Dpt", TCut(DAnaCut), HLTCutET8, nBin, bins, 1.0, 1.0);
	//g15ET = getEfficiency(ntDkpiMB,"Dpt", TCut(DAnaCut), HLTCutET15, nBin, bins, 1.0, 1.0);

    g50  = getEfficiency(ntDkpiMB,Form("Max$(Dpt*(%s))",DAnaCut.GetTitle()), TCut(DAnaCut), HLTCut50, nBin, bins, 1.0, 1.0);
    //g8ET  = getEfficiency(ntDkpiMB,Form("Max$(Dpt*(%s))",DAnaCut.GetTitle()), TCut(DAnaCut), HLTCutET8, nBin, bins, 1.0, 1.0);
    //g15ET = getEfficiency(ntDkpiMB,Form("Max$(Dpt*(%s))",DAnaCut.GetTitle()), TCut(DAnaCut), HLTCutET15, nBin, bins, 1.0, 1.0);

	hTmp->Draw();
	hTmp->SetXTitle("D Meson p_{T} (GeV/c)");
	hTmp->SetYTitle("D Trig Efficiency");
	/*
	   g5->SetLineColor(1);
	   g5->SetMarkerColor(1);
	   g5->Draw("pl same");

	   g8->SetLineColor(4);
	   g8->SetMarkerColor(4);
	   g8->Draw("pl same");

	   g15->SetLineColor(2);
	   g15->SetMarkerColor(2);
	   g15->Draw("pl same");

	   g30->SetLineColor(kGreen+2);
	   g30->SetMarkerColor(kGreen+2);
	   g30->Draw("pl same");
	   */
	g50->SetLineColor(4);
	g50->SetMarkerColor(4);
	g50->Draw("pl same");

	//g8ET->SetLineColor(kBlack);
	//g8ET->SetMarkerColor(kBlack);
	//g8ET->Draw("pl same");

	//g15ET->SetLineColor(kRed);
	//g15ET->SetMarkerColor(kRed);
	//g15ET->Draw("pl same");


	TLegend *leg = new TLegend(0.53,0.2,0.93,0.6);
	leg->SetBorderSize(0);
	leg->SetFillStyle(0);
	leg->SetTextSize(0.05);
	leg->SetTextFont(42);
	/*
	   leg->AddEntry(g5,"HLT D meson 5","pl");
	   leg->AddEntry(g8,"HLT D meson 8","pl");
	   leg->AddEntry(g15,"HLT D meson 15","pl");
	   leg->AddEntry(g30,"HLT D meson 30","pl");
	   */
	leg->AddEntry(g50,"D^{0} 50 Trig","pl");
	//leg->AddEntry(g8ET,"HLT D meson EvtTagging 8","pl");
	//leg->AddEntry(g15ET,"HLT D meson EvtTagging 15","pl");


	leg->Draw();
	cout<<"step4"<<endl;

	c->SaveAs(outf+"/Dmeson-HIHLTriggerEfficiency_Dpt50.pdf");
	c->SaveAs(outf+"/Dmeson-HIHLTriggerEfficiency_Dpt50.png");
	c->SaveAs(outf+"/Dmeson-HIHLTriggerEfficiency_Dpt50.C");
	TFile *fouput=new TFile(outf+"/fefficiency_Dpt50.root","recreate");
//	fouput->cd();
//	g5->SetName("g5");
//	g8->SetName("g8");
//	g15->SetName("g15");
//	g30->SetName("g30");
	g50->SetName("g50");
//	g5->Write();
//	g8->Write();
//	g15->Write();
//	g30->Write();
	g50->Write();
	fouput->Close();
}
