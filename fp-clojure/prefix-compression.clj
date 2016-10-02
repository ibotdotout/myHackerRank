; https://www.hackerrank.com/challenges/prefix-compression

; first

(let [a (read-line)
      b (read-line) 
      parts (->> (map #(vec [%1 %2]) a b) (partition-by #(= (first %) (second %))))
      n-prefix  (count (first parts))]
      (do
        (println n-prefix (apply str (take n-prefix a)))
        (println (- (count a) n-prefix) (apply str (drop n-prefix a)))
        (println (- (count b) n-prefix) (apply str (drop n-prefix b)))
      ))

; better

(let [a (read-line)
      b (read-line) 
      n-prefix (->> (map = a b) (take-while identity) (count))
      answers (#(vec [(subs a 0 %) (subs a %) (subs b %)]) n-prefix)]
     (doseq [i answers] 
      (println (#(str (count %) " " %) i))))
