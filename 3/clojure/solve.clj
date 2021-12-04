(require '[clojure.string :as str])

(defn split-lines 
    [data] (str/split data #"\n"))

(defn nth-col
    ([col rows]
        (nth-col col rows []))
    ([col [row & next :as all] xs]
        (if (empty? all)
            xs
            (nth-col col next (concat xs [(if (= (nth row col) \1) 1 0)])))))

(defn frequency
    ([bits] (/ (reduce + bits) (count bits))))

(defn frequency-col
    ([rows] (frequency-col rows (- (count (nth rows 0)) 1) []))
    ([rows count xs] 
        (if (= count -1)
            xs
            (frequency-col rows (- count 1) (concat [(frequency (nth-col count rows))] xs)))))

(defn gamma
    ([report] (map (fn [a] (if (>= a 1/2) 1 0)) (frequency-col report))))

(defn epsilon
    ([report] (map (fn [a] (if (= a 1) 0 1)) (gamma report))))

(defn bit-array-to-int
    ([bit-array] (bit-array-to-int (reverse bit-array) 1))
    ([[bit & next :as all] multiplier] 
        (if (empty? all) 0 (+ (* bit multiplier) (bit-array-to-int next (bit-shift-left multiplier 1))))))

(defn task1 [report]
    (* (bit-array-to-int (gamma report)) (bit-array-to-int (epsilon report))))

(defn task2 [report] "TODO")

(defn main []
    (def report (split-lines (slurp "../input.txt")))
    (println "Task 1: " (task1 report))
    (println "Task 2: " (task2 report))
)

(main)
