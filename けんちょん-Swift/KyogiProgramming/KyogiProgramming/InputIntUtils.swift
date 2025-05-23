//
//  InputIntUtils.swift
//  KyogiProgramming
//
//  Created by HIROKI IKEUCHI on 2022/12/16.
//

import Foundation

// MARK: - 数値 単体
/*
 // 入力: `1`
 let a = readInt() // a: 1

 // 入力: `1 2`
 let (a, b) = readInt2() // a: 1, b: 2

 // 入力: `1 2 3`
 let (a, b, c) = readInt3() // a: 1, b: 2, c: 3

 // 入力: `1 2 3 4`
 let (a, b, c, d) = readInt4() // a: 1, b: 2, c: 3, d: 4
 */

enum InputIntUtils {
    
    public func readInt() -> Int {
        Int(readLine()!)!
    }
    
    public func readInt2() -> (Int, Int) {
        let values = readLine()!.split(separator: " ").map { Int(String($0))! }
        precondition(values.count == 2)
        return (values[0], values[1])
    }
    
    public func readInt3() -> (Int, Int, Int) {
        let values = readLine()!.split(separator: " ").map { Int(String($0))! }
        precondition(values.count == 3)
        return (values[0], values[1], values[2])
    }
    
    public func readInt4() -> (Int, Int, Int, Int) {
        let values = readLine()!.split(separator: " ").map { Int(String($0))! }
        precondition(values.count == 4)
        return (values[0], values[1], values[2], values[3])
    }
    
    // MARK: - 数値 配列
    /*
     // 入力
     // 3
     // 1 2 3
     let n = readInt() // n: 3
     let aa = readIntArray() // aa: [1, 2, 3]
     precondition(aa.count == n)
     
     // 入力
     // 3
     // 1
     // 2
     // 3
     let n = readInt() // n: 3
     let aa = readNewLineIntArray(n) // aa: [1, 2, 3]
     precondition(aa.count == n)
     
     // 入力
     // 3
     // 1 2
     // 3 4
     // 5 6
     let n = readInt() // n: 3
     let aa = readNewLineInt2Array(n) // aa: [(1, 2), (3, 4), (5, 6)]
     precondition(aa.count == n)
     */
    
    public func readIntArray() -> [Int] {
        readLine()!.split(separator: " ").map { Int(String($0))! }
    }
    
    public func readNewLineIntArray(_ count: Int) -> [Int] {
        precondition(count > 0)
        return (1...count).map { _ in Int(readLine()!)! }
    }
    
    public func readNewLineInt2Array(_ count: Int) -> [(Int, Int)] {
        precondition(count > 0)
        return (1...count).map { _ in
            let values = readLine()!.split(separator: " ").map { Int(String($0))! }
            precondition(values.count == 2)
            return (values[0], values[1])
        }
    }
}
