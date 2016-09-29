; https://www.hackerrank.com/challenges/string-o-permute

(dotimes [t (Integer/parseInt (read-line))]
  (println (clojure.string/join (flatten (map #(vec [(second %1) (first %1)]) (partition 2 (read-line))))))
)
