//
//  InputStringUtils.swift
//  KyogiProgramming
//
//  Created by HIROKI IKEUCHI on 2022/12/16.
//

import Foundation

public enum InputStringUtils {
    
    // MARK: - 文字列 単体
    
    public func readString() -> String {
        readLine()!
    }
    
    public func readString2() -> (String, String) {
        let values = readLine()!.split(separator: " ").map { String($0) }
        precondition(values.count == 2)
        return (values[0], values[1])
    }
    
    public func readString3() -> (String, String, String) {
        let values = readLine()!.split(separator: " ").map { String($0) }
        precondition(values.count == 3)
        return (values[0], values[1], values[2])
    }
    
    public func readString4() -> (String, String, String, String) {
        let values = readLine()!.split(separator: " ").map { String($0) }
        precondition(values.count == 4)
        return (values[0], values[1], values[2], values[3])
    }
    
    // MARK: - 文字列 配列
    
    public func readStringArray() -> [String] {
        readLine()!.split(separator: " ").map { String($0) }
    }
    
    public func readNewLineStringArray(_ count: Int) -> [String] {
        precondition(count > 0)
        return (1...count).map { _ in readLine()! }
    }
    
    public func readNewLineString2Array(_ count: Int) -> [(String, String)] {
        precondition(count > 0)
        return (1...count).map { _ in
            let values = readLine()!.split(separator: " ").map { String($0) }
            precondition(values.count == 2)
            return (values[0], values[1])
        }
    }
}
