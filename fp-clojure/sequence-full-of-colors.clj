;https://www.hackerrank.com/challenges/sequence-full-of-colors
; Special thank to P'tap @visibletrap

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
