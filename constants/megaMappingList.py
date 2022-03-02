#!/usr/bin/python3
# coding: utf-8

megaMapping = {
 # VIRKESTOFFER
 'akalabrutinib': 'MANUELL',
 'amikacin': 'MANUELL',
 'bedakvilin': 'MANUELL',
 'bortezomid': 'MANUELL',
 'brentuksimab': 'Brentuksimab vedotin ',
 'bupropion': 'SPLITTE (bupropion, bupropion (røykeavhengighet))',
 'cannabidiol': 'MANUELL',
 'ceftolozan': 'MANUELL',
 'cilastatin': 'MANUELL',
 'deferasiroks': 'MANUELL',
 'dekstraner': 'SPLITTE (dekstran, dekstran med hypertont saltvann)',
 'dekstropropoksyfen': 'MANUELL',
 'delamanid': 'MANUELL',
 'dibotermin-alfa-2b (inductos)': 'MANUELL',
 'didanosin': 'MANUELL',
 'doripenem': 'MANUELL',
 'ergotamin': 'MANUELL',
 'etylmorfin': 'Etylmorfinkombinasjoner',
 # 'filgotinib': 'MATCHER',
 'flukloksacillin': 'MANUELL',
 'gadobenat': 'MANUELL',
 'gadobutrol': 'MANUELL',
 'gadoksetinsyre, dinatrium-': 'MANUELL',
 'gadoteridol': 'MANUELL',
 'gadotersyre': 'MANUELL',
 'guanetidin': 'MANUELL',
 'hetastivelse (hydroksyetylstivelse)': 'HETASTIVELSE',
 'heksametylmelamin': 'MANUELL',
 'histrelin': 'MANUELL',
 'iopentol': 'MANUELL',
 'jobitridol': 'MANUELL',
 'jodiksanol': 'MANUELL',
 'joheksol': 'MANUELL',
 'jomeprol': 'MANUELL',
 'joversol': 'MANUELL',
 'klavulanat': 'MANUELL',
 'klodronat': 'MANUELL',
 'kolekalsiferol': 'Vitamin D og analoger',
 'korifollitropin-alfa': 'korifollitropin alfa', # Sverre fiksa: uten bindestrek i tittel
 'krizanlizumab': 'MANUELL',
 'lepirudin': 'MANUELL',
 'lidokain': 'MANUELL',
 'metadon': 'MANUELL',
 'muromonab-cd3': 'MANUELL',
 'nintedanib': 'SPLITTE (Nintedanib (lunge), Nintedanib (onkologi))',
 'nusinersen': 'MANUELL',
 'paraaminosalisylsyre': 'MANUELL',
 'parathyreoideahormon': 'MANUELL',
 'peginterferon beta-1a': 'MANUELL',
 'pemigatinib': 'MANUELL',
 'piperacillin': 'MANUELL',
 'piperakin': 'MANUELL',
 'rokuronium': 'Rokuron',
 'sakinavir': 'MANUELL',
 'simeprevir': 'MANUELL',
 'sulfametoksazol': 'MANUELL',
 'telaprevir': 'MANUELL',
 'tenofovirdisoproksil (finnes også i kombinasjon med emtricitabin)': 'MANUELL',
 'tetrahydrocannabinol (thc)': 'IGNORER',
 'tipiracil': 'MANUELL',
 'tokofersolan': 'MANUELL',
 'tretinoin': 'SPLITTE (Tretinoin (akne), Tretinoin (onkologi))',
 'velpatasvir': 'MANUELL',
 'zoledronsyre': 'Zoledronat',
 'abemabciklib': 'IGNORER',
 'amprenavir': 'Amprenavir/fosamprenavir',
 'artemeter (+ lumefantrin)': 'Artemeter–lumefantrin',
 'biktegravir, emtricitabin, tenofoviralafenamid i kombinasjon (biktarvy)': 'MANUELL',
 'bulevirtid': 'IGNORER',
 'cabazitaxel': 'Kabazitaxel',
 'carbimazol': 'Karbimazol',
 'cyklizin': 'Syklizin',
 'danaparoid': 'IGNORER',
 'darolutamid': 'MANUELL',
 'diemal (barbital)': 'MANUELL',
 'drospirenon': 'MANUELL',
 'elbasvir og grazoprevir (kombinasjonspreparat)': 'MANUELL',
 'eluksadolin': 'MANUELL',
 'entrektinib': 'MANUELL',
 'etinyløstradiol': 'MANUELL',
 'etonogestrel': 'MANUELL',
 'fentiaziner': 'MANUELL',
 'ferumoksytol': 'MANUELL',
 'fosamprenavir': 'MANUELL',
 'gadoversetamid': 'MANUELL',
 'givosiran': 'MANUELL',
 'maviret': 'Glekaprevir-pibrentasvir',
 'griseofulvin': 'MANUELL',
 # 'inklisiran': 'MATCHER', # (lagt til 19. november)
 'interferon alfa': 'Interferon alfa-2, peginterferon alfa-2',
 'interferon beta': 'Interferon beta-1, peginterferon beta-1',
 'ivakaftor/tezakaftor': 'MANUELL',
 'kombinasjons p pille': 'MANUELL',
 'larotrektinib': 'MANUELL',
 'maoh a': 'MANUELL',
 'maoh b': 'MANUELL',
 'metronidazol': 'Metronidazol',
 'nateglinid': 'IGNORER',
 'natriumaurotiomalat': 'MANUELL',
 'norgestrel': 'MANUELL',

  # MAPPING - GRUPPEOMTALER
 'aminosyrer + glukose': 'MANUELL',
 'aminosyrer + glukose + fett': 'MANUELL',
 'angiotensin iireseptorantagonister': 'angiotensin II-reseptorantagonister',
 'antacida, kombinasjoner og komplekser av aluminium-, kalsium- og magnesiumforbindelser': 'Antacida',
 'at1reseptorantagonister': 'IGNORER',
 'betalaktampenicilliner': 'Betalaktamasefølsomme penicilliner',
 'betareseptorantagonister': 'Adrenerge betareseptorantagonister',
 'cannabinoider': 'MANUELL',
 'elektrolytter': 'MANUELL',
 'folsyreantagonister': 'MANUELL',
 'ikkesteroide antiinflammatoriske midler': 'Ikke‑steroide antiinflammatoriske midler (NSAID)',
 'jodholdige røntgenkontrastmidler': 'MANUELL',
 'kontrastmidler, jodholdige': 'MANUELL',
 'kontrastmidler ved magnettomografi': 'IGNORER',
 'nsaids (ikke-steroide antiinflammatoriske midler)': 'Ikke‑steroide antiinflammatoriske midler (NSAID)',
 'tiazid-/tiazidlignende diuretika': 'tiazider',
 'acehemmere': 'Angiotensinkonverterende enzymhemmere',
 'antidepressiva, ssri og tca': 'SPLITTE (Selektive serotoninreopptakshemmere, Trisykliske antidepressiva)',
 'antihistaminer (histamin h1antagonister)': 'Histamin H1‑antagonister',
 'antikoagulantia, perorale': 'MANUELL',
 'antikonsepsjonsmidler, perorale': 'MANUELL',
 'adrenerge alfa-1-reseptorantagonister': 'Adrenerge alfa-1 reseptorantagonister',
 'adrenerge reseptoragonister': 'MANUELL',
 'alfa-1-, betareseptorantagonister, kombinerte': 'MANUELL',
 'alfa-1-reseptorantagonister, adrenerge': 'MANUELL',
 'alkylsulfonater': 'MANUELL',
 'androgener/anabole steroider': 'Androgene/anabole steroider',
 'antidiabetika, perorale': 'Perorale blodglukosesenkende midler',
 'antihistaminer': 'MANUELL',
 'antikolinergika': 'MANUELL',
 'antrasykliner': 'MANUELL',
 '5asapreparater': '5-Aminosalisylsyreforbindelser',
 'betalaktamantibiotika': 'Betalaktamasefølsomme penicilliner',
 'bronkolytika, adrenerge': 'MANUELL',
 'epipodofyllotoksiner': 'MANUELL',
 'galaktoseagglomerater': 'MANUELL',
 'gnrhanaloger': 'Analoger av gonadotropinfrigjørende hormon',
 'gonadotropinfrisettende hormoner': 'IGNORER',
 'h1antagonister': 'Histamin H1‑antagonister',
 '5ht1agonister': 'Selektive 5-HT1-reseptoragonister',
 '5ht3antagonister': 'Serotoninantagonister',
 'kolinesterasehemmere': 'MANUELL',
 'kvitaminantagonister': 'Vitamin K-antagonister',
 'metylxantiner': 'MANUELL',
 'mineralkortikoider': 'MANUELL',
 'monoaminoksidasehemmere': 'MANUELL',
 'monoaminreopptakshemmere, uselektive (tca)': 'MANUELL',
 'muskelrelakserende midler, perifert virkende': 'IGNORER',
 'penicilliner': 'MANUELL',
 'perorale antidiabetika': 'Perorale blodglukosesenkende midler',
 'platehemmere': 'IGNORER',
 'progestogener': 'MANUELL',
 'prostaglandiner': 'Prostaglandiner/prostaglandinanaloger',
 'retinoider': 'MANUELL',
 'røntgenkontrastmidler': 'MANUELL',
 'sennepsgassderivater': 'MANUELL',
 'serotoninagonister': 'IGNORER',
 'slimhinneavsvellende legemidler': 'MANUELL',
 'steroidantibiotika': 'MANUELL',
 'sulfonamider': 'MANUELL',
 'sulfonylureaforbindelser': 'Sulfonylureaderivater',
 'tiaziddiuretika': 'Tiazider',
 'uselektive hemmere av monoaminoksidase': 'Irreversible, uselektive monoaminoksidasehemmere (MAOH)',
 'uselektive monoaminopptakshemmere': 'Irreversible, uselektive monoaminoksidasehemmere (MAOH)',
 'anestesimidler': 'MANUELL',
 'angiotensin ii-reseptorantagonister': 'angiotensin II-reseptorantagonister',
 'antidoter': 'MANUELL',
 'antihypertensiva': 'MANUELL',
 'antiinflammatoriske midler, ikke steroide': 'Ikke‑steroide antiinflammatoriske midler (NSAID)',
 'antikonseptiva': 'Antikonsepsjonsmidler',
 '5-asa-preparater': '5-Aminosalisylsyreforbindelser',
 'beta-2-reseptoragonister, adrenerge': 'Adrenerge beta-2-reseptoragonister',
 'cox-2-hemmere': 'MANUELL',
 'fungicider til lokal bruk': 'MANUELL',
 '5-ht1-agonister': 'Selektive 5-HT1-reseptoragonister',
 '5-ht3-antagonister': 'Serotoninantagonister',
 'immunsuppressive midler': 'MANUELL',
 'pankreasenzymer': 'Pankreasenzympreparater',
 'progesteroner': 'MANUELL',
 'thyreoideahormoner': 'Tyreoideahormoner',
 'trisykliske antidepressiva (tca)': 'Trisykliske antidepressiva',
 'vitamin d og vitamin d-analoger': 'Vitamin D og analoger',
}
