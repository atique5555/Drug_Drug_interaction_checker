
pairs = {
    ("paracetamol", "ibuprofen"): "No major interaction. Use with caution.",
    ("aspirin", "warfarin"): "High risk of bleeding. Avoid combination.",
    ("metronidazole", "alcohol"): "Severe nausea and vomiting. Avoid alcohol.",
    ("amoxicillin", "allopurinol"): "Increased risk of rash.",
    ("ciprofloxacin", "tizanidine"): "Severe hypotension. Avoid combination.",
    ("simvastatin", "clarithromycin"): "Increased risk of muscle toxicity.",
    ("digoxin", "verapamil"): "Risk of bradycardia. Monitor closely.",
    ("lisinopril", "potassium"): "Risk of hyperkalemia. Monitor potassium levels.",
    ("sildenafil", "nitrates"): "Severe drop in blood pressure. Contraindicated.",
    ("phenytoin", "fluconazole"): "Fluconazole increases phenytoin levels.",
    ("rifampin", "oral contraceptives"): "Reduced contraceptive effectiveness.",
    ("theophylline", "ciprofloxacin"): "Increased theophylline toxicity risk.",
    ("lithium", "NSAIDs"): "Increased lithium levels. Monitor closely.",
    ("spironolactone", "ACE inhibitors"): "Risk of hyperkalemia.",
    ("clopidogrel", "omeprazole"): "Reduced antiplatelet effect of clopidogrel.",
    ("warfarin", "metronidazole"): "Increased bleeding risk.",
    ("levothyroxine", "calcium carbonate"): "Calcium reduces absorption of levothyroxine.",
    ("isoniazid", "rifampin"): "Increased risk of liver toxicity.",
    ("linezolid", "SSRIs"): "Risk of serotonin syndrome.",
    ("methotrexate", "NSAIDs"): "Increased methotrexate toxicity.",
    ("carbamazepine", "erythromycin"): "Increased carbamazepine toxicity.",
    ("diltiazem", "beta blockers"): "Risk of bradycardia or heart block.",
    ("furosemide", "digoxin"): "Risk of digoxin toxicity due to hypokalemia.",
    ("statins", "grapefruit"): "Grapefruit increases statin levels. Avoid.",
    ("azithromycin", "antacids"): "Antacids reduce absorption of azithromycin.",
    ("tramadol", "sertraline"): "Risk of serotonin syndrome.",
    ("codeine", "alcohol"): "Increased CNS depression. Avoid combination.",
    ("metformin", "contrast media"): "Risk of lactic acidosis. Temporarily discontinue metformin.",
    ("atenolol", "verapamil"): "Increased risk of bradycardia and heart block.",
    ("chloramphenicol", "phenytoin"): "Chloramphenicol increases phenytoin levels.",
    ("rifampin", "protease inhibitors"): "Reduced effectiveness of protease inhibitors.",
    ("linezolid", "tyramine-rich foods"): "Hypertensive crisis. Avoid tyramine.",
    ("isoniazid", "phenytoin"): "Increased phenytoin levels. Monitor closely.",
    ("disulfiram", "alcohol"): "Severe reaction: nausea, vomiting, headache. Strictly contraindicated.",
    ("doxycycline", "calcium"): "Calcium reduces absorption of doxycycline.",
    ("methotrexate", "penicillin"): "Increased methotrexate toxicity.",
    ("valproate", "lamotrigine"): "Increased risk of serious skin reactions.",
    ("macrolides", "warfarin"): "Increased bleeding risk. Monitor INR.",
    ("antacids", "iron supplements"): "Antacids reduce iron absorption.",
    ("fluoxetine", "tramadol"): "Increased risk of seizures and serotonin syndrome.",
    ("azathioprine", "allopurinol"): "Increased risk of bone marrow suppression.",
    ("nifedipine", "grapefruit juice"): "Grapefruit increases nifedipine levels.",
    ("clozapine", "ciprofloxacin"): "Increased clozapine concentration. Risk of toxicity.",
    ("omeprazole", "clopidogrel"): "Omeprazole reduces effect of clopidogrel.",
    ("tetracycline", "milk"): "Calcium in milk reduces tetracycline absorption.",
    ("levodopa", "pyridoxine"): "Pyridoxine reduces effect of levodopa.",
    ("MAOIs", "meperidine"): "Risk of life-threatening serotonin syndrome.",
    ("nitrofurantoin", "magnesium trisilicate"): "Decreased nitrofurantoin absorption.",
    ("amiodarone", "warfarin"): "Increased bleeding risk. Monitor INR closely.",
    ("ceftriaxone", "calcium IV"): "Fatal precipitates in neonates. Avoid combination.",
    ("hydrochlorothiazide", "lithium"): "HCTZ may increase lithium levels. Monitor serum lithium.",
    ("azithromycin", "warfarin"): "May enhance the anticoagulant effect of warfarin.",
    ("clarithromycin", "colchicine"): "Increased risk of colchicine toxicity. Avoid combination.",
    ("verapamil", "simvastatin"): "Increased risk of statin-induced myopathy.",
    ("rifampin", "ketoconazole"): "Rifampin reduces effectiveness of ketoconazole.",
    ("fluconazole", "cyclosporine"): "Increased cyclosporine levels and toxicity risk.",
    ("cimetidine", "phenytoin"): "Cimetidine may increase phenytoin levels. Monitor closely.",
    ("erythromycin", "theophylline"): "Increased theophylline serum concentrations.",
    ("aspirin", "methotrexate"): "Increased methotrexate toxicity. Avoid or monitor.",
    ("alcohol", "acetaminophen"): "Increased risk of liver damage. Avoid heavy use.",
    ("digoxin", "quinidine"): "Quinidine increases digoxin levels. Monitor closely.",
    ("lisinopril", "NSAIDs"): "Reduced antihypertensive effect, increased renal risk.",
    ("metformin", "cimetidine"): "May increase metformin levels. Monitor for lactic acidosis.",
    ("amiodarone", "digoxin"): "Increased digoxin levels and toxicity risk.",
    ("ketoconazole", "simvastatin"): "Increased risk of statin toxicity. Avoid combination.",
    ("phenytoin", "dexamethasone"): "May decrease dexamethasone levels. Monitor efficacy.",
    ("spironolactone", "potassium supplements"): "High risk of hyperkalemia. Monitor potassium.",
    ("clozapine", "carbamazepine"): "Increased risk of agranulocytosis. Avoid combination.",
    ("tizanidine", "ciprofloxacin"): "Ciprofloxacin increases tizanidine effects. Severe hypotension possible.",
    ("SSRIs", "triptans"): "Increased risk of serotonin syndrome. Use with caution.",
    ("ciprofloxacin", "magnesium"): "Magnesium may reduce absorption of ciprofloxacin.",
    ("levothyroxine", "iron supplements"): "Iron may reduce absorption of levothyroxine.",
    ("digoxin", "licorice"): "Licorice may enhance digoxin toxicity.",
    ("carbamazepine", "fluoxetine"): "Fluoxetine may increase carbamazepine levels.",
    ("diazepam", "fluvoxamine"): "Fluvoxamine may increase diazepam effects.",
    ("chlorpromazine", "metoclopramide"): "Increased risk of extrapyramidal symptoms.",
    ("metronidazole", "lithium"): "May increase lithium levels and toxicity.",
    ("furosemide", "NSAIDs"): "NSAIDs may reduce diuretic effect of furosemide.",
    ("warfarin", "garlic supplements"): "Garlic may increase bleeding risk with warfarin.",
    ("diltiazem", "cyclosporine"): "Increased cyclosporine blood levels.",
    ("linezolid", "dopaminergic drugs"): "May increase blood pressure.",
    ("fluconazole", "glipizide"): "Fluconazole may increase hypoglycemic effect.",
    ("rifampin", "doxycycline"): "Rifampin reduces doxycycline effectiveness.",
    ("clozapine", "valproic acid"): "Increased risk of CNS depression.",
    ("omeprazole", "iron"): "Reduced iron absorption due to higher gastric pH.",
    ("atorvastatin", "clarithromycin"): "Increased risk of statin toxicity.",
    ("sotalol", "fluoroquinolones"): "Increased risk of QT prolongation.",
    ("sodium valproate", "lamotrigine"): "Increased risk of rash and toxicity.",
    ("gabapentin", "morphine"): "Morphine may increase gabapentin levels.",
    ("methotrexate", "proton pump inhibitors"): "Increased methotrexate toxicity.",
    ("trazodone", "linezolid"): "Increased risk of serotonin syndrome.",
    ("warfarin", "cranberry juice"): "May increase INR and bleeding risk.",
    ("spironolactone", "NSAIDs"): "Increased risk of kidney impairment.",
    ("quinine", "digoxin"): "Increased risk of digoxin toxicity.",
    ("tacrolimus", "fluconazole"): "Fluconazole may increase tacrolimus levels.",
    ("loperamide", "erythromycin"): "May increase risk of cardiac side effects.",
    ("phenobarbital", "oral contraceptives"): "Phenobarbital reduces contraceptive effectiveness.",
    ("sertraline", "MAOIs"): "Risk of fatal serotonin syndrome. Contraindicated.",
    ("acetazolamide", "salicylates"): "Increased risk of salicylate toxicity.",
    ("sildenafil", "erythromycin"): "Erythromycin increases sildenafil levels."
}

print("💊 Drug-Drug Interaction Checker 💊\n")

a = set()
for b in pairs:
    a.update(b)

while True:

    drug1 = input("Enter first drug name: ").lower().strip()
    if drug1 == "stop":
        print("Thank You!")
        break
    if drug1 not in a:
        print(f"\n❌ '{drug1.title()}' is not included among the 100 commonly \n known drugs that show drug-drug interactions.\n")
        continue
    print(f"\nDrug 1: {drug1.title()}\n")

    drug2 = input("Enter second drug name: ").lower().strip()
    if drug2 not in a:
        print(f"\n❌ '{drug2.title()}' is not included among the 100 commonly\n known drugs that show drug-drug interactions.\n")
        continue
    print(f"\nDrug 2: {drug2.title()}\n")


    x = (drug1, drug2)
    y = (drug2, drug1)

    if x in pairs:
        print(f"\n 🔍 {drug1.title()} x {drug2.title()} = ✅ Interaction: {pairs[x]}\n")
    elif y in pairs:
        print(f"\n 🔍 {drug1.title()} x {drug2.title()} = ✅ Interaction: {pairs[y]}\n")
    else:
        print(f"\n 🔍 {drug1.title()} x {drug2.title()} = ℹ️ No known interaction found.\n")
