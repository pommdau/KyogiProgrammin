//
//  InputCharacterUtils.swift
//  KyogiProgramming
//
//  Created by HIROKI IKEUCHI on 2022/12/16.
//

import Foundation

// MARK: - 文字 単数

public enum InputCharacterUtils {
    
    public func readCharacter() -> Character {
        Character(readLine()!)
    }
    
    public func readCharacter2() -> (Character, Character) {
        let values = readLine()!.split(separator: " ").map { Character(String($0)) }
        precondition(values.count == 2)
        return (values[0], values[1])
    }
    
    public func readCharacter3() -> (Character, Character, Character) {
        let values = readLine()!.split(separator: " ").map { Character(String($0)) }
        precondition(values.count == 3)
        return (values[0], values[1], values[2])
    }
    
    public func readCharacter4() -> (Character, Character, Character, Character) {
        let values = readLine()!.split(separator: " ").map { Character(String($0)) }
        precondition(values.count == 4)
        return (values[0], values[1], values[2], values[3])
    }
    
    // MARK: - 文字 配列
    
    public func readCharacterArray() -> [Character] {
        readLine()!.split(separator: " ").map { Character(String($0)) }
    }
    
    public func readNewLineCharacterArray(_ count: Int) -> [Character] {
        precondition(count > 0)
        return (1...count).map { _ in Character(readLine()!) }
    }
    
    public func readNewLineCharacter2Array(_ count: Int) -> [(Character, Character)] {
        precondition(count > 0)
        return (1...count).map { _ in
            let values = readLine()!.split(separator: " ").map { Character(String($0)) }
            precondition(values.count == 2)
            return (values[0], values[1])
        }
    }
}
