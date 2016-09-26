; https://www.hackerrank.com/challenges/string-mingling

(let [p (read-line)
      q (read-line)]
      (println (clojure.string/join (map #(str %1%2) p q))))
