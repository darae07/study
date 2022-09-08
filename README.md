# 공부 레포지토리

- [c언어의 포인터](cs/2022-09-02_pointer.markdown)

## 궁금한 것들

<details>
<summary>9월 1주</summary>
      
- [x] 시간복잡도 구할때 c와 n0으로 n구하는 부분
  - c는 상수를 초기화하여 그래프 형을 유지하기위한 공통 상수
- [x] 유클리드 알고리즘 최대 공약수 증명
- [x] 기초 자료형, 파생 자료형, 사용자 정의 자료형의 차이는 무엇일까?
  - 기초 자료형은 원시 타입, 파생 자료형은 
- [x] 추상 데이터 자료형과 인터페이스
  - 추상 데이터 타입: 사용자 정의 자료형
  - 상속자가 반드시 구현해야하는것 abstract function
  - extends - 객체를 가져다 쓰는거
  - interface - 상속받아서 구현하도록 강제하는것
- [x] 알고리즘 기초수학 수열. 등비수열 등차수열?
- [x] 2775
  - 등차수열 등비수열로 꼭 나눠서 정리할 필요는 없음. 
- [x] 배열의 응용: 다항식
  - 코드를 읽을 줄 알아야 한다. 모든 항을 저장하는 다항식 표현 방법에서는 최고차항과 계수값을 저장하며, 다항식의 덧셈에서는 새로운 구조체를 초기화하고 최고차항부터 차수가 같은 계수끼리 덧셈하며 구조체를 갱신해가며 완성된 구조체를 반환한다.
- [x] 2839
  - 완전탐색은 2의 n승(3,5)이기 때문에 적합하지 않고 그리디 혹은 dp로 구현하는 것이 좋음. 그리디가 가능한 이유는 3,5로 구성된 가장 짧은 배열을 만드는 것이기 때문에 항상 최선의 선택이 정해져 있음
- [x] 파이썬: 리스트 컴프리헨션과 함수+람다 표현식 중 뭐가 더 빠른지?
  - 리스트 컴프리헨션
- [x] 파이썬: 외부 숫자 변수 재할당이 안되서 풀이 보니까 class, self 변수 만들던데 어떻게 하는 건지
  - class, self 변수로 할수 있지만 추천하진 않음. 변수 global 설정으로 외부 변수 사용 가능. 인자로 받는 방향으로 설계할 수 있도록 하자.
- [x] 1978
  - 소수 판별은 제곱근까지 구하는 것이 맞고, 식의 오류를 찾기.
  - 천장함수를 취해서 거짓을 참으로 판별하는 등의 오류가 있을것으로 추정. 디버깅을 통해 찾자. 
  - -> 이 경우 수가 소수인지 판별해야 하므로 수를 변형하면 안됨.
</details>
<details>
<summary>9월 2주</summary>

- [ ] 브루트포스 2789: 조합 직접 구현시 시간초과 되는 이유
- [ ] 스택-[일반적인 배열 프로그램](cs/자료구조/스택.md)-포인터 변수 이해한 내용 맞는지
- [ ] 스택-동적 스택 프로그램: s = (StackType*)[malloc](cs/2022-09-02_pointer.markdown#-malloc-함수)(sizeof(StackType)); 스택타입에 *붙이는것? 스택타입의 크기만큼 메모리 할당? s가 포인터 변수라서?
- [ ] 스택-괄호 검사 프로그램#2 const char \*in?
- [ ] 큐의 응용: 버퍼 무슨소린지? 예시출력이 5의 배수도 아니고..
- [ ] 큐의 응용 프로그램 15p. 랜덤 시간 생성할때 srand = 랜덤 난수 생성?
- [ ] ch5 q->front, customer.id ->와 .의 차이
- [ ] 포인터 변수에 동적으로 메모리를 할당할때 malloc 함수로 메모리 할당?
- [ ] 연결리스트#2 리스트를 역순으로 만드는 연산 구현의 insert_last 함수가 이상함. 노드 순회후 마지막에 추가해야 하는것 아닌가?
- [ ] 헤드 노드는 데이터를 가지지 않고 가리키기만 하는데 head=node로 할당후 head 반환하는 이유? 헤드 포인터는 무엇?
- [ ] 노드 타입의 헤드를 가지는 연결리스트라는 추상 자료형을 쓰진 않는지.(헤드에 접근하고 함수 메서드화)
</details>
