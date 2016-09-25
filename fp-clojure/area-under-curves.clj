; https://www.hackerrank.com/challenges/area-under-curves-and-volume-of-revolving-a-curv/

; summation of f(x) * delta(x) with value of x ranging from lower limit to upper limit by delta(x) steps
; http://tutorial.math.lamar.edu/Classes/CalcI/Area_Volume_Formulas.aspx

(require '[clojure.string :as str])

(defn listInt []
  (map #(Float/parseFloat %) (str/split (read-line) #" "))
)

(defn fx [a b x]
    (reduce + (map #(* %1 (Math/pow x %2)) a b))
) 

(defn area [a b steps deltaX]
   (* (reduce + (map #(fx a b %) steps)) deltaX)
)

(defn volume [a b steps deltaX]
   (* (reduce + (map #(Math/pow (fx a b %) 2) steps)) deltaX 3.14)
)


(let [a (listInt)
      b (listInt)
      [L R] (listInt)
      steps (range L R 0.001)
      deltaX (/ (- R L) (count steps))]
      (println (area a b steps deltaX))
      (println (volume a b steps deltaX))
)
