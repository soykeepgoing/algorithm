function clearServer(nowServer,K, nowTime){
    let newServer = [] 
    for (let serverIndex = 0 ; serverIndex < nowServer.length ; serverIndex ++){
        let time = nowServer[serverIndex];
        if (time + K > nowTime) newServer.push(time);
    }
    return newServer
}

function updateServer(nowServer, time, nowServerCount, requiredServerCount){
    let count = 0 
    for (let i = 0; i < requiredServerCount - nowServerCount; i ++ ){
        nowServer.push(time);
        count++;
    }
    return count
}

function solution(players, m, k) {
    let answer = 0; // 몇 번 증설했는 가?
    let nowServer = []; // 현재 서버 대수
    
    for (let time = 0; time < 24; time ++){
        // 서버 있는 거 삭제 
        nowServer = clearServer(nowServer, k, time);
        let nowServerCount = nowServer.length;
        
        // 필요한 서버 개수 비교 
        let requiredServerCount = Math.floor(players[time] / m);
        
        // 증설 + 서버 배열 업데이트 
        answer += updateServer(nowServer, time, nowServerCount, requiredServerCount);
    }
    
    return answer;
}