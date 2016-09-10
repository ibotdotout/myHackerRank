;; https://www.hackerrank.com/challenges/fp-reverse-a-list

;; (fn[lst] (let [n (count lst)] (map #(nth lst (- n %1 1)) (range n))))

(fn [lst] (reduce conj () lst))
