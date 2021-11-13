#nameInfo = ['Name','Type','Category','Power','Accuracy','PP','Description','Target','Priority','TurnsToComplete','multiAttack','multiAttackMin','multiAttackMax','nvEffect','nvEffectChance','vEffect','vEffectChance','statEffect','statEffectChance','critStageBonus','AttackOnMoveNumber','GrantImmunity','CauseFlinch',FlinchChance,healthsteal,
absorbInfo = ['Absorb','Grass','Special',20,100,25,'User recovers half the HP inflicted on opponent.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
acidInfo = ['Acid','Poison','Special',40,100,30,'May lower opponent\'s Special Defense.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,-1,0,0,0,0],33,0,0,0,0,0,0]
acidArmorInfo = ['Acid Armor','Poison','Status', 0, 10000,20,'Sharply raises user\'s Defense.','Self',0,1,0,0,0,0,0,0,0,[0,0,2,0,0,0,0,0,0],100,0,0,0,0,0,0]
agilityInfo = ['Agility','Psychic','Status', 0, 10000,30,'Sharply raises user\'s Speed.','Self',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,2,0,0,0],100,0,0,0,0,0,0]
amnesiaInfo = ['Amnesia','Psychic','Status', 0, 10000,20,'Sharply raises user\'s Special Defense.','Self',0,1,0,0,0,0,0,0,0,[0,0,0,0,2,0,0,0,0],100,0,0,0,0,0,0]
auroraBeamInfo = ['Aurora Beam','Ice','Special',65,100,20,'May lower opponent\'s Attack.','Enemy',0,1,0,0,0,0,0,0,0,[0,-1,0,0,0,0,0,0,0],0,0,0,0,0,0,0]
barrageInfo = ['Barrage','Normal','Physical',15,85,20,'Hits 2-5 times in one turn.','Enemy',0,1,1,2,5,0,0,0,0,0,0,0,0,0,0,0,0]
barrierInfo = ['Barrier','Psychic','Status', 0, 10000,20,'Sharply raises user\'s Defense.','Self',0,1,0,0,0,0,0,0,0,[0,0,2,0,0,0,0,0,0],100,0,0,0,0,0,0]
bideInfo = ['Bide','Normal','Physical', 0, 10000,10,'User takes damage for two turns then strikes back double.','Enemy',0,3,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0]
bindInfo = ['Bind','Normal','Physical',15,85,20,'Traps opponent; damaging them for 4-5 turns.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
biteInfo = ['Bite','Dark','Physical',60,100,25,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
blizzardInfo = ['Blizzard','Ice','Special',110,70,5,'May freeze opponent.','Enemy',0,1,0,0,0,4,10,0,0,0,0,0,0,0,0,0,0]
bodySlamInfo = ['Body Slam','Normal','Physical',85,100,15,'May paralyze opponent.','Enemy',0,1,0,0,0,2,30,0,0,0,0,0,0,0,0,0,0]
boneClubInfo = ['Bone Club','Ground','Physical',65,85,20,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
bonemerangInfo = ['Bonemerang','Ground','Physical',50,90,10,'Hits twice in one turn.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bubbleInfo = ['Bubble','Water','Special',40,100,30,'May lower opponent\'s Speed.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,-1,0,0,0],33,0,0,0,0,0,0]
bubbleBeamInfo = ['Bubble Beam','Water','Special',65,100,20,'May lower opponent\'s Speed.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,-1,0,0,0],33,0,0,0,0,0,0]
clampInfo = ['Clamp','Water','Physical',35,85,10,'Traps opponent; damaging them for 4-5 turns.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cometPunchInfo = ['Comet Punch','Normal','Physical',18,85,15,'Hits 2-5 times in one turn.','Enemy',0,1,1,2,5,0,0,0,0,0,0,0,0,0,0,0,0]
confuseRayInfo = ['Confuse Ray','Ghost','Status', 0,100,10,'Confuses opponent.','Enemy',0,1,0,0,0,0,0,1,100,0,0,0,0,0,0,0,0]
confusionInfo = ['Confusion','Psychic','Special',50,100,25,'May confuse opponent.','Enemy',0,1,0,0,0,0,0,1,10,0,0,0,0,0,0,0,0]
constrictInfo = ['Constrict','Normal','Physical',10,100,35,'May lower opponent\'s Speed by one stage.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,-1,0,0,0],33,0,0,0,0,0,0]
conversionInfo = ['Conversion','Normal','Status', 0, 10000,30,'Changes user\'s type to that of its first move.','Self',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
counterInfo = ['Counter','Fighting','Physical', 0,100,20,'When hit by a Physical Attack; user strikes back with 2x power.','Enemy',-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
crabhammerInfo = ['Crabhammer','Water','Physical',100,90,10,'High critical hit ratio.','Enemy',0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
cutInfo = ['Cut','Normal','Physical',50,95,30,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
defenseCurlInfo = ['Defense Curl','Normal','Status',0,10000,40,'Raises user\'s Defense.','Self',0,1,0,0,0,0,0,0,0,[0,0,1,0,0,0,0,0,0],100,0,0,0,0,0,0]
digInfo = ['Dig','Ground','Physical',80,100,10,'Digs underground on first turn; attacks on second. Can also escape from caves.','Enemy',0,2,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0]
disableInfo = ['Disable','Normal','Status', 0,100,20,'Opponent can\'t use its last attack for a few turns.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dizzyPunchInfo = ['Dizzy Punch','Normal','Physical',70,100,10,'May confuse opponent.','Enemy',0,1,0,0,0,0,0,1,20,0,0,0,0,0,0,0,0]
doubleKickInfo = ['Double Kick','Fighting','Physical',30,100,30,'Hits twice in one turn.','Enemy',0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0]
doubleSlapInfo = ['Double Slap','Normal','Physical',15,85,10,'Hits 2-5 times in one turn.','Enemy',0,1,1,2,5,0,0,0,0,0,0,0,0,0,0,0,0]
doubleTeamInfo = ['Double Team','Normal','Status', 0, 10000,15,'Raises user\'s Evasiveness.','Self',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,0,0,1,0],100,0,0,0,0,0,0]
doubleEdgeInfo = ['Double-Edge','Normal','Physical',120,100,15,'User receives recoil damage.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dragonRageInfo = ['Dragon Rage','Dragon','Special', 0,100,10,'Always inflicts 40 HP.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dreamEaterInfo = ['Dream Eater','Psychic','Special',100,100,15,'User recovers half the HP inflicted on a sleeping opponent.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
drillPeckInfo = ['Drill Peck','Flying','Physical',80,100,20,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
earthquakeInfo = ['Earthquake','Ground','Physical',100,100,10,'Power is doubled if opponent is underground from using Dig.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
eggBombInfo = ['Egg Bomb','Normal','Physical',100,75,10,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
emberInfo = ['Ember','Fire','Special',40,100,25,'May burn opponent.','Enemy',0,1,0,0,0,1,10,0,0,0,0,0,0,0,0,0,0]
explosionInfo = ['Explosion','Normal','Physical',250,100,5,'User faints.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fireBlastInfo = ['Fire Blast','Fire','Special',110,85,5,'May burn opponent.','Enemy',0,1,0,0,0,1,30,0,0,0,0,0,0,0,0,0,0]
firePunchInfo = ['Fire Punch','Fire','Physical',75,100,15,'May burn opponent.','Enemy',0,1,0,0,0,1,10,0,0,0,0,0,0,0,0,0,0]
fireSpinInfo = ['Fire Spin','Fire','Special',35,85,15,'Traps opponent; damaging them for 4-5 turns.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fissureInfo = ['Fissure','Ground','Physical', 1000000, 30,5,'One-Hit-KO; if it hits.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
flamethrowerInfo = ['Flamethrower','Fire','Special',90,100,15,'May burn opponent.','Enemy',0,1,0,0,0,1,10,0,0,0,0,0,0,0,0,0,0]
flashInfo = ['Flash','Normal','Status', 0,100,20,'Lowers opponent\'s Accuracy.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,0,-1,0,0],100,0,0,0,0,0,0]
flyInfo = ['Fly','Flying','Physical',90,95,15,'Flies up on first turn; attacks on second turn.','Enemy',0,2,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0]
focusEnergyInfo = ['Focus Energy','Normal','Status', 0, 10000,30,'Increases critical hit ratio.','Self',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,0,0,0,1],100,0,0,0,0,0,0]
furyAttackInfo = ['Fury Attack','Normal','Physical',15,85,20,'Hits 2-5 times in one turn.','Enemy',0,1,1,2,5,0,0,0,0,0,0,0,0,0,0,0,0]
furySwipesInfo = ['Fury Swipes','Normal','Physical',18,80,15,'Hits 2-5 times in one turn.','Enemy',0,1,1,2,5,0,0,0,0,0,0,0,0,0,0,0,0]
glareInfo = ['Glare','Normal','Status', 0,100,30,'Paralyzes opponent.','Enemy',0,1,0,0,0,2,100,0,0,0,0,0,0,0,0,0,0]
growlInfo = ['Growl','Normal','Status', 0,100,40,'Lowers opponent\'s Attack.','Enemy',0,1,0,0,0,0,0,0,0,[0,-1,0,0,0,0,0,0,0],100,0,0,0,0,0,0]
growthInfo = ['Growth','Normal','Status', 0, 10000,40,'Raises user\'s Attack and Special Attack.','Self',0,1,0,0,0,0,0,0,0,[0,1,0,1,0,0,0,0,0],100,0,0,0,0,0,0]
guillotineInfo = ['Guillotine','Normal','Physical', 1000000, 30,5,'One-Hit-KO; if it hits.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
gustInfo = ['Gust','Flying','Special',40,100,35,'Hits Pokémon using Fly/Bounce with double power.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hardenInfo = ['Harden','Normal','Status', 0, 10000,30,'Raises user\'s Defense.','Self',0,1,0,0,0,0,0,0,0,[0,0,1,0,0,0,0,0,0],100,0,0,0,0,0,0]
hazeInfo = ['Haze','Ice','Status', 0, 10000,30,'Resets all stat changes.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
headbuttInfo = ['Headbutt','Normal','Physical',70,100,15,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
highJumpKickInfo = ['High Jump Kick','Fighting','Physical',130,90,10,'If it misses; the user loses half their HP.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hornAttackInfo = ['Horn Attack','Normal','Physical',65,100,25,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hornDrillInfo = ['Horn Drill','Normal','Physical', 1000000, 30,5,'One-Hit-KO; if it hits.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hydroPumpInfo = ['Hydro Pump','Water','Special',110,80,5,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hyperBeamInfo = ['Hyper Beam','Normal','Special',150,90,5,'User must recharge next turn.','Enemy',0,2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
hyperFangInfo = ['Hyper Fang','Normal','Physical',80,90,15,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
hypnosisInfo = ['Hypnosis','Psychic','Status', 0,60,20,'Puts opponent to sleep.','Enemy',0,1,0,0,0,3,100,0,0,0,0,0,0,0,0,0,0]
iceBeamInfo = ['Ice Beam','Ice','Special',90,100,10,'May freeze opponent.','Enemy',0,1,0,0,0,4,10,0,0,0,0,0,0,0,0,0,0]
icePunchInfo = ['Ice Punch','Ice','Physical',75,100,15,'May freeze opponent.','Enemy',0,1,0,0,0,4,10,0,0,0,0,0,0,0,0,0,0]
jumpKickInfo = ['Jump Kick','Fighting','Physical',100,95,10,'If it misses; the user loses half their HP.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
karateChopInfo = ['Karate Chop','Fighting','Physical',50,100,25,'High critical hit ratio.','Enemy',0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
kinesisInfo = ['Kinesis','Psychic','Status', 0,80,15,'Lowers opponent\'s Accuracy.','Enemy',0,1,0,0,0,0,0,0,0,[0,-1,0,0,0,0,0,0,0],100,0,0,0,0,0,0]
leechLifeInfo = ['Leech Life','Bug','Physical',80,100,10,'User recovers half the HP inflicted on opponent.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
leechSeedInfo = ['Leech Seed','Grass','Status', 0,90,10,'Drains HP from opponent each turn.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
leerInfo = ['Leer','Normal','Status', 0,100,30,'Lowers opponent\'s Defense.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,-1,0,0,0,0,0,0],100,0,0,0,0,0,0]
lickInfo = ['Lick','Ghost','Physical',30,100,30,'May paralyze opponent.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lightScreenInfo = ['Light Screen','Psychic','Status', 0, 10000,30,'Halves damage from Special attacks for 5 turns.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lovelyKissInfo = ['Lovely Kiss','Normal','Status', 0,75,10,'Puts opponent to sleep.','Enemy',0,1,0,0,0,3,100,0,0,0,0,0,0,0,0,0,0]
lowKickInfo = ['Low Kick','Fighting','Physical', 50,90,20,'Chance to flinch.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,30,0]
meditateInfo = ['Meditate','Psychic','Status', 0, 10000,40,'Raises user\'s Attack.','Self',0,1,0,0,0,0,0,0,0,[0,1,0,0,0,0,0,0,0],100,0,0,0,0,0,0]
megaDrainInfo = ['Mega Drain','Grass','Special',40,100,15,'User recovers half the HP inflicted on opponent.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
megaKickInfo = ['Mega Kick','Normal','Physical',120,75,5,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
megaPunchInfo = ['Mega Punch','Normal','Physical',80,85,20,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
metronomeInfo = ['Metronome','Normal','Status', 0, 10000,10,'User performs almost any move in the game at random.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mimicInfo = ['Mimic','Normal','Status', 0, 10000,10,'Copies the opponent\'s last move.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
minimizeInfo = ['Minimize','Normal','Status', 0, 10000,10,'Sharply raises user\'s Evasiveness.','Self',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,0,0,2,0],100,0,0,0,0,0,0]
mirrorMoveInfo = ['Mirror Move','Flying','Status', 0, 10000,20,'User performs the opponent\'s last move.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mistInfo = ['Mist','Ice','Status', 0, 10000,30,'User\'s stats cannot be changed for a period of time.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nightShadeInfo = ['Night Shade','Ghost','Special', 0,100,15,'Inflicts damage equal to user\'s level.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
payDayInfo = ['Pay Day','Normal','Physical',40,100,20,'A small amount of money is gained after the battle resolves.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
peckInfo = ['Peck','Flying','Physical',35,100,35,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
petalDanceInfo = ['Petal Dance','Grass','Special',120,100,10,'User attacks for 2-3 turns but then becomes confused.','Enemy',0,3,0,0,0,0,0,0,0,0,0,0,'All',0,0,0,0]
pinMissileInfo = ['Pin Missile','Bug','Physical',25,95,20,'Hits 2-5 times in one turn.','Enemy',0,1,1,2,5,0,0,0,0,0,0,0,0,0,0,0,0]
poisonGasInfo = ['Poison Gas','Poison','Status', 0,90,40,'Poisons opponent.','Enemy',0,1,0,0,0,5,100,0,0,0,0,0,0,0,0,0,0]
poisonPowderInfo = ['Poison Powder','Poison','Status', 0,75,35,'Poisons opponent.','Enemy',0,1,0,0,0,5,100,0,0,0,0,0,0,0,0,0,0]
poisonStingInfo = ['Poison Sting','Poison','Physical',15,100,35,'May poison the opponent.','Enemy',0,1,0,0,0,5,20,0,0,0,0,0,0,0,0,0,0]
poundInfo = ['Pound','Normal','Physical',40,100,35,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
psybeamInfo = ['Psybeam','Psychic','Special',65,100,20,'May confuse opponent.','Enemy',0,1,0,0,0,0,0,1,10,0,0,0,0,0,0,0,0]
psychicInfo = ['Psychic','Psychic','Special',90,100,10,'May lower opponent\'s Special Defense.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,-1,0,0,0,0],33,0,0,0,0,0,0]
psywaveInfo = ['Psywave','Psychic','Special', 0,80,15,'Inflicts damage 50-150% of user\'s level.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
quickAttackInfo = ['Quick Attack','Normal','Physical',40,100,30,'User attacks first.','Enemy',1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rageInfo = ['Rage','Normal','Physical',20,100,20,'Raises user\'s Attack when hit.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
razorLeafInfo = ['Razor Leaf','Grass','Physical',55,95,25,'High critical hit ratio.','Enemy',0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
razorWindInfo = ['Razor Wind','Normal','Special',80,100,10,'Charges on first turn; attacks on second. High critical hit ratio.','Enemy',0,2,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0]
recoverInfo = ['Recover','Normal','Status', 0, 10000,10,'User recovers half its max HP.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reflectInfo = ['Reflect','Psychic','Status', 0, 10000,20,'Halves damage from Physical attacks for 5 turns.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
restInfo = ['Rest','Psychic','Status', 0, 10000,10,'User sleeps for 2 turns; but user is fully healed.','Self',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
roarInfo = ['Roar','Normal','Status', 0, 10000,20,'In battles; the opponent switches. In the wild; the Pokémon runs.','Enemy',-6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rockSlideInfo = ['Rock Slide','Rock','Physical',75,90,10,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
rockThrowInfo = ['Rock Throw','Rock','Physical',50,90,15,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rollingKickInfo = ['Rolling Kick','Fighting','Physical',60,85,15,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
sandAttackInfo = ['Sand Attack','Ground','Status', 0,100,15,'Lowers opponent\'s Accuracy.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,0,-1,0,0],100,0,0,0,0,0,0]
scratchInfo = ['Scratch','Normal','Physical',40,100,35,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
screechInfo = ['Screech','Normal','Status', 0,85,40,'Sharply lowers opponent\'s Defense.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,-2,0,0,0,0,0,0],100,0,0,0,0,0,0]
seismicTossInfo = ['Seismic Toss','Fighting','Physical', 0,100,20,'Inflicts damage equal to user\'s level.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
selfDestructInfo = ['Self-Destruct','Normal','Physical',200,100,5,'User faints.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sharpenInfo = ['Sharpen','Normal','Status', 0, 10000,30,'Raises user\'s Attack.','Self',0,1,0,0,0,0,0,0,0,[0,1,0,0,0,0,0,0,0],100,0,0,0,0,0,0]
singInfo = ['Sing','Normal','Status', 0,55,15,'Puts opponent to sleep.','Enemy',0,1,0,0,0,3,100,0,0,0,0,0,0,0,0,0,0]
skullBashInfo = ['Skull Bash','Normal','Physical',130,100,10,'Raises Defense on first turn; attacks on second.','Enemy',0,2,0,0,0,0,0,0,0,[0,0,1,0,0,0,0,0,0],100,0,2,0,0,0,0]
skyAttackInfo = ['Sky Attack','Flying','Physical',140,90,5,'Charges on first turn; attacks on second. May cause flinching.','Enemy',0,2,0,0,0,0,0,0,0,0,0,0,2,0,1,10,0]
slamInfo = ['Slam','Normal','Physical',80,75,20,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
slashInfo = ['Slash','Normal','Physical',70,100,20,'High critical hit ratio.','Enemy',0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
sleepPowderInfo = ['Sleep Powder','Grass','Status', 0,75,15,'Puts opponent to sleep.','Enemy',0,1,0,0,0,3,100,0,0,0,0,0,0,0,0,0,0]
sludgeInfo = ['Sludge','Poison','Special',65,100,20,'May poison opponent.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
smogInfo = ['Smog','Poison','Special',30,70,20,'May poison opponent.','Enemy',0,1,0,0,0,5,50,0,0,0,0,0,0,0,0,0,0]
smokescreenInfo = ['Smokescreen','Normal','Status', 0,100,20,'Lowers opponent\'s Accuracy.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,0,-1,0,0],100,0,0,0,0,0,0]
softBoiledInfo = ['Soft-Boiled','Normal','Status', 0, 10000,10,'User recovers half its max HP.','Self',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
solarBeamInfo = ['Solar Beam','Grass','Special',120,100,10,'Charges on first turn; attacks on second.','Enemy',0,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0]
sonicBoomInfo = ['Sonic Boom','Normal','Special', 0,90,20,'Always inflicts 20 HP.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
spikeCannonInfo = ['Spike Cannon','Normal','Physical',20,100,15,'Hits 2-5 times in one turn.','Enemy',0,1,1,2,5,0,0,0,0,0,0,0,0,0,0,0,0]
splashInfo = ['Splash','Normal','Status', 0, 10000,40,'Doesn\'t do ANYTHING.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sporeInfo = ['Spore','Grass','Status', 0,100,15,'Puts opponent to sleep.','Enemy',0,1,0,0,0,3,100,0,0,0,0,0,0,0,0,0,0]
stompInfo = ['Stomp','Normal','Physical',65,100,20,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
strengthInfo = ['Strength','Normal','Physical',80,100,15,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stringShotInfo = ['String Shot','Bug','Status', 0,95,40,'Sharply lowers opponent\'s Speed.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,0,0,0,-2,0,0,0],100,0,0,0,0,0,0]
struggleInfo = ['Struggle','Normal','Physical',50,100, 0,'Only usable when all PP are gone. Hurts the user.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stunSporeInfo = ['Stun Spore','Grass','Status', 0,75,30,'Paralyzes opponent.','Enemy',0,1,0,0,0,2,100,0,0,0,0,0,0,0,0,0,0]
submissionInfo = ['Submission','Fighting','Physical',80,80,20,'User receives recoil damage.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
substituteInfo = ['Substitute','Normal','Status', 0, 10000,10,'Uses HP to creates a decoy that takes hits.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
superFangInfo = ['Super Fang','Normal','Physical', 0,90,10,'Always takes off half of the opponent\'s HP.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
supersonicInfo = ['Supersonic','Normal','Status', 0,55,20,'Confuses opponent.','Enemy',0,1,0,0,0,0,0,1,100,0,0,0,0,0,0,0,0]
surfInfo = ['Surf','Water','Special',90,100,15,'Hits all adjacent Pokémon.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
swiftInfo = ['Swift','Normal','Special',60,10000,20,'Ignores Accuracy and Evasiveness.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
swordsDanceInfo = ['Swords Dance','Normal','Status', 0, 10000,20,'Sharply raises user\'s Attack.','Self',0,1,0,0,0,0,0,0,0,[0,2,0,0,0,0,0,0,0],100,0,0,0,0,0,0]
tackleInfo = ['Tackle','Normal','Physical',40,100,35,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tailWhipInfo = ['Tail Whip','Normal','Status', 0,100,30,'Lowers opponent\'s Defense.','Enemy',0,1,0,0,0,0,0,0,0,[0,0,-1,0,0,0,0,0,0],100,0,0,0,0,0,0]
takeDownInfo = ['Take Down','Normal','Physical',90,85,20,'User receives recoil damage.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
teleportInfo = ['Teleport','Psychic','Status', 0, 10000,20,'Allows user to flee wild battles; also warps player to last PokéCenter.','Enemy',-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
thrashInfo = ['Thrash','Normal','Physical',120,100,10,'User attacks for 2-3 turns but then becomes confused.','Enemy',0,3,0,0,0,0,0,0,0,0,0,0,'All',0,0,0,0]
thunderInfo = ['Thunder','Electric','Special',110,70,10,'May paralyze opponent.','Enemy',0,1,0,0,0,2,10,0,0,0,0,0,0,0,0,0,0]
thunderPunchInfo = ['Thunder Punch','Electric','Physical',75,100,15,'May paralyze opponent.','Enemy',0,1,0,0,0,2,10,0,0,0,0,0,0,0,0,0,0]
thunderShockInfo = ['Thunder Shock','Electric','Special',40,100,30,'May paralyze opponent.','Enemy',0,1,0,0,0,2,10,0,0,0,0,0,0,0,0,0,0]
thunderWaveInfo = ['Thunder Wave','Electric','Status', 0,90,20,'Paralyzes opponent.','Enemy',0,1,0,0,0,2,100,0,0,0,0,0,0,0,0,0,0]
thunderboltInfo = ['Thunderbolt','Electric','Special',90,100,15,'May paralyze opponent.','Enemy',0,1,0,0,0,2,10,0,0,0,0,0,0,0,0,0,0]
toxicInfo = ['Toxic','Poison','Status', 0,90,10,'Badly poisons opponent.','Enemy',0,1,0,0,0,6,100,0,0,0,0,0,0,0,0,0,0]
transformInfo = ['Transform','Normal','Status', 0, 10000,10,'User takes on the form and attacks of the opponent.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
triAttackInfo = ['Tri Attack','Normal','Special',80,100,10,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
twineedleInfo = ['Twineedle','Bug','Physical',25,100,20,'Hits twice in one turn. May poison opponent.','Enemy',0,1,1,2,2,5,20,0,0,0,0,0,0,0,0,0,0]
viceGripInfo = ['Vice Grip','Normal','Physical',55,100,30,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
vineWhipInfo = ['Vine Whip','Grass','Physical',45,100,25,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
waterGunInfo = ['Water Gun','Water','Special',40,100,25,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
waterfallInfo = ['Waterfall','Water','Physical',80,100,15,'May cause flinching.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0]
whirlwindInfo = ['Whirlwind','Normal','Status', 0, 100,20,'In battles; the opponent switches. In the wild; the Pokémon runs.','Enemy',-6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
wingAttackInfo = ['Wing Attack','Flying','Physical',60,100,35,'','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
withdrawInfo = ['Withdraw','Water','Status', 0, 10000,40,'Raises user\'s Defense.','Self',0,1,0,0,0,0,0,0,0,[0,0,1,0,0,0,0,0,0],100,0,0,0,0,0,0]
wrapInfo = ['Wrap','Normal','Physical',15,90,20,'Traps opponent; damaging them for 4-5 turns.','Enemy',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

noneInfo = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

allMoveList = ['Absorb','Acid','Acid Armor','Agility','Amnesia','Aurora Beam','Barrage','Barrier','Bide','Bind','Bite','Blizzard','Body Slam','Bone Club','Bonemerang','Bubble','Bubble Beam','Clamp','Comet Punch','Confuse Ray','Confusion','Constrict','Conversion','Crabhammer','Cut','Defense Curl','Dig','Disable','Dizzy Punch','Double Kick','Double Slap','Double Team','Double-Edge','Dragon Rage','Dream Eater','Drill Peck','Earthquake','Egg Bomb','Ember','Explosion','Fire Blast','Fire Punch','Fire Spin','Fissure','Flamethrower','Flash','Fly','Focus Energy','Fury Attack','Fury Swipes','Glare','Growl','Growth','Guillotine','Gust','Harden','Haze','Headbutt','High Jump Kick','Horn Attack','Horn Drill','Hydro Pump','Hyper Beam','Hyper Fang','Hypnosis','Ice Beam','Ice Punch','Jump Kick','Karate Chop','Kinesis','Leech Life','Leech Seed','Leer','Lick','Light Screen','Lovely Kiss','Low Kick','Meditate','Mega Drain','Mega Kick','Mega Punch','Metronome','Mimic','Minimize','Mirror Move','Mist','Night Shade','Pay Day','Peck','Petal Dance','Pin Missile','Poison Gas','Poison Powder','Poison Sting','Pound','Psybeam','Psychic','Psywave','Quick Attack','Rage','Razor Leaf','Razor Wind','Recover','Reflect','Rest','Roar','Rock Slide','Rock Throw','Rolling Kick','Sand Attack','Scratch','Screech','Seismic Toss','Self-Destruct','Sharpen','Sing','Skull Bash','Sky Attack','Slam','Slash','Sleep Powder','Sludge','Smog','Smokescreen','Soft-Boiled','Solar Beam','Sonic Boom','Spike Cannon','Splash','Spore','Stomp','Strength','String Shot','Struggle','Stun Spore','Submission','Substitute','Super Fang','Supersonic','Surf','Swift','Swords Dance','Tackle','Tail Whip','Take Down','Teleport','Thrash','Thunder','Thunder Punch','Thunder Shock','Thunder Wave','Thunderbolt','Toxic','Transform','Tri Attack','Twineedle','Vice Grip','Vine Whip','Water Gun','Waterfall','Whirlwind','Wing Attack','Withdraw','Wrap']

hitSelfConfusionInfo =  ['Hit Self','Typeless','Physical',40,10000,10000,'Hit self in confusion.','Self',0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


#Option 1 > As it is currently, full names split by line
#|------------------------------------------------------|
#| 1 > Poison Powder - 20/20 PP                         |
#| 2 | High Jump Kick - 35/35 PP                        |
#| 3 | Thunder Punch - 20/20 PP                         |
#| 4 | Self-Destruct - 30/30 PP                         |
#| 5 | Back                                             |
#\------------------------------------------------------/
#
#Option 1 > Another example with shorter names
#|------------------------------------------------------|
#| 1 > Tail Whip - 20/20 PP                             |
#| 2 | Tackle - 35/35 PP                                |
#| 3 | Bide - 20/20 PP                                  |
#| 4 | Struggle - 30/30 PP                              |
#| 5 | Back                                             |
#\------------------------------------------------------/
#
#////////////////////////////////////////////////////////
#
#Option 2 > Change to game logic, certain moves will need 
#		   to be edited to 12 chars as below
#|------------------------------------------------------|
#| 1 > PoisonPowder 18/20PP  | 2 - Hi-Jump Kick 18/20PP |
#| 3 | ThunderPunch 20/20PP  | 4 - SelfDestruct 35/35PP |
#| 5 | Back                                             |
#\------------------------------------------------------/
#
#Option 2 > Another example with shorter names
#|------------------------------------------------------|
#| 1 > Tail Whip 18/20PP     | 2 - Tackle 18/20PP       |
#| 3 | Bide 20/20PP          | 4 - Struggle 35/35PP     |
#| 5 | Back                                             |
#\------------------------------------------------------/
#
#////////////////////////////////////////////////////////
#
#Option 3, similar to 2 but PP gets pushed to end 
#|------------------------------------------------------|
#| 1 > PoisonPowder 18/20PP  | 2 - Hi-Jump Kick 18/20PP |
#| 3 | ThunderPunch 20/20PP  | 4 - SelfDestruct 35/35PP |
#| 5 | Back                                             |
#\------------------------------------------------------/
#
#Option 3, similar to 2 but PP gets pushed to end 
#|------------------------------------------------------|	
#| 1 > Tail Whip     18/20PP | 2 - Tackle       18/20PP |
#| 3 | Bide          20/20PP | 4 - Struggle     35/35PP |
#| 5 | Back                                             |
#\------------------------------------------------------/
#
#
#High Jump Kick
#Poison Powder
#Self-Destruct
#Thunder Punch
#Thunder Shock