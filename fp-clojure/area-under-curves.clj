; summation of f(x) * delta(x) with value of x ranging from lower limit to upper limit by delta(x) steps
; http://tutorial.math.lamar.edu/Classes/CalcI/Area_Volume_Formulas.aspx

(let [read-nums (fn [] (map #(Float/parseFloat %) (clojure.string/split (read-line) #"\s+")))      
      coeffs (read-nums)
      exponents (read-nums)
      [low high] (read-nums)
      dx 0.001
      fx (fn [x] (->> exponents (map #(Math/pow x %)) (map * coeffs) (reduce +)))
      area (fn [r] (->> r (map fx) (reduce +) (* dx)))
      volume (fn [r] (->> r (map fx) (map #(* dx % % Math/PI)) (reduce +)))
      steps (range low (+ high dx) dx)]
      (println (area steps))
      (println (volume steps))
)
