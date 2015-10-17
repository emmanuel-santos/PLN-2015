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

    real	0m13.830s
    user	0m13.648s
    sys	0m0.156s


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
    
    real	1m5.059s
    user	1m4.817s
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

    real	5m27.223s
    user	5m26.121s
    sys	0m0.284s
    
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

    real	31m54.776s
    user	31m49.796s
    sys	0m1.092s

