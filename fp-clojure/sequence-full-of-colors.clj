;https://www.hackerrank.com/challenges/sequence-full-of-colors

;timeout

(defn countChar
  [char, word]
  (count (re-seq (re-pattern char) word)))
  
(defn equal?
  [word pairChar]
  (apply = (map #(countChar % word) pairChar)))

(defn diffOne?
  [word pairChar]
  (<= (Math/abs (apply - (map #(countChar % word) pairChar))) 1))


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

(defn checkFullConditions
  [word]
  (let [conds [RequG? YequB?]]
       (every? identity (map #(% word) conds))))

(defn printAnswer
  [result]
  (println (if result "True" "False")))
  
(defn getPrefixs
  [word]
  (vec (map #(subs word 0 %) (range 1 (count word))))
)

(defn checkPrefixConditions
  [prefixs]
  (every? identity (map #(and (RmoreOneG? %) (YmoreOneB? %)) prefixs))
)

(let [t (Integer/parseInt (read-line))]
  (dotimes [_ t]
    (let [word (read-line)
          prefixs (getPrefixs word)]
         (printAnswer (and (checkFullConditions word) (checkPrefixConditions prefixs))))))
