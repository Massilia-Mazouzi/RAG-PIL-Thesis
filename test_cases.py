
"""
This file contains the list of standardized test questions and ground truth answers
used to evaluate both RAG implementations (naïve and enhanced).
It is imported in both notebooks for consistent evaluation.
"""
test_cases=[
    {
        "question_id":"Q1",
        "question":" comment conserver humalog mix 25 100ui kwikpen ",
        "ground_truth":"Avant la première utilisation, Humalog Mix25 KwikPen doit être conservé au réfrigérateur entre 2°C et 8°C. Une fois en cours d'utilisation, il doit être conservé à température ambiante entre 15°C et 30°C et doit être jeté après 28 jours. Il ne doit pas être exposé à une chaleur excessive ou au soleil et ne doit pas être laissé au réfrigérateur .Le stylo KwikPen ne doit pas être conservé avec l’aiguille vissée dessus."
    },
    {
        "question_id":"Q2",
        "question":"Orapen 1500 000ui comp peut-il être utilisé en association avec un antihypertenseur?",
        "ground_truth":"Aucune information concernant les antihypertenseurs n'est mentionnée dans la notice."
    },    
    {
        "question_id":"Q3", 
        "question":"Quels sont les signes d une réaction allergique grave à Calcidose 500mg sachet dose ?",
        "ground_truth":"Aucun signe de réaction allergique grave n'est mentionné dans la notice"


    },
    {
        "question_id":"Q4",
        "question":"Quels sont les principes actifs contenus dans Calcidose 500mg sachet dose?",
        "ground_truth":"la substance active contenue dans ce medicament est Carbonate de calcium"
    },
    {
        "question_id":"Q5",
        "question":"Quels sont les effets négatifs de Calcidose 500mg sachet dose?",
        "ground_truth":"Les effets négatifs de Calcidose 500 peuvent inclure une bouche sèche et  en cas de traitement prolongé, un risque d'augmentation du taux de calcium dans le sang et les urines. SIGNALER À VOTRE MÉDECIN OU À VOTRE PHARMACIEN TOUT EFFET NON SOUHAITÉ ET GËNANT QUI NE SERAIT PAS MENTIONNÉ DANS CETTE NOTICE"
    },
    {
        "question_id":"Q6",
        "question":"Quelle est la posologie recommandée de AMODEX-Gé 250MG 5ML pdre pour un enfant de 10 ans?",
        "ground_truth":"la dose recommende pour un enfant de 10 ans est de 25 mg/kg à 150 mg/kg par 24 heures"
    },
    {
        "question_id":"Q7",
        "question":"Est-il possible d utiliser AMODEX-Gé 250MG 5ML pdre  pendant la grossesse?",
        "ground_truth":"Amodex Gé peut être utilisé pendant la grossesse Amodex Gé peut être utilisé pendant la grossesse en cas de besoin. D'UNE FAÇON GÉNÉRALE, IL CONVIENT AU COURS DE LA grossesse de toujours demander l avis de votre medecin ou de votre pharmacien"
    },
    {
        "question_id":"Q8",
        "question":"Est-ce que AMODEX-Gé 250MG 5ML pdre  peut causer la diarrhée pour un adulte ?",
        "ground_truth":"Oui, il peut causer des troubles digestifs comme la diarrhée "
    },
    {
        "question_id":"Q9",
        "question":" qu'est ce que TOBREX 300000ui colly en solution et dans quels cas est il utiliser?",
        "ground_truth":" TOBREX 0,3 est un collyre en solution est indiqué pour le traitement local de certaines infections de l'œil dues à des bactéries sensibles, telles que les conjonctivites, les kératites et les ulcères de la cornée."
    },     
    {
        "question_id":"Q10", 
        "question":"quels sont les effets indésirables possible de forlax 4g sach pdre solution buv pour un enfant ?",
        "ground_truth":"les effets indésirables possible de forlax 4g chez l'enfant sont: Douleurs abdominales, Diarrhée , Vomissements, Ballonnements, Nausée, Réactions d'hypersensibilité"
    },
    {
        "question_id":"Q11",
        "question":"quells sont Indications thérapeutiques de clovir 200mg comp?",
        "ground_truth":"CLOVIR 200mg est indiqué dans le traitement de Herpes simplex (incluant les primo-infections génitales et les récurrences ultérieures), des infections virales cutanées et de la membrane muqueuse, dans la prévention des infections à virus Herpes simplex chez les sujets immunodéprimés , et dans le traitement de l'Herpes Zoster"
    },
    {
        "question_id":"Q12", 
        "question":"Quels sont les médicaments à ne pas utiliser avec ENCOFLUIDE ADULTE 0,25g ?",
        "ground_truth":"Encofluide adulte ne doit pas etre utiliser avec les médicaments à effet antabuse et les psychotropes."
    },
    {
        "question_id":"Q13",
        "question":"Est-ce qu il existe un risque d'un surdosage de doliprane 300mg suppo ?",
        "ground_truth":"Oui,Il existe un risque de surdosage avec DOUPRANE 300 mg, suppositoireIl existe un risque de surdosage avec DOUPRANE 300 mg, suppositoire, et en cas de surdosage, un traitement symptomatique est nécessaire.."
    },
    {
        "question_id":"Q14",
        "question":"est ce que je peux utiliser doliprane 300mg suppo si j'ai une inflammation annale?",
        "ground_truth":"Non, ce médicament ne doit pas être utilisé en cas d inflammation recente anale."
    },
    {
        "question_id":"Q15", 
        "question":"Quels sont les cas à ne pas utiliser DEXOREN 0.25mg comp ",
        "ground_truth":"Ce médicament ne doit pas être utilisé dans les cas de certaines anomalies du fonctionnement cardiaque et en association avec le sultopride ou des injections intraveineuses de calcium."
    },
    {
        "question_id":"Q16",
        "question":"quels sont les Effets indésirables possibles de cital 50mg comp?",
        "ground_truth":"Les effets indésirables possibles de CITAL 50mg comprimé incluent : troubles de la vision ; bouffées de chaleur, maux de tête, étourdissement, vertiges ; troubles digestifs ; règles plus abondantes, saignement entre les règles ; nervosité, insomnie, état dépressif ; envie d'uriner fréquente ; réaction allergique cutanée ; et augmentation de la probabilité d'une grossesse multiple."
    },
    {
        "question_id":"Q17", 
        "question":"Quels sont les signes d'un surdosage du médicament DEXOREN 0.25mg comp ?",
        "ground_truth":"Les effets indésirables sont le plus souvent le signe d un surdosage : nausées, vomissements, diarrhée, perte de l appétit, coloration en jaune de la vision, vertiges, maux de tête, troubles psychiques (notamment chez la personne âgée), troubles du rythme cardiaque variés, palpitations."
    },
    {
        "question_id":"Q18",
        "question":"Est-ce que je peux prendre le médicament ipnodis 5mg ml sol inj si j'si des troubles respiratoires?",
        "ground_truth":"vous devez informer le medecin avant de prendre Ipnodis si vous avez des difficultés respiratoires"
    },
    {
        "question_id":"Q19", 
        "question":"est-il possible de prendre Cerazette 0,75 mg comp durant la grossesse ?",
        "ground_truth":"Il est déconseillé de prendre Cerazette pendant la grossesse"
    },
    {
        "question_id":"Q20",
        "question":"quels sont les effects indesirables du maalox maux destomac?",
        "ground_truth":"Les effets indésirables possibles de Maalox incluent : troubles digestifs comme la diarrhées ou la constipation et, en cas d'utilisation prolongée ou à fortes doses, une diminution du taux de phosphore dans le sang. "
    },
    {
        "question_id":"Q21",
        "question":"est ce que je peux  injecter le medicament insuman rapid 100ui sol dans la veine a la maison?",
        "ground_truth":"Non, l'administration d'insuline dans la veine exige de l'expérience et des précautions rigoureuses. Pour ces raisons, cela doit être fait en milieu hospitalier ou dans une structure spécialisée similaire, et non à domicile."
    },
    {
        "question_id":"Q22",
        "question":"C est quoi la thrombose associée avec Cerazette 0,75 mg comprimé ?",
        "ground_truth":" Une thrombose est la formation d'un caillot de sang susceptible d'obstruer un vaisseau sanguin, souvent dans une veine profonde de la jambe (thrombose veineuse profonde) ou dans les poumons (embolie pulmonaire) Le risque de thrombose est plus élevé chez les utilisatrices de pilules contraceptives, mais il est plus faible avec Cerazette, qui contient uniquement un progestatif, comparé aux pilules combinées contenant des œstrogènes."
    },
    {
        "question_id":"Q23",
        "question":" ce que Risperdal Consta LP 25mg est un medicament psychotrope?",
        "ground_truth":"Oui, Risperdal Consta LP 25mg est un medicament psychotrope "
    },
    {
        "question_id":"Q24", 
        "question":"Est-ce que je peux utiliser voltarene emulgel 0.01 pour traiter l'eczema?",
        "ground_truth":" Voltarene Emulgel gel ne doit pas être utilisé sur des zones de peau affectes par des lésions comme l'eczéma"
    },  
    {    
        "question_id":"Q25",
        "question":"quels sont les médicaments qui peuvent affecter l'activité d'IRESSA 250mg comp pelli  ?",
        "ground_truth":"Les médicaments qui peuvent affecter l'activité d'IRESSA sont : la phénytoïne, la carbamazépine, la rifampicine, l'itraconazole, les barbituriques, les remèdes à base de plantes contenant du Millepertuis, les inhibiteurs de la pompe à protons, les antagonistes des récepteurs H2 et les anti-acides."
    },
    {
        "question_id":"Q26", 
        "question":"Le medicament eprex 40000ui ml est utiliser pour traiter quelles maladies ?",
        "ground_truth":"EPREX est utilisé pour traiter l'anémie symptomatique due à des maladies du rein (chez les enfants en hémodialyse, adultes en hémodialyse ou dialyse péritonéale, et adultes non encore dialysés avec anémie sévère). Il est aussi utilisé dans le traitement de l'anémie chez les adultes sous chimiothérapie pour des tumeurs solides, lymphome malin ou myélome multiple, chez les adultes modérément anémiques donnant leur sang avant une chirurgie, et chez les adultes devant avoir une intervention chirurgicale orthopédique majeure pour diminuer le besoin de transfusions sanguines. Enfin, EPREX est utilisé pour traiter l'anémie chez les adultes atteints de syndromes myélodysplasiques."
    },
    {
        "question_id":"Q27",
        "question":" quels sont les hormones peuvent etre affecter par le medicament Risperdal Consta LP 25mg ?",
        "ground_truth":"Risperdal Consta peut augmenter les taux du hormone prolactine."
    },
    {
        "question_id":"Q28", 
        "question":"Est-ce que je peux utiliser BRONCHOCALM enfants 0,1 sirop pour un nouveau-né ?",
        "ground_truth":"Non, ce médicament ne peut pas etre utiliser pour un nouveau-ne."
    },
    {
        "question_id":"Q29",
        "question":"Quels sont les médicaments à ne pas associer avec BRONCHOCALM enfants 0,1 sirop ?",
        "ground_truth":"Il ne faut pas associer ce médicament avec les IMAO (antidépresseurs) ni avec d autres antitussifs."
    },
    {
        "question_id":"Q30", 
        "question":"Quelle est la dose recommandée de BRONCHOCALM enfants sirop pour un enfant de 45 kg ?",
        "ground_truth":"la dose recommandée pour enfant de 45 kg  est de:  2 cuillères-mesure par prise, à renouveler en cas de besoin au bout de 4 heures, sans dépasser 8 cuillères-mesure par jour."
    },
    {
        "question_id":"Q31",
        "question":"Quelle est la classe pharma du médicament kyncept 10mg comp orodispersible?",
        "ground_truth":"KYNCEPT 10mg appartient à la classe des médicaments appelés inhibiteurs de l'acétylcholinestérase"
    },
    {
        "question_id":"Q32", 
        "question":"Zyloric 100mg comp est utilisé pour traiter quels problemes de sante ?",
        "ground_truth":"ZYLORIC 100 mg, comprimé est utilisé pour réduire la formation de dépôts d’acide urique responsables de la goutte, de certains types de calculs rénaux ZYLORIC 100 mg, comprimé est utilisé pour réduire ou prévenir la formation de dépôts d’acide urique responsables de la goutte, de certains types de calculs rénaux ."
    },
    {
        "question_id":"Q33", 
        "question":" quels sont les contre indication de lamitor 5mg comp dispers ?",
        "ground_truth":"Lamitor 5mg comprimé dispersible ne doit pas être utilisé chez l'enfant de moins de 2 ans, en association avec le millepertuis, et pendant l'allaitement. "
    },
    {
        "question_id":"Q34", 
        "question":"comment conserver le medicament zinnat 250mg comp?",
        "ground_truth":"Conservez-le à une température ne dépassant pas 30°C"
    },
    {
        "question_id":"Q35", 
        "question":"Que contient le médicament trois B 125MG 125MG 0,55MG ?",
        "ground_truth":"Il contient 125 mg de vitamine B1, 125 mg de vitamine B6 et 0,55 mg de vitamine B12. "
    },
    {
        "question_id":"Q36", 
        "question":"TROIS B 125MG 125MG 0,55MG nécessite-t-il une ordonnance médicale ?",
        "ground_truth":"Oui , il necessite une ordonnance medicale."
    },
    {
        "question_id":"Q37", 
        "question":"Quels sont les dangers de prendre des doses élevées de TROIS B 125MG 125MG 0,55MG ?",
        "ground_truth":"De fortes doses de vitamine B12 peuvent induire une acné.De très fortes doses prolongées de vitamine B6 (≥ 500 mg pendant plus de 5 mois) peuvent entraîner des neuropathies sensitives périphériques, généralement réversibles après arrêt du traitement."
    },
    {
        "question_id":"Q38", 
        "question":"quelle est la dose recommende par jour de curacne 5mg caps?",
        "ground_truth":" La dose usuelle de CURACNE est de 0,5 mg par kilogramme par jour . Pour la plupart des patients, une plage de 0,5 à 1,0 mg/Kg/jour.",
    },
    {
        "question_id":"Q39",
        "question":"Quels sont les médicaments à ne pas utiliser avec METRONIDAZOLE BEKER 250mg ?",
        "ground_truth":"Il ne faut pas associer ce médicament avec : Le disulfirame (utilisé dans le traitement de l’alcoolo-dépendance),le busulfan ( utiliser pour traiter certaines maladies du sang et dans la préparation à la greffe de moelle).Certains inducteurs enzymatiques comme la carbamazépine."
    },
    {
        "question_id":"Q40",
        "question":"Quels sont les signe d'un surdosage accidentel de oxynorm 20mg 2ml sol pour inj?",
        "ground_truth": "Les signes d'un surdosage d'OxyNorm peuvent être : pupilles dilatées, insuffisance respiratoire, somnolence, déficience musculaire, pouls ralenti, hypotension. Dans les cas les plus sévères, une perte de conscience , une accumulation de liquide dans les poumons et un collapsus circulatoire peuvent se développer, pouvant entraîner la mort."

    },
    {
        
        "question_id":"Q41",
        "question":"quelle la psologie recommendee de stagid 700mg comp sec",
        "ground_truth": "La posologie recommandée de STAGID 700 mg, comprimé sécable est généralement de 1 comprimé trois fois par jour. Elle peut être determinees par le médecin en fonction des résultats d'examens de laboratoire."
    },
    {
        
        "question_id":"Q42",
        "question":"Est-ce que je peux utiliser Nexavar 200mg avec mes médicaments d épilepsie ?",
        "ground_truth":" certains médicaments pour l épilepsie peuvent interagir avec Nexavar.En particulier : la phénytoïne, la carbamazépine et le phénobarbital peuvent modifier l'effet de Nexavar. Informez votre médecin si vous prenez ces traitements."
    },
    {
        
        "question_id":"Q43",
        "question":" Quelle est la dose à prendre de Nexavar 200mg ?",
        "ground_truth": "La dose recommandée chez l adulte est de deux comprimés de 200 mg, deux fois par jour, soit une dose totale journalière de 800 mg (quatre comprimés par jour)"
    },
    {
        
        "question_id":"Q44",
        "question":"Est-ce que je peux utiliser Biafine 0,67 100g emuls comme crème solaire ?",
        "ground_truth": "Non, ce médicament n est pas un protecteur solaire. Il ne doit pas être utilisé comme crème de soin sur une peau saine."
    },
    {
        
        "question_id":"Q45",
        "question":"Est-ce que Biafine 100g emuls peut causer des effets indésirables ?",
        "ground_truth": "Oui, les effets indésirables suivants sont possibles : Douleurs (picotements) modérées et transitoires après application (15 à 30 minutes). Réactions allergiques de contact rares,rès rares cas d eczéma de contact nécessitant l Arrêt du traitement."
    },
    

]