//
//  main.swift
//  KyogiProgramming
//
//  Created by HIROKI IKEUCHI on 2022/12/16.
//

import Foundation

func main() {
    guard let line1 = readLine() else { fatalError("no input")}
    let results = logicFunction([line1])
    for result in results {
        print(result)
    }
}

#if !DEBUG
main()
#endif

func logicFunction(_: [String]) -> [String] {
    return ["1"]
}
