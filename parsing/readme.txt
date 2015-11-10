#Ejercicio 1: Evaluación de Parsers

##Baseline Flat:


          | Precision | Recall | F1
---------------------------------------
Labeled   |99.93%     |14.57%  |25.43% 
UnLabeled |100.00%     |14.58%  |25.45% 

real	0m8.269s
user	0m8.181s
sys	0m0.072s


##Baseline rbranch:

          | Precision | Recall | F1
---------------------------------------
Labeled   |8.81%     |14.57%  |10.98% 
UnLabeled |8.87%     |14.68%  |11.06% 

real	0m9.274s
user	0m9.160s
sys	0m0.100s

##Baseline lbranch:

          | Precision | Recall | F1
---------------------------------------
Labeled   |8.81%     |14.57%  |10.98% 
UnLabeled |14.71%     |24.33%  |18.33% 

real	0m9.158s
user	0m9.013s
sys	0m0.132s

#Ejercicio 3: PCFGs No Lexicalizadas

$ time python parsing/scripts/eval.py -i upcfg -m 20
Loading model...
Loading corpus...
Parsing...
100.0% (1444/1444)Label:(P=73.25%, R=72.95%, F1=73.10%) UnLabel:(P=75.36%, R=75.05%, F1=75.21%)
Parsed 1444 sentences
          | Precision | Recall | F1
---------------------------------------
Labeled   |73.25%     |72.95%  |73.10% 
UnLabeled |75.36%     |75.05%  |75.21% 

real	5m26.883s
user	5m26.101s
sys	0m0.581s

#Ejercicio 4: Markovización Horizonta

##Orden markov = 0

$ time python parsing/scripts/eval.py -i upcfg -m 20
Loading model...
Loading corpus...
Parsing...
100.0% (1444/1444)Label:(P=70.27%, R=70.04%, F1=70.16%) UnLabel:(P=72.14%, R=71.91%, F1=72.03%)
Parsed 1444 sentences
          | Precision | Recall | F1
---------------------------------------
Labeled   |70.27%     |70.04%  |70.16% 
UnLabeled |72.14%     |71.91%  |72.03% 

real	2m5.098s
user	2m4.942s
sys	0m0.140s

##Orden markov = 1

$ time python parsing/scripts/eval.py -i upcfg -m 20
Loading model...
Loading corpus...
Parsing...
100.0% (1444/1444)Label:(P=74.63%, R=74.54%, F1=74.58%) UnLabel:(P=76.50%, R=76.40%, F1=76.45%)
Parsed 1444 sentences
          | Precision | Recall | F1
---------------------------------------
Labeled   |74.63%     |74.54%  |74.58% 
UnLabeled |76.50%     |76.40%  |76.45% 

real	2m39.427s
user	2m39.266s
sys	0m0.148s


##Orden markov = 2

$ time python parsing/scripts/eval.py -i upcfg -m 20
Loading model...
Loading corpus...
Parsing...
3100.0% (1444/1444)Label:(P=74.84%, R=74.32%, F1=74.58%) UnLabel:(P=76.76%, R=76.23%, F1=76.49%)
Parsed 1444 sentences
          | Precision | Recall | F1
---------------------------------------
Labeled   |74.84%     |74.32%  |74.58% 
UnLabeled |76.76%     |76.23%  |76.49% 

real	4m22.143s
user	4m21.826s
sys	0m0.280s


##Orden markov = 3

$ time python parsing/scripts/eval.py -i upcfg -m 20
Loading model...
Loading corpus...
Parsing...
100.0% (1444/1444)Label:(P=74.12%, R=73.49%, F1=73.80%) UnLabel:(P=76.28%, R=75.63%, F1=75.95%)
Parsed 1444 sentences
          | Precision | Recall | F1
---------------------------------------
Labeled   |74.12%     |73.49%  |73.80% 
UnLabeled |76.28%     |75.63%  |75.95% 

real	4m59.198s
user	4m58.544s
sys	0m0.472s