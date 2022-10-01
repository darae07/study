# Instruction과 Pipelining

## 목차

- [Instruction](#instruction)
  - 구조
  - 타입
  - address와 메모리
- [Pipelining](#pipelining)
  - Five Stage
  - Pipelining Hazards
    - Data Hazards
    - Structural Hazards
    - Control Hazards

## Instruction

- CPU의 PC 레지스터에 의해 instruction memory 영역에 불러들여진 4byte 단위(32bit 운영체제 기준)의 기계어 코드이다.
- 구조
  - 4bit는 opcode로 명령어와 매핑된다.
  - rs, rt, td는 레지스터를 가리킨다.
  - address: 메모리 주소를 나타낸다.
- 타입: opcode에 따라 instruction의 타입이 결정된다.

  - R-type: 두 레지스터를 더한 결과값을 레지스터에 저장하는 instruction이다.
    - shamt: shift-amount로 저장된 레지스터를 4byte 단위로 맞추기 위해 수행해야 하는 shift 연산량을 의미한다.
  - Load/Store: 메모리 접근이 필요한 연산으로 주소를 포함한다.
  - Branch: 프로그램의 의사 결정 기능을 구현하는데 사용된다.

    - 두 레지스터와 address값을 가진다.
    - 다음 instruction을 받아둔다.
    - ALU에서 두 레지스터를 비교한 결과값에 따라 MUX는 address로 이동할 지 여부를 결정한다.

  - Jump: 직접 주소를 사용한 점프
    - 26bit의 address를 직접 입력하여 PC를 업데이트한다.
      <br> <br>

  ![instruction](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbtBI8Q%2FbtqAxhNeFQa%2FFbbmYWybw0IYjNfzP0oRN0%2Fimg.png)

  ##### CPU overview

  ![instruction](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdmBu63%2FbtqAvjrLZlr%2FS7Y8rOKJqxRyFDcFBN6JfK%2Fimg.png)

### address와 메모리

- 위 그림은 MIPS CPU를 도식화한 것이며, 32bit 운영체제이다.
- 32bit 운영체제의 경우 instruction의 메모리 주소를 최대 16bit로 표현한다.
- RAM은 byte-addressable array로서 접근 가능한 최소 단위가 byte이기 때문에 shift left 2 연산을 통해 단위를 맞춰준다.
- 따라서 한번에 RAM에서 읽어들일수 있는 데이터의 최대는 2 \*\*(16+2) = 2 \*\*(8+10)byte = 256kb이다.
- Jump instruction의 경우 26bit address에 shift left 2 연산을 취해 28bit address까지 한번에 읽어들일 수 있다. 이는 한번에 2 \*\* (8+10+10)byte = 256mb까지 읽어들일 수 있다는 것을 의미한다.

## Pipeline

- CPU의 동작 과정을 추상화 한 것이다.

## Pipelining

- instruction 처리량을 증가시키는 하드웨어 테크닉이다.
  ![pipeline_diagram](https://github.com/darae07/study/blob/master/image/pipeline_diagram.jpeg?raw=true)

### Five Stage

- 각각의 instruction은 완료 되기까지 5개의 단계를 거치고, 이를 Five Stage라고 한다.
- 모든 instruction은 IF, ID, EX 단계를 거치며, 오퍼레이션의 종류에 따라 수행되는 단계가 있다.(MEM, WB)

  - IF(instruction fetch): Cache 메모리에서 다음 instruction을 읽어들여 instruction memory로 불러들인다.
  - ID(instruction decode and register fetch): instruction memory에 올라온 명령어를 Mux(control unit)에 전달한다.
    - opcode를 control unit에서 해석하는 것이 decode다.
    - Mux는 오퍼레이션을 받아서 어떤 동작을 수행할지 결정한다.
  - EX(execute): 오퍼레이션이 실행된다.
  - MEM(memory access): 메모리에 접근하여 요청한 데이터를 읽어들인다.
    - 데이터의 위치에 따라 시간이 오래 걸릴 수 있으며, load 오퍼레이션일때 발생한다.
  - WB(register write back): 연산 결과를 레지스터에 저장한다.

    - store 오퍼레이션일때 발생한다.

      ![cpu_overview_forwarding_unit](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbbXIfm%2FbtqAB2J1cBR%2Fa6lomX1mcFX7dCgo6TqxwK%2Fimg.png)

### Pipelining Hazards

- 다음 clock cycle에서 다음 instuction이 실행되지 않을때 발생한다.
- Pipelining Hazards의 종류
  - Data hazards
  - Structural hazards
  - Control hazards

#### Data hazards

- 이전 연산의 결과가 저장(WB)되기 전에 필요한 경우 발생한다.

##### 해결 방안

- Stalling: 이전 instruction이 완료될 때까지 기다린다.
- 컴파일러 단계: 독립적인 instruction과 수행 순서를 바꾸거나, 아무 것도 수행하지 않는 명령어를 추가한다.
- Data forwarding: 수행 결과를 다음 instruction 실행 단계에 바로 전달한다.
  - hardware적인 해결 방안으로 Data forwarding unit의 추가가 필요하다.

#### Structural hazards

- hardware 측면에서의 문제점으로, 동일한 리소스에 동시에 접근할 때 발생한다.
- IF stage와 MEM stage는 동일한 메모리에 접근하므로, 두 stage가 동시에 처리될때 리소스 충돌이 발생한다.

##### 해결 방안

- Stalling: 이전 instruction과 충돌이 발생하지 않도록 기다린다.
- hardware: IF/MEM이 접근하는 하드웨어를 분리한다.(리소스 추가)

#### Control hazards

- 함수 호출, 조건문 등의 실행으로 instruction의 순서가 바뀌었을 때, 이를 알지 못해서 발생하는 문제이다.

##### 해결 방안

- Stalling: 다음으로 실행해야 할 instruction을 알 때까지 기다린다.

## 추가 정보

### Locality

- 시간 - Temporal Locality: 프로그램 실행 시 한번 접근이 이뤄진 주소의 영역은 자주 접근하게 된다. ex) 반복문 내의 지역변수들
- 공간 - Spatial Locality: 프로그램 실행 시 접근하는 메모리 영역은 이미 접근이 이뤄진 영역의 근처일 확률이 높음
- 수행 속도를 향상시키기 위해 Loaclity에 따라 메모리에 한번 접근할 때 주변의 일정 범위의 메모리 데이터를 한번에 읽어들인다.

### ISA

- Instruction Set Architecture
- 최하위 레벨의 프로그래밍 인터페이스로, 프로세서가 실행할 수 있는 모든 명령어들을 포함한다.
- 종류
  - CISC(Complex Instruction Set Computer): 복잡한 명령어 집합을 가진 프로세서이다.
    - 인텔 계열의 프로세서가 속한다.
  - RISC(Reduced Instruction Set Computer): 적은 수의 명령어를 수행하도록 설계된 마이크로 프로세서이다.
    - 복잡한 명령어를 제거하여 사용빈도가 높은 명령어 위주로 처리 속도를 향상한 프로세서이다.
    - 주로 스마트기기에 활용되며 ARM계열의 프로세서가 속한다.
- 기계어와 1대1로 문자화한 것이 어셈블리어이다.
- ISA는 소프트웨어에서 하드웨어로 넘어가는 단계에서 중재자 역할을 한다.

#### C언어 코드를 다른 기기에서 작동하도록 컴파일하기

- C언어의 라이브러리들은 so(shared object file)파일로 저장되기 때문에 각 CPU에 맞는 기계어로 작성되어 있다.
- 때문에 다른 CPU에서 작동하도록 컴파일하려면 타깃 CPU에 맞는 so 파일을 별도로 설치해야 한다.
- 만약 그렇지 않으면 링킹(ld)단계에서 컴파일이 실패하게 된다.
