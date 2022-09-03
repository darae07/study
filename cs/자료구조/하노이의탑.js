// 하노이의 탑
// 가장 밑바닥의 원반이 목적지에 가기위해선 그 위의 원반이 다른 곳에 정렬되어 있어야 함.
// 다른 곳에 정렬된 원반 중 가장 밑바닥의 원반이 목적지에 가려면, 그 위의 원반은 다른 곳에 있어야 함.
// 이와 같은 구조가 반복됨 -> 이렇게 하나씩 분할할 수 있음
// 다시, 가장 큰 원반이 목적지에 갔다면, 다른 곳에 있는 원반을 목적지로 옮겨야 함.
// 두번째 큰 원반이 목적지에 가기 위해선 그 위의 원반이 다른 곳에 정렬 되어 있어야 함.
// 따라서 동일한 로직으로 반복할 수 있음

function hanoi(n) {
  const answer = [];
  function hanoiDfs(num, from = 1, to = 3, other = 2) {
    if (num === 0) return;
    hanoiDfs(num - 1, from, other, to); // 직전 원반은 출밡지에서 다른곳으로 옮긴다
    console.log([from, to]);
    answer.push([from, to]); // 해당 원반을 옮기는 차례
    hanoiDfs(num - 1, other, to, from); // 다음 와야 할 원반은 다른곳에서 목적지로 옮긴다
  }
  hanoiDfs(n);
  return answer;
}

hanoi(3);

// 이를 예쁘게 정리하면..
// 이런 구조를 배열을 반환해야 하는 재귀에 활용할 수 있을듯!

function hanoiShort(n, from = 1, to = 3, other = 2) {
  return n === 1
    ? [[from, to]]
    : [
        ...hanoiShort(n - 1, from, other, to),
        ...hanoiShort(1, from, to, other),
        ...hanoiShort(n - 1, other, to, from),
      ];
}
