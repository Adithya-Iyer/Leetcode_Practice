func transpose(matrix [][]int) [][]int {
    var m, n int
    m = len(matrix)
    n = len(matrix[0])
    transpose := make([][]int, n)
    //var transpose [n][m]int
    /*for i := 0; i<m ; i++ {
        transpose[i] = make([]int, m)
    }*/
    for i := 0; i<m ; i++ {
        //transpose[i] = make([]int, m)
        for j := 0; j<n ; j++ {
            //transpose[j][i] = matrix[i][j]
            transpose[j] = append(transpose[j], matrix[i][j])
        }
    }
    return transpose
}