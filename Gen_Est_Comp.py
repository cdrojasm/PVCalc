def Gen_Est_Comp(HSP,Wp, Eff):
    return(HSP+Wp+Eff)

def Eficomp(MiMatch, ContEff, WirEff, InvEff, OrtEff, OverSiz):
    return(MiMatch*ContEff*WirEff*InvEff*OrtEff*OverSiz)


Hor=4.2
PotIns=7500
Efi=0.9
GEN=Gen_Est_Comp(Hor,PotIns,Efi)
print("To a HSP value of ",Hor,", a Watt Pike installed Power of ",PotIns," and a efficiency of ",Efi)
print("We obtain a generation of ",GEN)


