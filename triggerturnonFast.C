//#include "uti.h"

TString mbtrg = "1";
TString prefilter = "(Dmass>1.8&&Dmass<1.9)&&Dy>-1.&&Dy<1.&&Dtrk1highPurity&&Dtrk2highPurity&&Dtrk1Pt>2.0&&Dtrk2Pt>2.0&&(DsvpvDistance/DsvpvDisErr)>3.5&&(DlxyBS/DlxyBSErr)>2.5&&Dchi2cl>0.05&&Dalpha<0.12&&abs(Dtrk1Eta)<1.5&&abs(Dtrk2Eta)<1.5&&Dtrk1PtErr/Dtrk1Pt<0.3&&Dtrk2PtErr/Dtrk2Pt<0.3";
Bool_t isPbPb = false;

void triggerturnonFast(TString trigger="HLT_PADmesonPPTrackingGlobal_Dpt5_v1")
{
  TH1D* getYield(TTree* nt, TString triggerpass, TString triggername, TString prescale, TString variable, TString varname, TString varlatex, Int_t BIN_NUM, Double_t BIN_MIN, Double_t BIN_MAX, TString addcut="");
  void plotTurnOn(TH1D* hnominator, TH1D* hdenominator, TString triggerlegend, TString triggername, TString varname, TString varlatex, Int_t BIN_NUM, Double_t BIN_MIN, Double_t BIN_MAX);

  TString infname;
  infname = "openHLT.root";
  //infname = "/data/dmeson2015/Dntuple/ntD_pp_run262163PromptReco_MB_7MEvents.root";
  TFile* infile = new TFile(infname);
  TTree* root = (TTree*)infile->Get("Dfinder/ntDkpi");
  TTree* nthlt = (TTree*)infile->Get("hltbitanalysis/HltTree");
  root->AddFriend(nthlt);

  TH1D* hpp_pt = getYield(root,"","","","Dpt","pt","p_{T} (GeV/c)",10,0,20);
  TH1D* hpp_pt_Hlt = getYield(root,Form("&&%s",trigger.Data()),Form("_%s",trigger.Data()),Form("*%s_Prescl",trigger.Data()),"Dpt","pt","p_{T} (GeV/c)",10,0,20);
  plotTurnOn(hpp_pt_Hlt,hpp_pt,trigger,Form("_%s",trigger.Data()),"pt","p_{T} (GeV/c)",10,0,20);
}

TH1D* getYield(TTree* nt, TString triggerpass, TString triggername, TString prescale, TString variable, TString varname, TString varlatex, Int_t BIN_NUM, Double_t BIN_MIN, Double_t BIN_MAX, TString addcut="")
{
  TH1D* hDistrib = new TH1D(Form("h%s_Distrib_%s",triggername.Data(),varname.Data()),Form(";D %s;Event",varlatex.Data()),BIN_NUM,BIN_MIN,BIN_MAX);
  nt->Project(Form("h%s_Distrib_%s",triggername.Data(),varname.Data()),Form("%s%s",variable.Data(),prescale.Data()),Form("%s%s%s",prefilter.Data(),addcut.Data(),triggerpass.Data()));
  hDistrib->Sumw2();
  TCanvas* cDistrib = new TCanvas(Form("c%s_Distrib_%s",triggername.Data(),varname.Data()),"",500,500);
  hDistrib->Draw();
  hDistrib->SetStats(0);
  if(isPbPb) cDistrib->SaveAs(Form("triggerturnonPlots/data/pbpb/c%s_Distrib_%s.pdf",triggername.Data(),varname.Data()));
  else cDistrib->SaveAs(Form("triggerturnonPlots/data/pp/c%s_Distrib_%s.pdf",triggername.Data(),varname.Data()));

  return hDistrib;
}

void plotTurnOn(TH1D* hnominator, TH1D* hdenominator, TString triggerlegend, TString triggername, TString varname, TString varlatex, Int_t BIN_NUM, Double_t BIN_MIN, Double_t BIN_MAX)
{
  TEfficiency* pEff = new TEfficiency(*hnominator,*hdenominator);
  pEff->SetName(Form("p%s_Eff_%s",triggername.Data(),varname.Data()));
  TCanvas* cEff = new TCanvas(Form("c%s_Eff_%s",triggername.Data(),varname.Data()),"",500,500);
  TH2D* hempty = new TH2D(Form("hempty_%s_Eff_%s",triggername.Data(),varname.Data()),Form(";D^{0} %s;Pass efficiency",varlatex.Data()),BIN_NUM,BIN_MIN,BIN_MAX,10,0,1.2);
  hempty->SetStats(0);
  hempty->Draw();
  pEff->Draw("PSAME");
  TLatex* tex = new TLatex(0.18,0.96,triggerlegend);
  tex->SetNDC();
  tex->SetTextFont(42);
  tex->SetTextSize(0.04);
  tex->Draw();
  if(isPbPb) cEff->SaveAs(Form("triggerturnonPlots/data/pbpb/c%s_Eff_%s.pdf",triggername.Data(),varname.Data()));
  else cEff->SaveAs(Form("triggerturnonPlots/data/pp/c%s_Eff_%s.pdf",triggername.Data(),varname.Data()));
}
