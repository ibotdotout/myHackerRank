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

; pass
(defn abs [x] (max x (- x))) ; this better than (Math/abs) that make timeout
(defn eq [stats a b] (= (stats a) (stats b)))
(defn diff-one [stats a b] (-> (- (stats a) (stats b)) (abs) (<= 1)))

(defn anwser [[result stats]]
  (if (and result (eq stats \R \G) (eq stats \Y \B))
     "True"
     "False"))

(defn sequence-full-of-colors [word]
  (->> word
    (reduce (fn [[result stats] code]
      (if (and (diff-one stats \R \G) (diff-one stats \Y \B))
        [result (assoc stats code (inc (stats code)))]
        (reduced [false]))) 
      [true {\R 0 \G 0 \Y 0 \B 0}])
    (anwser)
    (println)))
    
(let [t (Integer/parseInt (read-line))]
  (dotimes [_ t]
    (let [word (read-line)]
      (sequence-full-of-colors word))))
