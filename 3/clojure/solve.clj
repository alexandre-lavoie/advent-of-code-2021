(require '[clojure.string :as str])

(defn split-lines [data] (str/split data #"\n"))

(defn bit-array [data] (map (fn [d] (if (= d \1) 1 0)) data))

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

(defn bit-array-to-int
    ([bit-array] (bit-array-to-int (reverse bit-array) 1))
    ([[bit & next :as all] multiplier] 
        (if (empty? all) 0 (+ (* bit multiplier) (bit-array-to-int next (bit-shift-left multiplier 1))))))

(defn most-common [frequency] (>= frequency 1/2))

(defn least-common [frequency] (< frequency 1/2))

(defn rating
    ([filter-fn report] (rating filter-fn report 0))
    ([filter-fn report bit]
        (if (<= (count report) 1) 
            (bit-array (nth report 0))
            (rating 
                filter-fn
                (filter (fn [v] (= (if (= (nth v bit) \1) 1 0) (if (filter-fn (frequency (nth-col bit report))) 1 0))) report)
                (+ bit 1)))))

(defn gamma [report] 
    (map (fn [a] (if (>= a 1/2) 1 0)) (frequency-col report)))

(defn epsilon [report] 
    (map (fn [a] (if (= a 1) 0 1)) (gamma report)))

(defn oxygen [report] 
    (rating most-common report))

(defn c02 [report] 
    (rating least-common report))

(defn task1 [report]
    (* (bit-array-to-int (gamma report)) (bit-array-to-int (epsilon report))))

(defn task2 [report] 
    (* (bit-array-to-int (oxygen report)) (bit-array-to-int (c02 report))))

(defn main []
    (def report (split-lines (slurp "../input.txt")))
    (println "Task 1: " (task1 report))
    (println "Task 2: " (task2 report)))

(main)
