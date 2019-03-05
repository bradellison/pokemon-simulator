from random import randint
from operator import add
import operator
import time
import random
import math

bulbasaurBaseStats = [45,49,49,65,65,45]
ivysaurBaseStats = [60,62,63,80,80,60]
venusaurBaseStats = [80,82,83,100,100,80]
charmanderBaseStats = [39,52,43,60,50,65]
charmeleonBaseStats = [58,64,58,80,65,80]
charizardBaseStats = [78,84,78,109,85,100]
squirtleBaseStats = [44,48,65,50,64,43]
wartortleBaseStats = [59,63,80,65,80,58]
blastoiseBaseStats = [79,83,100,85,105,78]
pidgeyBaseStats = [40,45,40,35,35,56]
rattataBaseStats = [30,56,35,25,35,72]

geodudeBaseStats = [40,80,100,30,30,20]
onixBaseStats = [35,45,160,30,45,70]

pokemonBaseStatListToDict = {'HP':0,'Atk':1,'Def':2,'SpAtk':3,'SpDef':4,'Spd':5,'Accuracy':6}
pokemonBaseStatDictToList = {0:'HP',1:'Atk',2:'Def',3:'SpAtk',4:'SpDef',5:'Spd',6:'Accuracy'}

effectivenessScale = {0.25:'it was not very effective and',0.5:'it was not very effective and',1:'',2:'it was super-effective and',4:'it was super-effective and'}

myPokemonCurrentStatStage = [0,0,0,0,0,0,0]
enemyPokemonCurrentStatStage = [0,0,0,0,0,0,0]

pokemonCurrentStatStages = {'My Pokemon':myPokemonCurrentStatStage, 'Enemy Pokemon':enemyPokemonCurrentStatStage}

pokemonStatStageToMult = {-6:0.25,-5:0.28,-4:0.33,-3:0.40,-2:0.50,-1:0.66,0:1,1:1.5,2:2,3:2.5,4:3,5:3.5,6:4}

nonVolatileStatusNumberToType = {0:'Nothing',1:'Burned',2:'Paralyzed',3:'Sleep',4:'Frozen',5:'Poisoned',6:'Toxic'}
volatileStatusNumberToType = {0:'Nothing',1:'Bound',2:'Confused',3:'Curse',4:'Embargo',5:'Encore',6:'Flinch',7:'Heal Block',8:'Identified',9:'Infatuation',10:'Leech Seed',11:'Nightmare',12:'Perish Song',13:'Taunt',14:'Telekinesis',15:'Torment'}

ballCatchModifiers = {'PokeBall':1,'Great Ball':2,'Ultra Ball':3,'Master Ball':'Master'}
statusCatchModifiers = {0:1,1:1.5,2:1.5,3:2,4:2,5:1.5,6:1.5}

pokemonCatchRate = {'Bulbasaur':45,'Ivysaur':45,'Venusaur':45,'Charmander':45,'Charmeleon':45,'Charizard':45,'Squirtle':45,'Wartortle':45,'Blastoise':45,'Pidgey':255,'Rattata':255}

bulbasaurType = {'Type One':'Grass','Type Two':'Poison'}
ivysaurType = {'Type One':'Grass','Type Two':'Poison'}
venusaurType = {'Type One':'Grass','Type Two':'Poison'}
charmanderType = {'Type One':'Fire','Type Two':'Null'}
charmeleonType = {'Type One':'Fire','Type Two':'Null'}
charizardType = {'Type One':'Fire','Type Two':'Flying'}
squirtleType = {'Type One':'Water','Type Two':'Null'}
wartortleType = {'Type One':'Water','Type Two':'Null'}
blastoiseType = {'Type One':'Water','Type Two':'Null'}
pidgeyType = {'Type One':'Normal','Type Two':'Flying'}
rattataType = {'Type One':'Normal','Type Two':'Null'}
geodudeType = {'Type One':'Rock', 'Type Two':'Ground'}
onixType = {'Type One':'Rock', 'Type Two':'Ground'}

bulbasaurExpGroup = {'Exp Group':'Fast','Exp Yield':64}
ivysaurExpGroup = {'Exp Group':'Fast','Exp Yield':142}
venusaurExpGroup = {'Exp Group':'Fast','Exp Yield':236}
charmanderExpGroup = {'Exp Group':'Fast','Exp Yield':62}
charmeleonExpGroup = {'Exp Group':'Fast','Exp Yield':142}
charizardExpGroup = {'Exp Group':'Fast','Exp Yield':240}
squirtleExpGroup = {'Exp Group':'Fast','Exp Yield':63}
wartortleExpGroup = {'Exp Group':'Fast','Exp Yield':142}
blastoiseExpGroup = {'Exp Group':'Fast','Exp Yield':239}
pidgeyExpGroup = {'Exp Group':'Medium Slow','Exp Yield':55}
rattataExpGroup = {'Exp Group':'Medium Fast','Exp Yield':57}
geodudeExpGroup = {'Exp Group':'Fast','Exp Yield':90}
onixExpGroup = {'Exp Group':'Fast','Exp Yield':77}


bulbasaurEvolution = {'Evolve':'Yes','Level':16,'Pokemon':'Ivysaur'}
ivysaurEvolution = {'Evolve':'Yes','Level':36,'Pokemon':'Venusaur'}
venusaurEvolution = {'Evolve':'No'}
charmanderEvolution = {'Evolve':'Yes','Level':16,'Pokemon':'Charmeleon'}
charmeleonEvolution = {'Evolve':'Yes','Level':36,'Pokemon':'Charizard'}
charizardEvolution = {'Evolve':'No'}
squirtleEvolution = {'Evolve':'Yes','Level':16,'Pokemon':'Wartortle'}
wartortleEvolution = {'Evolve':'Yes','Level':36,'Pokemon':'Blastoise'}
blastoiseEvolution = {'Evolve':'No'}
pidgeyEvolution = {'Evolve':'No'}
rattataEvolution = {'Evolve':'No'}
geodudeEvolution = {'Evolve':'No'}
onixEvolution = {'Evolve':'No'}

bulbasaurMovesByLevel = {1:'Tackle',3:'Growl',7:'Leech Seed',9:'Vine Whip',13:'Poison Powder',1400:'Sleep Powder',1500:'Take Down',1900:'Razor Leaf'}
ivysaurMovesByLevel = {1:'Tackle',3:'Growl',700:'Leech Seed',9:'Vine Whip',13:'Poison Powder',1400:'Sleep Powder',1500:'Take Down',2000:'Razor Leaf'}
venusaurMovesByLevel = {1:'Tackle',3:'Growl',700:'Leech Seed',9:'Vine Whip',13:'Poison Powder',1400:'Sleep Powder',1500:'Take Down',2000:'Razor Leaf'}
charmanderMovesByLevel = {1:'Scratch',2:'Growl',7:'Ember',10:'Smokescreen',1600:'Dragon Rage',19:'Scary Face',25:'Fire Fang'}
charmeleonMovesByLevel = {1:'Scratch',2:'Growl',7:'Ember',10:'Smokescreen',1700:'Dragon Rage',21:'Scary Face',28:'Fire Fang'}
charizardMovesByLevel = {1:'Scratch',2:'Growl',7:'Ember',10:'Smokescreen',1700:'Dragon Rage',21:'Scary Face',28:'Fire Fang'}
squirtleMovesByLevel = {1:'Tackle',4:'Tail Whip',7:'Water Gun',10:'Withdraw',13:'Bubble',16:'Bite'}
wartortleMovesByLevel = {1:'Tackle',4:'Tail Whip',7:'Water Gun',10:'Withdraw',13:'Bubble',16:'Bite'}
blastoiseMovesByLevel = {1:'Tackle',4:'Tail Whip',7:'Water Gun',10:'Withdraw',13:'Bubble',16:'Bite'}
pidgeyMovesByLevel = {1:'Tackle',500:'Sand Attack',9:'Gust',13:'Quick Attack'}
rattataMovesByLevel = {1:'Tackle',2:'Tail Whip',4:'Quick Attack',700:'Focus Energy',10:'Bite'}
geodudeMovesByLevel = {1:'Tackle',2:'Defense Curl',4:'Rock Polish',12:'Magnitude',16:'Rock Throw'}
onixMovesByLevel = {1:'Tackle',2:'Defense Curl',400:'Mud Sport',6:'Rock Polish',1000:'Rollout',12:'Magnitude',16:'Rock Throw'}

pokemonStats = {'Bulbasaur':bulbasaurBaseStats,'Ivysaur':ivysaurBaseStats,'Venusaur':venusaurBaseStats,'Charmander':charmanderBaseStats,'Charmeleon':charmeleonBaseStats,'Charizard':charizardBaseStats,'Squirtle':squirtleBaseStats,'Wartortle':wartortleBaseStats,'Blastoise':blastoiseBaseStats,'Pidgey':pidgeyBaseStats,'Rattata':rattataBaseStats,'Geodude':geodudeBaseStats,'Onix':onixBaseStats}
pokemonTypes = {'Bulbasaur':bulbasaurType,'Ivysaur':ivysaurType,'Venusaur':venusaurType,'Charmander':charmanderType,'Charmeleon':charmeleonType,'Charizard':charizardType,'Squirtle':squirtleType,'Wartortle':wartortleType,'Blastoise':blastoiseType,'Pidgey':pidgeyType,'Rattata':rattataType,'Geodude':geodudeType,'Onix':onixType}
pokemonMovesByLevel = {'Bulbasaur':bulbasaurMovesByLevel,'Ivysaur':ivysaurMovesByLevel,'Venusaur':venusaurMovesByLevel,'Charmander':charmanderMovesByLevel,'Charmeleon':charmeleonMovesByLevel,'Charizard':charizardMovesByLevel,'Squirtle':squirtleMovesByLevel,'Wartortle':wartortleMovesByLevel,'Blastoise':blastoiseMovesByLevel,'Pidgey':pidgeyMovesByLevel,'Rattata':rattataMovesByLevel,'Geodude':geodudeMovesByLevel,'Onix':onixMovesByLevel}
pokemonExpGroup = {'Bulbasaur':bulbasaurExpGroup,'Ivysaur':ivysaurExpGroup,'Venusaur':venusaurExpGroup,'Charmander':charmanderExpGroup,'Charmeleon':charmeleonExpGroup,'Charizard':charizardExpGroup,'Squirtle':squirtleExpGroup,'Wartortle':wartortleExpGroup,'Blastoise':blastoiseExpGroup,'Pidgey':pidgeyExpGroup,'Rattata':rattataExpGroup,'Geodude':geodudeExpGroup,'Onix':onixExpGroup}
pokemonEvolutionDetails = {'Bulbasaur':bulbasaurEvolution,'Ivysaur':ivysaurEvolution,'Venusaur':venusaurEvolution,'Charmander':charmanderEvolution,'Charmeleon':charmeleonEvolution,'Charizard':charizardEvolution,'Squirtle':squirtleEvolution,'Wartortle':wartortleEvolution,'Blastoise':blastoiseEvolution,'Pidgey':pidgeyEvolution,'Rattata':rattataEvolution,'Geodude':geodudeEvolution,'Onix':onixEvolution}

#pokemonTypes = {'Bulbasaur':bulbasaurType,'Ivysaur':ivysaurType,'Venusaur':venusaurType,'Charmander':charmanderType,'Charmeleon':charmeleonType,'Charizard':charizardType,'Squirtle':squirtleType,'Wartortle':wartortleType,'Blastoise':blastoiseType,'Caterpie':caterpieType,'Metapod':metapodType,'Butterfree':butterfreeType,'Weedle':weedleType,'Kakuna':kakunaType,'Beedrill':beedrillType,'Pidgey':pidgeyType,'Pidgeotto':pidgeottoType,'Pidgeot':pidgeotType,'Rattata':rattataType,'Raticate':raticateType,'Spearow':spearowType,'Fearow':fearowType,'Ekans':ekansType,'Arbok':arbokType,'Pikachu':pikachuType,'Raichu':raichuType,'Sandshrew':sandshrewType,'Sandslash':sandslashType,'NidoranF':nidoranFType,'Nidorina':nidorinaType,'Nidoqueen':nidoqueenType,'NidoranM':nidoranMType,'Nidorino':nidorinoType,'Nidoking':nidokingType,'Clefairy':clefairyType,'Clefable':clefableType,'Vulpix':vulpixType,'Ninetales':ninetalesType,'Jigglypuff':jigglypuffType,'Wigglytuff':wigglytuffType,'Zubat':zubatType,'Golbat':golbatType,'Oddish':oddishType,'Gloom':gloomType,'Vileplume':vileplumeType,'Paras':parasType,'Parasect':parasectType,'Venonat':venonatType,'Venomoth':venomothType,'Diglett':diglettType,'Dugtrio':dugtrioType,'Meowth':meowthType,'Persian':persianType,'Psyduck':psyduckType,'Golduck':golduckType,'Mankey':mankeyType,'Primeape':primeapeType,'Growlithe':growlitheType,'Arcanine':arcanineType,'Poliwag':poliwagType,'Poliwhirl':poliwhirlType,'Poliwrath':poliwrathType,'Abra':abraType,'Kadabra':kadabraType,'Alakazam':alakazamType,'Machop':machopType,'Machoke':machokeType,'Machamp':machampType,'Bellsprout':bellsproutType,'Weepinbell':weepinbellType,'Victreebel':victreebelType,'Tentacool':tentacoolType,'Tentacruel':tentacruelType,'Geodude':geodudeType,'Graveler':gravelerType,'Golem':golemType,'Ponyta':ponytaType,'Rapidash':rapidashType,'Slowpoke':slowpokeType,'Slowbro':slowbroType,'Magnemite':magnemiteType,'Magneton':magnetonType,'Farfetch\'d':farfetchdType,'Doduo':doduoType,'Dodrio':dodrioType,'Seel':seelType,'Dewgong':dewgongType,'Grimer':grimerType,'Muk':mukType,'Shellder':shellderType,'Cloyster':cloysterType,'Gastly':gastlyType,'Haunter':haunterType,'Gengar':gengarType,'Onix':onixType,'Drowzee':drowzeeType,'Hypno':hypnoType,'Krabby':krabbyType,'Kingler':kinglerType,'Voltorb':voltorbType,'Electrode':electrodeType,'Exeggcute':exeggcuteType,'Exeggutor':exeggutorType,'Cubone':cuboneType,'Marowak':marowakType,'Hitmonlee':hitmonleeType,'Hitmonchan':hitmonchanType,'Lickitung':lickitungType,'Koffing':koffingType,'Weezing':weezingType,'Rhyhorn':rhyhornType,'Rhydon':rhydonType,'Chansey':chanseyType,'Tangela':tangelaType,'Kangaskhan':kangaskhanType,'Horsea':horseaType,'Seadra':seadraType,'Goldeen':goldeenType,'Seaking':seakingType,'Staryu':staryuType,'Starmie':starmieType,'Mr Mime':mrMimeType,'Scyther':scytherType,'Jynx':jynxType,'Electabuzz':electabuzzType,'Magmar':magmarType,'Pinsir':pinsirType,'Tauros':taurosType,'Magikarp':magikarpType,'Gyarados':gyaradosType,'Lapras':laprasType,'Ditto':dittoType,'Eevee':eeveeType,'Vaporeon':vaporeonType,'Jolteon':jolteonType,'Flareon':flareonType,'Porygon':porygonType,'Omanyte':omanyteType,'Omastar':omastarType,'Kabuto':kabutoType,'Kabutops':kabutopsType,'Aerodactyl':aerodactylType,'Snorlax':snorlaxType,'Articuno':articunoType,'Zapdos':zapdosType,'Moltres':moltresType,'Dratini':dratiniType,'Dragonair':dragonairType,'Dragonite':dragoniteType,'Mewtwo':mewtwoType,'Mew':mewType}
#pokemonStats = {'Bulbasaur':bulbasaurBaseStats,'Ivysaur':ivysaurBaseStats,'Venusaur':venusaurBaseStats,'Charmander':charmanderBaseStats,'Charmeleon':charmeleonBaseStats,'Charizard':charizardBaseStats,'Squirtle':squirtleBaseStats,'Wartortle':wartortleBaseStats,'Blastoise':blastoiseBaseStats,'Caterpie':caterpieBaseStats,'Metapod':metapodBaseStats,'Butterfree':butterfreeBaseStats,'Weedle':weedleBaseStats,'Kakuna':kakunaBaseStats,'Beedrill':beedrillBaseStats,'Pidgey':pidgeyBaseStats,'Pidgeotto':pidgeottoBaseStats,'Pidgeot':pidgeotBaseStats,'Rattata':rattataBaseStats,'Raticate':raticateBaseStats,'Spearow':spearowBaseStats,'Fearow':fearowBaseStats,'Ekans':ekansBaseStats,'Arbok':arbokBaseStats,'Pikachu':pikachuBaseStats,'Raichu':raichuBaseStats,'Sandshrew':sandshrewBaseStats,'Sandslash':sandslashBaseStats,'Nidoran♀':nidoran♀BaseStats,'Nidorina':nidorinaBaseStats,'Nidoqueen':nidoqueenBaseStats,'Nidoran♂':nidoran♂BaseStats,'Nidorino':nidorinoBaseStats,'Nidoking':nidokingBaseStats,'Clefairy':clefairyBaseStats,'Clefable':clefableBaseStats,'Vulpix':vulpixBaseStats,'Ninetales':ninetalesBaseStats,'Jigglypuff':jigglypuffBaseStats,'Wigglytuff':wigglytuffBaseStats,'Zubat':zubatBaseStats,'Golbat':golbatBaseStats,'Oddish':oddishBaseStats,'Gloom':gloomBaseStats,'Vileplume':vileplumeBaseStats,'Paras':parasBaseStats,'Parasect':parasectBaseStats,'Venonat':venonatBaseStats,'Venomoth':venomothBaseStats,'Diglett':diglettBaseStats,'Dugtrio':dugtrioBaseStats,'Meowth':meowthBaseStats,'Persian':persianBaseStats,'Psyduck':psyduckBaseStats,'Golduck':golduckBaseStats,'Mankey':mankeyBaseStats,'Primeape':primeapeBaseStats,'Growlithe':growlitheBaseStats,'Arcanine':arcanineBaseStats,'Poliwag':poliwagBaseStats,'Poliwhirl':poliwhirlBaseStats,'Poliwrath':poliwrathBaseStats,'Abra':abraBaseStats,'Kadabra':kadabraBaseStats,'Alakazam':alakazamBaseStats,'Machop':machopBaseStats,'Machoke':machokeBaseStats,'Machamp':machampBaseStats,'Bellsprout':bellsproutBaseStats,'Weepinbell':weepinbellBaseStats,'Victreebel':victreebelBaseStats,'Tentacool':tentacoolBaseStats,'Tentacruel':tentacruelBaseStats,'Geodude':geodudeBaseStats,'Graveler':gravelerBaseStats,'Golem':golemBaseStats,'Ponyta':ponytaBaseStats,'Rapidash':rapidashBaseStats,'Slowpoke':slowpokeBaseStats,'Slowbro':slowbroBaseStats,'Magnemite':magnemiteBaseStats,'Magneton':magnetonBaseStats,'Farfetchd':farfetchdBaseStats,'Doduo':doduoBaseStats,'Dodrio':dodrioBaseStats,'Seel':seelBaseStats,'Dewgong':dewgongBaseStats,'Grimer':grimerBaseStats,'Muk':mukBaseStats,'Shellder':shellderBaseStats,'Cloyster':cloysterBaseStats,'Gastly':gastlyBaseStats,'Haunter':haunterBaseStats,'Gengar':gengarBaseStats,'Onix':onixBaseStats,'Drowzee':drowzeeBaseStats,'Hypno':hypnoBaseStats,'Krabby':krabbyBaseStats,'Kingler':kinglerBaseStats,'Voltorb':voltorbBaseStats,'Electrode':electrodeBaseStats,'Exeggcute':exeggcuteBaseStats,'Exeggutor':exeggutorBaseStats,'Cubone':cuboneBaseStats,'Marowak':marowakBaseStats,'Hitmonlee':hitmonleeBaseStats,'Hitmonchan':hitmonchanBaseStats,'Lickitung':lickitungBaseStats,'Koffing':koffingBaseStats,'Weezing':weezingBaseStats,'Rhyhorn':rhyhornBaseStats,'Rhydon':rhydonBaseStats,'Chansey':chanseyBaseStats,'Tangela':tangelaBaseStats,'Kangaskhan':kangaskhanBaseStats,'Horsea':horseaBaseStats,'Seadra':seadraBaseStats,'Goldeen':goldeenBaseStats,'Seaking':seakingBaseStats,'Staryu':staryuBaseStats,'Starmie':starmieBaseStats,'MrMime':mrMimeBaseStats,'Scyther':scytherBaseStats,'Jynx':jynxBaseStats,'Electabuzz':electabuzzBaseStats,'Magmar':magmarBaseStats,'Pinsir':pinsirBaseStats,'Tauros':taurosBaseStats,'Magikarp':magikarpBaseStats,'Gyarados':gyaradosBaseStats,'Lapras':laprasBaseStats,'Ditto':dittoBaseStats,'Eevee':eeveeBaseStats,'Vaporeon':vaporeonBaseStats,'Jolteon':jolteonBaseStats,'Flareon':flareonBaseStats,'Porygon':porygonBaseStats,'Omanyte':omanyteBaseStats,'Omastar':omastarBaseStats,'Kabuto':kabutoBaseStats,'Kabutops':kabutopsBaseStats,'Aerodactyl':aerodactylBaseStats,'Snorlax':snorlaxBaseStats,'Articuno':articunoBaseStats,'Zapdos':zapdosBaseStats,'Moltres':moltresBaseStats,'Dratini':dratiniBaseStats,'Dragonair':dragonairBaseStats,'Dragonite':dragoniteBaseStats,'Mewtwo':mewtwoBaseStats,'Mew':mewBaseStats}
#pokemonYields = {'Bulbasaur':bulbasaurYields,'Ivysaur':ivysaurYields,'Venusaur':venusaurYields,'Charmander':charmanderYields,'Charmeleon':charmeleonYields,'Charizard':charizardYields,'Squirtle':squirtleYields,'Wartortle':wartortleYields,'Blastoise':blastoiseYields,'Caterpie':caterpieYields,'Metapod':metapodYields,'Butterfree':butterfreeYields,'Weedle':weedleYields,'Kakuna':kakunaYields,'Beedrill':beedrillYields,'Pidgey':pidgeyYields,'Pidgeotto':pidgeottoYields,'Pidgeot':pidgeotYields,'Rattata':rattataYields,'Raticate':raticateYields,'Spearow':spearowYields,'Fearow':fearowYields,'Ekans':ekansYields,'Arbok':arbokYields,'Pikachu':pikachuYields,'Raichu':raichuYields,'Sandshrew':sandshrewYields,'Sandslash':sandslashYields,'Nidoran♀':nidoran♀Yields,'Nidorina':nidorinaYields,'Nidoqueen':nidoqueenYields,'Nidoran♂':nidoran♂Yields,'Nidorino':nidorinoYields,'Nidoking':nidokingYields,'Clefairy':clefairyYields,'Clefable':clefableYields,'Vulpix':vulpixYields,'Ninetales':ninetalesYields,'Jigglypuff':jigglypuffYields,'Wigglytuff':wigglytuffYields,'Zubat':zubatYields,'Golbat':golbatYields,'Oddish':oddishYields,'Gloom':gloomYields,'Vileplume':vileplumeYields,'Paras':parasYields,'Parasect':parasectYields,'Venonat':venonatYields,'Venomoth':venomothYields,'Diglett':diglettYields,'Dugtrio':dugtrioYields,'Meowth':meowthYields,'Persian':persianYields,'Psyduck':psyduckYields,'Golduck':golduckYields,'Mankey':mankeyYields,'Primeape':primeapeYields,'Growlithe':growlitheYields,'Arcanine':arcanineYields,'Poliwag':poliwagYields,'Poliwhirl':poliwhirlYields,'Poliwrath':poliwrathYields,'Abra':abraYields,'Kadabra':kadabraYields,'Alakazam':alakazamYields,'Machop':machopYields,'Machoke':machokeYields,'Machamp':machampYields,'Bellsprout':bellsproutYields,'Weepinbell':weepinbellYields,'Victreebel':victreebelYields,'Tentacool':tentacoolYields,'Tentacruel':tentacruelYields,'Geodude':geodudeYields,'Graveler':gravelerYields,'Golem':golemYields,'Ponyta':ponytaYields,'Rapidash':rapidashYields,'Slowpoke':slowpokeYields,'Slowbro':slowbroYields,'Magnemite':magnemiteYields,'Magneton':magnetonYields,'Farfetchd':farfetchdYields,'Doduo':doduoYields,'Dodrio':dodrioYields,'Seel':seelYields,'Dewgong':dewgongYields,'Grimer':grimerYields,'Muk':mukYields,'Shellder':shellderYields,'Cloyster':cloysterYields,'Gastly':gastlyYields,'Haunter':haunterYields,'Gengar':gengarYields,'Onix':onixYields,'Drowzee':drowzeeYields,'Hypno':hypnoYields,'Krabby':krabbyYields,'Kingler':kinglerYields,'Voltorb':voltorbYields,'Electrode':electrodeYields,'Exeggcute':exeggcuteYields,'Exeggutor':exeggutorYields,'Cubone':cuboneYields,'Marowak':marowakYields,'Hitmonlee':hitmonleeYields,'Hitmonchan':hitmonchanYields,'Lickitung':lickitungYields,'Koffing':koffingYields,'Weezing':weezingYields,'Rhyhorn':rhyhornYields,'Rhydon':rhydonYields,'Chansey':chanseyYields,'Tangela':tangelaYields,'Kangaskhan':kangaskhanYields,'Horsea':horseaYields,'Seadra':seadraYields,'Goldeen':goldeenYields,'Seaking':seakingYields,'Staryu':staryuYields,'Starmie':starmieYields,'MrMime':mrMimeYields,'Scyther':scytherYields,'Jynx':jynxYields,'Electabuzz':electabuzzYields,'Magmar':magmarYields,'Pinsir':pinsirYields,'Tauros':taurosYields,'Magikarp':magikarpYields,'Gyarados':gyaradosYields,'Lapras':laprasYields,'Ditto':dittoYields,'Eevee':eeveeYields,'Vaporeon':vaporeonYields,'Jolteon':jolteonYields,'Flareon':flareonYields,'Porygon':porygonYields,'Omanyte':omanyteYields,'Omastar':omastarYields,'Kabuto':kabutoYields,'Kabutops':kabutopsYields,'Aerodactyl':aerodactylYields,'Snorlax':snorlaxYields,'Articuno':articunoYields,'Zapdos':zapdosYields,'Moltres':moltresYields,'Dratini':dratiniYields,'Dragonair':dragonairYields,'Dragonite':dragoniteYields,'Mewtwo':mewtwoYields,'Mew':mewYields}
#pokemonEvolutionDetails = {'Bulbasaur':bulbasaurEvolution,'Ivysaur':ivysaurEvolution,'Venusaur':venusaurEvolution,'Charmander':charmanderEvolution,'Charmeleon':charmeleonEvolution,'Charizard':charizardEvolution,'Squirtle':squirtleEvolution,'Wartortle':wartortleEvolution,'Blastoise':blastoiseEvolution,'Caterpie':caterpieEvolution,'Metapod':metapodEvolution,'Butterfree':butterfreeEvolution,'Weedle':weedleEvolution,'Kakuna':kakunaEvolution,'Beedrill':beedrillEvolution,'Pidgey':pidgeyEvolution,'Pidgeotto':pidgeottoEvolution,'Pidgeot':pidgeotEvolution,'Rattata':rattataEvolution,'Raticate':raticateEvolution,'Spearow':spearowEvolution,'Fearow':fearowEvolution,'Ekans':ekansEvolution,'Arbok':arbokEvolution,'Pikachu':pikachuEvolution,'Raichu':raichuEvolution,'Sandshrew':sandshrewEvolution,'Sandslash':sandslashEvolution,'Nidoran♀':nidoran♀Evolution,'Nidorina':nidorinaEvolution,'Nidoqueen':nidoqueenEvolution,'Nidoran♂':nidoran♂Evolution,'Nidorino':nidorinoEvolution,'Nidoking':nidokingEvolution,'Clefairy':clefairyEvolution,'Clefable':clefableEvolution,'Vulpix':vulpixEvolution,'Ninetales':ninetalesEvolution,'Jigglypuff':jigglypuffEvolution,'Wigglytuff':wigglytuffEvolution,'Zubat':zubatEvolution,'Golbat':golbatEvolution,'Oddish':oddishEvolution,'Gloom':gloomEvolution,'Vileplume':vileplumeEvolution,'Paras':parasEvolution,'Parasect':parasectEvolution,'Venonat':venonatEvolution,'Venomoth':venomothEvolution,'Diglett':diglettEvolution,'Dugtrio':dugtrioEvolution,'Meowth':meowthEvolution,'Persian':persianEvolution,'Psyduck':psyduckEvolution,'Golduck':golduckEvolution,'Mankey':mankeyEvolution,'Primeape':primeapeEvolution,'Growlithe':growlitheEvolution,'Arcanine':arcanineEvolution,'Poliwag':poliwagEvolution,'Poliwhirl':poliwhirlEvolution,'Poliwrath':poliwrathEvolution,'Abra':abraEvolution,'Kadabra':kadabraEvolution,'Alakazam':alakazamEvolution,'Machop':machopEvolution,'Machoke':machokeEvolution,'Machamp':machampEvolution,'Bellsprout':bellsproutEvolution,'Weepinbell':weepinbellEvolution,'Victreebel':victreebelEvolution,'Tentacool':tentacoolEvolution,'Tentacruel':tentacruelEvolution,'Geodude':geodudeEvolution,'Graveler':gravelerEvolution,'Golem':golemEvolution,'Ponyta':ponytaEvolution,'Rapidash':rapidashEvolution,'Slowpoke':slowpokeEvolution,'Slowbro':slowbroEvolution,'Magnemite':magnemiteEvolution,'Magneton':magnetonEvolution,'Farfetchd':farfetchdEvolution,'Doduo':doduoEvolution,'Dodrio':dodrioEvolution,'Seel':seelEvolution,'Dewgong':dewgongEvolution,'Grimer':grimerEvolution,'Muk':mukEvolution,'Shellder':shellderEvolution,'Cloyster':cloysterEvolution,'Gastly':gastlyEvolution,'Haunter':haunterEvolution,'Gengar':gengarEvolution,'Onix':onixEvolution,'Drowzee':drowzeeEvolution,'Hypno':hypnoEvolution,'Krabby':krabbyEvolution,'Kingler':kinglerEvolution,'Voltorb':voltorbEvolution,'Electrode':electrodeEvolution,'Exeggcute':exeggcuteEvolution,'Exeggutor':exeggutorEvolution,'Cubone':cuboneEvolution,'Marowak':marowakEvolution,'Hitmonlee':hitmonleeEvolution,'Hitmonchan':hitmonchanEvolution,'Lickitung':lickitungEvolution,'Koffing':koffingEvolution,'Weezing':weezingEvolution,'Rhyhorn':rhyhornEvolution,'Rhydon':rhydonEvolution,'Chansey':chanseyEvolution,'Tangela':tangelaEvolution,'Kangaskhan':kangaskhanEvolution,'Horsea':horseaEvolution,'Seadra':seadraEvolution,'Goldeen':goldeenEvolution,'Seaking':seakingEvolution,'Staryu':staryuEvolution,'Starmie':starmieEvolution,'MrMime':mrMimeEvolution,'Scyther':scytherEvolution,'Jynx':jynxEvolution,'Electabuzz':electabuzzEvolution,'Magmar':magmarEvolution,'Pinsir':pinsirEvolution,'Tauros':taurosEvolution,'Magikarp':magikarpEvolution,'Gyarados':gyaradosEvolution,'Lapras':laprasEvolution,'Ditto':dittoEvolution,'Eevee':eeveeEvolution1,'Vaporeon':vaporeonEvolution,'Eevee':eeveeEvolution2,'Jolteon':jolteonEvolution,'Eevee':eeveeEvolution3,'Flareon':flareonEvolution,'Porygon':porygonEvolution,'Omanyte':omanyteEvolution,'Omastar':omastarEvolution,'Kabuto':kabutoEvolution,'Kabutops':kabutopsEvolution,'Aerodactyl':aerodactylEvolution,'Snorlax':snorlaxEvolution,'Articuno':articunoEvolution,'Zapdos':zapdosEvolution,'Moltres':moltresEvolution,'Dratini':dratiniEvolution,'Dragonair':dragonairEvolution,'Dragonite':dragoniteEvolution,'Mewtwo':mewtwoEvolution,'Mew':mewEvolution}
#pokemonExpGroup = {'Bulbasaur':bulbasaurExpGroup,'Ivysaur':ivysaurExpGroup,'Venusaur':venusaurExpGroup,'Charmander':charmanderExpGroup,'Charmeleon':charmeleonExpGroup,'Charizard':charizardExpGroup,'Squirtle':squirtleExpGroup,'Wartortle':wartortleExpGroup,'Blastoise':blastoiseExpGroup,'Caterpie':caterpieExpGroup,'Metapod':metapodExpGroup,'Butterfree':butterfreeExpGroup,'Weedle':weedleExpGroup,'Kakuna':kakunaExpGroup,'Beedrill':beedrillExpGroup,'Pidgey':pidgeyExpGroup,'Pidgeotto':pidgeottoExpGroup,'Pidgeot':pidgeotExpGroup,'Rattata':rattataExpGroup,'Raticate':raticateExpGroup,'Spearow':spearowExpGroup,'Fearow':fearowExpGroup,'Ekans':ekansExpGroup,'Arbok':arbokExpGroup,'Pikachu':pikachuExpGroup,'Raichu':raichuExpGroup,'Sandshrew':sandshrewExpGroup,'Sandslash':sandslashExpGroup,'Nidoran♀':nidoran♀ExpGroup,'Nidorina':nidorinaExpGroup,'Nidoqueen':nidoqueenExpGroup,'Nidoran♂':nidoran♂ExpGroup,'Nidorino':nidorinoExpGroup,'Nidoking':nidokingExpGroup,'Clefairy':clefairyExpGroup,'Clefable':clefableExpGroup,'Vulpix':vulpixExpGroup,'Ninetales':ninetalesExpGroup,'Jigglypuff':jigglypuffExpGroup,'Wigglytuff':wigglytuffExpGroup,'Zubat':zubatExpGroup,'Golbat':golbatExpGroup,'Oddish':oddishExpGroup,'Gloom':gloomExpGroup,'Vileplume':vileplumeExpGroup,'Paras':parasExpGroup,'Parasect':parasectExpGroup,'Venonat':venonatExpGroup,'Venomoth':venomothExpGroup,'Diglett':diglettExpGroup,'Dugtrio':dugtrioExpGroup,'Meowth':meowthExpGroup,'Persian':persianExpGroup,'Psyduck':psyduckExpGroup,'Golduck':golduckExpGroup,'Mankey':mankeyExpGroup,'Primeape':primeapeExpGroup,'Growlithe':growlitheExpGroup,'Arcanine':arcanineExpGroup,'Poliwag':poliwagExpGroup,'Poliwhirl':poliwhirlExpGroup,'Poliwrath':poliwrathExpGroup,'Abra':abraExpGroup,'Kadabra':kadabraExpGroup,'Alakazam':alakazamExpGroup,'Machop':machopExpGroup,'Machoke':machokeExpGroup,'Machamp':machampExpGroup,'Bellsprout':bellsproutExpGroup,'Weepinbell':weepinbellExpGroup,'Victreebel':victreebelExpGroup,'Tentacool':tentacoolExpGroup,'Tentacruel':tentacruelExpGroup,'Geodude':geodudeExpGroup,'Graveler':gravelerExpGroup,'Golem':golemExpGroup,'Ponyta':ponytaExpGroup,'Rapidash':rapidashExpGroup,'Slowpoke':slowpokeExpGroup,'Slowbro':slowbroExpGroup,'Magnemite':magnemiteExpGroup,'Magneton':magnetonExpGroup,'Farfetchd':farfetchdExpGroup,'Doduo':doduoExpGroup,'Dodrio':dodrioExpGroup,'Seel':seelExpGroup,'Dewgong':dewgongExpGroup,'Grimer':grimerExpGroup,'Muk':mukExpGroup,'Shellder':shellderExpGroup,'Cloyster':cloysterExpGroup,'Gastly':gastlyExpGroup,'Haunter':haunterExpGroup,'Gengar':gengarExpGroup,'Onix':onixExpGroup,'Drowzee':drowzeeExpGroup,'Hypno':hypnoExpGroup,'Krabby':krabbyExpGroup,'Kingler':kinglerExpGroup,'Voltorb':voltorbExpGroup,'Electrode':electrodeExpGroup,'Exeggcute':exeggcuteExpGroup,'Exeggutor':exeggutorExpGroup,'Cubone':cuboneExpGroup,'Marowak':marowakExpGroup,'Hitmonlee':hitmonleeExpGroup,'Hitmonchan':hitmonchanExpGroup,'Lickitung':lickitungExpGroup,'Koffing':koffingExpGroup,'Weezing':weezingExpGroup,'Rhyhorn':rhyhornExpGroup,'Rhydon':rhydonExpGroup,'Chansey':chanseyExpGroup,'Tangela':tangelaExpGroup,'Kangaskhan':kangaskhanExpGroup,'Horsea':horseaExpGroup,'Seadra':seadraExpGroup,'Goldeen':goldeenExpGroup,'Seaking':seakingExpGroup,'Staryu':staryuExpGroup,'Starmie':starmieExpGroup,'MrMime':mrMimeExpGroup,'Scyther':scytherExpGroup,'Jynx':jynxExpGroup,'Electabuzz':electabuzzExpGroup,'Magmar':magmarExpGroup,'Pinsir':pinsirExpGroup,'Tauros':taurosExpGroup,'Magikarp':magikarpExpGroup,'Gyarados':gyaradosExpGroup,'Lapras':laprasExpGroup,'Ditto':dittoExpGroup,'Eevee':eeveeExpGroup,'Vaporeon':vaporeonExpGroup,'Jolteon':jolteonExpGroup,'Flareon':flareonExpGroup,'Porygon':porygonExpGroup,'Omanyte':omanyteExpGroup,'Omastar':omastarExpGroup,'Kabuto':kabutoExpGroup,'Kabutops':kabutopsExpGroup,'Aerodactyl':aerodactylExpGroup,'Snorlax':snorlaxExpGroup,'Articuno':articunoExpGroup,'Zapdos':zapdosExpGroup,'Moltres':moltresExpGroup,'Dratini':dratiniExpGroup,'Dragonair':dragonairExpGroup,'Dragonite':dragoniteExpGroup,'Mewtwo':mewtwoExpGroup,'Mew':mewExpGroup}
#fff
pokemonWild = ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise']

routeTwoWildPokemon = ['Pidgey','Rattata']
routeTwoWildLevels = [2,3,4]

wildPokemonLocations = {'Route Two':routeTwoWildPokemon}
wildLevelLocations =  {'Route Two':routeTwoWildLevels}

tackleInfo = {'Base Damage':40, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
scratchInfo = {'Base Damage':40, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
emberInfo = {'Base Damage':45, 'Move Type':'Fire', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'Yes', 'Priority':0}
bubbleInfo = {'Base Damage':40, 'Move Type':'Water', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'Yes', 'Priority':0}
vineWhipInfo = {'Base Damage':40, 'Move Type':'Grass', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
growlInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':90, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
defenseCurlInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':10000, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
tailWhipInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
flamethrowerInfo = {'Base Damage':90, 'Move Type':'Fire', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'No', 'Priority':0}
hydroPumpInfo = {'Base Damage':110, 'Move Type':'Water', 'Move Accuracy':80, 'Move Variety':'Special', 'Added Effect':'No', 'Priority':0}
petalBlizzardInfo = {'Base Damage':90, 'Move Type':'Grass', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
hardenInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':10000, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
rockTombInfo = {'Base Damage':60, 'Move Type':'Rock', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'Yes', 'Priority':0}
rockThrowInfo = {'Base Damage':50, 'Move Type':'Rock', 'Move Accuracy':90, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
rockPolishInfo = {'Base Damage':0, 'Move Type':'Rock', 'Move Accuracy':10000, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
magnitudeInfo = {'Base Damage':50, 'Move Type':'Ground', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
leechSeedInfo = {'Base Damage':0, 'Move Type':'Grass', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
gustInfo = {'Base Damage':40, 'Move Type':'Flying', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
quickAttackInfo = {'Base Damage':40, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':1}
sandAttackInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
smokescreenInfo = {'Base Damage':0, 'Move Type':'Normal', 'Move Accuracy':100, 'Move Variety':'Support', 'Added Effect':'No', 'Priority':0}
biteInfo = {'Base Attack':60, 'Move Type':'Dark', 'Move Accuracy':100, 'Move Variety':'Physical', 'Added Effect':'No', 'Priority':0}
watergunInfo = {'Base Damage':40, 'Move Type':'Water', 'Move Accuracy':90, 'Move Variety':'Special', 'Added Effect':'No', 'Priority':0}

growlExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
tailWhipExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
emberExtraInfo = {'Stat Change':'None', 'Non-Volatile Status Change':'Yes', 'Volatile Status Change':'No'}
defenseCurlExtraInfo = {'Stat Change':'Self', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
hardenExtraInfo = {'Stat Change':'Self', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
rockPolishExtraInfo = {'Stat Change':'Self', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
rockTombExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
leechSeedExtraInfo = {'Stat Change':'None', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'Yes'}
sandAttackExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
smokescreenExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}
bubbleExtraInfo = {'Stat Change':'Enemy', 'Non-Volatile Status Change':'No', 'Volatile Status Change':'No'}

growlStatChangeInfo = {'HP':0,'Atk':-1,'Def':0,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
defenseCurlStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
tailWhipStatChangeInfo = {'HP':0,'Atk':0,'Def':-1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
hardenStatChangeInfo = {'HP':0,'Atk':0,'Def':1,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':0,'Chance':100}
rockPolishStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':2,'Accuracy':0,'Chance':100}
rockTombStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':-1,'Accuracy':0,'Chance':100}
sandAttackStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':-1,'Chance':100}
smokescreenStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':0,'Accuracy':-1,'Chance':100}
bubbleStatChangeInfo = {'HP':0,'Atk':0,'Def':0,'SpAtk':0,'SpDef':0,'Spd':-1,'Accuracy':0,'Chance':100}

emberNonVolatileStatusChangeInfo = {'Type':1,'Chance':10}

leechSeedVolatileStatusChangeInfo = {'Type':10,'Chance':100}

normalEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':1, 'Ghost':0, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
fightingEffect = {'Normal':2, 'Fighting':1, 'Flying':0.5, 'Poison':0.5, 'Ground':1, 'Rock':2, 'Bug':0.5, 'Ghost':0, 'Steel':2, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':0.5, 'Ice':2, 'Dragon':1, 'Dark':2, 'Fairy':0.5, 'Null':1}
flyingEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':2, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':2, 'Electric':0.5, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
poisonEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':0.5, 'Ground':0.5, 'Rock':0.5, 'Bug':1, 'Ghost':0.5, 'Steel':0, 'Fire':1, 'Water':1, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':2, 'Null':1}
groundEffect = {'Normal':1, 'Fighting':1, 'Flying':0, 'Poison':2, 'Ground':1, 'Rock':2, 'Bug':0.5, 'Ghost':1, 'Steel':2, 'Fire':2, 'Water':1, 'Grass':0.5, 'Electric':2, 'Psychic':1, 'Ice':1, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
rockEffect = {'Normal':1, 'Fighting':0.5, 'Flying':2, 'Poison':1, 'Ground':0.5, 'Rock':1, 'Bug':2, 'Ghost':1, 'Steel':0.5, 'Fire':2, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':2, 'Dragon':1, 'Dark':1, 'Fairy':1, 'Null':1}
bugEffect = {'Normal':1, 'Fighting':0.5, 'Flying':0.5, 'Poison':0.5, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':0.5, 'Steel':0.5, 'Fire':0.5, 'Water':1, 'Grass':2, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':2, 'Fairy':0.5, 'Null':1}
ghostEffect = {'Normal':0, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':2, 'Steel':1, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':0.5, 'Fairy':1, 'Null':1}
steelEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':2, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':0.5, 'Grass':1, 'Electric':0.5, 'Psychic':1, 'Ice':2, 'Dragon':1, 'Dark':1, 'Fairy':2, 'Null':1}
fireEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':0.5, 'Bug':2, 'Ghost':1, 'Steel':2, 'Fire':0.5, 'Water':0.5, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':2, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
waterEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':2, 'Rock':2, 'Bug':1, 'Ghost':1, 'Steel':1, 'Fire':2, 'Water':0.5, 'Grass':0.5, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
grassEffect = {'Normal':1, 'Fighting':1, 'Flying':0.5, 'Poison':0.5, 'Ground':2, 'Rock':2, 'Bug':0.5, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':2, 'Grass':0.5, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
electricEffect = {'Normal':1, 'Fighting':1, 'Flying':2, 'Poison':1, 'Ground':0, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':1, 'Fire':1, 'Water':2, 'Grass':0.5, 'Electric':0.5, 'Psychic':1, 'Ice':1, 'Dragon':0.5, 'Dark':1, 'Fairy':1, 'Null':1}
psychicEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':2, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':0.5, 'Ice':1, 'Dragon':1, 'Dark':0, 'Fairy':1, 'Null':1}
iceEffect = {'Normal':1, 'Fighting':1, 'Flying':2, 'Poison':1, 'Ground':2, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':0.5, 'Grass':2, 'Electric':1, 'Psychic':1, 'Ice':0.5, 'Dragon':2, 'Dark':1, 'Fairy':1, 'Null':1}
dragonEffect = {'Normal':1, 'Fighting':1, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':2, 'Dark':1, 'Fairy':0, 'Null':1}
darkEffect = {'Normal':1, 'Fighting':0.5, 'Flying':1, 'Poison':1, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':2, 'Steel':1, 'Fire':1, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':2, 'Ice':1, 'Dragon':1, 'Dark':0.5, 'Fairy':0.5, 'Null':1}
fairyEffect = {'Normal':1, 'Fighting':2, 'Flying':1, 'Poison':0.5, 'Ground':1, 'Rock':1, 'Bug':1, 'Ghost':1, 'Steel':0.5, 'Fire':0.5, 'Water':1, 'Grass':1, 'Electric':1, 'Psychic':1, 'Ice':1, 'Dragon':2, 'Dark':2, 'Fairy':1, 'Null':1}
allType = {'Normal':normalEffect, 'Fighting':fightingEffect, 'Flying':flyingEffect, 'Poison':poisonEffect, 'Ground':groundEffect, 'Rock':rockEffect, 'Bug':bugEffect, 'Ghost':ghostEffect, 'Steel':steelEffect, 'Fire':fireEffect, 'Water':waterEffect, 'Grass':grassEffect, 'Electric':electricEffect, 'Psychic':psychicEffect, 'Ice':iceEffect, 'Dragon':dragonEffect, 'Dark':darkEffect, 'Fairy':fairyEffect}

moveInfo = {'Tackle':tackleInfo,'Ember':emberInfo,'Bubble':bubbleInfo,'Vine Whip':vineWhipInfo,'Growl':growlInfo,'Defense Curl':defenseCurlInfo,'Scratch':scratchInfo,'Tail Whip':tailWhipInfo,'Flamethrower':flamethrowerInfo,'Hydro Pump':hydroPumpInfo,'Petal Blizzard':petalBlizzardInfo,'Harden':hardenInfo,'Rock Tomb':rockTombInfo,'Rock Throw':rockThrowInfo,'Rock Polish':rockPolishInfo,'Magnitude':magnitudeInfo,'Leech Seed':leechSeedInfo,'Gust':gustInfo,'Quick Attack':quickAttackInfo,'Sand Attack':sandAttackInfo,'Bite':biteInfo,'Smokescreen':smokescreenInfo,'Water Gun':watergunInfo}
moveExtraInfo = {'Ember':emberExtraInfo,'Growl':growlExtraInfo,'Defense Curl':defenseCurlExtraInfo,'Tail Whip':tailWhipExtraInfo,'Harden':hardenExtraInfo,'Rock Polish':rockPolishExtraInfo,'Rock Tomb':rockTombExtraInfo,'Leech Seed':leechSeedExtraInfo,'Sand Attack':sandAttackExtraInfo,'Smokescreen':smokescreenExtraInfo,'Bubble':bubbleExtraInfo}
moveStatChangeInfo = {'Growl':growlStatChangeInfo,'Defense Curl':defenseCurlStatChangeInfo,'Tail Whip':tailWhipStatChangeInfo,'Harden':hardenStatChangeInfo,'Rock Polish':rockPolishStatChangeInfo,'Rock Tomb':rockTombStatChangeInfo,'Sand Attack':sandAttackStatChangeInfo,'Smokescreen':smokescreenStatChangeInfo,'Bubble':bubbleStatChangeInfo}
moveNonVolatileStatusChangeInfo = {'Ember':emberNonVolatileStatusChangeInfo}
moveVolatileStatusChangeInfo = {'Leech Seed':leechSeedVolatileStatusChangeInfo}

def getRandomPokemon(location):
	pokemonSetSize = len(pokemonWild)
	pokemonNumber = randint(1,pokemonSetSize) - 1
	return pokemonWild[pokemonNumber]

def getWildPokemonByLocation(location):
	locationPokemon = wildPokemonLocations[location]
	pokemonList = random.sample(locationPokemon,1)
	pokemon = pokemonList[0]
	return pokemon

def getWildLevelByLocation(location):
	locationLevel = wildLevelLocations[location]
	levelList = random.sample(locationLevel,1)
	level = levelList[0]
	return level

def getRandomLevel():
	pokemonLevel = randint(1,100)
	return pokemonLevel

def getMoveOption(pokemon,moveNumber):
	pokemonMoveset = pokemonMoves[pokemon]
	if moveNumber == 0:
		return pokemonMoveset['Move One']
	if moveNumber == 1:
		return pokemonMoveset['Move Two']
	if moveNumber == 2:
		return pokemonMoveset['Move Three']
	if moveNumber == 3:
		return pokemonMoveset['Move Four']

def getPokemonMovesByLevel(pokemon):
	movesByLevel = pokemonMovesByLevel[pokemon]
	return movesByLevel

def getRandomIV():
	IV = []
	for _ in range(6):
		x = randint(1,31)
		IV.append(x)
	return IV

def getMoveSet(pokemon,level):
	allMoves = []
	pokemonMovesByLevel = getPokemonMovesByLevel(pokemon)
	for i in range(1,level+1):
		if i in pokemonMovesByLevel:
			allMoves.append(pokemonMovesByLevel[i])
	if len(allMoves) <= 4:
		return allMoves
	moveSet = random.sample(allMoves,4)
	return moveSet

def getRandomMoveFromSet(pokemon,level):
	moveSet = getMoveSet(pokemon,level)
	movesetSize = len(moveSet)
	moveNumber = randint(1,movesetSize) - 1
	moveList = moveSet[moveNumber]
	move = moveList(0)
	return move

def getPokemonHPMult(pokemon):
	pokemonCurrentStatStage = statStage
	pokemonHPStage = pokemonCurrentStatStage[0]
	if pokemonHPStage > 6:
		pokemonHPStage = 6
	if pokemonHPStage < -6:
		pokemonHPStage = -6
	pokemonHPMult = pokemonStatStageToMult[pokemonHPStage]
	return pokemonHPMult

def getPokemonAtkMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonAtkStage = pokemonCurrentStatStage[1]
	if pokemonAtkStage > 6:
		pokemonAtkStage = 6
	if pokemonAtkStage < -6:
		pokemonAtkStage = -6
	pokemonAtkMult = pokemonStatStageToMult[pokemonAtkStage]
	return pokemonAtkMult

def getPokemonDefMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonDefStage = pokemonCurrentStatStage[2]
	if pokemonDefStage > 6:
		pokemonDefStage = 6
	if pokemonDefStage < -6:
		pokemonDefStage = -6
	pokemonDefMult = pokemonStatStageToMult[pokemonDefStage]
	return pokemonDefMult

def getPokemonSpAtkMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonSpAtkStage = pokemonCurrentStatStage[3]
	if pokemonSpAtkStage > 6:
		pokemonSpAtkStage = 6
	if pokemonSpAtkStage < -6:
		pokemonSpAtkStage = -6
	pokemonSpAtkMult = pokemonStatStageToMult[pokemonSpAtkStage]
	return pokemonSpAtkMult

def getPokemonSpDefMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonSpDefStage = pokemonCurrentStatStage[4]
	if pokemonSpDefStage > 6:
		pokemonSpDefStage = 6
	if pokemonSpDefStage < -6:
		pokemonSpDefStage = -6
	pokemonSpDefMult = pokemonStatStageToMult[pokemonSpDefStage]
	return pokemonSpDefMult

def getPokemonSpdMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonSpdStage = pokemonCurrentStatStage[5]
	if pokemonSpdStage > 6:
		pokemonSpdStage = 6
	if pokemonSpdStage < -6:
		pokemonSpdStage = -6
	pokemonSpdMult = pokemonStatStageToMult[pokemonSpdStage]
	return pokemonSpdMult

def getPokemonAccMult(statStage):
	pokemonCurrentStatStage = statStage
	pokemonAccStage = pokemonCurrentStatStage[6]
	if pokemonAccStage > 6:
		pokemonAccStage = 6
	if pokemonAccStage < -6:
		pokemonAccStage = -6
	pokemonAccMult = pokemonStatStageToMult[pokemonAccStage]
	return pokemonAccMult

def gethpStat(pokemon,level,iv):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[0]
	return int(((2 * myPokemonStats[0] + iv) * level / 100 ) + level + 10)

def getAtkStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[1]
	pokemonAtkMult = getPokemonAtkMult(statStage)
	return pokemonAtkMult * (((2 * myPokemonStats[1] + iv) * level / 100 ) + 5)

def getDefStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[2]
	pokemonDefMult = getPokemonDefMult(statStage)
	return pokemonDefMult * (((2 * myPokemonStats[2] + iv) * level / 100 ) + 5)

def getSpAtkStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[3]
	pokemonSpAtkMult = getPokemonSpAtkMult(statStage)
	return pokemonSpAtkMult * (((2 * myPokemonStats[3] + iv) * level / 100 ) + 5)

def getSpDefStat(pokemon,level,iv,statStage):
	myPokemonStats = pokemonStats[pokemon]
	iv = iv[4]
	pokemonSpDefMult = getPokemonSpDefMult(statStage)
	return pokemonSpDefMult * (((2 * myPokemonStats[4] + iv) * level / 100 ) + 5)

def getSpdStat(pokemon,level,iv,statStage,status):
	myPokemonStats = pokemonStats[pokemon]
	statusType = getNonVolatileStatusType(status)
	if statusType == 'Paralyzed':
		statusMult = 0.5
	else:
		statusMult = 1
	iv = iv[5]
	pokemonSpdMult = getPokemonSpdMult(statStage)
	return pokemonSpdMult * statusMult * (((2 * myPokemonStats[5] + iv) * level / 100 ) + 5)

def getPokemonStatStage(pokemon):
	pokemonToApplyStatChange = pokemonCurrentStatStages[pokemon]
	return pokemonToApplyStatChange

def getStatChangeForWording(myPokemon,statChange):
	for i in range(7):
		if i == 0:
			stat = 'HP'
		if i == 1:
			stat = 'attack'
		if i == 2:
			stat = 'defense'
		if i == 3:
			stat = 'special attack'
		if i == 4:
			stat = 'special defense'
		if i == 5:
			stat = 'speed'
		if i == 6:
			stat = 'accuracy'

def getStatChangeWording(i)
		changeForStat = statChange[i]
		if changeForStat == 1:
			print(myPokemon + '\'s', stat, 'raised!')
		if changeForStat == 2:
			print(myPokemon + '\'s', stat, 'raised greatly!')
		if changeForStat >= 3:
			print(myPokemon + '\'s', stat, 'raised hugely!')
		if changeForStat == -1:
			print(myPokemon + '\'s', stat, 'fell!')
		if changeForStat == -2:
			print(myPokemon + '\'s', stat, 'fell greatly!')
		if changeForStat <= -3:
			print(myPokemon + '\'s', stat, 'fell hugely!')

def getBallCatchModifier(ball):
	modifier = ballCatchModifiers[ball]
	return modifier

def getStatusCatchModifier(status):
	modifier = statusCatchModifiers[status]
	return modifier

def getPokemonCatchRate(pokemon):
	modifier = pokemonCatchRate[pokemon]
	return modifier

def getPokemonTypeOne(pokemon):
	pokemonType = pokemonTypes[pokemon]
	return pokemonType['Type One']

def getPokemonTypeTwo(pokemon):
	pokemonType = pokemonTypes[pokemon]
	return pokemonType['Type Two']

def getMoveBaseDamage(move):
	moveBaseDam = moveInfo[move]
	return moveBaseDam['Base Damage']

def getMoveType(move):
	moveType = moveInfo[move]
	return moveType['Move Type']

def getMoveVariety(move):
	moveVariety = moveInfo[move]
	return moveVariety['Move Variety']

def getMoveExtra(move):
	moveExtra = moveInfo[move]
	return moveExtra['Added Effect'] 

def getMoveExtraForm(move):
	moveExtraForm = moveExtraInfo[move]
	return moveExtraForm['Stat Change']

def getNonVolatileStatusChange(move):
	statusChange = moveExtraInfo[move]
	return statusChange['Non-Volatile Status Change']

def getNonVolatileStatusChangeType(move):
	statusChangeType = moveNonVolatileStatusChangeInfo[move]
	return statusChangeType['Type']

def getNonVolatileStatusChangeChance(move):
	statusChangeChance = moveNonVolatileStatusChangeInfo[move]
	return statusChangeChance['Chance']

def getVolatileStatusChange(move):
	statusChange = moveExtraInfo[move]
	return statusChange['Volatile Status Change']

def getVolatileStatusChangeType(move):
	statusChangeType = moveVolatileStatusChangeInfo[move]
	return statusChangeType['Type']

def getVolatileStatusChangeChance(move):
	statusChangeChance = moveVolatileStatusChangeInfo[move]
	return statusChangeChance['Chance']

def getMoveStatChangeInfo(move,stat):
	moveStatChange = moveStatChangeInfo[move]
	return moveStatChange[stat]

def getMoveAccuracy(move):
	moveAccuracy = moveInfo[move]
	return moveAccuracy['Move Accuracy']

def getMovePriority(move):
	movePriority = moveInfo[move]
	return movePriority['Priority']

def getEffectiveness(move,pokemon):
	moveType = getMoveType(move)
	pokemonTypeOne = getPokemonTypeOne(pokemon)
	pokemonTypeTwo = getPokemonTypeTwo(pokemon)
	moveType2 = allType[moveType]
	return moveType2[pokemonTypeOne] * moveType2[pokemonTypeTwo]

def getEffectivesnessWording(i):
	effectivenessWording = effectivenessScale[i]
	return effectivenessWording

def getStabBonus(move,pokemon):
	moveType = getMoveType(move)
	pokemonTypeOne = getPokemonTypeOne(pokemon)
	pokemonTypeTwo = getPokemonTypeTwo(pokemon)
	if moveType == pokemonTypeOne:
		return 1.5
	if moveType == pokemonTypeTwo:
		return 1.5
	else:
		return 1 

def getHitOrMiss(move,statStage):
	accuracy = getMoveAccuracy(move)
	accMult = getPokemonAccMult(statStage)
	randomOf100 = randint(1,100)
	if randomOf100 <= accuracy * accMult:
		return 'Hit'
	else:
		return 'Miss'

def getExpGroup(pokemon):
	expInfo = pokemonExpGroup[pokemon]
	expGroup = expInfo['Exp Group']
	return expGroup

def getExpYield(pokemon,level):
	expInfo = pokemonExpGroup[pokemon]
	expYieldBase = expInfo['Exp Yield']
	expYield = int((expYieldBase * level) / 7)
	return expYield

def getExp(pokemon,level):
	expGroup = getExpGroup(pokemon)
	n = level
	if expGroup == 'Erratic':
		if n <= 50:
			exp = ((n**3)*(100-n))/50
		if 50 < n <= 68:
			exp = ((n**3)*(150-n))/100
		if 68 < n <= 98:
			exp = (((n**3)*((1911-10*n)/3))/500)
		if 98 < n <= 100:
			exp = ((n**3)*(160-n))/100
	if expGroup == 'Fast':
		exp = (4*n**3)/5
	if expGroup == 'Medium Fast':
		exp = n**3
	if expGroup == 'Medium Slow':
		exp = (6/5)*n**3 - 15*n**2 + 100*n - 140
	if expGroup == 'Slow':
		exp = (5*n**3)/4
	if expGroup == 'Fluctuating':
		if n <= 15:
			exp = n**3 * ((((n+1)/3)+24)/50)
		if 15 < n <= 36:
			exp = n**3 * ((n+14/50))
		if 36 < n <= 100:
			exp = n**3 * (((n/2)+32)/50)
	return int(exp)

def getPokemonEvolve(pokemon,level):
	pokemonEvolutionInfo = pokemonEvolutionDetails[pokemon]
	pokemonEvolve = pokemonEvolutionInfo['Evolve']
	if pokemonEvolve == 'No':
		return pokemonEvolve
	pokemonEvolveLevel = pokemonEvolutionInfo['Level']
	if pokemonEvolveLevel <= level:
		pokemonEvolution = pokemonEvolutionInfo['Pokemon']
		return pokemonEvolution
	if pokemonEvolveLevel > level:
		return 'No'

def getMoveDamage(move,atkPokemon,atkLevel,atkIV,atkStatStage,atkStatus,defPokemon,defLevel,defIV,defStatStage):
	moveBaseDamage = getMoveBaseDamage(move)
	effectiveness = getEffectiveness(move,defPokemon)
	stabBonus = getStabBonus(move,atkPokemon)
	moveVariety = getMoveVariety(move)
	statusType = getNonVolatileStatusType(atkStatus)
	if moveVariety == 'Physical':
		atkStat = getAtkStat(atkPokemon,atkLevel,atkIV,atkStatStage)
		defStat = getDefStat(defPokemon,defLevel,defIV,defStatStage)
		if statusType == 'Burned':
			statusMult = 0.5
		else:
			statusMult = 1
		moveDamage = int((((((2 * atkLevel / 5) + 2) * atkStat * moveBaseDamage / defStat) / 50 ) + 2) * stabBonus * effectiveness * statusMult * float(randint(0,15)+85)/100)
		return moveDamage	
	if moveVariety == 'Special':
		atkStat = getSpAtkStat(atkPokemon,atkLevel,atkIV,atkStatStage)
		defStat = getSpDefStat(defPokemon,defLevel,defIV,defStatStage)
		moveDamage = int((((((2 * atkLevel / 5) + 2) * atkStat * moveBaseDamage / defStat) / 50 ) + 2) * stabBonus * effectiveness * float(randint(0,15)+85)/100)
		return moveDamage
	if moveVariety == 'Support':
		moveExtraForm = getMoveExtraForm(move)
		if moveExtraForm == 'Self':
			return 0
		if moveExtraForm == 'Enemy':
			return 0

def getPokemonBaseStatDictToList(i):
	dictToList = pokemonBaseStatDictToList[i]
	return dictToList

def getStatChange(move):
	statChange=[]
	for i in range(0,7):
		stat = getPokemonBaseStatDictToList(i)
		moveStatChange = getMoveStatChangeInfo(move,stat)
		statChange.append(moveStatChange)
	return statChange

def getNonVolatileStatusType(i):
	StatusType = nonVolatileStatusNumberToType[i]
	return StatusType

def getPostMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP,myPokemonMaxHP):
	myPokemonNVStatusType = getNonVolatileStatusType(myPokemonNVStatus)
	if myPokemonNVStatusType != 'Nothing':
		if myPokemonNVStatusType == 'Burned':
			burnDamage = int(myPokemonMaxHP / 16)
			myPokemonHP = (myPokemonHP - burnDamage)
			print(myPokemon, 'took', burnDamage, 'HP damage due to it\'s burn! It has', myPokemonHP, '/', myPokemonMaxHP, 'HP remaining!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]
		elif myPokemonNonVolatileStatusType == 'Poisoned':
			poisonDamage = int(myPokemonMaxHP / 8)
			myPokemonHP = (myPokemonHP - poisonDamage)
			print(myPokemon, 'took', poisonDamage, 'HP damage due to being poisoned! It has', myPokemonHP, '/', myPokemonMaxHP, 'HP remaining!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]
		elif myPokemonNonVolatileStatusType == 'Toxic':
			myPokemonStatusCount = myPokemonStatusCount + 1
			toxicDamage = int(myPokemonMaxHP * myPokemonStatusCount / 16)
			myPokemonHP = myPokemonHP - toxicDamage
			print(myPokemon, 'took', toxicDamage, 'HP damage due to being badly poisoned! It has', myPokemonHP, '/', myPokemonMaxHP, 'HP remaining!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]
	return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP]

def getPreMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount):
	myPokemonNVStatusType = getNonVolatileStatusType(myPokemonNVStatus)
	if myPokemonNVStatusType != 'Nothing':
		if myPokemonNVStatusType == 'Paralyzed':
			print(myPokemon, 'is paralyzed and may not be able to move!')
			i = randint(1,4)
			if i == 1:
				print(myPokemon, 'couldn\'t move!')
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,1]	
		elif myPokemonNonVolatileStatusType == 'Sleep':
			print(myPokemon, 'is sleeping!')
			myPokemonNVStatusCount = myPokemonNVStatusCount - 1
			if myPokemonNVStatusCount > 0:
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,1]	
			myPokemonNVStatusType = 0
			print(myPokemon, 'woke up!')
			return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,0]
		elif myPokemonNonVolatileStatusType == 'Frozen':
			i = randint(1,5)
			if i == 1:
				myPokemonStatus = 0
				print(myPokemon, 'thawed out!')
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,0]
			else:
				print(myPokemon, 'is frozen and couldn\'t move!')
				return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,1]	
	return [myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,0]	

def getTurnOrder(myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage,myPokemonStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus):
	mySpd = getSpdStat(myPokemon,myPokemonLevel,myPokemonIV,myPokemonStatStage,myPokemonStatus)
	enemySpd = getSpdStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonStatStage,enemyPokemonStatus)
	if mySpd > enemySpd:
		return 'myPokemonFirst'
	if mySpd < enemySpd:
		return 'enemyPokemonFirst'
	if mySpd == enemySpd:
		x = randint(0,1)
		if x == 0:
			return 'myPokemonFirst'
		if x == 1:
			return 'enemyPokemonFirst'

def startMyTurn(move,myInformation,enemyInformation,environmentInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyWording = enemyPlayer[1]
	enemyPokemonMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myPokemonMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)					
	preMoveNVStatusCheck = getPreMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount)
	myPokemonInfo[15]=preMoveNVStatusCheck[1];myPokemonInfo[16]=preMoveNVStatusCheck[2];interrupt=preMoveNVStatusCheck[3]
	if interrupt == 0:
		#preMoveVStatusCheck = getPreMoveVStatusCheck(myPokemon,myPokemonVStatus,myPokemonVStatusCount)
		#myPokemonInfo[17]=preMoveVStatusCheck[1],myPokemonInfo[16]=preMoveVStatusCheck[2],interrupt=preMoveVStatusCheck[3]
		if interrupt == 0:
			hitOrMiss = getHitOrMiss(move,myPokemonCurrentStatStage)
			if hitOrMiss == 'Miss':
				print(myPokemon, 'used', move, 'but it missed!')
				interrupt = 1
			if interrupt == 0:
				moveVariety = getMoveVariety(move)
				if moveVariety == 'Support':
					moveExtraForm = getMoveExtraForm(move)
					if moveExtraForm == 'Enemy':
						statChange = getStatChange(move)
						enemyPokemonCurrentStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
						enemyPokemonInfo[19]=enemyPokemonCurrentStatStage
						print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon + '!')
						statChangeWording = getStatChangeWording(enemyPokemon,statChange)
					elif moveExtraForm == 'Self':
						statChange = getStatChange(move)
						myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
						myPokemonInfo[19]=myPokemonCurrentStatStage
						print('Your', myPokemon, 'used', move + '!')
						statChangeWording = getStatChangeWording(myPokemon,statChange)
					
					elif moveExtraForm == 'None':
						nonVolatileStatus = getNonVolatileStatusChange(move)
						if nonVolatileStatus == 'Yes':
							nonVolatileStatusType = getNonVolatileStatusType(move)
							nonVolatileStatusChangeChance = getNonVolatileStatusChangeChance(move)
				if moveVariety == 'Physical' or moveVariety == 'Special':
					moveDamage = getMoveDamage(move,myPokemon,myPokemonLevel,myPokemonIV,myPokemonCurrentStatStage,myPokemonNVStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonCurrentStatStage)
					effectiveness = getEffectiveness(move,enemyPokemon); effectivenessWording = getEffectivesnessWording(effectiveness)

					enemyPokemonHP = enemyPokemonHP - moveDamage 
					
					if enemyPokemonHP < 0:
						enemyPokemonHP = 0

					enemyPokemonInfo[5] = enemyPokemonHP	

					print(myPokemon, 'used', move, 'against the', enemyWording, enemyPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', enemyPokemon, 'has', enemyPokemonHP, '/', enemyPokemonMaxHP, 'HP remaining!')
					moveExtra = getMoveExtra(move)
					if moveExtra == 'Yes':		
						moveExtraForm = getMoveExtraForm(move)
						if moveExtraForm == 'Enemy':
							statChange = getStatChange(move)
							enemyPokemonCurrentStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
							enemyPokemonInfo[19]=enemyPokemonCurrentStatStage
							statChangeWording = getStatChangeWording(enemyPokemon,statChange)

						elif moveExtraForm == 'Self':
							statChange = getStatChange(move)
							myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
							myPokemonInfo[19]=myPokemonCurrentStatStage
							statChangeWording = getStatChangeWording(enemyPokemon,statChange)

						statusChange = getNonVolatileStatusChange(move)
						if statusChange == 'Yes':
							if enemyPokemonNVStatus == 0:
								statusChangeType = getNonVolatileStatusChangeType(move)
								statusChangeChance = getNonVolatileStatusChangeChance(move)
								x = randint(1,100)
								if x <= statusChangeChance:
									enemyPokemonStatus = statusChangeType
									statusType = getNonVolatileStatusType(enemyPokemonStatus)
									print(enemyPokemon, 'was', statusType + '!')
								if statusChangeType == 3:
									x = randint(1,3)	
									enemyPokemonStatusCount = x
	postMoveNVStatusCheck = getPostMoveNVStatusCheck(myPokemon,myPokemonNVStatus,myPokemonNVStatusCount,myPokemonHP,myPokemonMaxHP)
	myPokemonInfo[15]=preMoveNVStatusCheck[1];myPokemonInfo[16]=preMoveNVStatusCheck[2];myPokemonHP=preMoveNVStatusCheck[3]
	myTeam[0]=myPokemonInfo; myInformation[0]=myTeam
	enemyTeam[0]=enemyPokemonInfo; enemyInformation[0]=enemyTeam
	return [myInformation,enemyInformation,environmentInformation]


def startEnemyTurn(move,myInformation,enemyInformation,environmentInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyWording = enemyPlayer[1]
	enemyPokemonMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myPokemonMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)					
	#Check for Non-Volatile Status
	preMoveNVStatusCheck = getPreMoveNVStatusCheck(enemyPokemon,enemyPokemonNVStatus,enemyPokemonNVStatusCount)
	enemyPokemonInfo[15]=preMoveNVStatusCheck[1];enemyPokemonInfo[16]=preMoveNVStatusCheck[2];interrupt=preMoveNVStatusCheck[3]
	if interrupt == 0:
		#preMoveVStatusCheck = getPreMoveVStatusCheck(myPokemon,myPokemonVStatus,myPokemonVStatusCount)
		#myPokemonInfo[17]=preMoveVStatusCheck[1],myPokemonInfo[16]=preMoveVStatusCheck[2],interrupt=preMoveVStatusCheck[3]
		if interrupt == 0:
			hitOrMiss = getHitOrMiss(move,enemyPokemonCurrentStatStage)
			if hitOrMiss == 'Miss':
				print('The', enemyWording, enemyPokemon, 'used', move, 'but it missed!')
				interrupt = 1
			if interrupt == 0:
				moveVariety = getMoveVariety(move)
				if moveVariety == 'Support':
					moveExtraForm = getMoveExtraForm(move)
					if moveExtraForm == 'Enemy':
						statChange = getStatChange(move)
						myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
						myPokemonInfo[19]=myPokemonCurrentStatStage
						print(enemyPokemon, 'used', move, 'against the', myPokemon + '!')
						StatChangeWording = getStatChangeWording(myPokemon,statChange)					
					elif moveExtraForm == 'Self':
						statChange = getStatChange(move)
						enemyPokemonCurrentStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
						enemyPokemonInfo[19]=enemyPokemonCurrentStatStage
						print('The', enemyWording, enemyPokemon, 'used', move + '!')
						StatChangeWording = getStatChangeWording(enemyPokemon,statChange)
					elif moveExtraForm == 'None':
						nonVolatileStatus = getNonVolatileStatusChange(move)
						if nonVolatileStatus == 'Yes':
							nonVolatileStatusType = getNonVolatileStatusType(move)
							nonVolatileStatusChangeChance = getNonVolatileStatusChangeChance(move)
				if moveVariety == 'Physical' or moveVariety == 'Special':
					moveDamage = getMoveDamage(move,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonCurrentStatStage,enemyPokemonNVStatus,myPokemon,myPokemonLevel,myPokemonIV,myPokemonCurrentStatStage)
					effectiveness = getEffectiveness(move,myPokemon); effectivenessWording = getEffectivesnessWording(effectiveness)
					myPokemonHP = myPokemonHP - moveDamage
					if myPokemonHP < 0:
						myPokemonHP = 0
					myPokemonInfo[5] = myPokemonHP
					print('The', enemyWording, enemyPokemon, 'used', move, 'against', myPokemon, '-', effectivenessWording, 'it dealt', moveDamage, 'HP damage!', myPokemon, 'has', myPokemonHP, '/', myPokemonMaxHP, 'HP remaining!')
					moveExtra = getMoveExtra(move)
					if moveExtra == 'Yes':		
						moveExtraForm = getMoveExtraForm(move)
						if moveExtraForm == 'Enemy':
							statChange = getStatChange(move)
							myPokemonCurrentStatStage = list(map(add, myPokemonCurrentStatStage, statChange))
							StatChangeWording = getStatChangeWording(myPokemon,statChange)
						elif moveExtraForm == 'Self':
							statChange = getStatChange(move)
							enemyPokemonCurrentStatStage = list(map(add, enemyPokemonCurrentStatStage, statChange))
							StatChangeWording = getStatChangeWording(enemyPokemon,statChange)
						statusChange = getNonVolatileStatusChange(move)
						if statusChange == 'Yes':
							if myPokemonNVStatus == 0:
								statusChangeType = getNonVolatileStatusChangeType(move)
								statusChangeChance = getNonVolatileStatusChangeChance(move)
								x = randint(1,100)
								if x <= statusChangeChance:
									myPokemonStatus = statusChangeType
									statusType = getNonVolatileStatusType(myPokemonStatus)
									print(myPokemon, 'was', statusType + '!')
									myPokemonInfo[15]=statusChangeType; myPokemonInfo[16]=0
								if statusChangeType == 3:
									x = randint(1,3)	
									myPokemonInfo[16]=x
	postMoveNVStatusCheck = getPostMoveNVStatusCheck(enemyPokemon,enemyPokemonNVStatus,enemyPokemonNVStatusCount,enemyPokemonHP,enemyPokemonMaxHP)
	enemyPokemonInfo[15]=preMoveNVStatusCheck[1];enemyPokemonInfo[16]=preMoveNVStatusCheck[2];enemyPokemonHP=preMoveNVStatusCheck[3]
	myTeam[0]=myPokemonInfo; myInformation[0]=myTeam
	enemyTeam[0]=enemyPokemonInfo; enemyInformation[0]=enemyTeam
	return [myInformation,enemyInformation,environmentInformation]

def getMoveInput(pokemonMoveSet):
	movesetSize = len(pokemonMoveSet)
	while True:
		try:
			moveInput = input('-- ')
			if moveInput in pokemonMoveSet:
				return moveInput
				break			
			moveInput
			if int(moveInput) <= movesetSize and int(moveInput) > 0:
				return pokemonMoveSet[int(moveInput)-1]
				break	
			print("Please choose a move from the list above!")
		except ValueError:
			print("Please choose a move from the list.")

def getChoiceInput():
	while True:
		try:
			choiceInput = input('-- ')
			if choiceInput == 'Fight':
				return choiceInput
			if choiceInput == 'Bag':
				return choiceInput
			if choiceInput == 'Pokemon':
				return choiceInput
			if choiceInput == 'Run':
				return choiceInput						
			if int(choiceInput) == 1:
				choiceInput = 'Fight'
				return choiceInput
			if int(choiceInput) == 2:
				choiceInput = 'Bag'
				return choiceInput
			if int(choiceInput) == 3:
				choiceInput = 'Pokemon'
				return choiceInput
			if int(choiceInput) == 4:
				choiceInput = 'Run'
				return choiceInput
			print("Please choose an option from the list above!")
		except ValueError:
			print("Please choose an option from the list.")

def getStarterInput():
	while True:
		try:
			choiceInput = input('-- ')
			if choiceInput == 'Bulbasaur':
				return choiceInput
			if choiceInput == 'Charmander':
				return choiceInput
			if choiceInput == 'Squirtle':
				return choiceInput					
			if int(choiceInput) == 1:
				choiceInput = 'Bulbasaur'
				return choiceInput
			if int(choiceInput) == 2:
				choiceInput = 'Charmander'
				return choiceInput
			if int(choiceInput) == 3:
				choiceInput = 'Squirtle'
				return choiceInput
			print("Please choose a Pokemon from the list above!")
		except ValueError:
			print("Please choose a move from the list.")

def getRandomSwitchPokemon(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0];myPokemonOneName = myPokemonOneInfo[1];myPokemonOneLevel = myPokemonOneInfo[2];myPokemonOneIV = myPokemonOneInfo[3];myPokemonOneEV = myPokemonOneInfo[4];myPokemonOneHP = myPokemonOneInfo[5];myPokemonOneExperience = myPokemonOneInfo[6];myPokemonOneForm = myPokemonOneInfo[7];myPokemonOneGender = myPokemonOneInfo[8];myPokemonOneAbility = myPokemonOneInfo[9];myPokemonOneTypeOne = myPokemonOneInfo[10];myPokemonOneTypeTwo = myPokemonOneInfo[11];myPokemonOneItem = myPokemonOneInfo[12];myPokemonOneMoveSet = myPokemonOneInfo[13];myPokemonOneMovePP = myPokemonOneInfo[14];myPokemonOneNVStatus = myPokemonOneInfo[15];myPokemonOneNVStatusCount = myPokemonOneInfo[16];myPokemonOneVStatus = myPokemonOneInfo[17];myPokemonOneVStatusCount = myPokemonOneInfo[18];myPokemonOneCurrentStatStage = myPokemonOneInfo[19];myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0];myPokemonTwoName = myPokemonTwoInfo[1];myPokemonTwoLevel = myPokemonTwoInfo[2];myPokemonTwoIV = myPokemonTwoInfo[3];myPokemonTwoEV = myPokemonTwoInfo[4];myPokemonTwoHP = myPokemonTwoInfo[5];myPokemonTwoExperience = myPokemonTwoInfo[6];myPokemonTwoForm = myPokemonTwoInfo[7];myPokemonTwoGender = myPokemonTwoInfo[8];myPokemonTwoAbility = myPokemonTwoInfo[9];myPokemonTwoTypeOne = myPokemonTwoInfo[10];myPokemonTwoTypeTwo = myPokemonTwoInfo[11];myPokemonTwoItem = myPokemonTwoInfo[12];myPokemonTwoMoveSet = myPokemonTwoInfo[13];myPokemonTwoMovePP = myPokemonTwoInfo[14];myPokemonTwoNVStatus = myPokemonTwoInfo[15];myPokemonTwoNVStatusCount = myPokemonTwoInfo[16];myPokemonTwoVStatus = myPokemonTwoInfo[17];myPokemonTwoVStatusCount = myPokemonTwoInfo[18];myPokemonTwoCurrentStatStage = myPokemonTwoInfo[19];myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0];myPokemonThreeName = myPokemonThreeInfo[1];myPokemonThreeLevel = myPokemonThreeInfo[2];myPokemonThreeIV = myPokemonThreeInfo[3];myPokemonThreeEV = myPokemonThreeInfo[4];myPokemonThreeHP = myPokemonThreeInfo[5];myPokemonThreeExperience = myPokemonThreeInfo[6];myPokemonThreeForm = myPokemonThreeInfo[7];myPokemonThreeGender = myPokemonThreeInfo[8];myPokemonThreeAbility = myPokemonThreeInfo[9];myPokemonThreeTypeOne = myPokemonThreeInfo[10];myPokemonThreeTypeTwo = myPokemonThreeInfo[11];myPokemonThreeItem = myPokemonThreeInfo[12];myPokemonThreeMoveSet = myPokemonThreeInfo[13];myPokemonThreeMovePP = myPokemonThreeInfo[14];myPokemonThreeNVStatus = myPokemonThreeInfo[15];myPokemonThreeNVStatusCount = myPokemonThreeInfo[16];myPokemonThreeVStatus = myPokemonThreeInfo[17];myPokemonThreeVStatusCount = myPokemonThreeInfo[18];myPokemonThreeCurrentStatStage = myPokemonThreeInfo[19];myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0];myPokemonFourName = myPokemonFourInfo[1];myPokemonFourLevel = myPokemonFourInfo[2];myPokemonFourIV = myPokemonFourInfo[3];myPokemonFourEV = myPokemonFourInfo[4];myPokemonFourHP = myPokemonFourInfo[5];myPokemonFourExperience = myPokemonFourInfo[6];myPokemonFourForm = myPokemonFourInfo[7];myPokemonFourGender = myPokemonFourInfo[8];myPokemonFourAbility = myPokemonFourInfo[9];myPokemonFourTypeOne = myPokemonFourInfo[10];myPokemonFourTypeTwo = myPokemonFourInfo[11];myPokemonFourItem = myPokemonFourInfo[12];myPokemonFourMoveSet = myPokemonFourInfo[13];myPokemonFourMovePP = myPokemonFourInfo[14];myPokemonFourNVStatus = myPokemonFourInfo[15];myPokemonFourNVStatusCount = myPokemonFourInfo[16];myPokemonFourVStatus = myPokemonFourInfo[17];myPokemonFourVStatusCount = myPokemonFourInfo[18];myPokemonFourCurrentStatStage = myPokemonFourInfo[19];myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0];myPokemonFiveName = myPokemonFiveInfo[1];myPokemonFiveLevel = myPokemonFiveInfo[2];myPokemonFiveIV = myPokemonFiveInfo[3];myPokemonFiveEV = myPokemonFiveInfo[4];myPokemonFiveHP = myPokemonFiveInfo[5];myPokemonFiveExperience = myPokemonFiveInfo[6];myPokemonFiveForm = myPokemonFiveInfo[7];myPokemonFiveGender = myPokemonFiveInfo[8];myPokemonFiveAbility = myPokemonFiveInfo[9];myPokemonFiveTypeOne = myPokemonFiveInfo[10];myPokemonFiveTypeTwo = myPokemonFiveInfo[11];myPokemonFiveItem = myPokemonFiveInfo[12];myPokemonFiveMoveSet = myPokemonFiveInfo[13];myPokemonFiveMovePP = myPokemonFiveInfo[14];myPokemonFiveNVStatus = myPokemonFiveInfo[15];myPokemonFiveNVStatusCount = myPokemonFiveInfo[16];myPokemonFiveVStatus = myPokemonFiveInfo[17];myPokemonFiveVStatusCount = myPokemonFiveInfo[18];myPokemonFiveCurrentStatStage = myPokemonFiveInfo[19];myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0];myPokemonSixName = myPokemonSixInfo[1];myPokemonSixLevel = myPokemonSixInfo[2];myPokemonSixIV = myPokemonSixInfo[3];myPokemonSixEV = myPokemonSixInfo[4];myPokemonSixHP = myPokemonSixInfo[5];myPokemonSixExperience = myPokemonSixInfo[6];myPokemonSixForm = myPokemonSixInfo[7];myPokemonSixGender = myPokemonSixInfo[8];myPokemonSixAbility = myPokemonSixInfo[9];myPokemonSixTypeOne = myPokemonSixInfo[10];myPokemonSixTypeTwo = myPokemonSixInfo[11];myPokemonSixItem = myPokemonSixInfo[12];myPokemonSixMoveSet = myPokemonSixInfo[13];myPokemonSixMovePP = myPokemonSixInfo[14];myPokemonSixNVStatus = myPokemonSixInfo[15];myPokemonSixNVStatusCount = myPokemonSixInfo[16];myPokemonSixVStatus = myPokemonSixInfo[17];myPokemonSixVStatusCount = myPokemonSixInfo[18];myPokemonSixCurrentStatStage = myPokemonSixInfo[19];myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
	while True:
		try:
			choice = randint(1,numberOfPokemon)
			if int(choice) > 0 and int(choice) <= numberOfPokemon:
				choice = int(choice) - 1
				if choice == 0:
					change = 0
				else:
					change = 1
					pokemonToChangeTo = myTeam[choice]
					pokemonHP = pokemonToChangeTo[2]
					if pokemonHP > 0:
						myTeam[choice], myTeam[0] = myTeam[0], myTeam[choice]
						return [myTeam, change]
		except ValueError:
			change

def getTeamTotalHP(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0];myPokemonOneName = myPokemonOneInfo[1];myPokemonOneLevel = myPokemonOneInfo[2];myPokemonOneIV = myPokemonOneInfo[3];myPokemonOneEV = myPokemonOneInfo[4];myPokemonOneHP = myPokemonOneInfo[5];myPokemonOneExperience = myPokemonOneInfo[6];myPokemonOneForm = myPokemonOneInfo[7];myPokemonOneGender = myPokemonOneInfo[8];myPokemonOneAbility = myPokemonOneInfo[9];myPokemonOneTypeOne = myPokemonOneInfo[10];myPokemonOneTypeTwo = myPokemonOneInfo[11];myPokemonOneItem = myPokemonOneInfo[12];myPokemonOneMoveSet = myPokemonOneInfo[13];myPokemonOneMovePP = myPokemonOneInfo[14];myPokemonOneNVStatus = myPokemonOneInfo[15];myPokemonOneNVStatusCount = myPokemonOneInfo[16];myPokemonOneVStatus = myPokemonOneInfo[17];myPokemonOneVStatusCount = myPokemonOneInfo[18];myPokemonOneCurrentStatStage = myPokemonOneInfo[19];myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
		myTeamTotalHP = myPokemonOneHP
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0];myPokemonTwoName = myPokemonTwoInfo[1];myPokemonTwoLevel = myPokemonTwoInfo[2];myPokemonTwoIV = myPokemonTwoInfo[3];myPokemonTwoEV = myPokemonTwoInfo[4];myPokemonTwoHP = myPokemonTwoInfo[5];myPokemonTwoExperience = myPokemonTwoInfo[6];myPokemonTwoForm = myPokemonTwoInfo[7];myPokemonTwoGender = myPokemonTwoInfo[8];myPokemonTwoAbility = myPokemonTwoInfo[9];myPokemonTwoTypeOne = myPokemonTwoInfo[10];myPokemonTwoTypeTwo = myPokemonTwoInfo[11];myPokemonTwoItem = myPokemonTwoInfo[12];myPokemonTwoMoveSet = myPokemonTwoInfo[13];myPokemonTwoMovePP = myPokemonTwoInfo[14];myPokemonTwoNVStatus = myPokemonTwoInfo[15];myPokemonTwoNVStatusCount = myPokemonTwoInfo[16];myPokemonTwoVStatus = myPokemonTwoInfo[17];myPokemonTwoVStatusCount = myPokemonTwoInfo[18];myPokemonTwoCurrentStatStage = myPokemonTwoInfo[19];myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0];myPokemonThreeName = myPokemonThreeInfo[1];myPokemonThreeLevel = myPokemonThreeInfo[2];myPokemonThreeIV = myPokemonThreeInfo[3];myPokemonThreeEV = myPokemonThreeInfo[4];myPokemonThreeHP = myPokemonThreeInfo[5];myPokemonThreeExperience = myPokemonThreeInfo[6];myPokemonThreeForm = myPokemonThreeInfo[7];myPokemonThreeGender = myPokemonThreeInfo[8];myPokemonThreeAbility = myPokemonThreeInfo[9];myPokemonThreeTypeOne = myPokemonThreeInfo[10];myPokemonThreeTypeTwo = myPokemonThreeInfo[11];myPokemonThreeItem = myPokemonThreeInfo[12];myPokemonThreeMoveSet = myPokemonThreeInfo[13];myPokemonThreeMovePP = myPokemonThreeInfo[14];myPokemonThreeNVStatus = myPokemonThreeInfo[15];myPokemonThreeNVStatusCount = myPokemonThreeInfo[16];myPokemonThreeVStatus = myPokemonThreeInfo[17];myPokemonThreeVStatusCount = myPokemonThreeInfo[18];myPokemonThreeCurrentStatStage = myPokemonThreeInfo[19];myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0];myPokemonFourName = myPokemonFourInfo[1];myPokemonFourLevel = myPokemonFourInfo[2];myPokemonFourIV = myPokemonFourInfo[3];myPokemonFourEV = myPokemonFourInfo[4];myPokemonFourHP = myPokemonFourInfo[5];myPokemonFourExperience = myPokemonFourInfo[6];myPokemonFourForm = myPokemonFourInfo[7];myPokemonFourGender = myPokemonFourInfo[8];myPokemonFourAbility = myPokemonFourInfo[9];myPokemonFourTypeOne = myPokemonFourInfo[10];myPokemonFourTypeTwo = myPokemonFourInfo[11];myPokemonFourItem = myPokemonFourInfo[12];myPokemonFourMoveSet = myPokemonFourInfo[13];myPokemonFourMovePP = myPokemonFourInfo[14];myPokemonFourNVStatus = myPokemonFourInfo[15];myPokemonFourNVStatusCount = myPokemonFourInfo[16];myPokemonFourVStatus = myPokemonFourInfo[17];myPokemonFourVStatusCount = myPokemonFourInfo[18];myPokemonFourCurrentStatStage = myPokemonFourInfo[19];myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0];myPokemonFiveName = myPokemonFiveInfo[1];myPokemonFiveLevel = myPokemonFiveInfo[2];myPokemonFiveIV = myPokemonFiveInfo[3];myPokemonFiveEV = myPokemonFiveInfo[4];myPokemonFiveHP = myPokemonFiveInfo[5];myPokemonFiveExperience = myPokemonFiveInfo[6];myPokemonFiveForm = myPokemonFiveInfo[7];myPokemonFiveGender = myPokemonFiveInfo[8];myPokemonFiveAbility = myPokemonFiveInfo[9];myPokemonFiveTypeOne = myPokemonFiveInfo[10];myPokemonFiveTypeTwo = myPokemonFiveInfo[11];myPokemonFiveItem = myPokemonFiveInfo[12];myPokemonFiveMoveSet = myPokemonFiveInfo[13];myPokemonFiveMovePP = myPokemonFiveInfo[14];myPokemonFiveNVStatus = myPokemonFiveInfo[15];myPokemonFiveNVStatusCount = myPokemonFiveInfo[16];myPokemonFiveVStatus = myPokemonFiveInfo[17];myPokemonFiveVStatusCount = myPokemonFiveInfo[18];myPokemonFiveCurrentStatStage = myPokemonFiveInfo[19];myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP + myPokemonFiveHP
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0];myPokemonSixName = myPokemonSixInfo[1];myPokemonSixLevel = myPokemonSixInfo[2];myPokemonSixIV = myPokemonSixInfo[3];myPokemonSixEV = myPokemonSixInfo[4];myPokemonSixHP = myPokemonSixInfo[5];myPokemonSixExperience = myPokemonSixInfo[6];myPokemonSixForm = myPokemonSixInfo[7];myPokemonSixGender = myPokemonSixInfo[8];myPokemonSixAbility = myPokemonSixInfo[9];myPokemonSixTypeOne = myPokemonSixInfo[10];myPokemonSixTypeTwo = myPokemonSixInfo[11];myPokemonSixItem = myPokemonSixInfo[12];myPokemonSixMoveSet = myPokemonSixInfo[13];myPokemonSixMovePP = myPokemonSixInfo[14];myPokemonSixNVStatus = myPokemonSixInfo[15];myPokemonSixNVStatusCount = myPokemonSixInfo[16];myPokemonSixVStatus = myPokemonSixInfo[17];myPokemonSixVStatusCount = myPokemonSixInfo[18];myPokemonSixCurrentStatStage = myPokemonSixInfo[19];myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
		myTeamTotalHP = myPokemonOneHP + myPokemonTwoHP + myPokemonThreeHP + myPokemonFourHP + myPokemonFiveHP + myPokemonSixHP
	return myTeamTotalHP

def getSwitchPokemon(myTeam):
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0];
		myPokemonOne = myPokemonOneInfo[0];myPokemonOneName = myPokemonOneInfo[1];myPokemonOneLevel = myPokemonOneInfo[2];myPokemonOneIV = myPokemonOneInfo[3];myPokemonOneEV = myPokemonOneInfo[4];myPokemonOneHP = myPokemonOneInfo[5];myPokemonOneExperience = myPokemonOneInfo[6];myPokemonOneForm = myPokemonOneInfo[7];myPokemonOneGender = myPokemonOneInfo[8];myPokemonOneAbility = myPokemonOneInfo[9];myPokemonOneTypeOne = myPokemonOneInfo[10];myPokemonOneTypeTwo = myPokemonOneInfo[11];myPokemonOneItem = myPokemonOneInfo[12];myPokemonOneMoveSet = myPokemonOneInfo[13];myPokemonOneMovePP = myPokemonOneInfo[14];myPokemonOneNVStatus = myPokemonOneInfo[15];myPokemonOneNVStatusCount = myPokemonOneInfo[16];myPokemonOneVStatus = myPokemonOneInfo[17];myPokemonOneVStatusCount = myPokemonOneInfo[18];myPokemonOneCurrentStatStage = myPokemonOneInfo[19];myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0];myPokemonTwoName = myPokemonTwoInfo[1];myPokemonTwoLevel = myPokemonTwoInfo[2];myPokemonTwoIV = myPokemonTwoInfo[3];myPokemonTwoEV = myPokemonTwoInfo[4];myPokemonTwoHP = myPokemonTwoInfo[5];myPokemonTwoExperience = myPokemonTwoInfo[6];myPokemonTwoForm = myPokemonTwoInfo[7];myPokemonTwoGender = myPokemonTwoInfo[8];myPokemonTwoAbility = myPokemonTwoInfo[9];myPokemonTwoTypeOne = myPokemonTwoInfo[10];myPokemonTwoTypeTwo = myPokemonTwoInfo[11];myPokemonTwoItem = myPokemonTwoInfo[12];myPokemonTwoMoveSet = myPokemonTwoInfo[13];myPokemonTwoMovePP = myPokemonTwoInfo[14];myPokemonTwoNVStatus = myPokemonTwoInfo[15];myPokemonTwoNVStatusCount = myPokemonTwoInfo[16];myPokemonTwoVStatus = myPokemonTwoInfo[17];myPokemonTwoVStatusCount = myPokemonTwoInfo[18];myPokemonTwoCurrentStatStage = myPokemonTwoInfo[19];myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0];myPokemonThreeName = myPokemonThreeInfo[1];myPokemonThreeLevel = myPokemonThreeInfo[2];myPokemonThreeIV = myPokemonThreeInfo[3];myPokemonThreeEV = myPokemonThreeInfo[4];myPokemonThreeHP = myPokemonThreeInfo[5];myPokemonThreeExperience = myPokemonThreeInfo[6];myPokemonThreeForm = myPokemonThreeInfo[7];myPokemonThreeGender = myPokemonThreeInfo[8];myPokemonThreeAbility = myPokemonThreeInfo[9];myPokemonThreeTypeOne = myPokemonThreeInfo[10];myPokemonThreeTypeTwo = myPokemonThreeInfo[11];myPokemonThreeItem = myPokemonThreeInfo[12];myPokemonThreeMoveSet = myPokemonThreeInfo[13];myPokemonThreeMovePP = myPokemonThreeInfo[14];myPokemonThreeNVStatus = myPokemonThreeInfo[15];myPokemonThreeNVStatusCount = myPokemonThreeInfo[16];myPokemonThreeVStatus = myPokemonThreeInfo[17];myPokemonThreeVStatusCount = myPokemonThreeInfo[18];myPokemonThreeCurrentStatStage = myPokemonThreeInfo[19];myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0];myPokemonFourName = myPokemonFourInfo[1];myPokemonFourLevel = myPokemonFourInfo[2];myPokemonFourIV = myPokemonFourInfo[3];myPokemonFourEV = myPokemonFourInfo[4];myPokemonFourHP = myPokemonFourInfo[5];myPokemonFourExperience = myPokemonFourInfo[6];myPokemonFourForm = myPokemonFourInfo[7];myPokemonFourGender = myPokemonFourInfo[8];myPokemonFourAbility = myPokemonFourInfo[9];myPokemonFourTypeOne = myPokemonFourInfo[10];myPokemonFourTypeTwo = myPokemonFourInfo[11];myPokemonFourItem = myPokemonFourInfo[12];myPokemonFourMoveSet = myPokemonFourInfo[13];myPokemonFourMovePP = myPokemonFourInfo[14];myPokemonFourNVStatus = myPokemonFourInfo[15];myPokemonFourNVStatusCount = myPokemonFourInfo[16];myPokemonFourVStatus = myPokemonFourInfo[17];myPokemonFourVStatusCount = myPokemonFourInfo[18];myPokemonFourCurrentStatStage = myPokemonFourInfo[19];myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0];myPokemonFiveName = myPokemonFiveInfo[1];myPokemonFiveLevel = myPokemonFiveInfo[2];myPokemonFiveIV = myPokemonFiveInfo[3];myPokemonFiveEV = myPokemonFiveInfo[4];myPokemonFiveHP = myPokemonFiveInfo[5];myPokemonFiveExperience = myPokemonFiveInfo[6];myPokemonFiveForm = myPokemonFiveInfo[7];myPokemonFiveGender = myPokemonFiveInfo[8];myPokemonFiveAbility = myPokemonFiveInfo[9];myPokemonFiveTypeOne = myPokemonFiveInfo[10];myPokemonFiveTypeTwo = myPokemonFiveInfo[11];myPokemonFiveItem = myPokemonFiveInfo[12];myPokemonFiveMoveSet = myPokemonFiveInfo[13];myPokemonFiveMovePP = myPokemonFiveInfo[14];myPokemonFiveNVStatus = myPokemonFiveInfo[15];myPokemonFiveNVStatusCount = myPokemonFiveInfo[16];myPokemonFiveVStatus = myPokemonFiveInfo[17];myPokemonFiveVStatusCount = myPokemonFiveInfo[18];myPokemonFiveCurrentStatStage = myPokemonFiveInfo[19];myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0];myPokemonSixName = myPokemonSixInfo[1];myPokemonSixLevel = myPokemonSixInfo[2];myPokemonSixIV = myPokemonSixInfo[3];myPokemonSixEV = myPokemonSixInfo[4];myPokemonSixHP = myPokemonSixInfo[5];myPokemonSixExperience = myPokemonSixInfo[6];myPokemonSixForm = myPokemonSixInfo[7];myPokemonSixGender = myPokemonSixInfo[8];myPokemonSixAbility = myPokemonSixInfo[9];myPokemonSixTypeOne = myPokemonSixInfo[10];myPokemonSixTypeTwo = myPokemonSixInfo[11];myPokemonSixItem = myPokemonSixInfo[12];myPokemonSixMoveSet = myPokemonSixInfo[13];myPokemonSixMovePP = myPokemonSixInfo[14];myPokemonSixNVStatus = myPokemonSixInfo[15];myPokemonSixNVStatusCount = myPokemonSixInfo[16];myPokemonSixVStatus = myPokemonSixInfo[17];myPokemonSixVStatusCount = myPokemonSixInfo[18];myPokemonSixCurrentStatStage = myPokemonSixInfo[19];myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
	print('Who would you like to choose?')
	if numberOfPokemon > 0:
		print('1 -', myPokemonOne, '- Lvl', myPokemonOneLevel, '-', myPokemonOneHP, '/', myPokemonOneMaxHP, 'HP.')
	if numberOfPokemon > 1:
		print('2 -', myPokemonTwo, '- Lvl', myPokemonTwoLevel, '-', myPokemonTwoHP, '/', myPokemonTwoMaxHP, 'HP.')
	if numberOfPokemon > 2:
		print('3 -', myPokemonThree, '- Lvl', myPokemonThreeLevel, '-', myPokemonThreeHP, '/', myPokemonThreeMaxHP, 'HP.')			
	if numberOfPokemon > 3:
		print('4 -', myPokemonFour, '- Lvl', myPokemonFourLevel, '-', myPokemonFourHP, '/', myPokemonFourMaxHP, 'HP.')	
	if numberOfPokemon > 4:
		print('5 -', myPokemonFive, '- Lvl', myPokemonFiveLevel, '-', myPokemonFiveHP, '/', myPokemonFiveMaxHP, 'HP.')	
	if numberOfPokemon > 5:
		print('Pokemon 6 -', myPokemonSix, '- Lvl', myPokemonSixLevel, '-', myPokemonSixHP, '/', myPokemonSixMaxHP, 'HP.')
	while True:
		try:
			choice = input('-- ')
			if int(choice) > 0 and int(choice) <= numberOfPokemon:
				choice = int(choice) - 1
				if choice == 0:
					if myPokemonOneHP != 0:
						change = 0
						return [myTeam, change]
				else:
					change = 1
					pokemonToChangeToInfo = myTeam[choice]
					pokemon = pokemonToChangeToInfo[0]
					pokemonHP = pokemonToChangeToInfo[2]
					if pokemonHP > 0:
						myTeam[choice], myTeam[0] = myTeam[0], myTeam[choice]
						return [myTeam, change]
					if pokemonHP == 0:
						print(pokemon, 'has fainted! Choose another!')
			print('Please choose one of the above!')
		except ValueError:
			print("Please choose one of the above!")

def startRound(myInformation,enemyInformation,environmentInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyPlayerWording = enemyPlayer[1]
	enemyPokemonMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myPokemonMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)
	print('What will you do?')
	print('Fight - Bag - Pokemon - Run')
	choiceInput = getChoiceInput()
	if choiceInput == 'Fight':
		run = [0]
		print('\nWhat will', myPokemon, 'do?')
		print(myPokemonMoveSet + ['Back'])
		myMove = getMoveInput(myPokemonMoveSet + ['Back'])
		if myMove == 'Back':
			turnOutcomeInfo = startRound(myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			return turnOutcomeInfo
		print('')
		turnOrder = getTurnOrder(myPokemon,myPokemonLevel,myPokemonIV,myPokemonCurrentStatStage,myPokemonNVStatus,enemyPokemon,enemyPokemonLevel,enemyPokemonIV,enemyPokemonCurrentStatStage,enemyPokemonNVStatus)
		enemyMoveList = random.sample(enemyPokemonMoveSet,1); enemyMove = enemyMoveList[0]
		myMovePriority = getMovePriority(myMove); enemyMovePriority = getMovePriority(enemyMove)
		if myMovePriority > enemyMovePriority:
			turnOrder = 'myPokemonFirst'
		if enemyMovePriority > myMovePriority:
			turnOrder = 'enemyPokemonFirst'
		if turnOrder == 'myPokemonFirst':
			turnOutcomeInfo = startMyTurn(myMove,myInformation,enemyInformation,environmentInformation)			
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			if enemyPokemonHP == 0 or myPokemonHP == 0:
				roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
				return roundOutcomeInfo
			turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation,run]
			return roundOutcomeInfo
		if turnOrder == 'enemyPokemonFirst':
			turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			if myPokemonHP == 0 or enemyPokemonHP == 0:
				roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
				return roundOutcomeInfo
			turnOutcomeInfo = startMyTurn(myMove,myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
			return roundOutcomeInfo
	if choiceInput == 'Run':
		run = [1]
		roundOutcomeInfo = [myTeam,enemyTeam,run]
		return roundOutcomeInfo
	if choiceInput == 'Bag':
		print('You opened your bag! What pocket would you like to go into?')
		run = [0]
		myBalls = myBag[0]; myMedicine = myBag[1]
		print('Balls - Medicine - Back')
		pocketChoice = getPocketChoice()
		if pocketChoice == 'Back':
			turnOutcomeInfo = startRound(myInformation,enemyInformation,environmentInformation)
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			return turnOutcomeInfo
		if pocketChoice == 'Balls':
			numberOfBallTypes = len(myBalls)
			if numberOfBallTypes == 0:
				print('Empty!')
				return
			print(numberOfBallTypes)
			for i in range(0,numberOfBallTypes):
				currentBall = myBalls[i]
				print(i + 1, '-', currentBall[1] + 's x', currentBall[0])
			print(i+2,'- Back')
			print('What would you like to choose?')
			print(i)
			ballChoiceInput = int(getBallChoice(i))
			print(ballChoiceInput)
			if (ballChoiceInput) == i+2:
				turnOutcomeInfo = startRound(myInformation,enemyInformation,environmentInformation)
				myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
				enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
				myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
				return turnOutcomeInfo
			ballChoice = myBalls[ballChoiceInput - 1]
			ball = ballChoice[1]; ballChoice[0] = ballChoice[0] - 1
			if ballChoice[0] == 0:
				myBalls.remove(ballChoice)
			catch = getCatch(enemyPokemon,enemyPokemonLevel,enemyPokemonMaxHP,enemyPokemonHP,ball,enemyPokemonNVStatus)
			if catch == 1:
				print('You caught the wild', enemyPokemon + '!')
				myTeam.append(enemyPokemonInfo)
				return 'Caught'
		enemyMoveList = random.sample(enemyPokemonMoveSet,1); enemyMove = enemyMoveList[0]
		turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)
		myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]
		enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
		roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
		return roundOutcomeInfo
	if choiceInput == 'Pokemon':
		run = [0]
		oldPokemon = myPokemon
		changePokemon = getSwitchPokemon(myTeam)
		myTeam = changePokemon[0]; change = changePokemon[1]
		if change == 0:
			roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
			return roundOutcomeInfo
		myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
		print ('You switched from', oldPokemon, 'into', myPokemon + '!')
		enemyMoveList = random.sample(enemyPokemonMoveSet,1); enemyMove = enemyMoveList[0]
		turnOutcomeInfo = startEnemyTurn(enemyMove,myInformation,enemyInformation,environmentInformation)
		myTeam = turnOutcomeInfo[0]; myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
		enemyTeam = turnOutcomeInfo[1]; enemyPokemonInfo = enemyTeam[0]
		roundOutcomeInfo = [myInformation,enemyInformation,environmentInformation]
		return roundOutcomeInfo

def getCatch(enemyPokemon,enemyPokemonLevel,enemyPokemonMaxHP,enemyPokemonHP,ball,enemyPokemonNVStatus):
	ballModifier = getBallCatchModifier(ball)
	if ballModifier == 'Master':
		print('Catch')
		return 1
	pokemonCatchRate = getPokemonCatchRate(enemyPokemon)
	statusModifier = getStatusCatchModifier(enemyPokemonNVStatus)
	catchValue = ((( 3 * enemyPokemonMaxHP - 2 * enemyPokemonHP) * pokemonCatchRate * ballModifier) / ( 3 * enemyPokemonMaxHP) ) * statusModifier
	catch = 1048560 / math.sqrt(math.sqrt(16711680 / catchValue))
	count = 0
	for i in range(3):
		random = randint(1,65535)
		count = count + 1
		print('Shook', count, 'times!')
		time.sleep(1)
		if catch > random:		
			if count == 3:
				print('Catch')
				return 1
		else:
			if count == 1:
				print('Not even close!')
			if count == 2:
				print('Oh, nearly had it!')
			if count == 3:
				print('So so close!')
			return 0

def getUseItem(myInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	myBalls = myBag[0]; myMedicine = myBag[1]
	print('Which pocket would you like to look in?')
	print('Balls - Medicine - Go Back')
	pocketChoice = getPocketChoice()

def getBallChoice(i):
	options = i + 2
	while True:
		try:
			choiceInput = input('-- ')
			if int(choiceInput) <= options and int(choiceInput) > 0:
				return choiceInput
			print("Please choose an option from the list above!")
		except ValueError:
			print("Please choose an option from the list.")

def getPocketChoice():
	while True:
		try:
			choiceInput = input('-- ')
			if choiceInput == 'Balls':
				return choiceInput
			if choiceInput == 'Medicine':
				return choiceInput
			if choiceInput == 'Back':
				return choiceInput			
			if int(choiceInput) == 1:
				choiceInput = 'Balls'
				return choiceInput
			if int(choiceInput) == 2:
				choiceInput = 'Medicine'
				return choiceInput
			if int(choiceInput) == 3:
				choiceInput = 'Back'
				return choiceInput
			print("Please choose an option from the list above!")
		except ValueError:
			print("Please choose an option from the list.")

def getWildEnemyInformation(location):
	enemyPokemonOne = getWildPokemonByLocation(location)
	enemyPokemonOneName = enemyPokemonOne
	enemyPokemonOneLevel = getWildLevelByLocation(location)
	enemyPokemonOneIV = getRandomIV()
	enemyPokemonOneEV = 'xxx'
	enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV)
	enemyPokemonOneExperience = getExp(enemyPokemonOne,enemyPokemonOneLevel)
	enemyPokemonOneForm = 'NA'
	enemyPokemonOneGender = 'Male'
	enemyPokemonOneAbility = 'Chloraphyll'
	enemyPokemonOneTypeOne = getPokemonTypeOne(enemyPokemonOne)
	enemyPokemonOneTypeTwo = getPokemonTypeTwo(enemyPokemonOne)
	enemyPokemonOneItem = 'None'
	enemyPokemonOneMoveSet = getMoveSet(enemyPokemonOne,enemyPokemonOneLevel)
	enemyPokemonOneMovePP = [10, 10, 10]
	enemyPokemonOneNVStatus = 0
	enemyPokemonOneNVStatusCount = 0
	enemyPokemonOneVStatus = 0
	enemyPokemonOneVStatusCount = 0
	enemyPokemonOneCurrentStatStage = [0,0,0,0,0,0,0]
	enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneName,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneEV,enemyPokemonOneHP,enemyPokemonOneExperience,enemyPokemonOneForm,enemyPokemonOneGender,enemyPokemonOneAbility,enemyPokemonOneTypeOne,enemyPokemonOneTypeTwo,enemyPokemonOneItem,enemyPokemonOneMoveSet,enemyPokemonOneMovePP,enemyPokemonOneNVStatus,enemyPokemonOneNVStatusCount,enemyPokemonOneVStatus,enemyPokemonOneVStatusCount,enemyPokemonOneCurrentStatStage]
	enemyPlayer = ['Wild','wild']
	enemyBag = ['0']
	enemyTeam = [enemyPokemonOneList]
	enemyInformation=[enemyTeam,enemyBag,enemyPlayer]
	return enemyInformation

def startBattle(myInformation,enemyInformation,environmentInformation):
	myTeam = myInformation[0];myBag = myInformation[1];myPlayer = myInformation[2]
	myPokemonInfo = myTeam[0]
	myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
	enemyTeam = enemyInformation[0];enemyBag = enemyInformation[1];enemyPlayer = enemyInformation[2]
	enemyPokemonInfo = enemyTeam[0]
	enemyPokemon = enemyPokemonInfo[0];enemyPokemonName = enemyPokemonInfo[1];enemyPokemonLevel = enemyPokemonInfo[2];enemyPokemonIV = enemyPokemonInfo[3];enemyPokemonEV = enemyPokemonInfo[4];enemyPokemonHP = enemyPokemonInfo[5];enemyPokemonExperience = enemyPokemonInfo[6];enemyPokemonForm = enemyPokemonInfo[7];enemyPokemonGender = enemyPokemonInfo[8];enemyPokemonAbility = enemyPokemonInfo[9];enemyPokemonTypeOne = enemyPokemonInfo[10];enemyPokemonTypeTwo = enemyPokemonInfo[11];enemyPokemonItem = enemyPokemonInfo[12];enemyPokemonMoveSet = enemyPokemonInfo[13];enemyPokemonMovePP = enemyPokemonInfo[14];enemyPokemonNVStatus = enemyPokemonInfo[15];enemyPokemonNVStatusCount = enemyPokemonInfo[16];enemyPokemonVStatus = enemyPokemonInfo[17];enemyPokemonVStatusCount = enemyPokemonInfo[18];enemyPokemonCurrentStatStage = enemyPokemonInfo[19]
	enemyPlayerName = enemyPlayer[0]; enemyPlayerWording = enemyPlayer[1]
	enemyPokemonMaxHP = gethpStat(enemyPokemon,enemyPokemonLevel,enemyPokemonIV); myPokemonMaxHP = gethpStat(myPokemon,myPokemonLevel,myPokemonIV)					
	print('A wild lvl', enemyPokemonLevel, enemyPokemon, 'appeared! Go,', myPokemon + '!')	
	myTeamTotalHP = getTeamTotalHP(myTeam)
	enemyTeamTotalHP = getTeamTotalHP(enemyTeam)
	while myTeamTotalHP > 0 and enemyPokemonHP > 0:
		while myPokemonHP > 0 and enemyPokemonHP > 0:
			turnOutcomeInfo = startRound(myInformation,enemyInformation,environmentInformation)
			if turnOutcomeInfo == 'Caught':
				return
			myInformation = turnOutcomeInfo[0]; myTeam = myInformation[0]; myPokemonInfo = myTeam[0]
			enemyInformation = turnOutcomeInfo[1]; enemyTeam = enemyInformation[0]; enemyPokemonInfo = enemyTeam[0]
			myPokemonHP = myPokemonInfo[5]; enemyPokemonHP = enemyPokemonInfo[5]
			runLast=turnOutcomeInfo[2]; runLast=runLast[0]
			if int(runLast) > 0:
				print('You got away safely!')
				return 1
		myTeamTotalHP = int(getTeamTotalHP(myTeam)); enemyTeamTotalHP = int(getTeamTotalHP(enemyTeam))
		if myTeamTotalHP == 0:
			break
		if enemyTeamTotalHP == 0:
			break
		if myPokemonHP == 0:	
			print (myPokemon, 'fainted! Who would you like to switch to?')
			oldPokemon = myPokemon
			changePokemon = getSwitchPokemon(myTeam)
			myTeam = changePokemon[0]; change = changePokemon[1]
			if change == 0:
				roundOutcomeInfo = [myTeam,enemyTeam,run]
				return roundOutcomeInfo
			myPokemonInfo = myTeam[0]; myPokemon = myPokemonInfo[0]
			myPokemonHP = myPokemonInfo[2]
			print ('You switched from', oldPokemon, 'into', myPokemon + '!')
		if enemyPokemonHP == 0:
			print (enemyPokemon, 'fainted!')
			expOutcome = getExpOutcome(myPokemon,myPokemonLevel,myPokemonExperience,myPokemonMoveSet,enemyPokemon,enemyPokemonLevel)			
			myPokemonInfo[2] = expOutcome[0]; myPokemonInfo[6] = expOutcome[1]; myPokemonInfo[13] = expOutcome[2]; myPokemonInfo[0] = expOutcome[3]
			changePokemon = getRandomSwitchPokemon(enemyTeam)
			enemyTeam = changePokemon[0]; change = changePokemon[1]
			enemyPokemonInfo = enemyTeam[0]; enemyPokemon = enemyPokemonInfo[0]
			enemyPokemonHP = enemyPokemonInfo[5]
			print (enemyPlayerName, 'sent out', enemyPokemon + '!')
	myTeamTotalHP = getTeamTotalHP(myTeam)
	if myTeamTotalHP == 0:
		print('You whited out!')
	if enemyPokemonHP == 0:
		myPokemon = myPokemonInfo[0];myPokemonName = myPokemonInfo[1];myPokemonLevel = myPokemonInfo[2];myPokemonIV = myPokemonInfo[3];myPokemonEV = myPokemonInfo[4];myPokemonHP = myPokemonInfo[5];myPokemonExperience = myPokemonInfo[6];myPokemonForm = myPokemonInfo[7];myPokemonGender = myPokemonInfo[8];myPokemonAbility = myPokemonInfo[9];myPokemonTypeOne = myPokemonInfo[10];myPokemonTypeTwo = myPokemonInfo[11];myPokemonItem = myPokemonInfo[12];myPokemonMoveSet = myPokemonInfo[13];myPokemonMovePP = myPokemonInfo[14];myPokemonNVStatus = myPokemonInfo[15];myPokemonNVStatusCount = myPokemonInfo[16];myPokemonVStatus = myPokemonInfo[17];myPokemonVStatusCount = myPokemonInfo[18];myPokemonCurrentStatStage = myPokemonInfo[19]
		print('The wild', enemyPokemon, 'fainted! You win!')
		expOutcome = getExpOutcome(myPokemon,myPokemonLevel,myPokemonExperience,myPokemonMoveSet,enemyPokemon,enemyPokemonLevel)
		myPokemonInfo[2] = expOutcome[0]; myPokemonInfo[6] = expOutcome[1]; myPokemonInfo[13] = expOutcome[2]; myPokemonInfo[0] = expOutcome[3]
	return [myInformation,enemyInformation,environmentInformation]

def getExpOutcome(myPokemon,myPokemonLevel,myPokemonExp,myPokemonMoveSet,enemyPokemon,enemyPokemonLevel):
	expYield = getExpYield(enemyPokemon,enemyPokemonLevel)
	print(myPokemon, 'gained', expYield, 'exp!')
	myPokemonExp = myPokemonExp + expYield
	myPokemonNextLevel = getExp(myPokemon,myPokemonLevel+1)
	while myPokemonExp > myPokemonNextLevel:
		if myPokemonLevel == 100:
			return [myPokemon,myPokemonLevel,myPokemonExp,myPokemonMoveSet]
		pokemonMovesByLevel = getPokemonMovesByLevel(myPokemon)
		myPokemonLevel = myPokemonLevel+1
		print(myPokemon, 'went up one level and is now level', str(myPokemonLevel) + '!')
		if myPokemonLevel in pokemonMovesByLevel:
			newMove = pokemonMovesByLevel[myPokemonLevel]
			if len(myPokemonMoveSet) < 4:
				print(myPokemon, 'learnt', newMove + '!')
				myPokemonMoveSet.append(newMove)
			elif len(myPokemonMoveSet) > 3:
				print(myPokemon, 'wants to learn', newMove + '! Which move should be forgotton?')
				print(myPokemonMoveSet + ['Keep Current Moves'])
				moveInput = getMoveInput(myPokemonMoveSet + ['Keep Current Moves'])
				if moveInput != 'Keep Current Moves':
					print(myPokemon, 'forgot', moveInput, 'and learnt', newMove + '!')
					for n, i in enumerate(myPokemonMoveSet):
						if i == moveInput:
							myPokemonMoveSet[n] = newMove
				if moveInput == 'Keep Current Moves':
					print(myPokemon, 'did not learn', newMove + '.')
		myPokemonNextLevel = getExp(myPokemon,myPokemonLevel+1)
		pokemonEvolving = getPokemonEvolve(myPokemon,myPokemonLevel)
		if pokemonEvolving != 'No':
			oldPokemon = myPokemon; myPokemon = pokemonEvolving
			print(oldPokemon, 'just evolved into a', myPokemon + '!')
	return [myPokemonLevel,myPokemonExp,myPokemonMoveSet,myPokemon]

def startGame():
	print('Professor Oak: \n- Hello! Welcome to the wonderful world of Pokemon. My name is Professor Oak, it\'s great to meet you. What was your name again?')
	name = input(': ')
	print('Professor Oak: \n- Ah yes,', name + '. How could I forget?')
	input()
	print('- Woah now! You don\'t want to go into that long grass without a Pokemon! Come with me!')
	input()
	print('Gary: \n- Wahwahwah, I want one first!')
	input()
	print('Professor Oak: \n- Be patient, Gary!', name, 'is our guest. Go ahead and choose one of the balls in from of you. Will you choose:')
	print('Bulbasaur - the grass Pokemon. \nCharmander - the fire Pokemon. \nSquirtle - the water Pokemon.')
	myPokemonOne = getStarterInput()
	if myPokemonOne == 'Bulbasaur':
		enemyPokemonOne = 'Charmander'
	if myPokemonOne == 'Charmander':
		enemyPokemonOne = 'Squirtle'
	if myPokemonOne == 'Squirtle':
		enemyPokemonOne = 'Bulbasaur'
	myPokemonOneLevel = 5; myPokemonOneIV = getRandomIV(); myPokemonOneStatus = 0; myPokemonOneStatStage = [0,0,0,0,0,0,0]; myPokemonOneStatusCount = 0; myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage)
	enemyPokemonOneLevel = 5; enemyPokemonOneIV = getRandomIV(); enemyPokemonOneStatus = 0; enemyPokemonOneStatStage = [0,0,0,0,0,0,0]; enemyPokemonOneStatusCount = 0; enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneStatStage)
	myPokemonOneList = [myPokemonOne,myPokemonOneLevel,myPokemonOneHP,myPokemonOneIV,myPokemonOneStatus,myPokemonOneStatusCount,myPokemonOneStatStage]
	enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneHP,enemyPokemonOneIV,enemyPokemonOneStatus,enemyPokemonOneStatusCount,enemyPokemonOneStatStage]
	myTeam = [myPokemonOneList]
	enemyTeam = [enemyPokemonOneList]
	print('Gary: \n Fine, I choose', enemyPokemonOne + '! Let\'s fight!')
	input()
	startBattle(myTeam,enemyTeam,1)

def visitPokemonCenter(myInformation):
	print('Welcome to the Pokemon Center. Let\'s get your team healed up!')
	myTeam = myInformation[0]
	numberOfPokemon = len(myTeam)
	if numberOfPokemon > 0:
		myPokemonOneInfo = myTeam[0]
		myPokemonOne = myPokemonOneInfo[0];myPokemonOneName = myPokemonOneInfo[1];myPokemonOneLevel = myPokemonOneInfo[2];myPokemonOneIV = myPokemonOneInfo[3];myPokemonOneEV = myPokemonOneInfo[4];myPokemonOneHP = myPokemonOneInfo[5];myPokemonOneExperience = myPokemonOneInfo[6];myPokemonOneForm = myPokemonOneInfo[7];myPokemonOneGender = myPokemonOneInfo[8];myPokemonOneAbility = myPokemonOneInfo[9];myPokemonOneTypeOne = myPokemonOneInfo[10];myPokemonOneTypeTwo = myPokemonOneInfo[11];myPokemonOneItem = myPokemonOneInfo[12];myPokemonOneMoveSet = myPokemonOneInfo[13];myPokemonOneMovePP = myPokemonOneInfo[14];myPokemonOneNVStatus = myPokemonOneInfo[15];myPokemonOneNVStatusCount = myPokemonOneInfo[16];myPokemonOneVStatus = myPokemonOneInfo[17];myPokemonOneVStatusCount = myPokemonOneInfo[18];myPokemonOneCurrentStatStage = myPokemonOneInfo[19];myPokemonOneMaxHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
		myPokemonOneInfo[5] = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
		myTeam[0] = myPokemonOneInfo 
	if numberOfPokemon > 1:
		myPokemonTwoInfo = myTeam[1]
		myPokemonTwo = myPokemonTwoInfo[0];myPokemonTwoName = myPokemonTwoInfo[1];myPokemonTwoLevel = myPokemonTwoInfo[2];myPokemonTwoIV = myPokemonTwoInfo[3];myPokemonTwoEV = myPokemonTwoInfo[4];myPokemonTwoHP = myPokemonTwoInfo[5];myPokemonTwoExperience = myPokemonTwoInfo[6];myPokemonTwoForm = myPokemonTwoInfo[7];myPokemonTwoGender = myPokemonTwoInfo[8];myPokemonTwoAbility = myPokemonTwoInfo[9];myPokemonTwoTypeOne = myPokemonTwoInfo[10];myPokemonTwoTypeTwo = myPokemonTwoInfo[11];myPokemonTwoItem = myPokemonTwoInfo[12];myPokemonTwoMoveSet = myPokemonTwoInfo[13];myPokemonTwoMovePP = myPokemonTwoInfo[14];myPokemonTwoNVStatus = myPokemonTwoInfo[15];myPokemonTwoNVStatusCount = myPokemonTwoInfo[16];myPokemonTwoVStatus = myPokemonTwoInfo[17];myPokemonTwoVStatusCount = myPokemonTwoInfo[18];myPokemonTwoCurrentStatStage = myPokemonTwoInfo[19];myPokemonTwoMaxHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
		myPokemonTwoInfo[5] = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV)
		myTeam[1] = myPokemonTwoInfo
	if numberOfPokemon > 2:
		myPokemonThreeInfo = myTeam[2]	
		myPokemonThree = myPokemonThreeInfo[0];myPokemonThreeName = myPokemonThreeInfo[1];myPokemonThreeLevel = myPokemonThreeInfo[2];myPokemonThreeIV = myPokemonThreeInfo[3];myPokemonThreeEV = myPokemonThreeInfo[4];myPokemonThreeHP = myPokemonThreeInfo[5];myPokemonThreeExperience = myPokemonThreeInfo[6];myPokemonThreeForm = myPokemonThreeInfo[7];myPokemonThreeGender = myPokemonThreeInfo[8];myPokemonThreeAbility = myPokemonThreeInfo[9];myPokemonThreeTypeOne = myPokemonThreeInfo[10];myPokemonThreeTypeTwo = myPokemonThreeInfo[11];myPokemonThreeItem = myPokemonThreeInfo[12];myPokemonThreeMoveSet = myPokemonThreeInfo[13];myPokemonThreeMovePP = myPokemonThreeInfo[14];myPokemonThreeNVStatus = myPokemonThreeInfo[15];myPokemonThreeNVStatusCount = myPokemonThreeInfo[16];myPokemonThreeVStatus = myPokemonThreeInfo[17];myPokemonThreeVStatusCount = myPokemonThreeInfo[18];myPokemonThreeCurrentStatStage = myPokemonThreeInfo[19];myPokemonThreeMaxHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
		myPokemonThreeInfo[5] = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV)
		myTeam[2] = myPokemonThreeInfo
	if numberOfPokemon > 3:
		myPokemonFourInfo = myTeam[3]
		myPokemonFour = myPokemonFourInfo[0];myPokemonFourName = myPokemonFourInfo[1];myPokemonFourLevel = myPokemonFourInfo[2];myPokemonFourIV = myPokemonFourInfo[3];myPokemonFourEV = myPokemonFourInfo[4];myPokemonFourHP = myPokemonFourInfo[5];myPokemonFourExperience = myPokemonFourInfo[6];myPokemonFourForm = myPokemonFourInfo[7];myPokemonFourGender = myPokemonFourInfo[8];myPokemonFourAbility = myPokemonFourInfo[9];myPokemonFourTypeOne = myPokemonFourInfo[10];myPokemonFourTypeTwo = myPokemonFourInfo[11];myPokemonFourItem = myPokemonFourInfo[12];myPokemonFourMoveSet = myPokemonFourInfo[13];myPokemonFourMovePP = myPokemonFourInfo[14];myPokemonFourNVStatus = myPokemonFourInfo[15];myPokemonFourNVStatusCount = myPokemonFourInfo[16];myPokemonFourVStatus = myPokemonFourInfo[17];myPokemonFourVStatusCount = myPokemonFourInfo[18];myPokemonFourCurrentStatStage = myPokemonFourInfo[19];myPokemonFourMaxHP = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
		myPokemonFourInfo[5] = gethpStat(myPokemonFour,myPokemonFourLevel,myPokemonFourIV)
		myTeam[3] = myPokemonFourInfo
	if numberOfPokemon > 4:
		myPokemonFiveInfo = myTeam[4]
		myPokemonFive = myPokemonFiveInfo[0];myPokemonFiveName = myPokemonFiveInfo[1];myPokemonFiveLevel = myPokemonFiveInfo[2];myPokemonFiveIV = myPokemonFiveInfo[3];myPokemonFiveEV = myPokemonFiveInfo[4];myPokemonFiveHP = myPokemonFiveInfo[5];myPokemonFiveExperience = myPokemonFiveInfo[6];myPokemonFiveForm = myPokemonFiveInfo[7];myPokemonFiveGender = myPokemonFiveInfo[8];myPokemonFiveAbility = myPokemonFiveInfo[9];myPokemonFiveTypeOne = myPokemonFiveInfo[10];myPokemonFiveTypeTwo = myPokemonFiveInfo[11];myPokemonFiveItem = myPokemonFiveInfo[12];myPokemonFiveMoveSet = myPokemonFiveInfo[13];myPokemonFiveMovePP = myPokemonFiveInfo[14];myPokemonFiveNVStatus = myPokemonFiveInfo[15];myPokemonFiveNVStatusCount = myPokemonFiveInfo[16];myPokemonFiveVStatus = myPokemonFiveInfo[17];myPokemonFiveVStatusCount = myPokemonFiveInfo[18];myPokemonFiveCurrentStatStage = myPokemonFiveInfo[19];myPokemonFiveMaxHP = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
		myPokemonFiveInfo[5] = gethpStat(myPokemonFive,myPokemonFiveLevel,myPokemonFiveIV)
		myTeam[4] = myPokemonFiveInfo
	if numberOfPokemon > 5:
		myPokemonSixInfo = myTeam[5]
		myPokemonSix = myPokemonSixInfo[0];myPokemonSixName = myPokemonSixInfo[1];myPokemonSixLevel = myPokemonSixInfo[2];myPokemonSixIV = myPokemonSixInfo[3];myPokemonSixEV = myPokemonSixInfo[4];myPokemonSixHP = myPokemonSixInfo[5];myPokemonSixExperience = myPokemonSixInfo[6];myPokemonSixForm = myPokemonSixInfo[7];myPokemonSixGender = myPokemonSixInfo[8];myPokemonSixAbility = myPokemonSixInfo[9];myPokemonSixTypeOne = myPokemonSixInfo[10];myPokemonSixTypeTwo = myPokemonSixInfo[11];myPokemonSixItem = myPokemonSixInfo[12];myPokemonSixMoveSet = myPokemonSixInfo[13];myPokemonSixMovePP = myPokemonSixInfo[14];myPokemonSixNVStatus = myPokemonSixInfo[15];myPokemonSixNVStatusCount = myPokemonSixInfo[16];myPokemonSixVStatus = myPokemonSixInfo[17];myPokemonSixVStatusCount = myPokemonSixInfo[18];myPokemonSixCurrentStatStage = myPokemonSixInfo[19];myPokemonSixMaxHP = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
		myPokemonSixInfo[5] = gethpStat(myPokemonSix,myPokemonSixLevel,myPokemonSixIV)
		myTeam[5] = myPokemonSixInfo
	print('All healed! We hope to see you again!')
	myInformation[0] = myTeam
	return myInformation

def chooseGameplay():
	print('> To begin the game as normal, type 1\n> For a preset battle, type 2\n> Gym Leader Challenge, type 3\n> Wild Pokemon Hunt, type 4')
	x = input()
	if x == '1':
		startGame()
	if x == '2':
		myPokemonOne = 'Squirtle'; myPokemonOneLevel = 100; myPokemonOneIV = getRandomIV(); myPokemonOneStatus = 0; myPokemonOneStatStage = [0,0,0,0,0,0,0]; myPokemonOneStatusCount = 0; myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV,myPokemonOneStatStage); myPokemonOneExp = getExp(myPokemonOne,myPokemonOneLevel)
		myPokemonTwo = 'Charmander'; myPokemonTwoLevel = 50; myPokemonTwoIV = getRandomIV(); myPokemonTwoStatus = 0; myPokemonTwoStatStage = [0,0,0,0,0,0,0]; myPokemonTwoStatusCount = 0; myPokemonTwoHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage); myPokemonTwoExp = getExp(myPokemonTwo,myPokemonTwoLevel)
		myPokemonThree = 'Bulbasaur'; myPokemonThreeLevel = 19; myPokemonThreeIV = getRandomIV(); myPokemonThreeStatus = 0; myPokemonThreeStatStage = [0,0,0,0,0,0,0]; myPokemonThreeStatusCount = 0; myPokemonThreeHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage); myPokemonThreeExp = getExp(myPokemonThree,myPokemonThreeLevel)
		enemyPokemonOne = 'Venusaur'; enemyPokemonOneLevel = 100; enemyPokemonOneIV = getRandomIV(); enemyPokemonOneStatus = 0; enemyPokemonOneStatStage = [0,0,0,0,0,0,0]; enemyPokemonOneStatusCount = 0; enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneStatStage)
		enemyPokemonTwo = 'Ivysaur'; enemyPokemonTwoLevel = 50; enemyPokemonTwoIV = getRandomIV(); enemyPokemonTwoStatus = 0; enemyPokemonTwoStatStage = [0,0,0,0,0,0,0]; enemyPokemonTwoStatusCount = 0; enemyPokemonTwoHP = gethpStat(enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoIV,enemyPokemonTwoStatStage)
		myPokemonOneList = [myPokemonOne,myPokemonOneLevel,myPokemonOneHP,myPokemonOneIV,myPokemonOneStatus,myPokemonOneStatusCount,myPokemonOneStatStage,myPokemonOneExp]
		myPokemonTwoList = [myPokemonTwo,myPokemonTwoLevel,myPokemonTwoHP,myPokemonTwoIV,myPokemonTwoStatus,myPokemonTwoStatusCount,myPokemonTwoStatStage,myPokemonTwoExp]
		myPokemonThreeList = [myPokemonThree,myPokemonThreeLevel,myPokemonThreeHP,myPokemonThreeIV,myPokemonThreeStatus,myPokemonThreeStatusCount,myPokemonThreeStatStage,myPokemonThreeExp]
		enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneHP,enemyPokemonOneIV,enemyPokemonOneStatus,enemyPokemonOneStatusCount,enemyPokemonOneStatStage]
		enemyPokemonTwoList = [enemyPokemonTwo,enemyPokemonTwoLevel,enemyPokemonTwoHP,enemyPokemonTwoIV,enemyPokemonTwoStatus,enemyPokemonTwoStatusCount,enemyPokemonTwoStatStage]
		myTeam = [myPokemonOneList,myPokemonTwoList,myPokemonThreeList]
		enemyTeam = [enemyPokemonOneList,enemyPokemonTwoList]
		myTrainerInfo = [1]
		enemyTrainerInfo = ['Trainer','Jimbo','opposing']
		startBattle(myTeam,enemyTeam,myTrainerInfo,enemyTrainerInfo)
	if x == '3':
		myPokemonOne = 'Bulbasaur'
		myPokemonOneName = 'Bulba'
		myPokemonOneLevel = 15
		myPokemonOneIV = [31,31,31,31,31,31]
		myPokemonOneEV = 'xxx'
		myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
		myPokemonOneExperience = getExp(myPokemonOne,myPokemonOneLevel)
		myPokemonOneForm = 'NA'
		myPokemonOneGender = 'Male'
		myPokemonOneAbility = 'Chloraphyll'
		myPokemonOneTypeOne = 'Grass'
		myPokemonOneTypeTwo = 'Poison'
		myPokemonOneItem = 'None'
		myPokemonOneMoveSet = ['Tackle', 'Vine Whip', 'Tail Whip','Sand Attack']
		myPokemonOneMovePP = [10, 10, 10]
		myPokemonOneNVStatus = 0
		myPokemonOneNVStatusCount = 0
		myPokemonOneVStatus = 0
		myPokemonOneVStatusCount = 0
		myPokemonOneCurrentStatStage = [0,0,0,0,0,0,0]
		
		myPokemonOneList = [myPokemonOne,myPokemonOneName,myPokemonOneLevel,myPokemonOneIV,myPokemonOneEV,myPokemonOneHP,myPokemonOneExperience,myPokemonOneForm,myPokemonOneGender,myPokemonOneAbility,myPokemonOneTypeOne,myPokemonOneTypeTwo,myPokemonOneItem,myPokemonOneMoveSet,myPokemonOneMovePP,myPokemonOneNVStatus,myPokemonOneNVStatusCount,myPokemonOneVStatus,myPokemonOneVStatusCount,myPokemonOneCurrentStatStage]
		myPokemonTwoList = [myPokemonOne,myPokemonOneName,myPokemonOneLevel,myPokemonOneIV,myPokemonOneEV,myPokemonOneHP,myPokemonOneExperience,myPokemonOneForm,myPokemonOneGender,myPokemonOneAbility,myPokemonOneTypeOne,myPokemonOneTypeTwo,myPokemonOneItem,myPokemonOneMoveSet,myPokemonOneMovePP,myPokemonOneNVStatus,myPokemonOneNVStatusCount,myPokemonOneVStatus,myPokemonOneVStatusCount,myPokemonOneCurrentStatStage]
		#myPokemonTwo = 'Bulbasaur'; myPokemonTwoLevel = 13; myPokemonTwoIV = getRandomIV(); myPokemonTwoStatus = 0; myPokemonTwoStatStage = [0,0,0,0,0,0,0]; myPokemonTwoStatusCount = 0; myPokemonTwoHP = gethpStat(myPokemonTwo,myPokemonTwoLevel,myPokemonTwoIV,myPokemonTwoStatStage); myPokemonTwoExp = getExp(myPokemonTwo,myPokemonTwoLevel); myPokemonTwoMoveSet = ['Tackle','Growl','Vine Whip']
		#myPokemonThree = 'Squirtle'; myPokemonThreeLevel = 13; myPokemonThreeIV = getRandomIV(); myPokemonThreeStatus = 0; myPokemonThreeStatStage = [0,0,0,0,0,0,0]; myPokemonThreeStatusCount = 0; myPokemonThreeHP = gethpStat(myPokemonThree,myPokemonThreeLevel,myPokemonThreeIV,myPokemonThreeStatStage); myPokemonThreeExp = getExp(myPokemonThree,myPokemonThreeLevel); myPokemonThreeMoveSet = ['Tackle','Growl','Bubble']

		enemyPokemonOne = 'Charmander'
		enemyPokemonOneName = 'Bulba'
		enemyPokemonOneLevel = 16
		enemyPokemonOneIV = [31,31,31,31,31,31]
		enemyPokemonOneEV = 'xxx'
		enemyPokemonOneHP = 1
		#enemyPokemonOneHP = gethpStat(enemyPokemonOne,enemyPokemonOneLevel,enemyPokemonOneIV)
		enemyPokemonOneExperience = 800
		enemyPokemonOneForm = 'NA'
		enemyPokemonOneGender = 'Male'
		enemyPokemonOneAbility = 'Chloraphyll'
		enemyPokemonOneTypeOne = 'Grass'
		enemyPokemonOneTypeTwo = 'Poison'
		enemyPokemonOneItem = 'None'
		enemyPokemonOneMoveSet = ['Tackle', 'Vine Whip', 'Defense Curl']
		enemyPokemonOneMovePP = [10, 10, 10]
		enemyPokemonOneNVStatus = 0
		enemyPokemonOneNVStatusCount = 0
		enemyPokemonOneVStatus = 0
		enemyPokemonOneVStatusCount = 0
		enemyPokemonOneCurrentStatStage = [0,0,0,0,0,0,0]

		enemyPokemonOneList = [enemyPokemonOne,enemyPokemonOneName,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneEV,enemyPokemonOneHP,enemyPokemonOneExperience,enemyPokemonOneForm,enemyPokemonOneGender,enemyPokemonOneAbility,enemyPokemonOneTypeOne,enemyPokemonOneTypeTwo,enemyPokemonOneItem,enemyPokemonOneMoveSet,enemyPokemonOneMovePP,enemyPokemonOneNVStatus,enemyPokemonOneNVStatusCount,enemyPokemonOneVStatus,enemyPokemonOneVStatusCount,enemyPokemonOneCurrentStatStage]
		enemyPokemonTwoList = [enemyPokemonOne,enemyPokemonOneName,enemyPokemonOneLevel,enemyPokemonOneIV,enemyPokemonOneEV,enemyPokemonOneHP,enemyPokemonOneExperience,enemyPokemonOneForm,enemyPokemonOneGender,enemyPokemonOneAbility,enemyPokemonOneTypeOne,enemyPokemonOneTypeTwo,enemyPokemonOneItem,enemyPokemonOneMoveSet,enemyPokemonOneMovePP,enemyPokemonOneNVStatus,enemyPokemonOneNVStatusCount,enemyPokemonOneVStatus,enemyPokemonOneVStatusCount,enemyPokemonOneCurrentStatStage]



		myTeam = [myPokemonOneList,myPokemonTwoList]
		myBalls = [[5,'PokeBall'],[3,'Great Ball'],[1,'Ultra Ball']]
		myMedicine = [[2,'Potion']]

		myBag = [myBalls,myMedicine]; enemyBag = [0,0];
		myPlayer = [0,0]; enemyPlayer = ['Wild','wild']
		environmentInformation = [0,0]
		enemyTeam = [enemyPokemonOneList,enemyPokemonTwoList]
		myTrainerInfo = [1]
		enemyTrainerInfo = ['Trainer','Brock','gym leader\'s']


		myInformation=[myTeam,myBag,myPlayer]; enemyInformation=[enemyTeam,enemyBag,enemyPlayer]
		startBattle(myInformation,enemyInformation,environmentInformation)
	if x == '4':
		print('Who would you like to start with? \n 1 - Bulbasaur \n 2 - Charmander \n 3 - Squirtle')
		myPokemonOne = getStarterInput()
		myPokemonOneName = myPokemonOne
		myPokemonOneLevel = 5
		myPokemonOneIV = getRandomIV()
		myPokemonOneEV = 'xxx'
		myPokemonOneHP = gethpStat(myPokemonOne,myPokemonOneLevel,myPokemonOneIV)
		myPokemonOneExperience = getExp(myPokemonOne,myPokemonOneLevel)
		myPokemonOneForm = 'NA'
		myPokemonOneGender = 'Male'
		myPokemonOneAbility = 'NA'
		myPokemonOneTypeOne = getPokemonTypeOne(myPokemonOne)
		myPokemonOneTypeTwo = getPokemonTypeTwo(myPokemonOne)
		myPokemonOneItem = 'None'
		myPokemonOneMoveSet = getMoveSet(myPokemonOne,myPokemonOneLevel)
		myPokemonOneMovePP = [10, 10]
		myPokemonOneNVStatus = 0
		myPokemonOneNVStatusCount = 0
		myPokemonOneVStatus = 0
		myPokemonOneVStatusCount = 0
		myPokemonOneCurrentStatStage = [0,0,0,0,0,0,0]		
		
		myPokemonOneList = [myPokemonOne,myPokemonOneName,myPokemonOneLevel,myPokemonOneIV,myPokemonOneEV,myPokemonOneHP,myPokemonOneExperience,myPokemonOneForm,myPokemonOneGender,myPokemonOneAbility,myPokemonOneTypeOne,myPokemonOneTypeTwo,myPokemonOneItem,myPokemonOneMoveSet,myPokemonOneMovePP,myPokemonOneNVStatus,myPokemonOneNVStatusCount,myPokemonOneVStatus,myPokemonOneVStatusCount,myPokemonOneCurrentStatStage]
		location = 'Route Two'
		enemyInformation = getWildEnemyInformation(location)
		myBalls = [[5,'PokeBall'],[3,'Great Ball'],[1,'Ultra Ball']]
		myMedicine = [[2,'Potion']]
		myBag = [myBalls,myMedicine]; enemyBag = [0,0];
		myPlayer = [0,0];
		environmentInformation = [0,0]

		myTrainerInfo = [1]

		myTeam = [myPokemonOneList]; 
		myInformation=[myTeam,myBag,myPlayer];
		while True:
			battleOutcome = startBattle(myInformation,enemyInformation,environmentInformation)
			print('\n')
			enemyInformation = getWildEnemyInformation(location)
			healedteam = visitPokemonCenter(myInformation)
			print('\n')








chooseGameplay()

location = 'Route Two'

getWildLevelByLocation(location)
getWildPokemonByLocation(location)


