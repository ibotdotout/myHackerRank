; https://www.hackerrank.com/challenges/prefix-compression

(let [a (read-line)
      b (read-line) 
      parts (->> (map #(vec [%1 %2]) a b) (partition-by #(= (first %) (second %))))
      n-prefix  (count (first parts))]
      (do
        (println n-prefix (apply str (take n-prefix a)))
        (println (- (count a) n-prefix) (apply str (drop n-prefix a)))
        (println (- (count b) n-prefix) (apply str (drop n-prefix b)))
      ))
