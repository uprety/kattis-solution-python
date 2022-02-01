package main

import (
    "bufio"
    "fmt"
    "math"
    "os"
    "strconv"
    "strings"
)

func smallInverseFactorial(value string) int64 {
    var pre, ans int64
    pre = 1
    ans = 1
    intVal, _ := strconv.ParseInt(value, 10, 64)
    if intVal == 1 {
        return 1
    }
    for ans < intVal {
        ans *= pre
        pre += 1
    }
    return pre - 1
}

func largeInverseFactorial(n string) int64 {
    len_n := float64(len(n))
    var i float64 = 1
    var ans float64 = 1
    for {
        ans += math.Log10(i)
        if ans >= len_n {
            return int64(i)
        }
        i += 1
    }
    return 0
}

func main() {
    var value string
    value, _ = bufio.NewReader(os.Stdin).ReadString('\n')
    value = strings.Split(value, "\n")[0]
    if len(value) < 3 {
        fmt.Println(smallInverseFactorial(value))
    } else {
        fmt.Println(largeInverseFactorial(value))
    }
}
