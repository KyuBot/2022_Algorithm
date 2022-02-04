# 알고리즘 문제 풀이 시 몇가지 유용한 함수

1. Python

   - for 문을 간단히 쓰는 법 : [result for result in range( 범위 )]

   - 2차원 배열 ZIP

     - [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]

   - import math

     - math.gcd(n, m) ==> 최대 공약수!

   - import heapq

     - heapq.heapify() => heap으로 변환
     - heapq.heappop() => 작은 수 빼기!
     - heapq.heappush() => heap 함수에 push

   - for 문과 if문 간단하게 쓰는법

     - [i for i in list if 조건문]

   - 문자열 합치기

     - "".join(배열) => 리스트 배열 문자열 합치기 가능

   - 배열 거꾸로 만들기 (문자 -> 숫자로)

     - ```python
       def solution(n):
           n = list(str(n))
           answer = list(map(int, reversed(n)))
           return answer
       ```

   - 숫자 정렬 key 활용

     - a = sorted(arr, key=lambda x:x[n])
     
   - enumerate(arr) => (index, value) 출력

   - 소수를 구할때 1~n까지 구하는게 아니라 1~sqrt(n) 까지 구해야 빠르게 나온다!

   - 함수안에 함수 변수

     ```python
     def a():
     	b = 0
     	def c():
     		nonlocal b
     ```

   - 재귀는 for문 보다 느리고 메모리도 많이 쓴다

     ```python
     import sys
     sys.setrecursionlimit(10**6)
     
     재귀 제한을 늘려준다
     ```
     
   - ```python
     import collections
     
     cache = collections.deque(maxlen=20)
     
     이렇게 하면 20의 크기를 가지는 deque 함수가 만들어진다
     
     cache.remove(x) => x 를 제거
     
     ```

   - deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
   - deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
   - deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
   - deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
   - deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
   - deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
   - deque.remove(item): item을 데크에서 찾아 삭제한다.
   - deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

     ```
     
   - a = "123" 일때, a[:100] 이렇게 해도 out of index가 나오지 않는다.
     ```

2. MYSQL

   - 상위 1번쨰 행 : LIMIT 1;

   - count(*) => null 포함

   - count(컬럼명) => null 포함 x

   - if(조건, 참, 거짓)

   - 0~23 만들기

     ```sql
     SET @h=-1;
     
     SELECT @h:=@h+1 
     ...
     WHERE @h<23;
     ```

   - IFNULL(컬럼명, 대체값)

   - 대문자 : UPPER(컬럼명), 소문자 : LOWER(컬럼명)

   - 날짜 변경 : DATE_FORMAT(DATETIME, '%Y-%m-%d')

