/*

다음달에 누가 선물을 많이 받을지 

1. 주고받은 선물과 선물지수를 표로 만들기 
2. 한명씩 순회하면서 받을 선물 체크 
3. 선물 개수 max 리턴 

*/
function getCheckList(gifts, friends){
    const numFriends = friends.length;
    let checkList = Array.from({length: numFriends}, () => Array(numFriends).fill(0));
    
    for (let gift of gifts){
        const [giver, getter] = gift.split(" ");
        const [giverIndex, getterIndex] = [friends.indexOf(giver), friends.indexOf(getter)];
        checkList[giverIndex][getterIndex] += 1;
    }
    return checkList;
}

function getGiftScore(checkList, i, numFriends){
    const rowSum = checkList[i].reduce((sum, val) => sum + val, 0); // 행합
    let colSum = 0;
    for (let ci = 0; ci < numFriends; ci ++){
        colSum += checkList[ci][i];
    } // 열 합
    return rowSum - colSum;
}

function getMaxGift(checkList, friends){
    const numFriends = friends.length;
    let answer = 0;
    for (let i = 0; i < numFriends; i ++){
        let tmpGift = 0;
        const giftScore = getGiftScore(checkList, i, numFriends);
        for (let j = 0; j < numFriends; j ++){
            if (i === j) {
                continue;
            }
            if (checkList[i][j] > checkList[j][i]) { // 내가 받은게 더 크다면 
                tmpGift ++; 
            } else if (checkList[i][j] === checkList[j][i]){ // 동일한 경우 선물지수 확인
                const jGiftScore = getGiftScore(checkList, j, numFriends);
                if (giftScore > jGiftScore) { // 선물지수가 더 큰 경우 1 증가 
                    tmpGift ++;
                }
            }
        }
        answer = Math.max(answer, tmpGift); // 최대 값 업데이트
    } 
    return answer;
}

function solution(friends, gifts) {
    var answer = 0;
    const checkList = getCheckList(gifts, friends);
    answer = getMaxGift(checkList, friends)
    return answer;
}
