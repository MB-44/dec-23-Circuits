func countPairsWithCondition(a: [Int], n: Int) -> Int {
    var count = 0

    for i in 0..<n {
        for j in 0..<n where i != j && (a[i] - a[j]) == (i - j) {
            count += 1
        }
    }
    return count
}

let n = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").compactMap { Int($0) }

let result = countPairsWithCondition(a: arr, n: n)
print(result)
