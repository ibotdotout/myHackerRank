;; https://www.hackerrank.com/challenges/eval-ex

(dotimes [_ (Integer/parseInt (read-line))]
   (let [x (Float/parseFloat (read-line))]
     (-> (reduce + (map #(/ (reduce * (repeat %1 x)) (reduce * (range 1 (inc %1)))) (range 10)))
      (println))))
