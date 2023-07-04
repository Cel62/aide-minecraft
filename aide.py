mod_id = "skyfaction"

def register_simple_item(unlocalized_name):
    if isinstance(unlocalized_name, str):
        return "public static final Item " + unlocalized_name.upper() + ' = registerItem("' + unlocalized_name.lower() + '", new Item(new FabricItemSettings()));'
    return "unlocalized_name n'est pas une chaîne de caractères."

def register_simple_block(name_block):
    if isinstance(name_block, str):
        return "public static final Block " + name_block.upper() + ' = registerBlock("' + name_block.lower() + '", new Block(FabricBlockSettings.create()));'
    return "name_block n'est pas une chaîne de caractères."

# Convertisseur 1.8 vers 1.20
def convertissement_model_item():
    remplacer_chaine('builtin', 'minecraft:item')
    remplacer_chaine('items', 'item')
    supprimer_bloc_texte('"display"', "}")

# ---------------------------------------------------------------------------------------------------------------------------------- #

def remplacer_chaine(ancienne_chaine, nouvelle_chaine, dossier = './import'):
    from os import listdir
    from os.path import isfile, join
    
    # Parcours de tous les fichiers dans le dossier spécifié
    for nom_fichier in listdir(dossier):
        chemin_fichier = join(dossier, nom_fichier)
        
        # Vérification si le chemin correspond à un fichier
        if isfile(chemin_fichier):
            # Lecture du contenu du fichier
            with open(chemin_fichier, 'r', encoding="utf-8") as f:
                contenu = f.read()
            
            # Remplacement de la chaîne de caractères
            contenu_modifie = contenu.replace(ancienne_chaine, nouvelle_chaine)
            
            # Écriture du contenu modifié dans le fichier
            with open(chemin_fichier, 'w', encoding="utf-8") as f:
                f.write(contenu_modifie)

def supprimer_bloc_texte(debut_bloc, fin_bloc, dossier = './import'):
    from os import listdir
    from os.path import isfile, join
    
    for nom_fichier in listdir(dossier):
        chemin_fichier = join(dossier, nom_fichier)
        
        if isfile(chemin_fichier):
            with open(chemin_fichier, 'r', encoding="utf-8") as f:
                lignes = f.readlines()
            
            # Recherche des indices de début et de fin du bloc
            index_debut = 0
            index_fin = 0
            for i, ligne in enumerate(lignes):
                if debut_bloc in ligne:
                    index_debut = i
                if fin_bloc in ligne:
                    index_fin = i
            
            # Suppression du bloc de texte
            if index_debut != None and index_fin != None:
                del lignes[index_debut : index_fin + 1]
                
                with open(chemin_fichier, 'w', encoding="utf-8") as f:
                    f.writelines(lignes)
                    # ❗attention ça peut peut-être faire de la merde avec certains fichiers, à voir
                    if fin_bloc == "}":
                        f.writelines(["}"])
                        remplacer_chaine('},', '}')

def supprimer_ligne_texte(debut_ligne, fin_ligne, dossier = './import'):
    from os import listdir
    from os.path import isfile, join
    
    # Parcours de tous les fichiers dans le dossier spécifié
    for nom_fichier in listdir(dossier):
        chemin_fichier = join(dossier, nom_fichier)
        
        # Vérification si le chemin correspond à un fichier
        if isfile(chemin_fichier):
            # Lecture du contenu du fichier
            with open(chemin_fichier, 'r', encoding="utf-8") as f:
                lignes = f.readlines()
            
            # Suppression du bloc de texte
            if debut_ligne <= len(lignes) and fin_ligne <= len(lignes):
                del lignes[debut_ligne - 1 : fin_ligne]
                
                fin_ligne = len(lignes)
                
                # Écriture du contenu modifié dans le fichier
                with open(chemin_fichier, 'w', encoding="utf-8") as f:
                    f.writelines(lignes)

# 1.8 :  item.nitrite_ingot.name       =  Nitrite Ingot -> conversion
#1.20 : "item.skyfaction.nitrite_ingot": "Nitrite Ingot",
def traduction(category, unlocalized_name, translated_name, withComma = False):
    if isinstance(category, str) or isinstance(unlocalized_name, str) or isinstance(translated_name, str) or isinstance(withComma, bool):
        result = "La traduction est : "
        match category:
            case "item":
                result += '"item.' + mod_id + "." + unlocalized_name + '": "' + translated_name + '"'
            case "block":
                result += '"block.' + mod_id + "." + unlocalized_name + '": "' + translated_name + '"'
            case "itemGroup":
                result += '"itemGroup.' + unlocalized_name + '": "' + translated_name + '"'
            case _:
                return "Cette catégorie n'existe pas !"
        if withComma:
            result += ","
        return result + " "
            
    return "category, unlocalized_name ou translated_name n'est pas une chaîne de caractères ou withComma n'est pas un booléen"