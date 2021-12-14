require "matrix"

def task(check_line)
    data = File.open("../input.txt").readlines.map(&:chomp).map{|x| x.split(" -> ").map{|y| Vector.elements(y.split(",").map(&:to_i))}}

    grid = {}
    grid.default = 0

    data.each{|p1, p2|
        direction = (p2 - p1).normalize.round

        if check_line and direction.map{|v| v.abs}.sum > 1
            next
        end

        while p1 != p2 do
            grid[p1] += 1
            p1 += direction
        end

        grid[p2] += 1
    }

    grid.values.filter{|x| x > 1}.length
end

print("Task 1: ", task(true), "\n")
print("Task 2: ", task(false))
