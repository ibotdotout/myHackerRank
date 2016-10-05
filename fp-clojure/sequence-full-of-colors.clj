;https://www.hackerrank.com/challenges/sequence-full-of-colors

;draft

; Enter your code here. Read input from STDIN. Print output to STDOUT
;

(defn countChar
  [char, word]
  (count (re-seq (re-pattern char) word)))
  
(defn equal?
  [word pairChar]
  (apply = (map #(countChar % word) pairChar)))

(defn diffOne?
  [word pairChar]
  (= (Math/abs (apply - (map #(countChar % word) pairChar))) 1))

(defn RequG?
  [word]
  (equal? word ["R", "G"]))

(defn YequB?
  [word]
  (equal? word ["Y", "B"]))

(defn RmoreOneG?
  [word]
  (diffOne? word ["R", "G"]))

(defn YmoreOneB?
  [word]
  (diffOne? word ["Y", "B"]))

(defn checkConditions
  [word]
  (let [conds [RequG? YequB?]]
       (every? identity (map #(% word) conds))))

(defn printAnswer
  [result]
  (println (if result "True" "False")))

(let [t (Integer/parseInt (read-line))]
  (dotimes [_ t]
    (->> (read-line)
      (checkConditions)
      (printAnswer))))
