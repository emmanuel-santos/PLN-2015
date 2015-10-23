Ejercicio 1: Corpus Ancora: Estadísticas de etiquetas POS

sents: 17379
ocurrence_words: 517300
vocabulary_of_words: 46483
vocabulary_of_taggeds: 48


TAG      MEANING                    OCURRENCE_TAG    PERCENTAGE   WORDS

nc       nombre común               92002            17.785038%   ['años', 'presidente', 'millones', 'equipo', 'partido']
sp       adposición proposición     79904            15.446356%   ['de', 'en', 'a', 'del', 'con']
da       determinante artículo      54552            10.545525%   ['la', 'el', 'los', 'las', 'El']
vm       verbo principal            50609             9.783298%   ['está', 'tiene', 'dijo', 'puede', 'hace']
aq       adjetivo calificativo      33904             6.554031%   ['pasado', 'gran', 'mayor', 'nuevo', 'próximo']
fc       puntuación coma            30148             5.827953%   [',']
np       nombre propio              29113             5.627876%   ['Gobierno', 'España', 'PP', 'Barcelona', 'Madrid']
fp       puntuación (.)             21157             4.089890%   ['.', '(', ')']
rg       adverbio general           15333             2.964044%   ['más', 'hoy', 'también', 'ayer', 'ya']
cc       conjunción coordinada      15023             2.904118%   ['y', 'pero', 'o', 'Pero', 'e']



Ejercicio 3: Entrenamiento y Evaluación de Taggers

Accuracy: 89.01%
Accuracy Know: 95.32%
Accuracy UnKnow: 31.80%

Confusion matrix:
        nc      sp      da      vm      aq      np      fc      fp      rg      cc

nc       0      45     143    2106    2076    1942       0       0     297      13

sp      11       0       0       1       5       3       0       0      17       1

da       1       0       0       0       0       0       0       0       0       0

vm      89       0       0       0     214       0       0       0       0       0

aq     395       0       0     145       0       1       0       0      29       0

np       4       0       0       0       0       0       0       0       0       1

fc       0       0       0       0       0       0       0       0       0       0

fp       0       0       0       0       0       0       0       0       0       0

rg      32       5       0       0       3       0       0       0       0      46

cc       1       0       0       0       0       1       0       0      21       0


Ejercicio 5: HMM POS Tagger

n = 1:
    Accuracy: 89.01%
    Accuracy Know: 95.32%
    Accuracy UnKnow: 31.80%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      45     143    2105    2041    1935       0       0     297      12

    sp      11       0       0       1       5       3       0       0      17       1

    da       1       0       0       0       0       0       0       0       0       0

    vm      88       0       0       0     183       0       0       0       0       0

    aq     471       0       0     167       0       1       0       0      29       0

    np       4       0       0       0       0       0       0       0       0       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      32       5       0       0       3       0       0       0       0      46

    cc       1       0       0       0       0       1       0       0      21       0

    real	0m10.315s
    user	0m10.175s
    sys	0m0.108s


n = 2:
    Accuracy: 92.72%
    Accuracy Know: 97.61%
    Accuracy UnKnow: 48.42%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0       3      69     198     418     470       0       0      32       0

    sp      70       0       4     339     147      52       0       0      65       1

    da     168      13       0      86      98      37       0       0      25       0

    vm     176       5       8       0     300      90       0       0      43       1

    aq     344       1       1     195       0     148       0       0      51       0

    np     471       4      40     120     149       0       0       0      68      10

    fc      41       1       0      31      86      35       0       0       1       0

    fp       0       0       0       1       3       1       0       0       0       0

    rg      44      16       0      57      53      23       0       0       0      51

    cc       2       4       0       2       1       1       0       0      22       0

    real	0m17.510s
    user	0m17.330s
    sys	0m0.156s


n = 3:
    Accuracy: 93.16%
    Accuracy Know: 97.67%
    Accuracy UnKnow: 52.30%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0       2      81     235     433     541       0       0      42       0

    sp      42       0       0     309      95      48       0       0      58       0

    da     159      14       0      72      70      36       0       0      25       1

    vm     145       6       7       0     234      75       0       0      23       1

    aq     339       2       4     197       0     132       0       0      45       0

    np     320       5      30      83      88       0       0       0      32       8

    fc      24       1       0      59      74      24       0       0      10       0

    fp       2       0       0       1       4       4       0       0       0       0

    rg      40      14       0      62      54      52       0       0       0      60

    cc       7       3       0      12       5       4       0       0      21       0

    real	1m6.654s
    user	1m6.249s
    sys	0m0.224s

        
n = 4:
    Accuracy: 93.13%
    Accuracy Know: 97.43%
    Accuracy UnKnow: 54.09%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0       1      74     243     456     512       0       0      43       0

    sp      42       0       3     310      94      39       0       0      60       1

    da     139      13       0      72      67      42       0       0      27       1

    vm     119       5       8       0     256      82       0       0      26       1

    aq     349       1       4     185       0     126       0       0      51       3

    np     282       5      37      69      62       0       0       0      30       6

    fc      28       1       1      48      93      21       0       0       7       0

    fp       5       0       1       0       1       2       0       0       0       0

    rg      40      16       0      65      62      43       0       0       0      58

    cc       6       3       0      12      13      11       0       0      29       0

    real	8m53.952s
    user	8m52.704s
    sys	0m0.776s



Ejercicio 7: Maximum Entropy Markov Models

LogisticRegression con n = 1:
 
    Accuracy: 92.70%
    Accuracy Know: 95.28%
    Accuracy UnKnow: 69.32%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      11     118     393     672     238       0       0      48       1

    sp       9       0       0       1       5       2       0       0      16       1

    da       6       0       0       0       0       0       0       0       1       0

    vm     497      31       4       0     546      87       0       0     204      13

    aq     535      41       0     494       0      23       0       0     292       2

    np     115       0       4     167      44       0       0       0      32       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      16       4       0       0       2       0       0       0       0      44

    cc       1       0       0       0       0       1       0       0      21       0

    real    0m32.981s
    user    0m31.987s
    sys 0m0.196s
    


LogisticRegression con n = 2:    

    Accuracy: 91.99%
    Accuracy Know: 94.55%
    Accuracy UnKnow: 68.75%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      25     118     534     913     244       0       0     165       3

    sp       8       0       0       1       5       2       0       0      16       1

    da       6       0       0       0       0       0       0       0       1       0

    vm     543      34       3       0     539      88       0       0     208      13

    aq     713      33       0     567       0      16       0       0     176       1

    np     116       0       4     170      44       0       0       0      32       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      11       4       0       0       3       0       0       0       0      45

    cc       0       0       0       0       0       1       0       0      21       0

    real	0m34.851s
    user	0m34.646s
    sys	0m0.108s
    
    

LogisticRegression con n = 3:
    
    Accuracy: 92.18%
    Accuracy Know: 94.72%
    Accuracy UnKnow: 69.20%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      20     119     524     874     254       0       0     116       5

    sp      10       0       0       1       5       3       0       0      16       1

    da       6       0       0       0       0       0       0       0       1       0

    vm     509      37       3       0     523      80       0       0     258      12

    aq     696      36       0     533       0      19       0       0     181       3

    np     113       0       4     168      44       0       0       0      32       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      11       4       0       0       3       0       0       0       0      45

    cc       0       0       0       0       0       1       0       0      21       0

    real	0m37.816s
    user	0m37.593s
    sys	0m0.128s



LogisticRegression con n = 4:

    Accuracy: 92.23%
    Accuracy Know: 94.72%
    Accuracy UnKnow: 69.60%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      18     118     554     884     258       0       0     124       4

    sp      10       0       0       1       5       3       0       0      16       1

    da       4       0       0       0       0       0       0       0       1       0

    vm     444      38       3       0     495      77       0       0     247      12

    aq     703      35       0     539       0      21       0       0     192       3

    np     113       0       4     171      44       0       0       0      32       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      11       4       0       0       4       0       0       0       0      44

    cc       0       0       0       0       0       1       0       0      21       0

    real	0m39.729s
    user	0m39.508s
    sys	0m0.124s
    


LinearSVC con n = 1:
    
    Accuracy: 94.43%
    Accuracy Know: 97.04%
    Accuracy UnKnow: 70.82%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0       5      86     251     526     245       0       0      38       1

    sp      10       0       0       1       6       3       0       0      17       1

    da       1       0       0       0       0       0       0       0       0       0

    vm     331      11       1       0     388      59       0       0      73      10

    aq     388      16       0     368       0      19       0       0     151       0

    np     111       0       4     110      33       0       0       0       3       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      19       4       0       0      10       0       0       0       0      45

    cc       1       0       0       0       0       1       0       0      21       0

    real	0m31.848s
    user	0m31.640s
    sys	0m0.112s
    
    
    
LinearSVC con n = 2:

    Accuracy: 94.29%
    Accuracy Know: 96.91%
    Accuracy UnKnow: 70.57%
    Confusion matrix:

            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      10      86     344     589     248       0       0     100       1

    sp      10       0       0       1       5       3       0       0      17       1

    da       1       0       0       0       0       0       0       0       1       0

    vm     344      11       1       0     375      57       0       0      72      10

    aq     477      10       0     357       0      17       0       0      95       0

    np     110       0       4     112      34       0       0       0       3       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      12       4       0       0       9       0       0       0       0      45

    cc       1       0       0       0       0       1       0       0      21       0

    real	0m41.398s
    user	0m41.187s
    sys	0m0.144s



LinearSVC con n = 3:

    Accuracy: 94.40%
    Accuracy Know: 96.94%
    Accuracy UnKnow: 71.38%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      10      86     323     571     241       0       0      79       3

    sp      10       0       0       1       5       3       0       0      17       1

    da       1       0       0       0       0       0       0       0       0       0

    vm     319      11       1       0     349      63       0       0      94       5

    aq     490      10       0     371       0      19       0       0      98       5

    np     106       0       4     112      32       0       0       0       3       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      12       4       0       0       8       0       0       0       0      47

    cc       1       0       0       0       0       1       0       0      20       0

    real	0m37.247s
    user	0m37.045s
    sys	0m0.100s
    

    
LinearSVC con n = 4:

    Accuracy: 94.46%
    Accuracy Know: 96.96%
    Accuracy UnKnow: 71.81%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      10      87     348     579     242       0       0      78       3

    sp      10       0       0       1       5       3       0       0      17       1

    da       1       0       0       0       0       0       0       0       0       0

    vm     275      13       0       0     343      61       0       0      99       6

    aq     489       8       0     356       0      19       0       0      95       4

    np     106       0       4     112      32       0       0       0       3       1

    fc       0       0       0       0       0       0       0       0       0       0

    fp       0       0       0       0       0       0       0       0       0       0

    rg      12       4       0       0       8       0       0       0       0      47

    cc       1       0       0       0       0       1       0       0      21       0

    real	0m47.613s
    user	0m46.932s
    sys	0m0.184s


    
MultinomialNB con n = 1:

    Accuracy: 82.18%
    Accuracy Know: 85.85%
    Accuracy UnKnow: 48.89%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      10     107     479    1324     350       0       2     268      12

    sp     406       0       0     625    1234     140       0       1     405      17

    da     251      59       0     371     126     468       1       8     285     129

    vm      98       0       0       0     302      21       0       1     154       1

    aq      77       1       0      69       0       1       0       0     107       1

    np     111      43       5      26      18       0       0       0       7     104

    fc      10       1       0      60      46       1       0       0      32       0

    fp       0       1       0       5       4       0       0       0       3       0

    rg       2       2       0       0       0       0       0       0       0      46

    cc       0       0       0       0       0       1       0       0      14       0

    real	23m16.864s
    user	23m12.470s
    sys	0m0.687s
    
   
    
MultinomialNB con n = 2:
    
    Accuracy: 76.46%
    Accuracy Know: 80.41%
    Accuracy UnKnow: 40.68%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0      39     127     525    1113     332       4      22     263      57

    sp    1087       0       7     944    1396     288       0       0     413      20

    da     724     211       0     758     394     536       5      76     449     407

    vm     287       9       0       0     378      41       1      12     215      11

    aq     200       1       0     173       0       2       0       0     133       3

    np     123      49       4      37      17       0       0       2      13     110

    fc      51       3       0     153      87      12       0       0      66       3

    fp       1       1       0       6       4       0       0       0       2       0

    rg       2       1       0       0       1       0       0       0       0      49

    cc       0       0       0       0       0       1       0       0      12       0

    real	23m6.912s
    user	23m3.968s
    sys	0m0.216s
    
    
    
MultinomialNB con n = 3:

    Accuracy: 71.47%
    Accuracy Know: 75.09%
    Accuracy UnKnow: 38.59%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0     152     146     774    1267     399      28      42     332     111

    sp    1092       0      34    1094    1281     299       0       2     511      41

    da     887     509       0    1080     531     595       7     164     570     421

    vm     342      33       2       0     360      63       4      18     233      11

    aq     500       2      11     277       0       6       0       1     234       8

    np     124      45       5      42      15       0       0       0      17     116

    fc      80      18       4     175      77       9       0       0      61       3

    fp      25       0       0       9      15       0       0       0       6       0

    rg       6       1       0       4       9       0       0       0       0      43

    cc       0       0       0       0       1       1       0       1      15       0

    real	26m7.901s
    user	25m57.035s
    sys	0m1.222s



MultinomialNB con n = 4:

    Accuracy: 68.20%
    Accuracy Know: 71.31%
    Accuracy UnKnow: 40.01%

    Confusion matrix:
            nc      sp      da      vm      aq      np      fc      fp      rg      cc

    nc       0     202     142     939    1261     419      28      85     362     233

    sp     969       0      41    1155    1314     310       4      14     581      75

    da     786     548       0    1169     484     558      35     173     624     350

    vm     277      51       0       0     269      78      25      28     245      31

    aq     781       4      29     447       0      11       0       1     346      23

    np     192      52      20      88      51       0       0       6      54     128

    fc     135      29      15     181      77       2       0       0      60       4

    fp      74      35      11      63      61       3       0       0      23       1

    rg      12       1       0       9      24       2       0       0       0      46

    cc      15       2       0       0      34       1       0       2      35       0

    real	23m49.587s
    user	23m41.132s
    sys	0m1.043s
