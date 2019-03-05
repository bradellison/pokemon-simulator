from pokemonBaseStats import *
from pokemonTypes import *
from pokemonExpGroups import *
from pokemonEvolution import *
from pokemonLevelUpMoves import *
from pokemonYields import *
from pokemonCatchRates import *
from pokemonPossibleMovesByLevel import *

pokemonStatStageToMult = {-6:0.25,-5:0.28,-4:0.33,-3:0.40,-2:0.50,-1:0.66,0:1,1:1.5,2:2,3:2.5,4:3,5:3.5,6:4}
pokemonCritStageToMult = {0:1,1:4,2:12,3:24}

statDict = {0:'HP',1:'attack',2:'defence',3:'special attack',4:'special defence',5:'speed',6:'accuracy',7:'evasiveness',8:'critical hit ratio'}

effectivenessScale = {0:' and it didn\'t have any effect!',0.25:' and it was not very effective!',0.5:' and it was not very effective!',1:'!',2:' and it was super-effective!',4:' and it was super-effective!'}

nonVolatileStatusNumberToType = {0:'Nothing',1:'Burned',2:'Paralyzed',3:'Sleep',4:'Frozen',5:'Poisoned',6:'Toxic',7:'Tri Attack'}
volatileStatusNumberToType = {0:'Nothing',1:'Confused'}

#pokemonCatchRate = {'Bulbasaur':45,'Ivysaur':45,'Venusaur':45,'Charmander':45,'Charmeleon':45,'Charizard':45,'Squirtle':45,'Wartortle':45,'Blastoise':45}
#pokemonStats = {'Bulbasaur':bulbasaurBaseStats,'Ivysaur':ivysaurBaseStats,'Venusaur':venusaurBaseStats,'Charmander':charmanderBaseStats,'Charmeleon':charmeleonBaseStats,'Charizard':charizardBaseStats,'Squirtle':squirtleBaseStats,'Wartortle':wartortleBaseStats,'Blastoise':blastoiseBaseStats}
#pokemonTypes = {'Bulbasaur':bulbasaurType,'Ivysaur':ivysaurType,'Venusaur':venusaurType,'Charmander':charmanderType,'Charmeleon':charmeleonType,'Charizard':charizardType,'Squirtle':squirtleType,'Wartortle':wartortleType,'Blastoise':blastoiseType}
#pokemonExpGroup = {'Bulbasaur':bulbasaurExpGroup,'Ivysaur':ivysaurExpGroup,'Venusaur':venusaurExpGroup,'Charmander':charmanderExpGroup,'Charmeleon':charmeleonExpGroup,'Charizard':charizardExpGroup,'Squirtle':squirtleExpGroup,'Wartortle':wartortleExpGroup,'Blastoise':blastoiseExpGroup}
#pokemonLevelUpMoves = {'Bulbasaur':bulbasaurLevelUpMoves,'Ivysaur':ivysaurLevelUpMoves,'Venusaur':venusaurLevelUpMoves,'Charmander':charmanderLevelUpMoves,'Charmeleon':charmeleonLevelUpMoves,'Charizard':charizardLevelUpMoves,'Squirtle':squirtleLevelUpMoves,'Wartortle':wartortleLevelUpMoves,'Blastoise':blastoiseLevelUpMoves}
#pokemonEvolutionDetails = {'Bulbasaur':bulbasaurEvolution,'Ivysaur':ivysaurEvolution,'Venusaur':venusaurEvolution,'Charmander':charmanderEvolution,'Charmeleon':charmeleonEvolution,'Charizard':charizardEvolution,'Squirtle':squirtleEvolution,'Wartortle':wartortleEvolution,'Blastoise':blastoiseEvolution}
#pokemonYields = {'Bulbasaur':bulbasaurYields,'Ivysaur':ivysaurYields,'Venusaur':venusaurYields,'Charmander':charmanderYields,'Charmeleon':charmeleonYields,'Charizard':charizardYields,'Squirtle':squirtleYields,'Wartortle':wartortleYields,'Blastoise':blastoiseYields}

<<<<<<< HEAD
allPokemonList = ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','NidoranF','Nidorina','Nidoqueen','NidoranM','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch\'d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew']
=======
>>>>>>> 102fce82972e14ec021687b6eeec1ed3b0bc48f0

pokemonExpGroup = {'Bulbasaur':bulbasaurExpGroup,'Ivysaur':ivysaurExpGroup,'Venusaur':venusaurExpGroup,'Charmander':charmanderExpGroup,'Charmeleon':charmeleonExpGroup,'Charizard':charizardExpGroup,'Squirtle':squirtleExpGroup,'Wartortle':wartortleExpGroup,'Blastoise':blastoiseExpGroup,'Caterpie':caterpieExpGroup,'Metapod':metapodExpGroup,'Butterfree':butterfreeExpGroup,'Weedle':weedleExpGroup,'Kakuna':kakunaExpGroup,'Beedrill':beedrillExpGroup,'Pidgey':pidgeyExpGroup,'Pidgeotto':pidgeottoExpGroup,'Pidgeot':pidgeotExpGroup,'Rattata':rattataExpGroup,'Raticate':raticateExpGroup,'Spearow':spearowExpGroup,'Fearow':fearowExpGroup,'Ekans':ekansExpGroup,'Arbok':arbokExpGroup,'Pikachu':pikachuExpGroup,'Raichu':raichuExpGroup,'Sandshrew':sandshrewExpGroup,'Sandslash':sandslashExpGroup,'NidoranF':nidoranFExpGroup,'Nidorina':nidorinaExpGroup,'Nidoqueen':nidoqueenExpGroup,'NidoranM':nidoranMExpGroup,'Nidorino':nidorinoExpGroup,'Nidoking':nidokingExpGroup,'Clefairy':clefairyExpGroup,'Clefable':clefableExpGroup,'Vulpix':vulpixExpGroup,'Ninetales':ninetalesExpGroup,'Jigglypuff':jigglypuffExpGroup,'Wigglytuff':wigglytuffExpGroup,'Zubat':zubatExpGroup,'Golbat':golbatExpGroup,'Oddish':oddishExpGroup,'Gloom':gloomExpGroup,'Vileplume':vileplumeExpGroup,'Paras':parasExpGroup,'Parasect':parasectExpGroup,'Venonat':venonatExpGroup,'Venomoth':venomothExpGroup,'Diglett':diglettExpGroup,'Dugtrio':dugtrioExpGroup,'Meowth':meowthExpGroup,'Persian':persianExpGroup,'Psyduck':psyduckExpGroup,'Golduck':golduckExpGroup,'Mankey':mankeyExpGroup,'Primeape':primeapeExpGroup,'Growlithe':growlitheExpGroup,'Arcanine':arcanineExpGroup,'Poliwag':poliwagExpGroup,'Poliwhirl':poliwhirlExpGroup,'Poliwrath':poliwrathExpGroup,'Abra':abraExpGroup,'Kadabra':kadabraExpGroup,'Alakazam':alakazamExpGroup,'Machop':machopExpGroup,'Machoke':machokeExpGroup,'Machamp':machampExpGroup,'Bellsprout':bellsproutExpGroup,'Weepinbell':weepinbellExpGroup,'Victreebel':victreebelExpGroup,'Tentacool':tentacoolExpGroup,'Tentacruel':tentacruelExpGroup,'Geodude':geodudeExpGroup,'Graveler':gravelerExpGroup,'Golem':golemExpGroup,'Ponyta':ponytaExpGroup,'Rapidash':rapidashExpGroup,'Slowpoke':slowpokeExpGroup,'Slowbro':slowbroExpGroup,'Magnemite':magnemiteExpGroup,'Magneton':magnetonExpGroup,'Farfetch\'d':farfetchdExpGroup,'Doduo':doduoExpGroup,'Dodrio':dodrioExpGroup,'Seel':seelExpGroup,'Dewgong':dewgongExpGroup,'Grimer':grimerExpGroup,'Muk':mukExpGroup,'Shellder':shellderExpGroup,'Cloyster':cloysterExpGroup,'Gastly':gastlyExpGroup,'Haunter':haunterExpGroup,'Gengar':gengarExpGroup,'Onix':onixExpGroup,'Drowzee':drowzeeExpGroup,'Hypno':hypnoExpGroup,'Krabby':krabbyExpGroup,'Kingler':kinglerExpGroup,'Voltorb':voltorbExpGroup,'Electrode':electrodeExpGroup,'Exeggcute':exeggcuteExpGroup,'Exeggutor':exeggutorExpGroup,'Cubone':cuboneExpGroup,'Marowak':marowakExpGroup,'Hitmonlee':hitmonleeExpGroup,'Hitmonchan':hitmonchanExpGroup,'Lickitung':lickitungExpGroup,'Koffing':koffingExpGroup,'Weezing':weezingExpGroup,'Rhyhorn':rhyhornExpGroup,'Rhydon':rhydonExpGroup,'Chansey':chanseyExpGroup,'Tangela':tangelaExpGroup,'Kangaskhan':kangaskhanExpGroup,'Horsea':horseaExpGroup,'Seadra':seadraExpGroup,'Goldeen':goldeenExpGroup,'Seaking':seakingExpGroup,'Staryu':staryuExpGroup,'Starmie':starmieExpGroup,'Mr Mime':mrMimeExpGroup,'Scyther':scytherExpGroup,'Jynx':jynxExpGroup,'Electabuzz':electabuzzExpGroup,'Magmar':magmarExpGroup,'Pinsir':pinsirExpGroup,'Tauros':taurosExpGroup,'Magikarp':magikarpExpGroup,'Gyarados':gyaradosExpGroup,'Lapras':laprasExpGroup,'Ditto':dittoExpGroup,'Eevee':eeveeExpGroup,'Vaporeon':vaporeonExpGroup,'Jolteon':jolteonExpGroup,'Flareon':flareonExpGroup,'Porygon':porygonExpGroup,'Omanyte':omanyteExpGroup,'Omastar':omastarExpGroup,'Kabuto':kabutoExpGroup,'Kabutops':kabutopsExpGroup,'Aerodactyl':aerodactylExpGroup,'Snorlax':snorlaxExpGroup,'Articuno':articunoExpGroup,'Zapdos':zapdosExpGroup,'Moltres':moltresExpGroup,'Dratini':dratiniExpGroup,'Dragonair':dragonairExpGroup,'Dragonite':dragoniteExpGroup,'Mewtwo':mewtwoExpGroup,'Mew':mewExpGroup}
pokemonStats = {'Bulbasaur':bulbasaurBaseStats,'Ivysaur':ivysaurBaseStats,'Venusaur':venusaurBaseStats,'Charmander':charmanderBaseStats,'Charmeleon':charmeleonBaseStats,'Charizard':charizardBaseStats,'Squirtle':squirtleBaseStats,'Wartortle':wartortleBaseStats,'Blastoise':blastoiseBaseStats,'Caterpie':caterpieBaseStats,'Metapod':metapodBaseStats,'Butterfree':butterfreeBaseStats,'Weedle':weedleBaseStats,'Kakuna':kakunaBaseStats,'Beedrill':beedrillBaseStats,'Pidgey':pidgeyBaseStats,'Pidgeotto':pidgeottoBaseStats,'Pidgeot':pidgeotBaseStats,'Rattata':rattataBaseStats,'Raticate':raticateBaseStats,'Spearow':spearowBaseStats,'Fearow':fearowBaseStats,'Ekans':ekansBaseStats,'Arbok':arbokBaseStats,'Pikachu':pikachuBaseStats,'Raichu':raichuBaseStats,'Sandshrew':sandshrewBaseStats,'Sandslash':sandslashBaseStats,'NidoranF':nidoranFBaseStats,'Nidorina':nidorinaBaseStats,'Nidoqueen':nidoqueenBaseStats,'NidoranM':nidoranMBaseStats,'Nidorino':nidorinoBaseStats,'Nidoking':nidokingBaseStats,'Clefairy':clefairyBaseStats,'Clefable':clefableBaseStats,'Vulpix':vulpixBaseStats,'Ninetales':ninetalesBaseStats,'Jigglypuff':jigglypuffBaseStats,'Wigglytuff':wigglytuffBaseStats,'Zubat':zubatBaseStats,'Golbat':golbatBaseStats,'Oddish':oddishBaseStats,'Gloom':gloomBaseStats,'Vileplume':vileplumeBaseStats,'Paras':parasBaseStats,'Parasect':parasectBaseStats,'Venonat':venonatBaseStats,'Venomoth':venomothBaseStats,'Diglett':diglettBaseStats,'Dugtrio':dugtrioBaseStats,'Meowth':meowthBaseStats,'Persian':persianBaseStats,'Psyduck':psyduckBaseStats,'Golduck':golduckBaseStats,'Mankey':mankeyBaseStats,'Primeape':primeapeBaseStats,'Growlithe':growlitheBaseStats,'Arcanine':arcanineBaseStats,'Poliwag':poliwagBaseStats,'Poliwhirl':poliwhirlBaseStats,'Poliwrath':poliwrathBaseStats,'Abra':abraBaseStats,'Kadabra':kadabraBaseStats,'Alakazam':alakazamBaseStats,'Machop':machopBaseStats,'Machoke':machokeBaseStats,'Machamp':machampBaseStats,'Bellsprout':bellsproutBaseStats,'Weepinbell':weepinbellBaseStats,'Victreebel':victreebelBaseStats,'Tentacool':tentacoolBaseStats,'Tentacruel':tentacruelBaseStats,'Geodude':geodudeBaseStats,'Graveler':gravelerBaseStats,'Golem':golemBaseStats,'Ponyta':ponytaBaseStats,'Rapidash':rapidashBaseStats,'Slowpoke':slowpokeBaseStats,'Slowbro':slowbroBaseStats,'Magnemite':magnemiteBaseStats,'Magneton':magnetonBaseStats,'Farfetch\'d':farfetchdBaseStats,'Doduo':doduoBaseStats,'Dodrio':dodrioBaseStats,'Seel':seelBaseStats,'Dewgong':dewgongBaseStats,'Grimer':grimerBaseStats,'Muk':mukBaseStats,'Shellder':shellderBaseStats,'Cloyster':cloysterBaseStats,'Gastly':gastlyBaseStats,'Haunter':haunterBaseStats,'Gengar':gengarBaseStats,'Onix':onixBaseStats,'Drowzee':drowzeeBaseStats,'Hypno':hypnoBaseStats,'Krabby':krabbyBaseStats,'Kingler':kinglerBaseStats,'Voltorb':voltorbBaseStats,'Electrode':electrodeBaseStats,'Exeggcute':exeggcuteBaseStats,'Exeggutor':exeggutorBaseStats,'Cubone':cuboneBaseStats,'Marowak':marowakBaseStats,'Hitmonlee':hitmonleeBaseStats,'Hitmonchan':hitmonchanBaseStats,'Lickitung':lickitungBaseStats,'Koffing':koffingBaseStats,'Weezing':weezingBaseStats,'Rhyhorn':rhyhornBaseStats,'Rhydon':rhydonBaseStats,'Chansey':chanseyBaseStats,'Tangela':tangelaBaseStats,'Kangaskhan':kangaskhanBaseStats,'Horsea':horseaBaseStats,'Seadra':seadraBaseStats,'Goldeen':goldeenBaseStats,'Seaking':seakingBaseStats,'Staryu':staryuBaseStats,'Starmie':starmieBaseStats,'Mr Mime':mrMimeBaseStats,'Scyther':scytherBaseStats,'Jynx':jynxBaseStats,'Electabuzz':electabuzzBaseStats,'Magmar':magmarBaseStats,'Pinsir':pinsirBaseStats,'Tauros':taurosBaseStats,'Magikarp':magikarpBaseStats,'Gyarados':gyaradosBaseStats,'Lapras':laprasBaseStats,'Ditto':dittoBaseStats,'Eevee':eeveeBaseStats,'Vaporeon':vaporeonBaseStats,'Jolteon':jolteonBaseStats,'Flareon':flareonBaseStats,'Porygon':porygonBaseStats,'Omanyte':omanyteBaseStats,'Omastar':omastarBaseStats,'Kabuto':kabutoBaseStats,'Kabutops':kabutopsBaseStats,'Aerodactyl':aerodactylBaseStats,'Snorlax':snorlaxBaseStats,'Articuno':articunoBaseStats,'Zapdos':zapdosBaseStats,'Moltres':moltresBaseStats,'Dratini':dratiniBaseStats,'Dragonair':dragonairBaseStats,'Dragonite':dragoniteBaseStats,'Mewtwo':mewtwoBaseStats,'Mew':mewBaseStats}
pokemonLevelUpMoves = {'Bulbasaur':bulbasaurLevelUpMoves,'Ivysaur':ivysaurLevelUpMoves,'Venusaur':venusaurLevelUpMoves,'Charmander':charmanderLevelUpMoves,'Charmeleon':charmeleonLevelUpMoves,'Charizard':charizardLevelUpMoves,'Squirtle':squirtleLevelUpMoves,'Wartortle':wartortleLevelUpMoves,'Blastoise':blastoiseLevelUpMoves,'Caterpie':caterpieLevelUpMoves,'Metapod':metapodLevelUpMoves,'Butterfree':butterfreeLevelUpMoves,'Weedle':weedleLevelUpMoves,'Kakuna':kakunaLevelUpMoves,'Beedrill':beedrillLevelUpMoves,'Pidgey':pidgeyLevelUpMoves,'Pidgeotto':pidgeottoLevelUpMoves,'Pidgeot':pidgeotLevelUpMoves,'Rattata':rattataLevelUpMoves,'Raticate':raticateLevelUpMoves,'Spearow':spearowLevelUpMoves,'Fearow':fearowLevelUpMoves,'Ekans':ekansLevelUpMoves,'Arbok':arbokLevelUpMoves,'Pikachu':pikachuLevelUpMoves,'Raichu':raichuLevelUpMoves,'Sandshrew':sandshrewLevelUpMoves,'Sandslash':sandslashLevelUpMoves,'NidoranF':nidoranFLevelUpMoves,'Nidorina':nidorinaLevelUpMoves,'Nidoqueen':nidoqueenLevelUpMoves,'NidoranM':nidoranMLevelUpMoves,'Nidorino':nidorinoLevelUpMoves,'Nidoking':nidokingLevelUpMoves,'Clefairy':clefairyLevelUpMoves,'Clefable':clefableLevelUpMoves,'Vulpix':vulpixLevelUpMoves,'Ninetales':ninetalesLevelUpMoves,'Jigglypuff':jigglypuffLevelUpMoves,'Wigglytuff':wigglytuffLevelUpMoves,'Zubat':zubatLevelUpMoves,'Golbat':golbatLevelUpMoves,'Oddish':oddishLevelUpMoves,'Gloom':gloomLevelUpMoves,'Vileplume':vileplumeLevelUpMoves,'Paras':parasLevelUpMoves,'Parasect':parasectLevelUpMoves,'Venonat':venonatLevelUpMoves,'Venomoth':venomothLevelUpMoves,'Diglett':diglettLevelUpMoves,'Dugtrio':dugtrioLevelUpMoves,'Meowth':meowthLevelUpMoves,'Persian':persianLevelUpMoves,'Psyduck':psyduckLevelUpMoves,'Golduck':golduckLevelUpMoves,'Mankey':mankeyLevelUpMoves,'Primeape':primeapeLevelUpMoves,'Growlithe':growlitheLevelUpMoves,'Arcanine':arcanineLevelUpMoves,'Poliwag':poliwagLevelUpMoves,'Poliwhirl':poliwhirlLevelUpMoves,'Poliwrath':poliwrathLevelUpMoves,'Abra':abraLevelUpMoves,'Kadabra':kadabraLevelUpMoves,'Alakazam':alakazamLevelUpMoves,'Machop':machopLevelUpMoves,'Machoke':machokeLevelUpMoves,'Machamp':machampLevelUpMoves,'Bellsprout':bellsproutLevelUpMoves,'Weepinbell':weepinbellLevelUpMoves,'Victreebel':victreebelLevelUpMoves,'Tentacool':tentacoolLevelUpMoves,'Tentacruel':tentacruelLevelUpMoves,'Geodude':geodudeLevelUpMoves,'Graveler':gravelerLevelUpMoves,'Golem':golemLevelUpMoves,'Ponyta':ponytaLevelUpMoves,'Rapidash':rapidashLevelUpMoves,'Slowpoke':slowpokeLevelUpMoves,'Slowbro':slowbroLevelUpMoves,'Magnemite':magnemiteLevelUpMoves,'Magneton':magnetonLevelUpMoves,'Farfetch\'d':farfetchdLevelUpMoves,'Doduo':doduoLevelUpMoves,'Dodrio':dodrioLevelUpMoves,'Seel':seelLevelUpMoves,'Dewgong':dewgongLevelUpMoves,'Grimer':grimerLevelUpMoves,'Muk':mukLevelUpMoves,'Shellder':shellderLevelUpMoves,'Cloyster':cloysterLevelUpMoves,'Gastly':gastlyLevelUpMoves,'Haunter':haunterLevelUpMoves,'Gengar':gengarLevelUpMoves,'Onix':onixLevelUpMoves,'Drowzee':drowzeeLevelUpMoves,'Hypno':hypnoLevelUpMoves,'Krabby':krabbyLevelUpMoves,'Kingler':kinglerLevelUpMoves,'Voltorb':voltorbLevelUpMoves,'Electrode':electrodeLevelUpMoves,'Exeggcute':exeggcuteLevelUpMoves,'Exeggutor':exeggutorLevelUpMoves,'Cubone':cuboneLevelUpMoves,'Marowak':marowakLevelUpMoves,'Hitmonlee':hitmonleeLevelUpMoves,'Hitmonchan':hitmonchanLevelUpMoves,'Lickitung':lickitungLevelUpMoves,'Koffing':koffingLevelUpMoves,'Weezing':weezingLevelUpMoves,'Rhyhorn':rhyhornLevelUpMoves,'Rhydon':rhydonLevelUpMoves,'Chansey':chanseyLevelUpMoves,'Tangela':tangelaLevelUpMoves,'Kangaskhan':kangaskhanLevelUpMoves,'Horsea':horseaLevelUpMoves,'Seadra':seadraLevelUpMoves,'Goldeen':goldeenLevelUpMoves,'Seaking':seakingLevelUpMoves,'Staryu':staryuLevelUpMoves,'Starmie':starmieLevelUpMoves,'Mr Mime':mrMimeLevelUpMoves,'Scyther':scytherLevelUpMoves,'Jynx':jynxLevelUpMoves,'Electabuzz':electabuzzLevelUpMoves,'Magmar':magmarLevelUpMoves,'Pinsir':pinsirLevelUpMoves,'Tauros':taurosLevelUpMoves,'Magikarp':magikarpLevelUpMoves,'Gyarados':gyaradosLevelUpMoves,'Lapras':laprasLevelUpMoves,'Ditto':dittoLevelUpMoves,'Eevee':eeveeLevelUpMoves,'Vaporeon':vaporeonLevelUpMoves,'Jolteon':jolteonLevelUpMoves,'Flareon':flareonLevelUpMoves,'Porygon':porygonLevelUpMoves,'Omanyte':omanyteLevelUpMoves,'Omastar':omastarLevelUpMoves,'Kabuto':kabutoLevelUpMoves,'Kabutops':kabutopsLevelUpMoves,'Aerodactyl':aerodactylLevelUpMoves,'Snorlax':snorlaxLevelUpMoves,'Articuno':articunoLevelUpMoves,'Zapdos':zapdosLevelUpMoves,'Moltres':moltresLevelUpMoves,'Dratini':dratiniLevelUpMoves,'Dragonair':dragonairLevelUpMoves,'Dragonite':dragoniteLevelUpMoves,'Mewtwo':mewtwoLevelUpMoves,'Mew':mewLevelUpMoves}
pokemonPossibleMovesByLevel = {'Bulbasaur':bulbasaurPossibleMovesByLevel,'Ivysaur':ivysaurPossibleMovesByLevel,'Venusaur':venusaurPossibleMovesByLevel,'Charmander':charmanderPossibleMovesByLevel,'Charmeleon':charmeleonPossibleMovesByLevel,'Charizard':charizardPossibleMovesByLevel,'Squirtle':squirtlePossibleMovesByLevel,'Wartortle':wartortlePossibleMovesByLevel,'Blastoise':blastoisePossibleMovesByLevel,'Caterpie':caterpiePossibleMovesByLevel,'Metapod':metapodPossibleMovesByLevel,'Butterfree':butterfreePossibleMovesByLevel,'Weedle':weedlePossibleMovesByLevel,'Kakuna':kakunaPossibleMovesByLevel,'Beedrill':beedrillPossibleMovesByLevel,'Pidgey':pidgeyPossibleMovesByLevel,'Pidgeotto':pidgeottoPossibleMovesByLevel,'Pidgeot':pidgeotPossibleMovesByLevel,'Rattata':rattataPossibleMovesByLevel,'Raticate':raticatePossibleMovesByLevel,'Spearow':spearowPossibleMovesByLevel,'Fearow':fearowPossibleMovesByLevel,'Ekans':ekansPossibleMovesByLevel,'Arbok':arbokPossibleMovesByLevel,'Pikachu':pikachuPossibleMovesByLevel,'Raichu':raichuPossibleMovesByLevel,'Sandshrew':sandshrewPossibleMovesByLevel,'Sandslash':sandslashPossibleMovesByLevel,'NidoranF':nidoranFPossibleMovesByLevel,'Nidorina':nidorinaPossibleMovesByLevel,'Nidoqueen':nidoqueenPossibleMovesByLevel,'NidoranM':nidoranMPossibleMovesByLevel,'Nidorino':nidorinoPossibleMovesByLevel,'Nidoking':nidokingPossibleMovesByLevel,'Clefairy':clefairyPossibleMovesByLevel,'Clefable':clefablePossibleMovesByLevel,'Vulpix':vulpixPossibleMovesByLevel,'Ninetales':ninetalesPossibleMovesByLevel,'Jigglypuff':jigglypuffPossibleMovesByLevel,'Wigglytuff':wigglytuffPossibleMovesByLevel,'Zubat':zubatPossibleMovesByLevel,'Golbat':golbatPossibleMovesByLevel,'Oddish':oddishPossibleMovesByLevel,'Gloom':gloomPossibleMovesByLevel,'Vileplume':vileplumePossibleMovesByLevel,'Paras':parasPossibleMovesByLevel,'Parasect':parasectPossibleMovesByLevel,'Venonat':venonatPossibleMovesByLevel,'Venomoth':venomothPossibleMovesByLevel,'Diglett':diglettPossibleMovesByLevel,'Dugtrio':dugtrioPossibleMovesByLevel,'Meowth':meowthPossibleMovesByLevel,'Persian':persianPossibleMovesByLevel,'Psyduck':psyduckPossibleMovesByLevel,'Golduck':golduckPossibleMovesByLevel,'Mankey':mankeyPossibleMovesByLevel,'Primeape':primeapePossibleMovesByLevel,'Growlithe':growlithePossibleMovesByLevel,'Arcanine':arcaninePossibleMovesByLevel,'Poliwag':poliwagPossibleMovesByLevel,'Poliwhirl':poliwhirlPossibleMovesByLevel,'Poliwrath':poliwrathPossibleMovesByLevel,'Abra':abraPossibleMovesByLevel,'Kadabra':kadabraPossibleMovesByLevel,'Alakazam':alakazamPossibleMovesByLevel,'Machop':machopPossibleMovesByLevel,'Machoke':machokePossibleMovesByLevel,'Machamp':machampPossibleMovesByLevel,'Bellsprout':bellsproutPossibleMovesByLevel,'Weepinbell':weepinbellPossibleMovesByLevel,'Victreebel':victreebelPossibleMovesByLevel,'Tentacool':tentacoolPossibleMovesByLevel,'Tentacruel':tentacruelPossibleMovesByLevel,'Geodude':geodudePossibleMovesByLevel,'Graveler':gravelerPossibleMovesByLevel,'Golem':golemPossibleMovesByLevel,'Ponyta':ponytaPossibleMovesByLevel,'Rapidash':rapidashPossibleMovesByLevel,'Slowpoke':slowpokePossibleMovesByLevel,'Slowbro':slowbroPossibleMovesByLevel,'Magnemite':magnemitePossibleMovesByLevel,'Magneton':magnetonPossibleMovesByLevel,'Farfetch\'d':farfetchdPossibleMovesByLevel,'Doduo':doduoPossibleMovesByLevel,'Dodrio':dodrioPossibleMovesByLevel,'Seel':seelPossibleMovesByLevel,'Dewgong':dewgongPossibleMovesByLevel,'Grimer':grimerPossibleMovesByLevel,'Muk':mukPossibleMovesByLevel,'Shellder':shellderPossibleMovesByLevel,'Cloyster':cloysterPossibleMovesByLevel,'Gastly':gastlyPossibleMovesByLevel,'Haunter':haunterPossibleMovesByLevel,'Gengar':gengarPossibleMovesByLevel,'Onix':onixPossibleMovesByLevel,'Drowzee':drowzeePossibleMovesByLevel,'Hypno':hypnoPossibleMovesByLevel,'Krabby':krabbyPossibleMovesByLevel,'Kingler':kinglerPossibleMovesByLevel,'Voltorb':voltorbPossibleMovesByLevel,'Electrode':electrodePossibleMovesByLevel,'Exeggcute':exeggcutePossibleMovesByLevel,'Exeggutor':exeggutorPossibleMovesByLevel,'Cubone':cubonePossibleMovesByLevel,'Marowak':marowakPossibleMovesByLevel,'Hitmonlee':hitmonleePossibleMovesByLevel,'Hitmonchan':hitmonchanPossibleMovesByLevel,'Lickitung':lickitungPossibleMovesByLevel,'Koffing':koffingPossibleMovesByLevel,'Weezing':weezingPossibleMovesByLevel,'Rhyhorn':rhyhornPossibleMovesByLevel,'Rhydon':rhydonPossibleMovesByLevel,'Chansey':chanseyPossibleMovesByLevel,'Tangela':tangelaPossibleMovesByLevel,'Kangaskhan':kangaskhanPossibleMovesByLevel,'Horsea':horseaPossibleMovesByLevel,'Seadra':seadraPossibleMovesByLevel,'Goldeen':goldeenPossibleMovesByLevel,'Seaking':seakingPossibleMovesByLevel,'Staryu':staryuPossibleMovesByLevel,'Starmie':starmiePossibleMovesByLevel,'Mr Mime':mrMimePossibleMovesByLevel,'Scyther':scytherPossibleMovesByLevel,'Jynx':jynxPossibleMovesByLevel,'Electabuzz':electabuzzPossibleMovesByLevel,'Magmar':magmarPossibleMovesByLevel,'Pinsir':pinsirPossibleMovesByLevel,'Tauros':taurosPossibleMovesByLevel,'Magikarp':magikarpPossibleMovesByLevel,'Gyarados':gyaradosPossibleMovesByLevel,'Lapras':laprasPossibleMovesByLevel,'Ditto':dittoPossibleMovesByLevel,'Eevee':eeveePossibleMovesByLevel,'Vaporeon':vaporeonPossibleMovesByLevel,'Jolteon':jolteonPossibleMovesByLevel,'Flareon':flareonPossibleMovesByLevel,'Porygon':porygonPossibleMovesByLevel,'Omanyte':omanytePossibleMovesByLevel,'Omastar':omastarPossibleMovesByLevel,'Kabuto':kabutoPossibleMovesByLevel,'Kabutops':kabutopsPossibleMovesByLevel,'Aerodactyl':aerodactylPossibleMovesByLevel,'Snorlax':snorlaxPossibleMovesByLevel,'Articuno':articunoPossibleMovesByLevel,'Zapdos':zapdosPossibleMovesByLevel,'Moltres':moltresPossibleMovesByLevel,'Dratini':dratiniPossibleMovesByLevel,'Dragonair':dragonairPossibleMovesByLevel,'Dragonite':dragonitePossibleMovesByLevel,'Mewtwo':mewtwoPossibleMovesByLevel,'Mew':mewPossibleMovesByLevel}
pokemonEvolutionDetails = {'Bulbasaur':bulbasaurEvolution,'Ivysaur':ivysaurEvolution,'Venusaur':venusaurEvolution,'Charmander':charmanderEvolution,'Charmeleon':charmeleonEvolution,'Charizard':charizardEvolution,'Squirtle':squirtleEvolution,'Wartortle':wartortleEvolution,'Blastoise':blastoiseEvolution,'Caterpie':caterpieEvolution,'Metapod':metapodEvolution,'Butterfree':butterfreeEvolution,'Weedle':weedleEvolution,'Kakuna':kakunaEvolution,'Beedrill':beedrillEvolution,'Pidgey':pidgeyEvolution,'Pidgeotto':pidgeottoEvolution,'Pidgeot':pidgeotEvolution,'Rattata':rattataEvolution,'Raticate':raticateEvolution,'Spearow':spearowEvolution,'Fearow':fearowEvolution,'Ekans':ekansEvolution,'Arbok':arbokEvolution,'Pikachu':pikachuEvolution,'Raichu':raichuEvolution,'Sandshrew':sandshrewEvolution,'Sandslash':sandslashEvolution,'NidoranF':nidoranFEvolution,'Nidorina':nidorinaEvolution,'Nidoqueen':nidoqueenEvolution,'NidoranM':nidoranMEvolution,'Nidorino':nidorinoEvolution,'Nidoking':nidokingEvolution,'Clefairy':clefairyEvolution,'Clefable':clefableEvolution,'Vulpix':vulpixEvolution,'Ninetales':ninetalesEvolution,'Jigglypuff':jigglypuffEvolution,'Wigglytuff':wigglytuffEvolution,'Zubat':zubatEvolution,'Golbat':golbatEvolution,'Oddish':oddishEvolution,'Gloom':gloomEvolution,'Vileplume':vileplumeEvolution,'Paras':parasEvolution,'Parasect':parasectEvolution,'Venonat':venonatEvolution,'Venomoth':venomothEvolution,'Diglett':diglettEvolution,'Dugtrio':dugtrioEvolution,'Meowth':meowthEvolution,'Persian':persianEvolution,'Psyduck':psyduckEvolution,'Golduck':golduckEvolution,'Mankey':mankeyEvolution,'Primeape':primeapeEvolution,'Growlithe':growlitheEvolution,'Arcanine':arcanineEvolution,'Poliwag':poliwagEvolution,'Poliwhirl':poliwhirlEvolution,'Poliwrath':poliwrathEvolution,'Abra':abraEvolution,'Kadabra':kadabraEvolution,'Alakazam':alakazamEvolution,'Machop':machopEvolution,'Machoke':machokeEvolution,'Machamp':machampEvolution,'Bellsprout':bellsproutEvolution,'Weepinbell':weepinbellEvolution,'Victreebel':victreebelEvolution,'Tentacool':tentacoolEvolution,'Tentacruel':tentacruelEvolution,'Geodude':geodudeEvolution,'Graveler':gravelerEvolution,'Golem':golemEvolution,'Ponyta':ponytaEvolution,'Rapidash':rapidashEvolution,'Slowpoke':slowpokeEvolution,'Slowbro':slowbroEvolution,'Magnemite':magnemiteEvolution,'Magneton':magnetonEvolution,'Farfetch\'d':farfetchdEvolution,'Doduo':doduoEvolution,'Dodrio':dodrioEvolution,'Seel':seelEvolution,'Dewgong':dewgongEvolution,'Grimer':grimerEvolution,'Muk':mukEvolution,'Shellder':shellderEvolution,'Cloyster':cloysterEvolution,'Gastly':gastlyEvolution,'Haunter':haunterEvolution,'Gengar':gengarEvolution,'Onix':onixEvolution,'Drowzee':drowzeeEvolution,'Hypno':hypnoEvolution,'Krabby':krabbyEvolution,'Kingler':kinglerEvolution,'Voltorb':voltorbEvolution,'Electrode':electrodeEvolution,'Exeggcute':exeggcuteEvolution,'Exeggutor':exeggutorEvolution,'Cubone':cuboneEvolution,'Marowak':marowakEvolution,'Hitmonlee':hitmonleeEvolution,'Hitmonchan':hitmonchanEvolution,'Lickitung':lickitungEvolution,'Koffing':koffingEvolution,'Weezing':weezingEvolution,'Rhyhorn':rhyhornEvolution,'Rhydon':rhydonEvolution,'Chansey':chanseyEvolution,'Tangela':tangelaEvolution,'Kangaskhan':kangaskhanEvolution,'Horsea':horseaEvolution,'Seadra':seadraEvolution,'Goldeen':goldeenEvolution,'Seaking':seakingEvolution,'Staryu':staryuEvolution,'Starmie':starmieEvolution,'Mr Mime':mrMimeEvolution,'Scyther':scytherEvolution,'Jynx':jynxEvolution,'Electabuzz':electabuzzEvolution,'Magmar':magmarEvolution,'Pinsir':pinsirEvolution,'Tauros':taurosEvolution,'Magikarp':magikarpEvolution,'Gyarados':gyaradosEvolution,'Lapras':laprasEvolution,'Ditto':dittoEvolution,'Eevee':eeveeEvolution,'Vaporeon':vaporeonEvolution,'Jolteon':jolteonEvolution,'Flareon':flareonEvolution,'Porygon':porygonEvolution,'Omanyte':omanyteEvolution,'Omastar':omastarEvolution,'Kabuto':kabutoEvolution,'Kabutops':kabutopsEvolution,'Aerodactyl':aerodactylEvolution,'Snorlax':snorlaxEvolution,'Articuno':articunoEvolution,'Zapdos':zapdosEvolution,'Moltres':moltresEvolution,'Dratini':dratiniEvolution,'Dragonair':dragonairEvolution,'Dragonite':dragoniteEvolution,'Mewtwo':mewtwoEvolution,'Mew':mewEvolution}
pokemonYields = {'Bulbasaur':bulbasaurYields,'Ivysaur':ivysaurYields,'Venusaur':venusaurYields,'Charmander':charmanderYields,'Charmeleon':charmeleonYields,'Charizard':charizardYields,'Squirtle':squirtleYields,'Wartortle':wartortleYields,'Blastoise':blastoiseYields,'Caterpie':caterpieYields,'Metapod':metapodYields,'Butterfree':butterfreeYields,'Weedle':weedleYields,'Kakuna':kakunaYields,'Beedrill':beedrillYields,'Pidgey':pidgeyYields,'Pidgeotto':pidgeottoYields,'Pidgeot':pidgeotYields,'Rattata':rattataYields,'Raticate':raticateYields,'Spearow':spearowYields,'Fearow':fearowYields,'Ekans':ekansYields,'Arbok':arbokYields,'Pikachu':pikachuYields,'Raichu':raichuYields,'Sandshrew':sandshrewYields,'Sandslash':sandslashYields,'NidoranF':nidoranFYields,'Nidorina':nidorinaYields,'Nidoqueen':nidoqueenYields,'NidoranM':nidoranMYields,'Nidorino':nidorinoYields,'Nidoking':nidokingYields,'Clefairy':clefairyYields,'Clefable':clefableYields,'Vulpix':vulpixYields,'Ninetales':ninetalesYields,'Jigglypuff':jigglypuffYields,'Wigglytuff':wigglytuffYields,'Zubat':zubatYields,'Golbat':golbatYields,'Oddish':oddishYields,'Gloom':gloomYields,'Vileplume':vileplumeYields,'Paras':parasYields,'Parasect':parasectYields,'Venonat':venonatYields,'Venomoth':venomothYields,'Diglett':diglettYields,'Dugtrio':dugtrioYields,'Meowth':meowthYields,'Persian':persianYields,'Psyduck':psyduckYields,'Golduck':golduckYields,'Mankey':mankeyYields,'Primeape':primeapeYields,'Growlithe':growlitheYields,'Arcanine':arcanineYields,'Poliwag':poliwagYields,'Poliwhirl':poliwhirlYields,'Poliwrath':poliwrathYields,'Abra':abraYields,'Kadabra':kadabraYields,'Alakazam':alakazamYields,'Machop':machopYields,'Machoke':machokeYields,'Machamp':machampYields,'Bellsprout':bellsproutYields,'Weepinbell':weepinbellYields,'Victreebel':victreebelYields,'Tentacool':tentacoolYields,'Tentacruel':tentacruelYields,'Geodude':geodudeYields,'Graveler':gravelerYields,'Golem':golemYields,'Ponyta':ponytaYields,'Rapidash':rapidashYields,'Slowpoke':slowpokeYields,'Slowbro':slowbroYields,'Magnemite':magnemiteYields,'Magneton':magnetonYields,'Farfetch\'d':farfetchdYields,'Doduo':doduoYields,'Dodrio':dodrioYields,'Seel':seelYields,'Dewgong':dewgongYields,'Grimer':grimerYields,'Muk':mukYields,'Shellder':shellderYields,'Cloyster':cloysterYields,'Gastly':gastlyYields,'Haunter':haunterYields,'Gengar':gengarYields,'Onix':onixYields,'Drowzee':drowzeeYields,'Hypno':hypnoYields,'Krabby':krabbyYields,'Kingler':kinglerYields,'Voltorb':voltorbYields,'Electrode':electrodeYields,'Exeggcute':exeggcuteYields,'Exeggutor':exeggutorYields,'Cubone':cuboneYields,'Marowak':marowakYields,'Hitmonlee':hitmonleeYields,'Hitmonchan':hitmonchanYields,'Lickitung':lickitungYields,'Koffing':koffingYields,'Weezing':weezingYields,'Rhyhorn':rhyhornYields,'Rhydon':rhydonYields,'Chansey':chanseyYields,'Tangela':tangelaYields,'Kangaskhan':kangaskhanYields,'Horsea':horseaYields,'Seadra':seadraYields,'Goldeen':goldeenYields,'Seaking':seakingYields,'Staryu':staryuYields,'Starmie':starmieYields,'Mr Mime':mrMimeYields,'Scyther':scytherYields,'Jynx':jynxYields,'Electabuzz':electabuzzYields,'Magmar':magmarYields,'Pinsir':pinsirYields,'Tauros':taurosYields,'Magikarp':magikarpYields,'Gyarados':gyaradosYields,'Lapras':laprasYields,'Ditto':dittoYields,'Eevee':eeveeYields,'Vaporeon':vaporeonYields,'Jolteon':jolteonYields,'Flareon':flareonYields,'Porygon':porygonYields,'Omanyte':omanyteYields,'Omastar':omastarYields,'Kabuto':kabutoYields,'Kabutops':kabutopsYields,'Aerodactyl':aerodactylYields,'Snorlax':snorlaxYields,'Articuno':articunoYields,'Zapdos':zapdosYields,'Moltres':moltresYields,'Dratini':dratiniYields,'Dragonair':dragonairYields,'Dragonite':dragoniteYields,'Mewtwo':mewtwoYields,'Mew':mewYields}
pokemonTypes = {'Bulbasaur':bulbasaurType,'Ivysaur':ivysaurType,'Venusaur':venusaurType,'Charmander':charmanderType,'Charmeleon':charmeleonType,'Charizard':charizardType,'Squirtle':squirtleType,'Wartortle':wartortleType,'Blastoise':blastoiseType,'Caterpie':caterpieType,'Metapod':metapodType,'Butterfree':butterfreeType,'Weedle':weedleType,'Kakuna':kakunaType,'Beedrill':beedrillType,'Pidgey':pidgeyType,'Pidgeotto':pidgeottoType,'Pidgeot':pidgeotType,'Rattata':rattataType,'Raticate':raticateType,'Spearow':spearowType,'Fearow':fearowType,'Ekans':ekansType,'Arbok':arbokType,'Pikachu':pikachuType,'Raichu':raichuType,'Sandshrew':sandshrewType,'Sandslash':sandslashType,'NidoranF':nidoranFType,'Nidorina':nidorinaType,'Nidoqueen':nidoqueenType,'NidoranM':nidoranMType,'Nidorino':nidorinoType,'Nidoking':nidokingType,'Clefairy':clefairyType,'Clefable':clefableType,'Vulpix':vulpixType,'Ninetales':ninetalesType,'Jigglypuff':jigglypuffType,'Wigglytuff':wigglytuffType,'Zubat':zubatType,'Golbat':golbatType,'Oddish':oddishType,'Gloom':gloomType,'Vileplume':vileplumeType,'Paras':parasType,'Parasect':parasectType,'Venonat':venonatType,'Venomoth':venomothType,'Diglett':diglettType,'Dugtrio':dugtrioType,'Meowth':meowthType,'Persian':persianType,'Psyduck':psyduckType,'Golduck':golduckType,'Mankey':mankeyType,'Primeape':primeapeType,'Growlithe':growlitheType,'Arcanine':arcanineType,'Poliwag':poliwagType,'Poliwhirl':poliwhirlType,'Poliwrath':poliwrathType,'Abra':abraType,'Kadabra':kadabraType,'Alakazam':alakazamType,'Machop':machopType,'Machoke':machokeType,'Machamp':machampType,'Bellsprout':bellsproutType,'Weepinbell':weepinbellType,'Victreebel':victreebelType,'Tentacool':tentacoolType,'Tentacruel':tentacruelType,'Geodude':geodudeType,'Graveler':gravelerType,'Golem':golemType,'Ponyta':ponytaType,'Rapidash':rapidashType,'Slowpoke':slowpokeType,'Slowbro':slowbroType,'Magnemite':magnemiteType,'Magneton':magnetonType,'Farfetch\'d':farfetchdType,'Doduo':doduoType,'Dodrio':dodrioType,'Seel':seelType,'Dewgong':dewgongType,'Grimer':grimerType,'Muk':mukType,'Shellder':shellderType,'Cloyster':cloysterType,'Gastly':gastlyType,'Haunter':haunterType,'Gengar':gengarType,'Onix':onixType,'Drowzee':drowzeeType,'Hypno':hypnoType,'Krabby':krabbyType,'Kingler':kinglerType,'Voltorb':voltorbType,'Electrode':electrodeType,'Exeggcute':exeggcuteType,'Exeggutor':exeggutorType,'Cubone':cuboneType,'Marowak':marowakType,'Hitmonlee':hitmonleeType,'Hitmonchan':hitmonchanType,'Lickitung':lickitungType,'Koffing':koffingType,'Weezing':weezingType,'Rhyhorn':rhyhornType,'Rhydon':rhydonType,'Chansey':chanseyType,'Tangela':tangelaType,'Kangaskhan':kangaskhanType,'Horsea':horseaType,'Seadra':seadraType,'Goldeen':goldeenType,'Seaking':seakingType,'Staryu':staryuType,'Starmie':starmieType,'Mr Mime':mrMimeType,'Scyther':scytherType,'Jynx':jynxType,'Electabuzz':electabuzzType,'Magmar':magmarType,'Pinsir':pinsirType,'Tauros':taurosType,'Magikarp':magikarpType,'Gyarados':gyaradosType,'Lapras':laprasType,'Ditto':dittoType,'Eevee':eeveeType,'Vaporeon':vaporeonType,'Jolteon':jolteonType,'Flareon':flareonType,'Porygon':porygonType,'Omanyte':omanyteType,'Omastar':omastarType,'Kabuto':kabutoType,'Kabutops':kabutopsType,'Aerodactyl':aerodactylType,'Snorlax':snorlaxType,'Articuno':articunoType,'Zapdos':zapdosType,'Moltres':moltresType,'Dratini':dratiniType,'Dragonair':dragonairType,'Dragonite':dragoniteType,'Mewtwo':mewtwoType,'Mew':mewType}
pokemonCatchRates = {'Bulbasaur':bulbasaurCatchRate,'Ivysaur':ivysaurCatchRate,'Venusaur':venusaurCatchRate,'Charmander':charmanderCatchRate,'Charmeleon':charmeleonCatchRate,'Charizard':charizardCatchRate,'Squirtle':squirtleCatchRate,'Wartortle':wartortleCatchRate,'Blastoise':blastoiseCatchRate,'Caterpie':caterpieCatchRate,'Metapod':metapodCatchRate,'Butterfree':butterfreeCatchRate,'Weedle':weedleCatchRate,'Kakuna':kakunaCatchRate,'Beedrill':beedrillCatchRate,'Pidgey':pidgeyCatchRate,'Pidgeotto':pidgeottoCatchRate,'Pidgeot':pidgeotCatchRate,'Rattata':rattataCatchRate,'Raticate':raticateCatchRate,'Spearow':spearowCatchRate,'Fearow':fearowCatchRate,'Ekans':ekansCatchRate,'Arbok':arbokCatchRate,'Pikachu':pikachuCatchRate,'Raichu':raichuCatchRate,'Sandshrew':sandshrewCatchRate,'Sandslash':sandslashCatchRate,'NidoranF':nidoranFCatchRate,'Nidorina':nidorinaCatchRate,'Nidoqueen':nidoqueenCatchRate,'NidoranM':nidoranMCatchRate,'Nidorino':nidorinoCatchRate,'Nidoking':nidokingCatchRate,'Clefairy':clefairyCatchRate,'Clefable':clefableCatchRate,'Vulpix':vulpixCatchRate,'Ninetales':ninetalesCatchRate,'Jigglypuff':jigglypuffCatchRate,'Wigglytuff':wigglytuffCatchRate,'Zubat':zubatCatchRate,'Golbat':golbatCatchRate,'Oddish':oddishCatchRate,'Gloom':gloomCatchRate,'Vileplume':vileplumeCatchRate,'Paras':parasCatchRate,'Parasect':parasectCatchRate,'Venonat':venonatCatchRate,'Venomoth':venomothCatchRate,'Diglett':diglettCatchRate,'Dugtrio':dugtrioCatchRate,'Meowth':meowthCatchRate,'Persian':persianCatchRate,'Psyduck':psyduckCatchRate,'Golduck':golduckCatchRate,'Mankey':mankeyCatchRate,'Primeape':primeapeCatchRate,'Growlithe':growlitheCatchRate,'Arcanine':arcanineCatchRate,'Poliwag':poliwagCatchRate,'Poliwhirl':poliwhirlCatchRate,'Poliwrath':poliwrathCatchRate,'Abra':abraCatchRate,'Kadabra':kadabraCatchRate,'Alakazam':alakazamCatchRate,'Machop':machopCatchRate,'Machoke':machokeCatchRate,'Machamp':machampCatchRate,'Bellsprout':bellsproutCatchRate,'Weepinbell':weepinbellCatchRate,'Victreebel':victreebelCatchRate,'Tentacool':tentacoolCatchRate,'Tentacruel':tentacruelCatchRate,'Geodude':geodudeCatchRate,'Graveler':gravelerCatchRate,'Golem':golemCatchRate,'Ponyta':ponytaCatchRate,'Rapidash':rapidashCatchRate,'Slowpoke':slowpokeCatchRate,'Slowbro':slowbroCatchRate,'Magnemite':magnemiteCatchRate,'Magneton':magnetonCatchRate,'Farfetch\'d':farfetchdCatchRate,'Doduo':doduoCatchRate,'Dodrio':dodrioCatchRate,'Seel':seelCatchRate,'Dewgong':dewgongCatchRate,'Grimer':grimerCatchRate,'Muk':mukCatchRate,'Shellder':shellderCatchRate,'Cloyster':cloysterCatchRate,'Gastly':gastlyCatchRate,'Haunter':haunterCatchRate,'Gengar':gengarCatchRate,'Onix':onixCatchRate,'Drowzee':drowzeeCatchRate,'Hypno':hypnoCatchRate,'Krabby':krabbyCatchRate,'Kingler':kinglerCatchRate,'Voltorb':voltorbCatchRate,'Electrode':electrodeCatchRate,'Exeggcute':exeggcuteCatchRate,'Exeggutor':exeggutorCatchRate,'Cubone':cuboneCatchRate,'Marowak':marowakCatchRate,'Hitmonlee':hitmonleeCatchRate,'Hitmonchan':hitmonchanCatchRate,'Lickitung':lickitungCatchRate,'Koffing':koffingCatchRate,'Weezing':weezingCatchRate,'Rhyhorn':rhyhornCatchRate,'Rhydon':rhydonCatchRate,'Chansey':chanseyCatchRate,'Tangela':tangelaCatchRate,'Kangaskhan':kangaskhanCatchRate,'Horsea':horseaCatchRate,'Seadra':seadraCatchRate,'Goldeen':goldeenCatchRate,'Seaking':seakingCatchRate,'Staryu':staryuCatchRate,'Starmie':starmieCatchRate,'Mr Mime':mrMimeCatchRate,'Scyther':scytherCatchRate,'Jynx':jynxCatchRate,'Electabuzz':electabuzzCatchRate,'Magmar':magmarCatchRate,'Pinsir':pinsirCatchRate,'Tauros':taurosCatchRate,'Magikarp':magikarpCatchRate,'Gyarados':gyaradosCatchRate,'Lapras':laprasCatchRate,'Ditto':dittoCatchRate,'Eevee':eeveeCatchRate,'Vaporeon':vaporeonCatchRate,'Jolteon':jolteonCatchRate,'Flareon':flareonCatchRate,'Porygon':porygonCatchRate,'Omanyte':omanyteCatchRate,'Omastar':omastarCatchRate,'Kabuto':kabutoCatchRate,'Kabutops':kabutopsCatchRate,'Aerodactyl':aerodactylCatchRate,'Snorlax':snorlaxCatchRate,'Articuno':articunoCatchRate,'Zapdos':zapdosCatchRate,'Moltres':moltresCatchRate,'Dratini':dratiniCatchRate,'Dragonair':dragonairCatchRate,'Dragonite':dragoniteCatchRate,'Mewtwo':mewtwoCatchRate,'Mew':mewCatchRate}