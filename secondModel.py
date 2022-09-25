import numpy as np
import tf as tf
from keras import Sequential
from keras.layers import Dense
from keras.models import load_model


y_train = np.array([-0.65, -0.32, 0.145, 0.17, -0.22, 1.035, 1.365, 1.245, 0.805,
                    0.57, 0.26, 0.56, -0.105,
                    -0.32, -0.17, 0.545, 1.19,
                    1.475, 2.195, 1.54, 1.96, 10.335, -1.01, -0.39
])

x_train = np.array(
[[0.0, 0.0, 0.0, 0.0, 0.42685761653592336, 0.5807125305348753, 0.09612310808585497, 0.04214427040456111, 0.0, 0.0013937425348582715, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.006232278724903658, 0.0, 0.0, 0.0, -0.0003094841340972523, 0.00417562297147366, -0.0102509588077064, 0.013606590466067863, 0.008597883597883601, 0.0013160076280109992, 0.010525622735885304, 0.09658122171033245, 0.0, 0.01132137077597593, -0.005238036945613436, 0.016497255364008395, 0.0, -0.0026360878396776517, -0.0041477117899454035], [0.0005734054838686218, 0.0003459828184578509, -0.021969598599028382, 0.03624876996517968, -0.002292780129702247, 0.016940348974209648, -0.000923006603960933, -0.03494208061650948, 0.058175189581237456, 0.010263649512256938, -0.004331358559176259, 9.780148942622263e-05, 0.025516105069308057, 0.01639400018745956, -0.004272458125714921, 0.0013103536159139947, 0.034609935643126914, 0.0008755908722808567, -0.007522110353016354, 0.011471227917015745, 0.005457195322358913, -0.004123322424905812, 0.005432125975213557, -0.013176462009879793, 0.0005534863021510809, 0.002940802542041212, 0.09094827586206897, 0.0031295825629011776, -0.004738501842637111, -0.0020408163265306124, 0.015002735813096264], [0.04522582308289236, 0.009603887559696536, 0.0025772088360361293, 0.0666597798766603, 0.017151130341045328, 0.0004556497266159487, 0.0028569477800033808, 0.005180460065191698, 0.014976607382211389, 0.05781104475628178, 0.01917614255944065, 0.0032910564902755837, 0.002099920614872659, 0.00374041959996423, -0.0068243327493260975, 0.09442578949796464, -0.017972926814062967, 0.03517972567203969, 0.041192730520866694, -0.002217091608451506, -0.004175653382990916, 0.004649613794557043, 0.007181634636872936, 0.004067702453033842, -0.0050142359877106595, 0.004311993679453383, -0.001657179985133453, 0.005492875163164979, 0.0025526831892111073, -0.005400891273001069, -0.0039213145295970715], [0.02505001752722102, -0.0516793879185651, 0.0, 0.010355704826229505, -0.008272126443519835, 0.0019452166659632497, -0.027510719119692703, 0.032308054370723926, 0.021034980248293138, -0.0018483751284971185, 0.0016717514133630011, 0.00911031464520935, -0.009188092869295183, -0.004062893054920153, 0.0, 0.009205195357682808, 0.0, 0.03182751210142254, 0.0, 0.0, 0.01760495990361972, 0.013036475136232158, 0.007158601189355874, 0.0013586104239302337, 0.0026295364257793237, 0.001149743407173736, -0.007539170100720337, 0.0567865481203937, -0.02153062668861519, 0.000517345223199039, 0.007406055591864849], [0.0013524822550488964, 0.02587309204145044, 0.0087295653216201, -0.024109330559836308, 0.0, 0.0038270940178001833, -0.002476025098245617, 0.0, 0.0013056922643139004, 0.006386318139476268, 0.0, 0.0, 0.0012120899850344387, 0.007359906577921287, -0.004008038814047327, 0.0, 0.012537316771745303, 0.0, 0.0, -0.005160249259318572, -0.008464956808116098, 0.0691318625600567, 0.00018945887662586794, 0.0011650195189924642, 0.001007418416677501, -0.001401040236308752, -0.010454448706233573, -0.03766582371964417, 0.0, 0.0, -0.005425817010402429], [0.0, 0.008505506270653987, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.014879666717040696, 0.0067147069359371975, 0.02381625477953576, 0.031082018452599575, 0.03325961648293747, 0.006754301195542821, 0.0017452807437044564, -0.00020590117130251293, 0.0007719411608173844, 0.004106675012084325, -0.001698127864184719, 0.0, 0.0, 0.0, 0.006875687568756876, -0.00363601917559165, -0.00023245002324499985], [-0.0071877646068869705, 4.7757665140074194e-05, 0.0, 0.0, 0.009294214096974156, 0.0013567922937226748, -0.0007340461854749947, 0.0, -0.019276379464772436, 0.01921139134842096, 0.0, 0.0, 0.0, 0.018270791571547942, -0.004175765601654137, -0.0231761575015442, -0.0018401587993975457, 0.00139496621463094, 0.0003730650591895705, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0011906280284696028, -0.1575324248767018, -0.005695959655030219, 0.0038500690422154293, 0.0, 0.0, 0.0, 0.0, -0.0007825810575574797, 0.00021958717610891622, -0.00015856065028916163, -0.0007648858554954095, 0.0, 0.0, 0.0, 0.0, 0.0012379364456649722, 0.0, 0.00210970464135021, 0.06896153439991552, 0.0, 0.0, -7.74423600745755e-05, 0.0, 0.0, -0.0006989683396660812], [0.017072471723851793, 0.0, 0.0, 0.0, 6.389776357826893e-05, 0.0, 0.0, 0.0, 0.0, 0.0, -0.010840108401084007, 0.0005981145924929441, -0.001025641025641022, 0.0, 0.008783058117400475, 0.035015896578315636, 0.040527703640077135, -0.004016482139490317, 0.041693578911384935, 0.07341647079160621, 0.0, 0.04312426616967338, 0.01206707450559561, 0.0028239635940192887, 0.0, 0.0022710816512439146, 0.010789465695559945, 0.0, 0.0, 0.016253185357542065, 0.0033529595907967028], [-9.683082929483681e-05, -0.16619392626343799, 0.0, 0.0, 0.17284933288718363, 0.0, 0.0, 0.0012488234859352489, 0.002946186279625669, -0.0025506279439705586, -0.00017377952385740103, 0.009755486160125894, 0.0, 0.0012299269431466978, 0.0, 0.005708678603102946, 0.020440322218540027, 0.007005013476800071, 0.0, 0.0, 0.0031314474057325533, 0.01130964455501614, -0.004929650354546697, 0.0, -0.001550825397813614, 0.006673794606419223, 0.0, 0.0, 0.00618116033820636, -0.0015649388581112221, 0.07398756581417239], [0.0, 0.05824197650370916, 0.06660822700234471, 0.0, 0.0, 0.08331758212500605, 0.0, 0.0, 0.041740506311880914, 0.0, 0.0, 0.0, 0.0, -0.16313250260820988, 0.008822767360247456, -0.01541641534691307, -0.006392256749872645, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.009677027274339048, 0.0, 0.0, -0.008832931200470538, 0.1063317940430841, 0.02029192091216647], [0.028985288339930797, 0.0, 0.002341468168676075, 0.003317570456708508, 0.006824463711055532, 0.00015074429998116018, 0.0, 0.0, 0.0, 0.0, 0.0, -0.008129266165864962, 0.0, 0.0, 0.015459886125351915, 0.0, 0.0, -0.008669244473394417, 0.0, 0.0, 0.0, 0.0, 0.013188004330949589, 0.005806985520501618, 0.0, 0.0, 0.06892251629588173, 0.0, 0.0, 0.0, 0.0036926064265883378], [0.0, 0.0, 0.0035402474521855957, 0.0, -0.0714285714285714, 0.0, -0.0638887080284911, 0.0, -0.007733480391373806, -0.0024886269564964847, -0.005778034589723474, 0.0064750934138530685, 0.045548503033632066, 0.0, 0.0007630553959685997, -0.021078928914660084, 0.0, 0.0, 0.0014756228639353358, 0.0, 0.0, 0.028524824013555036, 0.033825448210989095, 0.007702638998055245, 0.0, 0.0, 0.0, -0.0096432465382466, -0.0019878330409259294, 0.04782598478096177, 0.035240472237154374], [0.056182255465882756, 0.027842501690519016, 0.017534486487702047, 0.002158629596333499, 0.03620653310400704, -0.005882473618077501, 0.020222379517655018, 0.030082100175469546, 0.034035837481149016, -0.0025349923554488785, 0.0, 0.024504644036246078, 0.00792771093962688, 0.0, 0.07300618591701305, 0.0, -0.11668867439562777, 0.0, 0.05482803578303031, 0.009101005903102909, -0.12111009986050222, -0.000286368843069873, 0.0, 0.24520514610545563, -0.20321035399475085, -0.01140112027399071, -0.20473199852014878, 0.061733791576519564, 0.10445646820798896, -0.13922560956425498, 0.0], [0.23071115512734064, 0.015288361078639366, 0.0, 0.15388922387802562, -0.025775960021884065, -0.0027976296479784012, 0.003860876685218839, -0.002664957955983672, -0.0006692252338690408, 0.003176098430382005, -0.02279706042618409, 0.0, -0.010876722250109726, 0.0, -0.0013091717683316035, -0.004232392791097047, 0.24544326300951635, 0.08938988512354305, 0.008370012701990179, 0.000545447691212995, 0.0688218130092167, -0.1866818883844208, 0.0033393851931210953, -0.004643883434669087, 0.006230870875196506, 0.001982299609734224, -0.20000001155968872, 0.12424699566761899, -0.012777929997342391, 0.00021786492374727592, 0.007944262754740583], [0.016625349320984483, 0.02153889857477528, -0.01341380214915544, -0.14621842385669903, 0.0, 0.0, 0.005847953216374213, -0.0968578301723345, 0.0, 0.0, 0.0, 0.0, -0.050496342788203995, 0.01920534944751956, -0.07640221493902158, 0.11415881314508433, -0.1597163778676606, 0.0, 0.042672136579536835, 0.09843406375090459, -0.036008862113532325, -0.202933139793665, 0.0, 0.0, 0.0, 0.0, -0.0009071493177736367, 0.012118380062305367, 0.0, 0.0010820644737863001, 0.0], [0.0, 0.021254296978495565, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.02460625856750121, 0.007860681485129441, -0.03346717811645775, -0.186580827932436, 0.0, -0.026404008456020964, 0.23721784138427218, -0.014091108973787347, 0.0031552733245663878, 0.003173875437296567, -0.017306964934640002, 0.0, 0.0, -0.019167866064518077, 0.0, 0.00036692678596054383, 0.07218434044231525, 0.0, -0.020606688917136507, 0.0024380344503540574, -0.0036385688295936932, 0.0, -0.1810003356911234], [0.19612193362193361, -0.0008048607741523162, 0.044669758140226806, -0.016589643808696253, 0.0010260381263907492, 0.09000228681248372, -0.12713472485768496, -0.0119429754563527, -0.0027080634418754634, -0.19999999999999996, -0.0033783783783783994, -0.00219780219780219, 0.0, 0.2282993197278912, 0.002868480725623568, 0.02687651331719132, 0.07739182187160513, 0.0, -0.056177650146829405, -0.02370618586477341, 0.014031774877198653, 0.0, 0.003548160156126523, 0.004754302757305151, 0.0, 0.06818181818181812, 0.034537998205818266, 0.0, 0.0, 0.017636113357655737, -0.004380485501576883], [0.004409196816229499, 0.013809925972577908, 0.0, 0.0, -0.005988023952095856, 0.008488541243632188, -0.052664117460466016, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.04153148957839835, -0.013605442176870763, 0.010892983699503894, 0.024307287533286887, 0.7397260273972603, 0.00421940928270037, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.003620964732598153, -0.0065316675749325205, 0.0663738880637091, -0.014399209760687834, 0.023457514571695252, 0.022034499853021878, 0.0, 0.0035460992907800915, 0.025042511688853186, 0.0029653459683947614, 0.0268788364981473, 0.04101518241559021, 0.0, 0.013232125435885358, -0.018338204833626616, 0.0, 0.02777777777777768, 0.06052422360522911, -0.026176369578185404], [0.0, -0.0470374678738808, -0.0035457739922889107, 0.0, 0.0, 0.00027574745088868036, 0.0, 0.0, -0.0017636684303351524, 0.0, 0.0, 0.01041666666666663, -0.010903426791277204, 0.008602150537634357, 0.19083969465648853, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
print(x_train.shape[1])
model = Sequential()
model.add(Dense(32, activation='linear', input_shape=(x_train.shape[1],)))
model.add(Dense(64, activation='linear'))
model.add(Dense(1, activation='linear'))  # sigmoid, т.к. данные от 0 до 1

print(model.summary())  # архитектура нашей модели

model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

history = model.fit(x_train,
                    y_train,
                    epochs=800,
                    validation_split=0.8,
                    verbose=2
                    )

def pred(a):
    x = np.array([a])
    return (model.predict(x))


x_test = np.array([[-0.0007978189942379131, -0.009429876023820508, 0.0, 0.0, 0.017144701938990838, 0.02847267158282298, 0.0, 0.30408198519593294, -0.06997978753702855, 0.7655632420690028, -0.21143347813331032, 0.03247941911068711, -0.12870477640177921, 0.27075097387979064, -0.06121916756102717, -0.1875868481356801, -0.2009573192380553, 0.019942635363181707, -0.0060110422764099326, -0.10363855381213825, -0.15630252946669132, 0.15176597219120053, -0.6276219786089974, 0.03704369067845382, 0.1746523520165635, -0.04003480296350936, -0.004666057199137134, -0.1971088847324206, -0.062099277321618705, -0.026788900180061293, 0.1446700027559711], [-0.005707344169547873, -0.15742252770000656, 0.0, -0.10349686065764725, 0.43114905394641295, 0.2385350017700993, 0.20691222385471456, 0.04424784401185, 713.2708475868053, 0.3414365519497024, 0.19479329379302346, 0.3293084781845786, 2.5145393428390697, 1.4163322328155792, 17.346667249656814, 4.196493507724686, 0.17941411246229197, 0.7327634495079874, 0.40108940186402553, 0.09810174103999407, 0.11673340372694582, 0.00446437367198219, 0.025685322340795704, 0.0, 0.4048315902425508, 0.21796099948065262, 0.29206236134787583, 0.027526802006174193, 2.8673984914356523, 0.2812235169272548, 0.7236818046748902], [0.5048210604975742, 1.1334590080310463, 0.2886121726433248, 0.16891213034858277, 0.16015335855727617, 3.501685485497524, 0.15768165700691567, 0.20471861213533707, 0.037329705621117454, 0.013507449088928383, 0.040703910009316994, -0.0020689233368122307, 0.33221326509559185, 0.09189812200106044, 0.018893155148109655, 0.012427050513317365, 0.05846562206720745, 0.08109309199750828, 0.0011623191062259792, -0.006702150945233022, 0.18946142607972047, 0.09932690270805059, 0.025823319767634998, 0.10268799240321924, 0.12306655645489456, 0.27285617954990204, 0.1465825949613309, 0.12489916630846105, 0.0, 0.08958096782186002, 0.08404717575036467], [0.10633262235785979, 0.061808578540017936, 0.039403165967703976, 0.06686692901631927, 0.492675975778371, 0.43989793036752256, 0.1537551503421959, 0.4657774606313483, 0.3552804756992581, 0.054785567604208205, 0.02913537887316942, 0.011671023664187288, 2290.5476248102805, 351.12213613991617, 0.22028885281725322, 241.7318823947893, 338.8631840847512, 448.27547189146094, 1854.6734774925703, 0.1426169467054325, -0.04938637822349724, 0.06724423224456699, -0.0058807943666201, 225.6613199647444, 0.14567424446059368, -0.012585585960789403, 0.15972240881923497, -0.03637481727779888, 0.12110198501104442, -0.03323973442519219, 0.017118184536016375], [0.1151637331730248, 593.7771975480952, 0.018558223655976477, 3.5740626698495297, 0.09105590454364329, 0.05366097020492581, -0.042034933880239114, 1117.7537670736533, -0.0061606263017526895, 511.97868725375355, 4898.695468490298, 0.0, 6264.361336677274, 291.1512514905801, 808.0675517618691, 1.0779734693779122, 0.11731034851782911, -0.008221951374778696, 0.06428672898486588, 0.10665258731955014, 0.09367010551975319, -0.0038422021955306675, 0.023727548295249867, -0.09428570259437223, 0.0, -0.021850866623550638, 0.007124426828646968, 0.019949843685846912, -0.02954278619493395, -0.01934206420388864, 4.208194932915488], [-0.044154389529694325, 0.0, -0.07944183060993362, 0.01198210625187007, 0.037034966549547146, 0.12863892894593462, 0.09278983481821405, 0.039425413072752616, -0.08802400583473681, 0.09951453280579452, 0.06291090526051024, 0.04196522506738765, 0.025193402278608786, 0.0, 0.03956674240755605, 0.466314887508544, 0.047232872822534196, 0.0075195602850810115, 0.0, 0.0691231070422652, 0.11075979552895329, 0.06041939054389597, 0.03337186593746063, 0.08459604452090166, 0.0, 0.17679352226994968, 0.058766916375936055, 0.048915401856283104, 0.08156303535643475, 0.05682165566577451, 0.09836948596243122], [0.0359016541928626, -0.07632224480936849, 0.0, 0.002172071680997268, 0.1253077338719659, 0.007835554080160963, -0.04121823828097631, -0.030611905977508402, 0.0, 0.0, 0.0, 0.05007736230238633, 0.0, 0.0, -0.03207177155919533, 0.12929620703377362, -0.017684290439806988, 0.016311908309666875, -0.004486183492317134, 0.20471085308945658, 0.0, 0.23325610000448824, 0.0, 0.0, 0.0824241389663251, 0.0, 0.10494245229776218, 0.0, 0.0, 0.0, 0.0], [0.038420087402856705, 0.02543003206918738, -0.005198270559928373, 0.0, 0.04362265761008247, 0.08875920550544754, 0.0, 0.005735931499445127, 0.03570866445920606, 0.016958661318726795, 0.23243723738474906, 0.04153139067146099, 0.0, 0.011903558823263384, -0.034623103586494494, 0.0, 0.0555406256055288, 0.0, -0.013844518409889373, 0.015988683383422127, 0.0, 0.04500499230592033, 0.025589999012954428, 0.0, -0.003926915361260908, 0.02060899665237353, 0.03327072722837233, 0.0, 0.0, 0.0, 0.049835432608851864], [0.036122212516228304, 0.06472604075335647, -0.025559757732892655, -0.07895130405373137, -0.05351046063881049, -0.027063207847109187, -0.03032058718764076, 0.05299822919313477, 0.01454355025203246, 0.004610089975563885, 0.034111102186242845, 0.09144066412937639, 0.030548669861811747, 0.05046712788243909, 0.015560352412367388, 0.057191765602113906, 0.033159880168091495, 0.0370017957315422, 0.021327964865611608, 0.015558515376929032, 0.02364693035999672, 0.0010656793677461035, 0.01205862748363356, 0.02435686467520338, 0.049308896932912294, 0.0, -0.016141141290970707, 0.0026412671291619377, 0.023618138727141042, 0.0369183573670127, -0.013170003773272487], [-0.011846739246450655, -0.01927914095890686, -0.0002315104920653547, 0.029829127995418977, 0.0210636104688476, 0.030238360334236405, 0.02572908319488132, -0.033546403838361695, 0.025334570654842823, 0.011471513312205067, 0.01606485021423735, 0.007056881742209672, 0.06689124543109402, 0.009817028951481191, 0.041179075611694954, 0.10164068169584364, 0.012129010412244729, 0.16213276968887, 0.04390855395936649, 0.06849042724686352, 0.011167116550836369, 4.4687749048048245e-05, 0.13358860155081687, 0.03612492662525865, 0.04574580264593469, 0.640670538972472, 0.23875354925232284, 0.035004933260723, 0.11609357124470776, 0.03023424429282226, 0.03847458240000256], [0.06337625064393575, 0.04933894836706996, 0.09658772946040944, 0.18625345319848494, 0.024429267684251185, 0.1493983379391011, 0.11599504889849943, -0.038707363982898535, 0.0, 0.0, 0.047020350415775736, 0.04764117954781878, 0.15636978731494672, 0.03208787706376288, 0.04737596963537414, 0.029553982306521287, 0.2227923102782819, -0.01005040617839418, 0.07387199947217339, 0.1384923327376605, 0.0003557749213701889, 0.018290960297411743, 0.2634111921944802, -0.06570399330105413, -0.014937128523816293, -0.003575710963799606, 0.0, 0.012042243985270984, 0.18609247968413598, 0.03355322406626507, 0.019989854278216045], [-0.02738298979606995, 0.04189082035718215, 0.24062225014275584, 0.229797649690116, 0.013533961443466034, 0.04528180898392611, 0.09816678861633173, 0.020744253800180953, 0.003922513923241007, 0.09176336365755414, 0.01844790272560772, 0.1133027480718292, 0.17029766851913047, 0.06050810807392563, -0.07229656255495286, 0.04621246801616801, -0.039933343189611406, 0.02894384857510862, -0.004558186731773914, -0.034262206860978923, 0.05922912785208306, 0.03860873963860882, 0.06754629157291615, 0.01639384911447052, 0.05233436784996287, 0.12934041920507966, 0.00013603897151242815, -0.07562434164959783, 0.012248806986063634, 0.01020982403989511, 0.020883843086241752], [0.04032881953395503, 0.08235951242997162, 0.042292067621881965, -0.056289942161847024, 0.016015972668696796, 0.03721692077930609, 0.08529801742597867, 0.046519117849651244, 0.04878299665454887, 0.13282153512290995, 0.05632626165693406, 0.06987633620930228, 0.1688946442148546, -0.014045896083390257, 0.12322535790978198, 0.03132780148070195, 0.07635162388262588, -0.03197749552600091, -0.014132064210532633, 0.006745850175275064, 0.04928488369791157, 0.01584674000645062, 0.0, -0.12853027918522053, 0.03460252960062144, 0.17399816950644076, 0.07714666101274419, 0.1274137669029408, 0.012428115245428207, 0.07078427666368625, 0.07764835152681775], [0.06217006319322925, 0.010000898234623369, -0.022285113184189815, 0.0894353901166896, -0.015227802932191364, 0.044159210457247224, 0.10833911838999766, 0.012277742309622499, -0.013566660238221754, 0.020917186770399113, 0.006976535780162433, 0.024736995026150704, 0.015789131651011274, -0.010330638899764337, -0.07931237183147818, 0.009041653776980527, 0.017351361599000012, 0.04860684138637097, 0.001461332841896414, -0.008645549005927494, -0.08249399276710216, 0.0, -0.0002619531322125111, 0.18225981523816795, 0.01418878045920336, 0.063853457871371, 0.013524440656691459, 0.11985020363968131, 0.091934939644757, 0.0010720753874572607, 0.05263002380939162], [0.14564464545869907, 0.09075149047323974, 0.16443143121140963, 0.04952790786827485, 0.05047804186345768, 0.0074180920323551535, -0.0008674722862214703, 0.11114732367396249, 0.004168103704805938, 0.04197600003374815, 0.13452292808918784, 0.009805866477323073, -0.0154062399682235, 0.006119356092071985, 0.014248271711667499, 0.016422134714958864, 0.03924953374662493, -0.0314587788445479, 0.006890360924678812, 0.03389326072396512, -0.11780708080051187, 0.05199884198597897, 0.025183367590387428, 0.041968675449528564, 0.07008184484024935, 0.10523945506379105, 0.06632871535917757, 0.04854843684222786, 0.08423788172488438, 0.04725576342920373, 0.00752935420251381], [0.04575022737063249, 0.029848227194560522, -0.051808978001436586, 0.04029055885478664, 0.08769441690401929, -0.013830672896401915, 0.04672320804388865, 0.015584660124689597, 0.06640553617512257, 0.08977154458228222, 0.09087280942543889, 0.46763711632064026, -0.007484047832752399, 0.16225799195441976, 0.21237198314778133, -0.12395494284152611, -0.10902165698572705, 0.10828027039314335, 0.09272192922062343, 0.07631935313328941, 0.03892724868016125, 0.048203961169270754, 0.05252994630701928, 0.026071236360426558, 0.011513051939747028, -0.011783144829029176, 0.022163613062640714, 0.1946107355633311, -0.008261237543633247, 0.3839383503492384, 0.03401523865376861], [0.04990860548189349, 0.11408587760567444, 0.021982177396154205, 0.015286082641741803, 0.002291715451728752, 0.21316534615319135, 0.03105259195686665, -0.020159534307149105, 0.023763701987240374, 0.034002612107569906, 0.01718375881446624, 0.02028303132412155, 0.03679912475544108, -0.06547707145598336, 0.009999056048914053, 0.1266392117679441, -0.003278129001213865, 0.13422552026077705, 0.07108092698542885, -0.016790045654641584, 0.06341839071351163, 0.05172170277674145, 0.001764344954197634, 0.004857250430422877, -0.0011129675280870384, 0.03441674023508707, 0.10711160257139592, -0.2493637557104166, 0.05966075171989292, 0.18720062505360036, 0.053773867980696936], [0.08183917936093894, 0.05637267210675975, 0.0025528405615384223, 0.044792879719517106, 0.005262475593296168, 0.02825201485209759, -0.001852400857556279, 0.010371181932319527, 0.005702181939090436, 0.0, 0.16943510586936722, -0.21668987229598685, 0.07876522529696231, 0.019936157421905052, 0.018795885254338958, 0.04298645605457077, 0.0438874271637982, 0.011213948569952921, 0.026383184597717033, 0.004933957227786515, 0.08447186809094435, 0.015133800185221572, 0.05234929475239458, 0.03032662082041426, 0.011145051140332837, -0.028878693062484515, 0.015705463476646878, -0.0031321186670934796, 0.17073278281295348, 0.15042530584830266, -0.06223840234979267], [-0.07957687577063897, -0.07813166156440193, -0.017933442260161716, 0.08422121622952625, 0.12585982947377605, 0.18868711561462062, -0.07364755209710032, -0.04564582801958664, 0.07146768809214923, 0.06876469797483332, 0.024014582639535202, 0.16480369961295482, 0.3392524969865677, -0.11235326001319346, 0.021169851530460283, 0.007649136771686266, 0.12824293419896932, 0.034019239016992275, -0.09859551546040311, 0.05017769045883743, -0.2499737287386283, 0.031122825173874717, 0.08675175526661762, 0.015800532599532985, 0.003163933656286594, -0.04834629876988364, 0.09512908904224004, 0.05514456352461027, 0.048291690955202485, -0.006843271428759861, 0.027327162605558012], [0.018314461674337573, 0.030884686029032826, 0.12220377405487196, 0.010321272032017393, -0.060807032779056594, 0.0642702551534373, -0.0009333732550224243, 0.04514477281125623, 0.05781841361654213, 0.1401090381178309, 0.03203198673626102, -0.10126495648032648, 0.11313220037360043, -0.008621803508058731, 0.029615809829025744, 0.051975415681457846, 0.06178604437332316, 0.0068875405583659136, -0.08092267869544031, 0.08729457208384721, 0.021570779545065984, 0.05319946587048508, 0.08085067569954478, 0.06990603073751046, 0.04995063919487717, 0.014967134860512132, 0.06475058054402526, 0.1395689322020219, 0.139265587138467, 0.07980087601906365, 0.10978800357485863], [0.09351456632174668, 0.26932437490140704, 0.38566966251530704, 0.19853783975631847, 0.10823315852719065, 0.18223240364278473, 0.10961685553039144, 0.11258533108787558, 0.140583227479357, 0.1713732379787189, 0.114367890493223, 0.06703959248411888, 0.12874903811267627, 0.0984899396639612, 0.06159895673400892, 0.2135500960170525, 0.4155757859294355, 0.053042471375806866, 0.02489516720239495, 0.029776579491589347, 0.04406807858669223, 0.028985020256978085, 8.65497889785946e-06, 0.02749480574787732, 0.01441969190673148, -0.00043474570019637815, 0.07208730983946288, 0.0015391361660248325, 0.002212742242261105, 0.010893051821792586, 0.0], [0.017693207044641415, 0.024675804080674667, 0.008539129761044206, 0.01535735035680236, 0.03493031798748766, 0.013086523137904352, 0.1425195339010344, 0.13743649916496245, 0.14330520244323267, -0.03328763040587721, 0.0, 0.06952487150398544, 0.33686994902461675, -0.0003196836988478557, -0.0062989065051200135, 0.00276097418543882, 0.02048610561972235, 0.027309695941885086, 0.0, 0.04518602046100525, 23.748396674883868, 0.005870054694248712, 0.02432187755488257, 0.014957002936785833, 0.06559049158216972, 0.012484569100940585, -0.03701831591781425, 0.00518135056841522, -0.0087045262729868, -0.009878501611970144, 0.006310912600630141], [-0.004259428612631804, 0.0008407675198893631, 0.028079521110916633, 0.010493916021712145, 0.01865587454833194, 0.04429662616415281, 0.011046164991046511, 0.02073483241027955, 0.00537838095747946, 0.012635838805078422, 0.03373758659248779, -0.018352015078127743, -0.024307582161476923, -0.0018492376322984886, 0.020226224420710984, 0.08021038931153367, 0.029947815044198158, 0.0493887887449661, -0.009754571307377453, -0.0010630177230996232, -0.02511548100129418, -0.04359094839018264, 0.003726813865330396, 0.014927367597341758, 0.019395091198636555, 0.04554577894139163, -0.016985092259623833, -0.015512094368233269, -0.02174724191162649, 0.010529834346395605, -0.003873040231962011], [0.0025218148564557187, 0.0, -0.0022334496054899153, 0.009573933372296402, 0.004855707533984915, 0.029852099446062423, 0.02562204574174377, 0.028419745388515737, 0.03327224835215246, 0.03223880465371911, 0.03706691825270212, -0.009962169317723197, 0.02166255646518905, 0.019685938437810507, 0.004312880950179456, 0.008753858685526628, -0.002753361488123051, 0.024237429273600102, -0.005060980855645566, 0.01305122830453504, 0.030258136626479686, 0.004496438941483388, -0.007379485343766978, -0.003528889094978441, -0.005535670831025649, -0.0001890758390057436, 0.010775500648243532, -0.011502078044588035, -0.005922969187040026, -0.007456287157922539, -0.004351037452750814]]
)
#print(model.evaluate(x_train, y_train))
print(pred(x_test[6]))
