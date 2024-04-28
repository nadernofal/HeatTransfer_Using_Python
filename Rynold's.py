#book: incropera Appendix A.4
co=[
{"temp":200 ,"Density" :1.6888 ,"Cp":1.045 ,"Vis":127 ,"kyn_vis":7.52 ,"conductivity":17.0 ,"diff":9.63 ,"Pr":0.781},
{"temp":220 ,"Density" :1.5341 ,"Cp":1.044 ,"Vis":137 ,"kyn_vis":8.93 ,"conductivity":19.0 ,"diff":11.9,"Pr": 0.753},
{"temp":240 ,"Density" :1.4055 ,"Cp":1.043 ,"Vis":147 ,"kyn_vis":10.5 ,"conductivity":20.6 ,"diff":14.1 ,"Pr":0.744},
{"temp":260 ,"Density" :1.2967 ,"Cp":1.043 ,"Vis":157 ,"kyn_vis":12.1 ,"conductivity":22.1 ,"diff":16.3 ,"Pr":0.741},
{"temp":280 ,"Density" :1.2038 ,"Cp":1.042 ,"Vis":166 ,"kyn_vis":13.8 ,"conductivity":23.6 ,"diff":18.8,"Pr": 0.733},
{"temp":300 ,"Density" :1.1233 ,"Cp":1.043 ,"Vis":175 ,"kyn_vis":15.6 ,"conductivity":25.0 ,"diff":21.3,"Pr": 0.730},
{"temp":320 ,"Density" :1.0529 ,"Cp":1.043 ,"Vis":184 ,"kyn_vis":17.5 ,"conductivity":26.3 ,"diff":23.9 ,"Pr":0.730},
{"temp":340 ,"Density" :0.9909 ,"Cp":1.044 ,"Vis":193 ,"kyn_vis":19.5 ,"conductivity":27.8 ,"diff":26.9 ,"Pr":0.725},
{"temp":360 ,"Density" :0.9357 ,"Cp":1.045 ,"Vis":202 ,"kyn_vis":21.6 ,"conductivity":29.1 ,"diff":29.8 ,"Pr":0.725},
{"temp":380 ,"Density" :0.8864 ,"Cp":1.047 ,"Vis":210 ,"kyn_vis":23.7 ,"conductivity":30.5 ,"diff":32.9 ,"Pr":0.729},
{"temp":400 ,"Density" :0.8421 ,"Cp":1.049 ,"Vis":218 ,"kyn_vis":25.9 ,"conductivity":31.8 ,"diff":36.0 ,"Pr":0.719},
{"temp":450 ,"Density" :0.7483 ,"Cp":1.055 ,"Vis":237 ,"kyn_vis":31.7 ,"conductivity":35.0 ,"diff":44.3,"Pr": 0.714},
{"temp":500 ,"Density" :0.67352 ,"Cp":1.065 ,"Vis":254 ,"kyn_vis":37.7 ,"conductivity":38.1,"diff": 53.1,"Pr": 0.710},
{"temp":550,"Density" : 0.61226 ,"Cp":1.076 ,"Vis":271 ,"kyn_vis":44.3 ,"conductivity":41.1 ,"diff":62.4 ,"Pr":0.710},
{"temp":600 ,"Density" :0.56126 ,"Cp":1.088 ,"Vis":286 ,"kyn_vis":51.0 ,"conductivity":44.0,"diff": 72.1,"Pr": 0.707},
{"temp":650 ,"Density" :0.51806 ,"Cp":1.101 ,"Vis":301 ,"kyn_vis":58.1,"conductivity": 47.0 ,"diff":82.4,"Pr": 0.705},
{"temp":700 ,"Density" :0.48102 ,"Cp":1.114,"Vis": 315 ,"kyn_vis":65.5 ,"conductivity":50.0 ,"diff":93.3,"Pr": 0.702},
{"temp":750,"Density" : 0.44899 ,"Cp":1.127 ,"Vis":329 ,"kyn_vis":73.3,"conductivity": 52.8 ,"diff":104 ,"Pr":0.702},
{"temp":800 ,"Density" :0.42095,"Cp": 1.140 ,"Vis":343 ,"kyn_vis":81.5,"conductivity": 55.5 ,"diff":116 ,"Pr":0.705},
]
co2=[{'temp':280,'Density':1.9022,'Cp':0.830,'Vis':140,'kyn_vis':7.36,'conductivity':15.20,'diff':9.63,'Pr':0.765,},
{'temp':300,'Density':1.7730,'Cp':0.851,'Vis':149,'kyn_vis':8.40,'conductivity':16.55,'diff':11.0,'Pr':0.766,},
{'temp':320,'Density':1.6609,'Cp':0.872,'Vis':156,'kyn_vis':9.39,'conductivity':18.05,'diff':12.5,'Pr':0.754,},
{'temp':340,'Density':1.5618,'Cp':0.891,'Vis':165,'kyn_vis':10.6,'conductivity':19.70,'diff':14.2,'Pr':0.746,},
{'temp':360,'Density':1.4743,'Cp':0.908,'Vis':173,'kyn_vis':11.7,'conductivity':21.2,'diff':15.8,'Pr':0.741,},
{'temp':380,'Density':1.3961,'Cp':0.926,'Vis':181,'kyn_vis':13.0,'conductivity':22.75,'diff':17.6,'Pr':0.737,},
{'temp':400,'Density':1.3257,'Cp':0.942,'Vis':190,'kyn_vis':14.3,'conductivity':24.3,'diff':19.5,'Pr':0.737,},
{'temp':450,'Density':1.1782,'Cp':0.981,'Vis':210,'kyn_vis':17.8,'conductivity':28.3,'diff':24.5,'Pr':0.728,},
{'temp':500,'Density':1.0594,'Cp':1.02,'Vis':231,'kyn_vis':21.8,'conductivity':32.5,'diff':30.1,'Pr':0.725,},
{'temp':550,'Density':0.9625,'Cp':1.05,'Vis':251,'kyn_vis':26.1,'conductivity':36.6,'diff':36.2,'Pr':0.721,},
{'temp':600,'Density':0.8826,'Cp':1.08,'Vis':270,'kyn_vis':30.6,'conductivity':40.7,'diff':42.7,'Pr':0.717,},
{'temp':650,'Density':0.8143,'Cp':1.10,'Vis':288,'kyn_vis':35.4,'conductivity':44.5,'diff':49.7,'Pr':0.712,},
{'temp':700,'Density':0.7564,'Cp':1.13,'Vis':305,'kyn_vis':40.3,'conductivity':48.1,'diff':56.3,'Pr':0.717,},
{'temp':750,'Density':0.7057,'Cp':1.15,'Vis':321,'kyn_vis':45.5,'conductivity':51.7,'diff':63.7,'Pr':0.714,},
{'temp':800,'Density':0.6614,'Cp':1.17,'Vis':337,'kyn_vis':51.0,'conductivity':55.1,'diff':71.2,'Pr':0.716,},]

nh3=[{'temp':300,'Density':0.6894,'Cp':2.158,'Vis':101.5,'kyn_vis':14.7,'conductivity':24.7,'diff':16.6,'Pr':0.887,},
{'temp':320,'Density':0.6448,'Cp':2.170,'Vis':109,'kyn_vis':16.9,'conductivity':27.2,'diff':19.4,'Pr':0.870,},
{'temp':340,'Density':0.6059,'Cp':2.192,'Vis':116.5,'kyn_vis':19.2,'conductivity':29.3,'diff':22.1,'Pr':0.872,},
{'temp':360,'Density':0.5716,'Cp':2.221,'Vis':124,'kyn_vis':21.7,'conductivity':31.6,'diff':24.9,'Pr':0.872,},
{'temp':380,'Density':0.5410,'Cp':2.254,'Vis':131,'kyn_vis':24.2,'conductivity':34.0,'diff':27.9,'Pr':0.869,},
{'temp':400,'Density':0.5136,'Cp':2.287,'Vis':138,'kyn_vis':26.9,'conductivity':37.0,'diff':31.5,'Pr':0.853,},
{'temp':420,'Density':0.4888,'Cp':2.322,'Vis':145,'kyn_vis':29.7,'conductivity':40.4,'diff':35.6,'Pr':0.833,},
{'temp':440,'Density':0.4664,'Cp':2.357,'Vis':152.5,'kyn_vis':32.7,'conductivity':43.5,'diff':39.6,'Pr':0.826,},
{'temp':460,'Density':0.4460,'Cp':2.393,'Vis':159,'kyn_vis':35.7,'conductivity':46.3,'diff':43.4,'Pr':0.822,},
{'temp':480,'Density':0.4273,'Cp':2.430,'Vis':166.5,'kyn_vis':39.0,'conductivity':49.2,'diff':47.4,'Pr':0.822,},
{'temp':500,'Density':0.4101,'Cp':2.467,'Vis':173,'kyn_vis':42.2,'conductivity':52.5,'diff':51.9,'Pr':0.813,},
{'temp':520,'Density':0.3942,'Cp':2.504,'Vis':180,'kyn_vis':45.7,'conductivity':54.5,'diff':55.2,'Pr':0.827,},
{'temp':540,'Density':0.3795,'Cp':2.540,'Vis':186.5,'kyn_vis':49.1,'conductivity':57.5,'diff':59.7,'Pr':0.824,},
{'temp':560,'Density':0.3708,'Cp':2.577,'Vis':193,'kyn_vis':52.0,'conductivity':60.6,'diff':63.4,'Pr':0.827,},
{'temp':580,'Density':0.3533,'Cp':2.613,'Vis':199.5,'kyn_vis':56.5,'conductivity':63.8,'diff':69.1,'Pr':0.817,},]

air=[{'temp':100,'Density':3.5562,'Cp':1.032,'Vis':71.1,'kyn_vis':2.00,'conductivity':9.34,'diff':2.54,'Pr':0.786,},
{'temp':150,'Density':2.3364,'Cp':1.012,'Vis':103.4,'kyn_vis':4.426,'conductivity':13.8,'diff':5.84,'Pr':0.758,},
{'temp':200,'Density':1.7458,'Cp':1.007,'Vis':132.5,'kyn_vis':7.590,'conductivity':18.1,'diff':10.3,'Pr':0.737,},
{'temp':250,'Density':1.3947,'Cp':1.006,'Vis':159.6,'kyn_vis':11.44,'conductivity':22.3,'diff':15.9,'Pr':0.720,},
{'temp':300,'Density':1.1614,'Cp':1.007,'Vis':184.6,'kyn_vis':15.89,'conductivity':26.3,'diff':22.5,'Pr':0.707,},
{'temp':350,'Density':0.9950,'Cp':1.009,'Vis':208.2,'kyn_vis':20.92,'conductivity':30.0,'diff':29.9,'Pr':0.700,},
{'temp':400,'Density':0.8711,'Cp':1.014,'Vis':230.1,'kyn_vis':26.41,'conductivity':33.8,'diff':38.3,'Pr':0.690,},
{'temp':450,'Density':0.7740,'Cp':1.021,'Vis':250.7,'kyn_vis':32.39,'conductivity':37.3,'diff':47.2,'Pr':0.686,},
{'temp':500,'Density':0.6964,'Cp':1.030,'Vis':270.1,'kyn_vis':38.79,'conductivity':40.7,'diff':56.7,'Pr':0.684,},
{'temp':550,'Density':0.6329,'Cp':1.040,'Vis':288.4,'kyn_vis':45.57,'conductivity':43.9,'diff':66.7,'Pr':0.683,},
{'temp':600,'Density':0.5804,'Cp':1.051,'Vis':305.8,'kyn_vis':52.69,'conductivity':46.9,'diff':76.9,'Pr':0.685,},
{'temp':650,'Density':0.5356,'Cp':1.063,'Vis':322.5,'kyn_vis':60.21,'conductivity':49.7,'diff':87.3,'Pr':0.690,},
{'temp':700,'Density':0.4975,'Cp':1.075,'Vis':338.8,'kyn_vis':68.10,'conductivity':52.4,'diff':98.0,'Pr':0.695,},
{'temp':750,'Density':0.4643,'Cp':1.087,'Vis':354.6,'kyn_vis':76.37,'conductivity':54.9,'diff':109,'Pr':0.702,},
{'temp':800,'Density':0.4354,'Cp':1.099,'Vis':369.8,'kyn_vis':84.93,'conductivity':57.3,'diff':120,'Pr':0.709,},
{'temp':850,'Density':0.4097,'Cp':1.110,'Vis':384.3,'kyn_vis':93.80,'conductivity':59.6,'diff':131,'Pr':0.716,},
{'temp':900,'Density':0.3868,'Cp':1.121,'Vis':398.1,'kyn_vis':102.9,'conductivity':62.0,'diff':143,'Pr':0.720,},
{'temp':950,'Density':0.3666,'Cp':1.131,'Vis':411.3,'kyn_vis':112.2,'conductivity':64.3,'diff':155,'Pr':0.723,},
{'temp':1000,'Density':0.3482,'Cp':1.141,'Vis':424.4,'kyn_vis':121.9,'conductivity':66.7,'diff':168,'Pr':0.726,},
{'temp':1100,'Density':0.3166,'Cp':1.159,'Vis':449.0,'kyn_vis':141.8,'conductivity':71.5,'diff':195,'Pr':0.728,},
{'temp':1200,'Density':0.2902,'Cp':1.175,'Vis':473.0,'kyn_vis':162.9,'conductivity':76.3,'diff':224,'Pr':0.728,},
{'temp':1300,'Density':0.2679,'Cp':1.189,'Vis':496.0,'kyn_vis':185.1,'conductivity':82,'diff':257,'Pr':0.719,},
{'temp':1400,'Density':0.2488,'Cp':1.207,'Vis':530,'kyn_vis':213,'conductivity':91,'diff':303,'Pr':0.703,},
{'temp':1500,'Density':0.2322,'Cp':1.230,'Vis':557,'kyn_vis':240,'conductivity':100,'diff':350,'Pr':0.685,},
{'temp':1600,'Density':0.2177,'Cp':1.248,'Vis':584,'kyn_vis':268,'conductivity':106,'diff':390,'Pr':0.688,},
{'temp':1700,'Density':0.2049,'Cp':1.267,'Vis':611,'kyn_vis':298,'conductivity':113,'diff':435,'Pr':0.685,},
{'temp':1800,'Density':0.1935,'Cp':1.286,'Vis':637,'kyn_vis':329,'conductivity':120,'diff':482,'Pr':0.683,},
{'temp':1900,'Density':0.1833,'Cp':1.307,'Vis':663,'kyn_vis':362,'conductivity':128,'diff':534,'Pr':0.677,},
{'temp':2000,'Density':0.1741,'Cp':1.337,'Vis':689,'kyn_vis':396,'conductivity':137,'diff':589,'Pr':0.672,},
{'temp':2100,'Density':0.1658,'Cp':1.372,'Vis':715,'kyn_vis':431,'conductivity':147,'diff':646,'Pr':0.667,},
{'temp':2200,'Density':0.1582,'Cp':1.417,'Vis':740,'kyn_vis':468,'conductivity':160,'diff':714,'Pr':0.655,},
{'temp':2300,'Density':0.1513,'Cp':1.478,'Vis':766,'kyn_vis':506,'conductivity':175,'diff':783,'Pr':0.647,},
{'temp':2400,'Density':0.1448,'Cp':1.558,'Vis':792,'kyn_vis':547,'conductivity':196,'diff':869,'Pr':0.630,},
{'temp':2500,'Density':0.1389,'Cp':1.665,'Vis':818,'kyn_vis':589,'conductivity':222,'diff':960,'Pr':0.613,},
{'temp':3000,'Density':0.1135,'Cp':2.726,'Vis':955,'kyn_vis':841,'conductivity':486,'diff':1570,'Pr':0.536,},]

h2=[{'temp':100,'Density':0.24255,'Cp':11.23,'Vis':42.1,'kyn_vis':17.4,'conductivity':67.0,'diff':24.6,'Pr':0.707,},
{'temp':150,'Density':0.16156,'Cp':12.60,'Vis':56.0,'kyn_vis':34.7,'conductivity':101,'diff':49.6,'Pr':0.699,},
{'temp':200,'Density':0.12115,'Cp':13.54,'Vis':68.1,'kyn_vis':56.2,'conductivity':131,'diff':79.9,'Pr':0.704,},
{'temp':250,'Density':0.09693,'Cp':14.06,'Vis':78.9,'kyn_vis':81.4,'conductivity':157,'diff':115,'Pr':0.707,},
{'temp':300,'Density':0.08078,'Cp':14.31,'Vis':89.6,'kyn_vis':111,'conductivity':183,'diff':158,'Pr':0.701,},
{'temp':350,'Density':0.06924,'Cp':14.43,'Vis':98.8,'kyn_vis':143,'conductivity':204,'diff':204,'Pr':0.700,},
{'temp':400,'Density':0.06059,'Cp':14.48,'Vis':108.2,'kyn_vis':179,'conductivity':226,'diff':258,'Pr':0.695,},
{'temp':450,'Density':0.05386,'Cp':14.50,'Vis':117.2,'kyn_vis':218,'conductivity':247,'diff':316,'Pr':0.689,},
{'temp':500,'Density':0.04848,'Cp':14.52,'Vis':126.4,'kyn_vis':261,'conductivity':266,'diff':378,'Pr':0.691,},
{'temp':550,'Density':0.04407,'Cp':14.53,'Vis':134.3,'kyn_vis':305,'conductivity':285,'diff':445,'Pr':0.685,},
{'temp':600,'Density':0.04040,'Cp':14.55,'Vis':142.4,'kyn_vis':352,'conductivity':305,'diff':519,'Pr':0.678,},
{'temp':700,'Density':0.03463,'Cp':14.61,'Vis':157.8,'kyn_vis':456,'conductivity':342,'diff':676,'Pr':0.675,},
{'temp':800,'Density':0.03030,'Cp':14.70,'Vis':172.4,'kyn_vis':569,'conductivity':378,'diff':849,'Pr':0.670,},
{'temp':900,'Density':0.02694,'Cp':14.83,'Vis':186.5,'kyn_vis':692,'conductivity':412,'diff':1030,'Pr':0.671,},
{'temp':1000,'Density':0.02424,'Cp':14.99,'Vis':201.3,'kyn_vis':830,'conductivity':448,'diff':1230,'Pr':0.673,},
{'temp':1100,'Density':0.02204,'Cp':15.17,'Vis':213.0,'kyn_vis':966,'conductivity':488,'diff':1460,'Pr':0.662,},
{'temp':1200,'Density':0.02020,'Cp':15.37,'Vis':226.2,'kyn_vis':1120,'conductivity':528,'diff':1700,'Pr':0.659,},
{'temp':1300,'Density':0.01865,'Cp':15.59,'Vis':238.5,'kyn_vis':1279,'conductivity':568,'diff':1955,'Pr':0.655,},
{'temp':1400,'Density':0.01732,'Cp':15.81,'Vis':250.7,'kyn_vis':1447,'conductivity':610,'diff':2230,'Pr':0.650,},
{'temp':1500,'Density':0.01616,'Cp':16.02,'Vis':262.7,'kyn_vis':1626,'conductivity':655,'diff':2530,'Pr':0.643,},
{'temp':1600,'Density':0.0152,'Cp':16.28,'Vis':273.7,'kyn_vis':1801,'conductivity':697,'diff':2815,'Pr':0.639,},
{'temp':1700,'Density':0.0143,'Cp':16.58,'Vis':284.9,'kyn_vis':1992,'conductivity':742,'diff':3130,'Pr':0.637,},
{'temp':1800,'Density':0.0135,'Cp':16.96,'Vis':296.1,'kyn_vis':2193,'conductivity':786,'diff':3435,'Pr':0.639,},
{'temp':1900,'Density':0.0128,'Cp':17.49,'Vis':307.2,'kyn_vis':2400,'conductivity':835,'diff':3730,'Pr':0.643,},
{'temp':2000,'Density':0.0121,'Cp':18.25,'Vis':318.2,'kyn_vis':2630,'conductivity':878,'diff':3975,'Pr':0.661,},]

n2=[{'temp':100,'Density':3.4388,'Cp':1.070,'Vis':68.8,'kyn_vis':2.00,'conductivity':9.58,'diff':2.60,'Pr':0.768,},
{'temp':150,'Density':2.2594,'Cp':1.050,'Vis':100.6,'kyn_vis':4.45,'conductivity':13.9,'diff':5.86,'Pr':0.759,},
{'temp':200,'Density':1.6883,'Cp':1.043,'Vis':129.2,'kyn_vis':7.65,'conductivity':18.3,'diff':10.4,'Pr':0.736,},
{'temp':250,'Density':1.3488,'Cp':1.042,'Vis':154.9,'kyn_vis':11.48,'conductivity':22.2,'diff':15.8,'Pr':0.727,},
{'temp':300,'Density':1.1233,'Cp':1.041,'Vis':178.2,'kyn_vis':15.86,'conductivity':25.9,'diff':22.1,'Pr':0.716,},
{'temp':350,'Density':0.9625,'Cp':1.042,'Vis':200.0,'kyn_vis':20.78,'conductivity':29.3,'diff':29.2,'Pr':0.711,},
{'temp':400,'Density':0.8425,'Cp':1.045,'Vis':220.4,'kyn_vis':26.16,'conductivity':32.7,'diff':37.1,'Pr':0.704,},
{'temp':450,'Density':0.7485,'Cp':1.050,'Vis':239.6,'kyn_vis':32.01,'conductivity':35.8,'diff':45.6,'Pr':0.703,},
{'temp':500,'Density':0.6739,'Cp':1.056,'Vis':257.7,'kyn_vis':38.24,'conductivity':38.9,'diff':54.7,'Pr':0.700,},
{'temp':550,'Density':0.6124,'Cp':1.065,'Vis':274.7,'kyn_vis':44.86,'conductivity':41.7,'diff':63.9,'Pr':0.702,},
{'temp':600,'Density':0.5615,'Cp':1.075,'Vis':290.8,'kyn_vis':51.79,'conductivity':44.6,'diff':73.9,'Pr':0.701,},
{'temp':700,'Density':0.4812,'Cp':1.098,'Vis':321.0,'kyn_vis':66.71,'conductivity':49.9,'diff':94.4,'Pr':0.706,},
{'temp':800,'Density':0.4211,'Cp':1.122,'Vis':349.1,'kyn_vis':82.90,'conductivity':54.8,'diff':116,'Pr':0.715,},
{'temp':900,'Density':0.3743,'Cp':1.146,'Vis':375.3,'kyn_vis':100.3,'conductivity':59.7,'diff':139,'Pr':0.721,},
{'temp':1000,'Density':0.3368,'Cp':1.167,'Vis':399.9,'kyn_vis':118.7,'conductivity':64.7,'diff':165,'Pr':0.721,},
{'temp':1100,'Density':0.3062,'Cp':1.187,'Vis':423.2,'kyn_vis':138.2,'conductivity':70.0,'diff':193,'Pr':0.718,},
{'temp':1200,'Density':0.2807,'Cp':1.204,'Vis':445.3,'kyn_vis':158.6,'conductivity':75.8,'diff':224,'Pr':0.707,},
{'temp':1300,'Density':0.2591,'Cp':1.219,'Vis':466.2,'kyn_vis':179.9,'conductivity':81.0,'diff':256,'Pr':0.701,},]

o2=[{'temp':100,'Density':3.945,'Cp':0.962,'Vis':76.4,'kyn_vis':1.94,'conductivity':9.25,'diff':2.44,'Pr':0.796,},
{'temp':150,'Density':2.585,'Cp':0.921,'Vis':114.8,'kyn_vis':4.44,'conductivity':13.8,'diff':5.80,'Pr':0.766,},
{'temp':200,'Density':1.930,'Cp':0.915,'Vis':147.5,'kyn_vis':7.64,'conductivity':18.3,'diff':10.4,'Pr':0.737,},
{'temp':250,'Density':1.542,'Cp':0.915,'Vis':178.6,'kyn_vis':11.58,'conductivity':22.6,'diff':16.0,'Pr':0.723,},
{'temp':300,'Density':1.284,'Cp':0.920,'Vis':207.2,'kyn_vis':16.14,'conductivity':26.8,'diff':22.7,'Pr':0.711,},]