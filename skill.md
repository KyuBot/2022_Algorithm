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

   - 재귀는 for문 보다 느리고 메모리도 많이 쓴다

     ```python
     import sys
     sys.setrecursionlimit(10**6)
     
     재귀 제한을 늘려준다
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

