function bfs(node, visited, computers, n, networkNum){
    queue = [node];
    
    while (queue.length > 0){
        let node = queue.shift(); 
        for (let nextNode = 0; nextNode < n; nextNode ++){
            if (node !== nextNode){
                if (visited[nextNode] === -1 && computers[node][nextNode] === 1){
                    queue.push(nextNode);
                    visited[nextNode] = networkNum
                }
            }
        }
    } 
}

function solution(n, computers) {
    let visited = Array(n).fill(-1)
    let networkNum = 0; 
    for (let i = 0 ; i < n ; i ++){
        if (visited[i] === -1){
            visited[i] = networkNum;
            bfs(i, visited, computers, n, networkNum);
            networkNum ++;
        }
    }
    return networkNum;
}