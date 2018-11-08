import random

Length = random.randint(1,4)

#Peshran

First_Name1 = ['I','Ayl','Nen','Ara','Yas','Ae','Yee','Ukr','Bor','Ush','Ur','Sh','Vastr','Asta','Tar','Uk','Uz','Uzk','Ino','Anta','Kaz','Cirk','Seen','Seene','Talu','Tabo','Dashkour','Ma','Keni','Er','Ri','Zer','Mek','Etus','Nan','Hriv','Wal','Kaza','Kyar','Yab','Kev','Lan','Yan','Yue','Lova','Heg','Shuk','Ven','In']
First_Name2 = ['i','ayl','nen','ara','yas','ae','yee','ukr','bor','ush','ur','sh','vastr','asta','tar','uk','uz','uzk','ino','anta','kaz','cirk','seen','seene','talu','tabo','dashkour','ma','keni','er','ri','zer','mek','etus','nan','hriv','wal','kaza','kyar','yab','kev','lan','yan','yue','lova','heg','shuk','ven','in']


Last_Name1 = ['I','Ayl' ,'Nen','Ara','Yas','Ae','Yee','Ukr','Bor','Ush','Ur','Sh','Vastr','Asta','Tar','Uk','Uz','Uzk','Ino','Anta','Kaz','Cirk','Seen','Seene','Talu','Tabo','Dashkour','Ma','Keni','Er','Ri','Zer','Mek','Etus','Nan','Hriv','Wal','Kaza','Kyar','Yab','Kev','Lan','Yan','Yue','Lova','Heg','Shuk','Ven','in']
Last_Name2 = ['i','ayl','nen','ara','yas','ae','yee','ukr','bor','ush','ur','sh','vastr','asta','tar','uk','uz','uzk','ino','anta','kaz','cirk','seen','seene','talu','tabo','dashkour','ma','keni','er','ri','zer','mek','etus','nan','hriv','wal','kaza','kyar','yab','kev','lan','yan','yue','lova','heg','shuk','ven','in']
Full_Name = (random.choice(First_Name1)+random.choice(First_Name2),random.choice(Last_Name1)+random.choice(Last_Name2))

#CharacterName
if Length == 1:
    print("Peshran Name: "+random.choice(First_Name1)+random.choice(First_Name2),random.choice(Last_Name1)+random.choice(Last_Name2))

if Length == 2 or Length == 3 or Length == 4:
    print("Peshran Name: "+random.choice(First_Name1)+random.choice(First_Name2)+random.choice(First_Name2),random.choice(Last_Name1)+random.choice(Last_Name2)+random.choice(Last_Name2))
#LocationName
print("Peshran Location: "+random.choice(First_Name1)+random.choice(First_Name2)+random.choice(First_Name2))

#Cardian

CFirst_Name1 = ['Run','Un','Wa','Nu','Dian','Radian','Re','Dar','Aran','Ike','Jikro','Kilmon','Kano','Ax','Hal','Di','Da','De','Du','Kal','Ki','Ka','Ke','Ku','Lar','Qi','Dikilar','Do','Me','Jek','Ya','Bu','Ba','Uo','Ko','Po',"Kee'","Sol","Kai","Wad","Del","Wano","Kash"]
CFirst_Name2 = ['run','un','wa','nu','dian','radian','re','dar','aran','ike','jikro','kilmon','kano','ax','hal','di','da','de','du','kal','ki','ka','ke','ku','lar','qi','dikilar','do','me','jek','ya','bu','ba','uol','kol','pa',"keei","sol","kai","wad","del","war","kir"]

CLast_Name1 = ['Run','Un','Wa','Nu','Dian','Radian','Re','Dar','Aran','Ike','Jikro','Kilmon','Kano','Ax','Hal','Di','Da','De','Du','Kal','Ki','Ka','Ke','Ku','Lar','Qi','Dikilar','Do','Me','Jek','Ya','Bu','Ba','Uo','Ko','Po',"Kee'","Sol","Kai","Wad","Del","Wano","Kash"]
CLast_Name2 = ['run','un','wa','nu','dian','radian','re','dar','aran','ike','jikro','kilmon','kano','ax','hal','di','da','de','du','kal','ki','ka','ke','ku','lar','qi','dikilar','do','me','jek','ya','bu','ba','uol','kol','pa',"keei","sol","kai","wad"," del","war","kir"]

print()


#CharacterName
print("Cardian Name: "+random.choice(CFirst_Name1)+random.choice(CFirst_Name2),random.choice(CLast_Name1)+random.choice(CLast_Name2))

#LocationName
if Length == 1:
    print("Cardian Location: "+random.choice(CFirst_Name1)+random.choice(CFirst_Name2))

if Length == 2 or Length == 3 or Length == 4:
    print("Cardian Location: "+random.choice(CFirst_Name1)+random.choice(CFirst_Name2)+random.choice(CFirst_Name2))

print()

#Ecanine

EFirst_Name1 = ['Da','Ven','Val','Gjo','Rode','Savs','Branu','Ko','Mar','Tar','Fule','Egak','Fif','Ya','Mo','Reen','Kar','Skop','Taf','Sar','Gak','Lan','Fuer','Di','De','Du','Fer','Noes','Gordj','Yek','Bek','Tek','Rek','Sek','Kek','Uek','Pek','Iek','Hek','Lek','Mes','Ral','To','Si','Saf']
EFirst_Name2 = ['da','ve','va','jo','rode','sav','branu','ko','ma','ta','fu','ega','fif','fi','ya','mo','re','ka','skopp','ta','sa','ga','la','fu','di','de','noes','oush','toush','hom','palr','shom','gges','nod','es','see','ree','maf','terf','eca','en','ay','me','ka','les','lat','ga','dad']


ELast_Name1 = ['Da','V','Ven','Val','Gjo','Rode','Savs','Branu','Ko','Mar','Tar','Fule','Egak','Fif','Ya','Mo','Reen','Kar','Skop','Taf','Sar','Gak','Lan','Fuer','Di','De','Du','Fer','Noes','Gordj','Yek','Bek','Tek','Rek','Sek','Kek','Uek','Pek','Iek','Hek','Lek','Mes','Ral','To','Si','Saf']
ELast_Name2 = ['da','v','ve','va','jo','rode','sav','branu','ko','ma','ta','fu','ega','fif','fi','ya','mo','re','ka','skopp','ta','sa','ga','la','fu','di','de','noes','oush','toush','hom','palr','shom','gges','nod','es','see','ree','maf','terf','eca','uda','es','en','tice','ay','me','ka','les','lat','ga','dad']

#Ecanine Name:
if Length == 1:
    print("Ecanine Name: "+random.choice(EFirst_Name1)+random.choice(EFirst_Name2), random.choice(ELast_Name1)+random.choice(ELast_Name2))

if Length == 2 or Length == 3 or Length == 4:
    print("Ecanine Name: "+random.choice(EFirst_Name1)+random.choice(EFirst_Name2)+random.choice(EFirst_Name2), random.choice(ELast_Name1)+random.choice(ELast_Name2))


#Ecanine Location

if Length == 1:
    print("Ecanine Location: "+random.choice(EFirst_Name1)+random.choice(ELast_Name2))
if Length == 2:
    print("Ecanine Location: "+random.choice(EFirst_Name1)+random.choice(EFirst_Name2)+random.choice(ELast_Name2))
if Length == 3 or Length == 4:
    print("Ecanine Location: "+random.choice(EFirst_Name1)+random.choice(EFirst_Name2)+random.choice(EFirst_Name2)+random.choice(ELast_Name2))
    
print()

#TavazanName

TFirst_Name = ['Jun','Jul''Zug','Tav','Az','Val','En','Rag','An','Ug','Mak','Tak','Al','Gur','Yeg','Ya','Ge','Va','Vug','Vag','Taz','Ter','Yug','Ug-','Geu-','Ger-','Tey-','Za-','Yg','Yg-','Dah','Gah','Sav','Sahv','Tshev-','Tsheg-','Tshar','Say','Hu-','Gu-','Az-','Eg','Da-']

TLast_Name = ['zug','tav','jun','jul','az','val','en','rag','an','ug','mak','tak','al','gur','yeg','ya','ge','va','vug','vag','taz','ter','yug','gumeg','gumayu','meg','vag','yava','yohg','dah','gah','sav','sahv','sheg','shev','say','zah','zug','vag','gaz','oc','od','riv','ik','ic','eg' ]


if Length == 1:
    print("Tavazan Name: Talabad "+random.choice(TFirst_Name)+random.choice(TLast_Name))

if Length == 2:
    print("Tavazan Name: Talabad "+random.choice(TFirst_Name)+random.choice(TLast_Name)+random.choice(TLast_Name))

if Length == 3:
    print("Tavazan Name: Talabad "+random.choice(TFirst_Name)+random.choice(TLast_Name)+random.choice(TLast_Name)+random.choice(TLast_Name))

if Length == 4:
    print("Tavazan Name: Talabad "+random.choice(TFirst_Name)+random.choice(TLast_Name)+random.choice(TLast_Name)+random.choice(TLast_Name))
    
#TavazanLocation

if Length == 1:
    print("Tavazan Location: Tabadalaba "+random.choice(TFirst_Name)+random.choice(TLast_Name))

if Length == 2:
    print("Tavazan Location: Tabadalaba "+random.choice(TFirst_Name)+random.choice(TLast_Name)+random.choice(TLast_Name))

if Length == 3:
    print("Tavazan Location: Tabadalaba "+random.choice(TFirst_Name)+random.choice(TLast_Name)+random.choice(TLast_Name)+random.choice(TLast_Name))

if Length == 4:
    print("Tavazan Location: Tabadalaba "+random.choice(TFirst_Name)+random.choice(TLast_Name)+random.choice(TLast_Name)+random.choice(TLast_Name))
    
print()

#Andari Name

AFirst_Name = ["Don",'Dar','Dor','Kah','Ra','Ken','Kai','An','And', 'Cat', 'Tada', 'As','Anda','Kor','Ke','Ko','Par','Mi','Ch','Ma','Ter','Nar','Qir','Tende','Ran','Zet','Uv','On','Lo','Pa','Je','Mar','Doa','Afan','Fa','Fes','Nur','Tak','Mo','Zar','Kel','Dol','Beyan','Fel','Ter','Apu','Pu','Dja','Muna','Yuol','Tad','Sarre']

ALast_Name = ['don','run','dar','dor','kah','ra','ken','kai','an','and', 'cat', 'tada', 'as','anda','kor','ke','ko','par','mi','ch','ma','ter','nar','qir','tende','ran','zet','uv','on','lo','pa','je','mar','doa','afan','fa','fes','nur','tak','mo','zar','kel','dol','beyn','fel','ter','apu','pu','dja','muna','yuol','tad','lai','marai','sarai','makano','sarre']

if Length == 1:
    print("Andari Name:", random.choice(AFirst_Name)+random.choice(ALast_Name), random.choice(AFirst_Name)+random.choice(ALast_Name))

if Length == 2 :
    print("Andari Name:", random.choice(AFirst_Name)+random.choice(ALast_Name), random.choice(AFirst_Name)+random.choice(ALast_Name)+random.choice(ALast_Name))

if Length == 3 or Length == 4:
     print("Andari Name:", random.choice(AFirst_Name)+random.choice(ALast_Name)+random.choice(ALast_Name)+random.choice(ALast_Name), random.choice(AFirst_Name)+random.choice(ALast_Name)+random.choice(ALast_Name)+random.choice(ALast_Name)+random.choice(ALast_Name))
     
#Andari Location
     
if Length == 1:
     print("Andari Place:", random.choice(AFirst_Name)+random.choice(ALast_Name),"Kel")

if Length == 2:
    print("Andari Place:", random.choice(AFirst_Name)+random.choice(ALast_Name)+random.choice(ALast_Name),"Dol")
         
if Length == 3:
     print("Andari Place:", random.choice(AFirst_Name)+random.choice(ALast_Name)+random.choice(ALast_Name)+random.choice(ALast_Name),"Kel")

if Length == 4:
    print("Andari Place:", random.choice(AFirst_Name)+random.choice(ALast_Name)+random.choice(ALast_Name)+random.choice(ALast_Name),"Dol")

print()

#Kyem Name

KFirst_Name = ["Mu","Mik","Nuv","Ur","Tal","Ynt","Kiue","Suk","Kar","Mau","Ka","Ta","Kii","Opa","Yel","Mua","Luo","Pat","Ten","Iop","Jeje","Tatr","Deg","Nene","Sen","Jep","Fel","Mad","Ku","Su","Yel","Tap","Ba","Maku","Sen","Tet","Kere","Senj","Lep","Pal","Yel","Kata","Ay"]    
KLast_Name = ["mu","mik","nuv","ur","tal","ynt","kiue","suk","kar","mau","ka","ta","kii","opa","yel","mua","luo","pat","ten","iop","jeje","tatr","deg","nene","sen","jep","fel","mad","ku","su","yel","tap","ba","saku","sen","tet","kere","senj","lep","pal","yel","kata","kem","ynt","rienne","ykem"] 

if Length == 1:
    print("Kyem Name:", random.choice(KFirst_Name)+random.choice(KLast_Name), random.choice(KFirst_Name)+random.choice(KLast_Name))

if Length == 2 :
    print("Kyem Name:", random.choice(KFirst_Name)+random.choice(KLast_Name), random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name))

if Length == 3:
    print("Kyem Name:", random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name), random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name))
    
if Length == 4:
     print("Kyem Name:", random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name)+random.choice(KLast_Name), random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name)+random.choice(KLast_Name)+random.choice(KLast_Name))

#Kyem Location

if Length == 1:
    print("Kyem Location: "+random.choice(KFirst_Name)+random.choice(KLast_Name))
if Length == 2:
    print("Kyem Location: "+random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name))
if Length == 3:
    print("Kyem Location: "+random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name)+random.choice(KLast_Name))
if Length == 4:
    print("Kyem Location: "+random.choice(KFirst_Name)+random.choice(KLast_Name)+random.choice(KLast_Name)+random.choice(KLast_Name)+random.choice(KLast_Name))